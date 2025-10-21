import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class InputScene {

    private Stage primaryStage;

    public InputScene(Stage primaryStage) {
        this.primaryStage = primaryStage;
    }

    public void show() {
        Label nameLabel = new Label("Name:");
        TextField nameField = new TextField();

        Label ageLabel = new Label("Age:");
        TextField ageField = new TextField();

        Button submitButton = new Button("Submit");
        submitButton.setOnAction(e -> {
            // Write data to a file
            writeToFile(nameField.getText(), ageField.getText());
            // Close the application
            primaryStage.close();
        });

        VBox layout = new VBox(10);
        layout.getChildren().addAll(nameLabel, nameField, ageLabel, ageField, submitButton);

        Scene scene = new Scene(layout, 300, 200);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void writeToFile(String name, String age) {
        try {
            FileWriter fileWriter = new FileWriter("userdata.txt");
            PrintWriter printWriter = new PrintWriter(fileWriter);
            printWriter.println("Name: " + name);
            printWriter.println("Age: " + age);
            printWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
