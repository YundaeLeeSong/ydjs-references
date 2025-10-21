import javafx.application.Application;
import javafx.stage.Stage;

public class MainFX extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        // Load the first scene (menu)
        MenuScene menuScene = new MenuScene(primaryStage);
        menuScene.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}