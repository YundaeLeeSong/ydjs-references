package main;

public class MyFilmPane extends javafx.scene.layout.VBox {
    // Attributes
    private String filmName;
    private javafx.scene.image.ImageView filmImage;
    private String filmTimePeriod;
    private String filmDescription;
    // Attributes for counting tickets sold
    private int ticketsSold;                    // ****************** important for file process
    private int filmIndex;                      // ****************** important for file process
    // Constructor
    MyFilmPane(String filmName, int index) {
        this.filmIndex = index;
        this.ticketsSold = 0;
        this.filmName = filmName;
        this.filmImage = new javafx.scene.image.ImageView(new javafx.scene.image.Image("image/" + this.filmName +".jpg"));
        this.filmImage.setFitWidth(250);
        this.filmImage.setPreserveRatio(true);
        java.io.File file = new java.io.File("description/" + filmName + ".txt");
        try {
            if (file.exists()) {
                // Scanner Object Definition (File Connection, text I/O)
                java.util.Scanner inputFile = new java.util.Scanner(file);
                // Read - time period information
                this.filmTimePeriod = inputFile.nextLine();
                this.filmDescription = inputFile.nextLine();
                // Close
                inputFile.close();
            }
        }
        catch (java.io.IOException exeption) {
        }
        update();
    }
    // Methods
    public String getFilmName() {
        update();
        return this.filmName;
    }
    public String getFilmTimePeriod() {
        update();
        return this.filmTimePeriod;
    }
    public String getFilmDescription() {
        update();
        return this.filmDescription;
    }
    public javafx.scene.image.ImageView getFilmImage() {
        update();
        return this.filmImage;
    }
    public int getFilmIndex() {
        return this.filmIndex;
    }
    // Methods for Tickets Sold
    public void increaseTicketsSold(int x) {
        this.ticketsSold += x;
    }
    public int getTicketsSold() {
        return this.ticketsSold;
    }
    // Internal Work
    private void update() {
        this.getChildren().clear();
        
        javafx.scene.control.Label title = new javafx.scene.control.Label(this.filmName);
        title.setFont(javafx.scene.text.Font.font("Times New Roman", javafx.scene.text.FontWeight.EXTRA_BOLD, 20));
        this.setAlignment(javafx.geometry.Pos.CENTER);
        this.getChildren().add(title);
        this.getChildren().add(this.filmImage);
        this.getChildren().add(new javafx.scene.control.Label(this.filmTimePeriod));
        //////// getChildren().add(new javafx.scene.control.Label(this.filmDescription));
        this.setStyle("-fx-background-color: white;-fx-border-color: black");
    }
}
