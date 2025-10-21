import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class MenuScene {

    private Stage primaryStage;

    public MenuScene(Stage primaryStage) {
        this.primaryStage = primaryStage;
    }

    public void show() {
        Button startButton = new Button("Start");
        startButton.setOnAction(e -> {
            // Load the second scene (input form)
            InputScene inputScene = new InputScene(primaryStage);
            inputScene.show();
        });

        Button exitButton = new Button("Exit");
        exitButton.setOnAction(e -> primaryStage.close());

        VBox layout = new VBox(10);
        layout.getChildren().addAll(startButton, exitButton);

        Scene scene = new Scene(layout, 200, 150);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
