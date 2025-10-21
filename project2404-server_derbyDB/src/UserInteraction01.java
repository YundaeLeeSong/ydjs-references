import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class UserInteraction01 {
    // 1. initialize
    private static final BufferedReader keyboardUI = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) {
        System.out.println("Type something (press 'q' to quit):");
        while (true) { // 2. process
            try {
                String lineInput = keyboardUI.readLine();
                // Print the pressed key
                System.out.println("You ented: " + lineInput);
                // Check if 'q' is pressed to quit
                if (lineInput.charAt(0) == 'q') {
                    System.out.println("Exiting...");
                    break;
                }
            } catch (IOException e) { e.printStackTrace(); }
        }
        // 3. close
        try { keyboardUI.close(); } catch (IOException e) { e.printStackTrace(); }
    }
}
