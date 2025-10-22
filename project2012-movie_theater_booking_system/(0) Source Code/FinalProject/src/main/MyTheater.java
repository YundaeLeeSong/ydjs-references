package main;

public class MyTheater extends javafx.scene.layout.GridPane {
    // Attributes 
    private MyFilmPane film;                // ****************** important for file process
    // Attributes for seats
    javafx.scene.control.Button seats[];
    private boolean seatsClicked[];         // ****************** important for file process
    private boolean seatsBooked[];          // ****************** important for file process
    // Attributes for counting seats
    private final int numberOfSeats = 50;
    private int seatsAvailable;             // ****************** important for file process
    // Constructor
    MyTheater() {
        this(null);
    }
    MyTheater(MyFilmPane film) {
        this.seatsAvailable = numberOfSeats;
        this.film = film;
        this.seats = new javafx.scene.control.Button[numberOfSeats];
        for (int i = 0; i < this.seats.length; i++) {
            this.seats[i] = new javafx.scene.control.Button(new java.lang.String() + (i + 1));
            this.seats[i].setMaxSize(80, 80);
            this.seats[i].setStyle("-fx-background-color: white;-fx-border-color: green");
        }
        this.seatsClicked = new boolean[numberOfSeats];
        for (int i = 0; i < this.seatsClicked.length; i++) {
            seatsClicked[i] = false;
        }
        this.seatsBooked = new boolean[numberOfSeats];
        for (int i = 0; i < this.seatsBooked.length; i++) {
            seatsBooked[i] = false;
        }
        update();
    }
    // Methods
    public void setFilm(MyFilmPane film) {
        this.film = film;
        update();
    }
    public MyFilmPane getFilm() {
        update();
        return this.film;
    }
    public boolean hasFilm() {
        if (this.film == null)
            return false;
        else
            return true;
    }
    public javafx.scene.control.Button getSeat(int numberOfSeat) {
        update();
        return seats[numberOfSeat - 1];
    }
    public int getSeatsAvailable() {
        update();
        return this.seatsAvailable;
    }
    public void clickSeat(int numberOfSeat) {
        if (this.seatsBooked[numberOfSeat - 1] == false) {
            if (this.seatsClicked[numberOfSeat - 1] == true) {
                this.seatsClicked[numberOfSeat - 1] = false;
            }
            else {
                this.seatsClicked[numberOfSeat - 1] = true;
            }
        }
        update();
    }
    public void bookSeat() {
        int seatsBeforeCount = this.numberOfSeats - this.seatsAvailable;
        int seatsCounter = 0;
        for (int i = 0; i < numberOfSeats; i++) {
            if (this.seatsClicked[i] == true)
                this.seatsBooked[i] = true;
            if (this.seatsBooked[i] == true)
                seatsCounter++;
        }
        this.seatsAvailable = this.numberOfSeats - seatsCounter;
        int seatsNewlyCounted = seatsCounter - seatsBeforeCount;
        this.film.increaseTicketsSold(seatsNewlyCounted);
        /*
        if (this.seatsBooked[numberOfSeat - 1] == false)
            this.seatsBooked[numberOfSeat - 1] = true;*/
        update();
    }
    // Internal Work
    private void update() {
        for (int i = 0; i < this.seats.length; i++) {
            if (this.seatsBooked[i] == true){
                this.seats[i].setStyle("-fx-background-color: red;-fx-border-color: black");
            } 
            else if (this.seatsClicked[i] == false) {
                this.seats[i].setStyle("-fx-background-color: white;-fx-border-color: green");
            }
            else {
                this.seats[i].setStyle("-fx-background-color: green;-fx-border-color: black");
            }
        }
        this.getChildren().clear();
        this.setAlignment(javafx.geometry.Pos.CENTER);
        this.setPadding(new javafx.geometry.Insets(10));
        this.setHgap(10); this.setVgap(10);
        this.setStyle("-fx-background-color: gray;-fx-border-color: black");
        int index = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 10; j++) {
                this.add(seats[index], j, i);
                index++;
            }
        }
    }
    // File Operation
    public void writeOn(java.io.PrintWriter outputFile) {
        outputFile.println(this.seatsAvailable);
        for (int i = 0; i < this.seatsClicked.length; i++) {
            outputFile.println(this.seatsClicked[i]);
        }
        for (int i = 0; i < this.seatsBooked.length; i++) {
            outputFile.println(this.seatsBooked[i]);
        }
    }
    public void readFrom(java.util.Scanner inputFile) {
        this.seatsAvailable = inputFile.nextInt();
        for (int i = 0; i < this.seatsClicked.length; i++) {
            this.seatsClicked[i] = inputFile.nextBoolean();
        }
        for (int i = 0; i < this.seatsBooked.length; i++) {
            this.seatsBooked[i] = inputFile.nextBoolean();
        }
    }
}