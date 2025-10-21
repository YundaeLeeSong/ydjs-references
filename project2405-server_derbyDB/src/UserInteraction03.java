// import java.awt.AWTException;
// import java.awt.Robot;
// import java.awt.event.KeyEvent;
// import java.awt.event.MouseEvent;
// import java.awt.event.MouseListener;

// public class UserInteraction03 {
//     public static void main(String[] args) {
//         try {
//             // Create a Robot instance to interact with the mouse and keyboard
//             Robot robot = new Robot();

//             // Add a mouse listener to capture mouse events
//             robot.addMouseListener(new MouseListener() {
//                 @Override
//                 public void mouseClicked(MouseEvent e) {
//                     // Handle mouse click event
//                     System.out.println("Mouse Clicked: " + e);
//                 }

//                 @Override
//                 public void mousePressed(MouseEvent e) {
//                     // Handle mouse press event
//                     System.out.println("Mouse Pressed: " + e);
//                 }

//                 @Override
//                 public void mouseReleased(MouseEvent e) {
//                     // Handle mouse release event
//                     System.out.println("Mouse Released: " + e);
//                 }

//                 @Override
//                 public void mouseEntered(MouseEvent e) {
//                     // Handle mouse enter event
//                 }

//                 @Override
//                 public void mouseExited(MouseEvent e) {
//                     // Handle mouse exit event
//                 }
//             });

//             // Infinite loop to keep the program running
//             while (true) {
//                 // Capture keyboard events
//                 for (int i = 0; i < 256; i++) {
//                     if (robot.isKeyDown(i)) {
//                         System.out.println("Key Pressed: " + KeyEvent.getKeyText(i));
//                     }
//                 }

//                 // Delay to avoid high CPU usage
//                 Thread.sleep(100);
//             }
//         } catch (AWTException | InterruptedException e) {
//             e.printStackTrace();
//         }
//     }
// }
