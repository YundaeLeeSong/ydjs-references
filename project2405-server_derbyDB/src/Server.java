import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.sql.SQLException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private static final int PORT_NUMBER = 8080;
    private static final String IP_ADDRESS = "localhost";
    public static Socket client;
    
    public static void start() {
        try (ServerSocket server = new ServerSocket(PORT_NUMBER)) {
            System.out.println("Server is running...");
            System.out.println("\tServer IP Address: " + InetAddress.getLocalHost().getHostAddress() + " [auto]");
            System.out.println("\tServer IP Address: " + IP_ADDRESS + " [manual]");
            System.out.println("\tPort Number: " + PORT_NUMBER);
            System.out.println("\tQuit: ctrl + c");
            ////////////////////////////////////////////////////////////////////////
            // System Setting: client connection (Do not change this code)
            ////////////////////////////////////////////////////////////////////////
            while (true) {
                Server.client = server.accept();
                System.out.println("Client connected: " + Server.client);
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try (
                            BufferedReader in = new BufferedReader(new InputStreamReader(Server.client.getInputStream())); // request (in)
                            PrintWriter out = new PrintWriter(Server.client.getOutputStream(), true)                       // response (out)
                        ) {
                            // [optional] welcome message (to client)
                            out.println("Welcome to our service! You are now connected.");
                            // request -> response
                            String request, response;
                            while ((request = in.readLine()) != null) { // 1. request
                                response = process(request); // 2. process
                                out.println(response); // 3. response
                            }
                        } catch (IOException e) { e.printStackTrace(); } finally {
                            // DatabaseManager.resetInstance();
                        }
                    }
                    /**************************************************************************************
                     **** Business Logic (database): Store App Data, partially immutable for data safty ***
                     **************************************************************************************/
                    public String process(String request) {
                        String response;
                        switch (request.toUpperCase().substring(0, 2)) {
                            case "IN": // Command: INSERT 
                                response = "DML (INSERT statement)";
                                response = dml(request);
                                break;
                            case "UP": // Command: UPDATE 
                                response = "DML (UPDATE statement)";
                                response = dml(request);
                                break;
                            case "DE": // Command: DELETE 
                                response = "DML (DELETE statement)";
                                response = dml(request);
                                break;
                            case "SE": // Command: SELECT
                                response = "DQL (SELECT statement)";
                                response = dql(request);
                                break;
                            default:
                                response = "IDLE...";
                                break;
                        }
                        return response;
                    }
                    public String dml(String request) {
                        try {
                            DatabaseManager.getInstance().manipulate(request); 
                            DatabaseManager.getInstance().commit();
                            return "Success: Your SQL has been successfully processed!";
                        } catch (ClassNotFoundException e) {
                            return "Error: Server failed to load JDBC driver..";
                        } catch (SQLException e) {
                            return "Error: Your SQL is invalid..";
                        } catch (IOException e) {
                            return "Error: File IO of Your Server has trouble..";
                        }
                    }
                    public String dql(String request) {
                        try {
                            return DatabaseManager.getInstance().query(request);
                        } catch (ClassNotFoundException e) {
                            return "Error: Server failed to load JDBC driver..";
                        } catch (SQLException e) {
                            return "Error: Your SQL is invalid..";
                        } catch (IOException e) {
                            return "Error: File IO of Your Server has trouble..";
                        }
                    }
                }).start();
            }
        } catch (IOException e) { e.printStackTrace(); }
    }

    /**
     * ........................TEST........................
     */
    public static void main(String[] args) {
        Server.start();
    }
}