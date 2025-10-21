import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.io.IOException;

/**
 * Utility class for parsing and serializing strings
 * <p>
 * This class also provides the following functionalities:
 * <ol>
 *     <li>.</li>
 *     <li>.</li>
 *     <li>.</li>
 *     <li>In a "directory", delete files with "reserved code" and "extension".</li>
 * </ol>
 * 
 * @author Jaehoon Song
 * @version 0.3.0
 * @since 2024-03-24
 */
public class StringManager {
    private StringManager() {
        // Private constructor to prevent instantiation
    }
    /******************************************************
     ********************* SERIALIZE **********************
     ******************************************************/
    // constants
    private static final String REGEX_DATE = "\\d{4}-\\d{2}-\\d{2}";     // [1] Parsing java.util.Date (assuming date format: yyyy-MM-dd)
    private static final String REGEX_DOUBLE = "[-+]?\\d*\\.\\d+";       // [2] Parsing double
    private static final String REGEX_INT = "[-+]?\\d+";                 // [3] Parsing int
    private static final String REGEX_STRING = ".*";                     // [4] Parsing String
    // Determines the data type of the input string and returns the corresponding code.
    private static int getDataType(String input) {
        if (input == null || input.equalsIgnoreCase("null")) return 0;          // [0] null
        if (Pattern.compile(REGEX_DATE).matcher(input).matches()) return 1;     // [1] java.util.Date
        if (Pattern.compile(REGEX_DOUBLE).matcher(input).matches()) return 2;   // [2] double
        if (Pattern.compile(REGEX_INT).matcher(input).matches()) return 3;      // [3] int
        if (Pattern.compile(REGEX_STRING).matcher(input).matches()) return 4;   // [4] String
        return -1;                                                              // (no match)
    }
    /**
     * Serializes the given input string into a JSON object format.
     *
     * @param input The input string to be serialized into a JSON object.
     * @return A string representing the input string enclosed within curly braces, indicating a JSON object.
     */
    public static String serializeJSONObject(String input) {
        return "{" + input + "}";
    }
    /**
     * Serializes the given input string into an appropriate data format suitable for JSON.
     *
     * @param input The input string to be serialized into a JSON-compatible format.
     * @return An object representing the serialized data, compatible with JSON formatting.
     */
    public static Object serializeJSONEntry(String input) {
        int dataType = getDataType(input);
        switch (dataType) {
            case 0: return "null";
            case 1: return "\"" + input + "\"";
            case 2: return Double.parseDouble(input);
            case 3: return Integer.parseInt(input);
            case 4: return "\"" + input + "\"";
            default: return null;
        }
    }













    /******************************************************
     *********************** PARSE ************************
     ******************************************************/
    /**
     * Parses a JSON string representing tab-separated values (TSV) into a formatted string.
     *
     * @param json a JSON string containing tab-separated values
     * @return a formatted string representing the parsed tab-separated values
     */
    public static String parseTSV(String json) {
        Matcher matcher = Pattern.compile("\"rows\":\\s*\\[(.*?)\\]").matcher(json); 
        if (matcher.find()) json = matcher.group(1);    // 1. extract rows
        return json.replaceAll("\"", "")                // 3. erase double quotes
            .replaceAll("\\s*\\w+:\\s*", "")            // 4. erase fieldnames
            .replaceAll("\\}\\s*,\\s*\\{", "\n")        // 5. record delimiter ***
            .replaceAll(",", "\t")                      // 6. field delimiter ***
            .replaceAll("^\\{|\\}$", "").trim();        // 7. clean
    }
    // constants
    private static final String REGEX_CLEAN = "[\\s\\t]+";          // clean parsing
    private static final String REGEX_SQL = "(?i)(SELECT|" +        // parsing a string to a list of sql strings
    "INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|TRUNCATE)\\s+.*?(?=;)";
    /**
     * Parses SQL statements from a given string (chunck of SQL statements, delimeter: ";").
     *
     * @param sqlString the SQL string to parse
     * @return a list of parsed SQL statements
     */
    public static List<String> parseSQL(String sqlString) { // for init (setup)
        List<String> sqls = new ArrayList<>();
        // 1. clean
        String sqlStringClean = Pattern.compile(REGEX_CLEAN).matcher(sqlString).replaceAll(" ");
        // 2. parse
        Matcher matcher = Pattern.compile(REGEX_SQL).matcher(sqlStringClean);
        while (matcher.find()) {
            sqls.add(matcher.group());
        }
        return sqls;
    }
    /**
     * Parses SQL statements just like above.
     * Restores SQL INSERT statements from TSV data.
     *
     * @param tablename the name of the table (filename) for the INSERT statements
     * @param tsvString the TSV string (content) containing the data
     * @return a list of SQL INSERT statements
     */
    public static List<String> parseSQL(String tablename, String tsvString) { // for init (restore)
        List<String> sqls = new ArrayList<>();
        List<String> csv = new ArrayList<>();
        // 1. clean
        for (String tsvRow : tsvString.split("\\n")) {
            tsvRow = tsvRow.trim(); // trim
            if (tsvRow.isEmpty()) continue; // ignore empty row
            StringBuilder builder = new StringBuilder();
            for (String entry : Arrays.asList(tsvRow.replaceAll("\\s*\t\\s*", ",").split(","))) { // columns
                builder.append(parseSQLEntry(entry)).append(",");
            }
            builder.setLength(builder.length() - 1); // Remove the comma of last column
            csv.add(builder.toString());
        }
        // 2. parse
        for (String csvRow : csv) {
            sqls.add("INSERT INTO " + tablename + " VALUES (" + csvRow + ")");
        }
        return sqls;
    }
    /**
     * Parses the given input string into an appropriate data format suitable for SQL.
     *
     * @param input The input string to be parsed into a SQL-compatible format.
     * @return An object representing the parsed data, compatible with SQL formatting.
     */
    private static Object parseSQLEntry(String input) {
        int dataType = getDataType(input);
        switch (dataType) {
            case 0: return "NULL";
            case 1: return "DATE(" + input + ")";
            case 2: return Double.parseDouble(input);
            case 3: return Integer.parseInt(input);
            case 4: return "'" + input + "'";
            default: return null;
        }
    }










    /******************************************************
     ************************ TEST ************************
     ******************************************************/
    public static void main(String[] args) {
        // /////////////// JSON serializing (from SQL results)
        // String[] keys = {"name", "age", "city", "phone", "date"};
        // String[] values = {"John", "30", null, "1234567890", "2024-03-26"};
        // StringBuilder builder = new StringBuilder();
        // for (int i = 0; i < keys.length; i++) {
        //     builder.append(StringManager.serializeJSONEntry(keys[i]))
        //         .append(":")
        //         .append(StringManager.serializeJSONEntry(values[i]));
        //     if (keys.length != i + 1) builder.append(",");
        // }
        // System.out.println("JSONObject: " + StringManager.serializeJSONObject(builder.toString()));


        
        // /////////////// SQL parsing (from SQL)                   * for define (init)
        // try {
        //     System.out.println("sql file contents:");
        //     for (String sql : StringManager.parseSQL(FileManager.readAll(FileManager.DIR_SQL, "01", ".sql"))) {
        //         System.out.println(sql);
        //     }
        // } catch (IOException e) {System.err.println("An error occurred while reading files:");e.printStackTrace();}



        // /////////////// SQL parsing (from TSV)                      * for restore (init)
        // try {
        //     for (String filename : FileManager.searchAll(FileManager.DIR_TSV)) {
        //         String filenameTrimed = filename.replaceAll("\\.[^.]*$", ""); // skip extension
        //         List<String> parsedSQLs = StringManager.parseSQL(filenameTrimed,FileManager.read(FileManager.DIR_TSV, filename));
        //         parsedSQLs.remove(0); // skip the meta-data
        //         for (String sql : parsedSQLs) {
        //             System.out.println(sql);
        //         }
        //     }
        // } catch (IOException e) {e.printStackTrace(); }

        
        /////////////// TSV parsing (from json)                  * for backup
        String json = "{\"tablename\":\"employee\",\"num_rows\":3,\"rows\":[{\"id\":\"240324081530\",\"name\":\"John Doe\",\"position\":\"Software Engineer\",\"department_id\":1,\"salary\":80000,\"tall\":231},{\"id\":\"240324081531\",\"name\":\"Jane Smith\",\"position\":\"Marketing Manager\",\"department_id\":2,\"salary\":90000,\"tall\":11},{\"id\":\"240324081532\",\"name\":\"Alice Johnson\",\"position\":\"HR Coordinator\",\"department_id\":3,\"salary\":70000,\"tall\":123}]}";
        // json = "{\"tablename\": \"employee\", \"num_rows\": 3, \"rows\": [{\"id\": \"240324081530\", \"name\": \"John Doe\", \"position\": \"Software Engineer\", \"department_id\": 1}, {\"id\": \"240324081531\", \"name\": \"Jane Smith\", \"position\": \"Marketing Manager\", \"department_id\": 2}, {\"id\": \"240324081532\", \"name\": \"Alice Johnson\", \"position\": \"HR Coordinator\", \"department_id\": 3}]}";
        System.out.println(StringManager.parseTSV(json));
    }








    public static String getBackupID() {
        return "id" + (new SimpleDateFormat("yyMMddHHmmss")).format(new Date());
    }
}