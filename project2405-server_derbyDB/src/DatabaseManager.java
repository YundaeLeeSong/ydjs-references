import java.sql.*;   // JDBC classes library
import java.sql.SQLException;
import java.io.IOException;
import java.util.*;

public class DatabaseManager {
	// constants
    final String DB_PROTOCOL = "jdbc";
    final String DB_SUBPROTOCOL = "derby";
    final String DB_PATH = "./res/db";
    final String DB_URL = DB_PROTOCOL + ":" + DB_SUBPROTOCOL + ":" + DB_PATH + ";" + "create=true";
    private static Connection conn;
	/**
	 * Design Pattern: singleton
	 */
    private static DatabaseManager instance;
    private DatabaseManager() throws ClassNotFoundException, SQLException, IOException {
        Class.forName("org.apache.derby.jdbc.EmbeddedDriver"); // Load the JDBC driver
        conn = DriverManager.getConnection(DB_URL); 
        for (String sql : StringManager.parseSQL(FileManager.readAll(FileManager.DIR_SQL, "01", ".sql"))) {
            this.define(sql); // initialization (CRUD, Create)
        }
        this.rollback(FileManager.DIR_TSV); // initialization (CRUD, Update)
    }
    public static DatabaseManager getInstance() throws ClassNotFoundException, SQLException, IOException {
        if (instance == null) instance = new DatabaseManager();
        return instance;
    }
    public static void resetInstance() throws SQLException {
		if (conn == null) throw new RuntimeException("no connecntions found in database");
		if (conn.isClosed()) throw new RuntimeException("connecntion is already closed in database");
		conn.close();
		conn = null;
		instance = null;
    }
	/**
	 * Executes a SQL statement for defining database objects (DDL - Data Definition Language).
	 * This method is used to execute SQL statements that create, modify, or drop database 
	 * objects like tables, indexes, etc.
	 * 
	 * Commands: CREATE, ALTER, and DROP
	 * 
	 * @param sql is a DDL statement to be executed for defining database objects.
	 * @throws SQLException if a database access error occurs while defining.
	 */
    private void define(String sql) throws SQLException {
        Statement stmt = conn.createStatement();
        stmt.execute(sql);
    }
	/**
	 * Executes a SQL statement for data manipulation (DML - Data Manipulation Language).
	 * This method is used to execute SQL statements that manipulate data in the database.
	 * 
	 * Commands: INSERT, UPDATE, and DELETE
	 * 
	 * @param sql is a DML statement to be executed for data manipulation.
	 * @throws SQLException if a database access error occurs while manipulating.
	 */
    public void manipulate(String sql) throws SQLException {
        Statement stmt = conn.createStatement();
        stmt.execute(sql);
    }
    /**
     * Commits changes made in the database by exporting data from tables to corresponding TSV files.
     *
     * Commands: COMMIT
     *
     * @throws SQLException If a database access error occurs or SQL execution fails.
     * @throws IOException  If an I/O error occurs while writing to TSV files.
     */
    public void commit() throws SQLException, IOException {
        DatabaseMetaData metadata = conn.getMetaData();
        ResultSet resultSet = metadata.getTables(null, null, "%", new String[] {"TABLE"}); // Get table names
        while (resultSet.next()) {
            String tableName = resultSet.getString("TABLE_NAME").toLowerCase();
            String filename = tableName + ".tsv";
            String dql = "SELECT * FROM " + tableName;
            FileManager.write(FileManager.DIR_TSV, filename, StringManager.parseTSV(this.query(dql)));
        }
    }
    /**
     * Rollback changes made by applying SQL commands stored in TSV files 
     * within the specified directory.
     *
     * Commands: ROLLBACK
     *
     * @param directoryTSV The directory path containing TSV files to rollback changes from.
     * @throws SQLException If a database access error occurs or SQL execution fails.
     * @throws IOException  If an I/O error occurs while reading TSV files.
     */
    public void rollback(String directoryTSV) throws SQLException, IOException { // init
        List<String> ex = Arrays.asList(
            "staff.tsv",
            "patient.tsv",
            "patient_staff.tsv",
            "daily_report_data.tsv",
            "notification.tsv"
        ); FileManager.searchAll(directoryTSV); // hardcoded for now.
        for (String filename : ex) {
            String filenameTrimed = filename.replaceAll("\\.[^.]*$", ""); // skip extension
            List<String> parsedSQLs = StringManager.parseSQL(filenameTrimed,FileManager.read(FileManager.DIR_TSV, filename));
            for (String sql : parsedSQLs) {
                this.manipulate(sql); // initialization (CRUD, Update)
            }
        }
    }
    /**
     * Executes a SQL statement for data query (DQL - Data Query Language).
	 * This method is used to execute SQL query statements to retrieve data from the database.
     * 
	 * Commands: SELECT
	 * 
     * If the SQL statement contains a JOIN operation, the result shows "null" for the tablename field.
     *
     * @param sql is a DQL statement to be executed to retrieve data from the database.
     * @return a String containing the JSON representation of the query result.
     * @throws SQLException if a database access error occurs while querying.
     */
    public String query(String sql) throws SQLException {
        ResultSet resultSet;
        String json = null;
        Statement stmt = conn.createStatement();
        if (stmt.execute(sql)) resultSet = stmt.getResultSet();
        else return null;
        if (sql.toLowerCase().contains("join")) json = serialize(resultSet, true);
        else json = serialize(resultSet, false);
        resultSet.close();
        return json;
    }
    private String serialize(ResultSet resultSet, boolean isJoin) throws SQLException {
		if (resultSet == null) throw new RuntimeException("resultSet is null, does not make sense.");
		// 1. prep Object entries
        ResultSetMetaData metaData = resultSet.getMetaData();
        String tablename = (isJoin) ? "null" : metaData.getTableName(1);
        int num_rows = 0;
        List<String> rows = new ArrayList<>();
        // 2. serialize row entries (process database)
        while (resultSet.next()) { // for each row
            num_rows++;
            StringBuilder row = new StringBuilder();
            for (int i = 1; i <= metaData.getColumnCount(); i++) { // for each column
                row.append(StringManager.serializeJSONEntry(metaData.getColumnName(i).toLowerCase()))
					.append(":")
					.append(StringManager.serializeJSONEntry(resultSet.getString(i)));
                if (i < metaData.getColumnCount()) row.append(",");
            }
            rows.add(StringManager.serializeJSONObject(row.toString()));
        }
        // 3. serialize Object entries
        return StringManager.serializeJSONObject(
			StringManager.serializeJSONEntry("tablename") + ":" + ((String) StringManager.serializeJSONEntry(tablename)).toLowerCase() +
			"," +
			StringManager.serializeJSONEntry("num_rows") + ":" + num_rows +
			"," +
			StringManager.serializeJSONEntry("rows") + ":" + rows
        );
    }



	
    /******************************************************
     ************************ TEST ************************
     ******************************************************/
    public static void main(String[] args) {
        ////////// Display the current working directory
        System.out.println("Current working directory, user.dir: " + System.getProperty("user.dir"));
        System.out.println("user.home: " + System.getProperty("user.home"));
        System.out.println("java.version: " + System.getProperty("java.version"));
        System.out.println("java.home: " + System.getProperty("java.home"));
        System.out.println("java.class.path: " + System.getProperty("java.class.path"));
        System.out.println("os.name: " + System.getProperty("os.name"));
        System.out.println("os.arch: " + System.getProperty("os.arch"));
        System.out.println("file.separator: " + System.getProperty("file.separator"));
        System.out.println("line.separator: " + System.getProperty("line.separator"));
        System.out.println("path.separator: " + System.getProperty("path.separator"));
        ////////// Set the user.dir system property to point to your "res" directory
        // System.setProperty("user.dir", "path/to/your/res/directory");
		System.out.println("\n\n\n");


		
		String request;
        String response;
		try {
            // start example
            DatabaseManager.getInstance();
        } 
		catch (ClassNotFoundException e) {System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());} 
		catch (SQLException e) {System.out.println("SQL exception while db initializing: " + e.getMessage());} 
		catch (IOException e) {System.out.println("IO exception while db initializing: " + e.getMessage());}


        
        try {
            // 1. read data
            request = "SELECT * FROM patient ";
            response = DatabaseManager.getInstance().query(request);
            System.out.println(response);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        try {
            // 2. read data
            request = "SELECT MAX(patient_id) AS max_patient_id FROM patient";
            response = DatabaseManager.getInstance().query(request);
            System.out.println(response);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }

        try {
            // 3. Helper function to get current patients associated with a staff member
            String request1 = "SELECT patient.patient_firstname, patient.patient_lastname, patient.mrn " +
                              "FROM patient JOIN patient_staff ON patient.patient_id = patient_staff.patient_cid " +
                              "WHERE patient_staff.staff_cid = 1"; // Example value for staff_id (John)
            String response1 = DatabaseManager.getInstance().query(request1);
            System.out.println(response1);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        
        try {
            // Helper function to get new patients not associated with any staff member
            String request2 = "SELECT patient_firstname, patient_lastname, mrn " +
                              "FROM patient " +
                              "WHERE patient_id NOT IN (SELECT patient_cid FROM patient_staff)";
            String response2 = DatabaseManager.getInstance().query(request2);
            System.out.println(response2);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        
        try {
            // Helper function to get patient ID from MRN
            String request3 = "SELECT patient_id " +
                              "FROM patient " +
                              "WHERE mrn = 'MRN123456'"; // Example value for MRN of a patient (Alice)
            String response3 = DatabaseManager.getInstance().query(request3);
            System.out.println(response3);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        
        try {
            // Helper function to get daily report data list for a patient
            String request4 = "SELECT * " +
                              "FROM daily_report_data " +
                              "WHERE patient_id = 1 " + // Example value for patient_id (Alice)
                              "ORDER BY report_date";
            String response4 = DatabaseManager.getInstance().query(request4);
            System.out.println(response4);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        
        try {
            // Helper function to get daily report data for a patient
            String request5 = "SELECT report_date, weight " +
                              "FROM daily_report_data " +
                              "WHERE patient_id = 1"; // Example value for patient_id (Alice)
            String response5 = DatabaseManager.getInstance().query(request5);
            System.out.println(response5);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        
        try {
            // Helper function to get detail of a patient
            String request6 = "SELECT patient_firstname, patient_lastname, mrn " +
                              "FROM patient " +
                              "WHERE patient_id = 1"; // Example value for patient_id (Alice)
            String response6 = DatabaseManager.getInstance().query(request6);
            System.out.println(response6);
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL exception while querying: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO exception while db initializing: " + e.getMessage());
        }
        



        // new Scanner(System.in).nextLine();
        




        try {
            // commit example
            DatabaseManager.getInstance().commit();
        }
		catch (ClassNotFoundException e) {System.out.println("Class not found exception to load JDBC driver: " + e.getMessage());} 
		catch (SQLException e) {System.out.println("SQL exception while querying: " + e.getMessage());}
		catch (IOException e) {System.out.println("IO exception while db initializing: " + e.getMessage());}



		// close example
        try {
            DatabaseManager.resetInstance();
        } 
		catch (SQLException e) {System.out.println("SQL exception while db resetting: " + e.getMessage());}
		new Scanner(System.in).nextLine();
    }
}