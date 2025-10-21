import java.awt.*;
import java.awt.event.*;

public class UserInteraction02 {
    private static final Frame frame = new Frame("");
    private static boolean shouldExit = false;
    
    public static void main(String[] args) {
        System.out.println("Type something (press 'q' to quit):");
        
        // Add key listener to this frame
        frame.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                char keyChar = e.getKeyChar();
                System.out.println("Key pressed: " + keyChar);
                
                // Check if 'q' is pressed to quit
                if (keyChar == 'q') {
                    System.out.println("Exiting...");
                    shouldExit = true;
                    System.exit(0);
                    // frame.dispose(); // Close the frame
                }
            }
        });
        
        // Set the frame visible
        frame.setSize(1, 1);
        frame.setVisible(true);
        
        // Focus the frame to ensure it receives key events
        frame.requestFocus();
        
        // Keep the program running until 'q' is pressed
        while (!shouldExit) {
            try {
                Thread.sleep(100); // Sleep to avoid consuming CPU
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}