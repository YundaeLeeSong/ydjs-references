import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/**
 * Utility class for file operations such as reading, writing, searching, and deleting files.
 * <p>
 * This class also provides the following functionalities:
 * <ol>
 *     <li>In a "directory", write a "file" with a string "content" given.</li>
 *     <li>In a "directory", read files with "reserved code" and "extension" as a string.</li>
 *     <li>In a "directory", search for files with "reserved code" and "extension" as a list of string.</li>
 *     <li>In a "directory", delete files with "reserved code" and "extension".</li>
 * </ol>
 * 
 * @author Jaehoon Song
 * @version 0.3.0
 * @since 2024-03-24
 */
public class FileManager {
    private FileManager() {
        // Private constructor to prevent instantiation
    }
    // constants
    public static final String DIR_RES = "./res";
    public static final String DIR_CSV = DIR_RES + "/csv";
    public static final String DIR_SQL = DIR_RES + "/sql";
    public static final String DIR_TSV = DIR_RES + "/tsv";

     /**
     * [CRUD] Create: Writes content to a file.
     * @param directory The directory where the file will be written.
     * @param filename The name of the file.
     * @param content The content to be written to the file.
     * @throws IOException If an I/O error occurs.
     */
    public static void write(String directory, String filename, String content) throws IOException {
        Path filePath = Path.of(directory, filename);
        Files.writeString(filePath, content, StandardCharsets.UTF_8);
    }



    /**
     * [CRUD] Read: Reads the contents of all files in a directory with a given prefix and suffix.
     * @param directory The directory where the files are located.
     * @param prefix The prefix (reserved code) of the file names to search for.
     * @param suffix The suffix (extension) of the file names to search for.
     * @return A string containing the concatenated contents of all matching files. Data type: <b>String</b>
     * @throws IOException If an I/O error occurs.
     */
    public static String readAll(String directory, String prefix, String suffix) throws IOException {
        StringBuilder builder = new StringBuilder();
        List<String> filelist = searchAll(directory, prefix, suffix);
        for (String filename : filelist) {
            builder.append(read(directory, filename)).append("\n");
        }
        return builder.toString();
    }
    public static String readAll(String directory, String suffix) throws IOException {
        return readAll(directory, "", suffix); // overloaded method call
    }
    public static String readAll(String directory) throws IOException {
        return readAll(directory, "", ""); // overloaded method call
    }
    public static String read(String directory, String filename) throws IOException {
        Path filePath = Path.of(directory, filename);
        if (!Files.exists(filePath)) throw new RuntimeException("File '" + filename + "' not found");
        return Files.readString(filePath, StandardCharsets.UTF_8);
    }
    /**
     * [CRUD] Read (Helper): Searches for files in a directory with a given prefix and suffix.
     * @param directory The directory where the files are located.
     * @param prefix The prefix (reserved code) of the file names to search for.
     * @param suffix The suffix (extension) of the file names to search for.
     * @return A list of filenames matching the criteria. Data type: <b>List<String></b>
     */
    public static List<String> searchAll(String directory, String prefix, String suffix) {
        File[] files = new File(directory).listFiles();
        if (files == null) throw new RuntimeException("No files found in directory: " + directory);
        List<String> filelist = new ArrayList<>();
        for (File file : files) {
            if (!file.isFile()) continue;
            String filename = file.getName();
            if (filename.startsWith(prefix) && filename.endsWith(suffix)) {
                filelist.add(filename);
            }
        }
        return filelist;
    }
    public static List<String> searchAll(String directory, String suffix) {
        return searchAll(directory, "", suffix); // overloaded method call
    }
    public static List<String> searchAll(String directory) {
        return searchAll(directory, "", ""); // overloaded method call
    }
    
    /**
     * [CRUD] Delete: Deletes all files in a directory with a given prefix and suffix.
     * @param directory The directory where the files are located.
     * @param prefix The prefix (reserved code) of the file names to delete.
     * @param suffix The suffix (extension) of the file names to delete.
     */
    public static void deleteAll(String directory, String prefix, String suffix) {
        List<String> filelist = searchAll(directory, prefix, suffix);
        for (String filename : filelist) {
            delete(directory, filename);
        }
    }
    public static void deleteAll(String directory, String suffix) {
        deleteAll(directory, "", suffix); // overloaded method call
    }
    public static void deleteAll(String directory) {
        deleteAll(directory, "", ""); // overloaded method call
    }
    public static void delete(String directory, String filename) {
        File fileToDelete = new File(directory, filename);
        if (!fileToDelete.exists()) throw new RuntimeException("File '" + filename + "' does not exist in directory: " + directory);
        if (!fileToDelete.delete()) throw new RuntimeException("Failed to delete file '" + filename + "' in directory: " + directory);
        return;
    }





    /******************************************************
     ************************ TEST ************************
     ******************************************************/
    public static void main(String[] args) {
        /***************************************************
         * samples
         ***************************************************/
        String file1Content = "Line 1\n\nLine 2\nLine 3\nLine 4\nLinee55";
        String file2Content = "Line A\n\nLine B\nLine C\nLine D\n\n";
        String file3Content = "1,2,3,4,5,6,7,10\n";
        String file1Name = "file1.txt";
        String file2Name = "file2.txt";
        String file3Name = "file3.csv";

        System.out.println("\n\n\n"); // Write the string to the files
        try {
            FileManager.write(FileManager.DIR_RES, file1Name, file1Content);
            FileManager.write(FileManager.DIR_RES, file2Name, file2Content);
            FileManager.write(FileManager.DIR_RES, file3Name, file3Content);
        } catch (IOException e) {System.err.println("An error occurred while writing to files:"); e.printStackTrace();}
        
        System.out.println("\n\n\n"); // Search all files and Read each file
        System.out.println("looking for txt files..." + FileManager.searchAll(FileManager.DIR_RES, ".txt"));
        System.out.println("looking for csv files..." + FileManager.searchAll(FileManager.DIR_RES, ".csv"));
        System.out.println("looking for all files..." + FileManager.searchAll(FileManager.DIR_RES));
        for (String filename : FileManager.searchAll(FileManager.DIR_RES)) {
            try {
                String fileContent = FileManager.read(FileManager.DIR_RES, filename);
                System.out.println("Contents of " + filename + ":");
                System.out.println(fileContent);
            } catch (IOException e) {
                System.err.println("An error occurred while reading " + filename + " (individual):");
                e.printStackTrace();
            }
        }

        System.out.println("\n\n\n"); // Read all files
        try {
            String allFileContents = FileManager.readAll(FileManager.DIR_RES);
            System.out.println("All file contents:");
            System.out.println(allFileContents);
        } catch (IOException e) {System.err.println("An error occurred while reading files:");e.printStackTrace();}
        



        System.out.println("\n\n\n"); // Delete all files
        FileManager.deleteAll(FileManager.DIR_RES);


        /***************************************************
         * future references
         ***************************************************/
        System.out.println("\n\n\n"); // Read all files
        try {
            System.out.println("sql file contents:");
            System.out.println(FileManager.readAll(FileManager.DIR_SQL));
        } catch (IOException e) {System.err.println("An error occurred while reading files:");e.printStackTrace();}

        System.out.println("\n\n\n"); // Search all files (filename -> tablename)
        for (String filename : searchAll(FileManager.DIR_SQL)) {
            String tablename = (filename.lastIndexOf('.') != -1) ? (filename.substring(0, filename.lastIndexOf('.'))) : (filename);
            System.out.println("converted into tablename:::: " + filename + " >>> " + tablename);
        }
    }
}