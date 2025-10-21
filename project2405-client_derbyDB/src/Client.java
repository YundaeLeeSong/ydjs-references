// Client.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    private static final int PORT_NUMBER = 8080;
    private static final String IP_ADDRESS = "localhost";

    /**
     * Singleton Pattern
     */
    private static Client instance; private Socket server;
    private PrintWriter out;    // output request to server
    private BufferedReader in;  // input the response from server
    private Client() {
        try {
            server = new Socket(IP_ADDRESS, PORT_NUMBER);
            out = new PrintWriter(server.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(server.getInputStream()));
            System.out.println(in.readLine()); // [optional] welcome message (from server)
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static Client getInstance() {
        if (instance == null) instance = new Client();
        return instance;
    }


    /**
     * Sends an POST request to the server and returns the response.
     *
     * @param request the INSERT SQL to be sent to the server
     * @return the response received from the server
     * @throws RuntimeException if the input request is invalid or an I/O error occurs
     */
    public String post(String request) {
        if (!(request.toUpperCase().startsWith("IN"))) throw new RuntimeException("...invalid input: " + request);
        try {
            out.println(request); // 1. request (to server)
            //////////////////////// 2. process
            return in.readLine(); // 3. response
        } catch (IOException e) {e.printStackTrace();}
        return null;
    }

    /**
     * Sends an PUT request to the server and returns the response.
     *
     * @param request the UPDATE SQL to be sent to the server
     * @return the response received from the server
     * @throws RuntimeException if the input request is invalid or an I/O error occurs
     */
    public String put(String request) { 
        if (!(request.toUpperCase().startsWith("UP"))) throw new RuntimeException("...invalid input: " + request);
        try {
            out.println(request); // 1. request (to server)
            //////////////////////// 2. process
            return in.readLine(); // 3. response
        } catch (IOException e) {e.printStackTrace();}
        return null;
    }

    /**
     * Sends a DELETE request to the server and returns the response.
     *
     * @param request the DELETE SQL to be sent to the server
     * @return the response received from the server
     * @throws RuntimeException if the input request is invalid or an I/O error occurs
     */
    public String delete(String request) {
        if (!(request.toUpperCase().startsWith("DE"))) throw new RuntimeException("...invalid input: " + request);
        try {
            out.println(request); // 1. request (to server)
            //////////////////////// 2. process
            return in.readLine(); // 3. response
        } catch (IOException e) {e.printStackTrace();}
        return null;
    }

    /**
     * Sends a GET request to the server and returns the response.
     *
     * @param request the SELECT SQL to be sent to the server
     * @return the response received from the server
     * @throws RuntimeException if the input request is invalid or an I/O error occurs
     */
    public String get(String request) {
        if (!(request.toUpperCase().startsWith("SE"))) throw new RuntimeException("...invalid input" + request);
        try {
            out.println(request); // 1. request
            //////////////////////// 2. process
            return in.readLine(); // 3. response
        } catch (IOException e) {e.printStackTrace();}
        return null;
    }

    /**
     * ........................TEST........................
     */
    public static void main(String[] args) {
        System.out.println("test of put(): " + Client.getInstance().post("INSERT"));

        System.out.println("test of get(): " + Client.getInstance().get("SELEct"));
        System.out.println("test of get(): " + Client.getInstance().get("SELECT * FROM patient"));
    }
}