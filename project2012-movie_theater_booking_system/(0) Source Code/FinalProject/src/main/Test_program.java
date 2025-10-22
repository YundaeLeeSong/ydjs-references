package main;

public class Test_program extends javafx.application.Application {
    /***************** Data *****************/  
    // Constant Data (Permanant)
    String[] filmTitles = {"Antebellum", "Mulan", "Onward", "Soul",
        "Tenet","The Invisible Man","The Trial of the Chicago 7","The Witches"};
    String[] theaterTitles = {"Theater 1", "Theater 2", "Theater 3", "Theater 4"};
    String[] theaterTime = {"Theater 1 - 10 a.m.", "Theater 1 - 3 p.m.", "Theater 1 - 8 p.m.", 
                            "Theater 2 - 10 a.m.", "Theater 2 - 3 p.m.", "Theater 2 - 8 p.m.", 
                            "Theater 3 - 10 a.m.", "Theater 3 - 3 p.m.", "Theater 3 - 8 p.m.", 
                            "Theater 4 - 10 a.m.", "Theater 4 - 3 p.m.", "Theater 4 - 8 p.m."};
    // Buttons (Permanant)
    private javafx.scene.control.Button btNew = new javafx.scene.control.Button("Start New");
    private javafx.scene.control.Button btLoad = new javafx.scene.control.Button("Load File");
    private javafx.scene.control.Button btOk = new javafx.scene.control.Button("Ok");
    private javafx.scene.control.Button btBack = new javafx.scene.control.Button("Back");
    private javafx.scene.control.Button btCancel = new javafx.scene.control.Button("Cancel");
    private javafx.scene.control.Button btTicket = new javafx.scene.control.Button("Ticket");
    private javafx.scene.control.Button btStatus = new javafx.scene.control.Button("Theater Information");
    private javafx.scene.control.Button btReport = new javafx.scene.control.Button("Film Information");
    private javafx.scene.control.Button btSave = new javafx.scene.control.Button("Save");
    private javafx.scene.control.Button btTheaters[] = {
        new javafx.scene.control.Button(theaterTime[0]), 
        new javafx.scene.control.Button(theaterTime[1]),
        new javafx.scene.control.Button(theaterTime[2]),
        new javafx.scene.control.Button(theaterTime[3]),
        new javafx.scene.control.Button(theaterTime[4]),
        new javafx.scene.control.Button(theaterTime[5]),
        new javafx.scene.control.Button(theaterTime[6]), 
        new javafx.scene.control.Button(theaterTime[7]),
        new javafx.scene.control.Button(theaterTime[8]),
        new javafx.scene.control.Button(theaterTime[9]),
        new javafx.scene.control.Button(theaterTime[10]),
        new javafx.scene.control.Button(theaterTime[11])};
    // My Data for the Theater Ticketing Program
    MyFilmPane films[];
    MyTheater theaters[];
    
    /***************** Start the Program *****************/ 
    public static void main(String[] args) {
        javafx.application.Application.launch(args);
    }
    @Override
    public void start(javafx.stage.Stage stage) {
        modeSelection(stage);
    }
    
    // 1. select if the employee wants to start new data or to continue to the latest data.
    private void modeSelection(javafx.stage.Stage stage) {
        // Initialization of Data
        films = new MyFilmPane[filmTitles.length];
        for (int i = 0; i < films.length; i++) {
            films[i] = new MyFilmPane(filmTitles[i], i);
        }
        theaters = new MyTheater[12];
        for (int i = 0; i < theaters.length; i++) {
            theaters[i] = new MyTheater();
        }
        // Buttons (Permanant)
        btOk.setPadding(new javafx.geometry.Insets(10));
        btOk.setMaxSize(50, 50);
        btBack.setPadding(new javafx.geometry.Insets(10));
        btBack.setMaxSize(50, 50);
        btCancel.setPadding(new javafx.geometry.Insets(10));
        btCancel.setMaxSize(200, 50);
        btReport.setPadding(new javafx.geometry.Insets(10));
        btReport.setMaxSize(200, 50);
        btStatus.setPadding(new javafx.geometry.Insets(10));
        btStatus.setMaxSize(200, 50);
        btTicket.setPadding(new javafx.geometry.Insets(10));
        btTicket.setMaxSize(200, 50);
        btSave.setPadding(new javafx.geometry.Insets(10));
        btSave.setMaxSize(200, 50);
        btLoad.setPadding(new javafx.geometry.Insets(10));
        btLoad.setMaxSize(200, 50);
        btNew.setPadding(new javafx.geometry.Insets(10));
        btNew.setMaxSize(200, 50);
        for (int i = 0; i < btTheaters.length; i++) {
            btTheaters[i].setPadding(new javafx.geometry.Insets(10));
            btTheaters[i].setMaxSize(300, 100);
        }    
        
        // ================== JavaFX Event Source ==================
        // Parent (Pane)
        javafx.scene.layout.GridPane pane = new javafx.scene.layout.GridPane();
        pane.setAlignment(javafx.geometry.Pos.CENTER);
        pane.setPadding(new javafx.geometry.Insets(5));
        pane.setHgap(5);
        pane.setVgap(5);
        pane.add(btNew, 0, 0); pane.add(btLoad, 1, 0);
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Mode Selection");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btNew.setOnAction((javafx.event.ActionEvent e) -> {
            setting(stage, 0);
        });
        btLoad.setOnAction((javafx.event.ActionEvent e) -> {
            startWithLoadedFile(stage);
        });
    }
    // 1 - case 1. Display menu for "employees" to assign films to each theater.
    private void setting(javafx.stage.Stage stage, int theaterIndex) { // assign filems to theaters
        // ================== JavaFX Event Source ==================
        // Parent (Pane) - Center
        javafx.scene.layout.GridPane centerPane = new javafx.scene.layout.GridPane();
        centerPane.setAlignment(javafx.geometry.Pos.CENTER);
        centerPane.setPadding(new javafx.geometry.Insets(10, 10, 10, 0));
        centerPane.setHgap(10); centerPane.setVgap(10);
        int index = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) {
                centerPane.add(films[index], i, j);
                index++;
            }
        }

        // Parent (Pane) - Left
        javafx.scene.text.Text text = new javafx.scene.text.Text("N/A");
        text.setFont(javafx.scene.text.Font.font("Arial", 15));
        javafx.scene.text.Text textForNotification = new javafx.scene.text.Text("(!) Film is not assigned");
        textForNotification.setFont(javafx.scene.text.Font.font("Arial", javafx.scene.text.FontWeight.EXTRA_LIGHT, 15));
        textForNotification.setStroke(javafx.scene.paint.Color.RED);
        javafx.scene.control.Label mode = new javafx.scene.control.Label("Employees Only");
        mode.setFont(javafx.scene.text.Font.font("Arial", javafx.scene.text.FontWeight.EXTRA_BOLD, 20));
        mode.setPadding(new javafx.geometry.Insets(10));
        mode.setStyle("-fx-border-color: red");
        javafx.scene.layout.VBox leftPane = new javafx.scene.layout.VBox();
        leftPane.getChildren().addAll(mode,
                new javafx.scene.control.Label("Theater Number:              " + theaterTime[theaterIndex].substring(8, 9)), 
                new javafx.scene.control.Label("Show-Time:                  " + theaterTime[theaterIndex].substring(12, theaterTime[theaterIndex].length())),
                new javafx.scene.control.Label("\n\nAssigned Film: "),
                text,
                textForNotification);
        leftPane.setPadding(new javafx.geometry.Insets(10));
        leftPane.setSpacing(10);
        
        // Parent (Pane) - Bottom
        javafx.scene.layout.HBox bottomPane = new javafx.scene.layout.HBox();
        bottomPane.setPadding(new javafx.geometry.Insets(10)); 
        bottomPane.setSpacing(10);
        bottomPane.setStyle("-fx-border-color: black");
        bottomPane.setAlignment(javafx.geometry.Pos.CENTER);
        bottomPane.getChildren().add(new javafx.scene.control.Label("Choose one of the films: "));
        javafx.scene.control.TextField tf = new javafx.scene.control.TextField();
        tf.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        tf.setMaxWidth(200);
        tf.setPrefColumnCount(filmTitles[6].length());
        bottomPane.getChildren().add(tf);
        
        // Parent (Pane) - Right
        javafx.scene.layout.VBox rightPane = new javafx.scene.layout.VBox();
        rightPane.getChildren().addAll(btOk);
        rightPane.setPadding(new javafx.geometry.Insets(10));
        rightPane.setSpacing(10);
        rightPane.setAlignment(javafx.geometry.Pos.CENTER);
        
        // Parent of Parent (Pane)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(new javafx.scene.control.ScrollPane(centerPane));
        pane.setBottom(bottomPane);
        pane.setRight(rightPane);
        pane.setLeft(leftPane);
        
        
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Setting");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btOk.setOnAction((javafx.event.ActionEvent e) -> {
            if (theaterIndex == 11) {
                menu(stage);
            }
            else { 
                setting(stage, theaterIndex + 1);
            }
        });
        tf.setOnAction(e -> {
            text.setText(tf.getText());
            switch (theaterIndex) {
                case 0:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    }
                    break;
                case 1:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 2:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 3:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;                
                case 4:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 5:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 6:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 7:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 8:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 9:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;               
                case 10:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
                case 11:
                    for (int i = 0; i < filmTitles.length; i++) {
                        if (filmTitles[i].equalsIgnoreCase(tf.getText())){
                            theaters[theaterIndex].setFilm(films[i]);
                            textForNotification.setText("Film is assigned!");
                            textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
                        }
                    } break;
            }
            tf.clear();
        });
    }
    // 1 - csae 2. Read the file to load all data needed for the program.
    private void startWithLoadedFile(javafx.stage.Stage stage) {
        java.io.File file = new java.io.File("saveFile.txt");
        try {
            if (file.exists()) {
                // Scanner Object Definition (File Connection, text I/O)
                java.util.Scanner inputFile = new java.util.Scanner(file);
                // Read (MyFilmPane - ticketsSold)
                for (int i = 0; i < films.length; i++) {
                    films[i].increaseTicketsSold(inputFile.nextInt());
                }
                // Read (MyTheater - MyFilmPane - filmIndex)
                for (int i = 0; i < theaters.length; i++) {
                    int temp = inputFile.nextInt();
                    if (temp != -1)
                        theaters[i].setFilm(films[temp]);
                }
                // Read (MyTheater - seatsClicked[], seatsBooked[], and seatsAvailable)
                for (int i = 0; i < theaters.length; i++) {
                    theaters[i].readFrom(inputFile);
                }
                // Close
                inputFile.close();
            }
        }
        catch (java.io.IOException exeption) {
            System.out.println("Input Error");
        }
        menu(stage);
    }
    
    // 2. Display menu for "customers" to ticket films, get theater information, and film information.
    private void menu(javafx.stage.Stage stage) {
        // ================== JavaFX Event Source ==================
        // Parent (Pane)
        javafx.scene.layout.GridPane pane = new javafx.scene.layout.GridPane();
        pane.setAlignment(javafx.geometry.Pos.CENTER);
        pane.setPadding(new javafx.geometry.Insets(5));
        pane.setHgap(5);
        pane.setVgap(5);
        pane.add(btTicket, 3, 0);
        pane.add(btStatus, 3, 1);
        pane.add(btReport, 3, 2);
        pane.add(btSave, 4, 5);
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Menu");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btTicket.setOnAction((javafx.event.ActionEvent e) -> {
            ticket1(stage);
        });
        btStatus.setOnAction((javafx.event.ActionEvent e) -> {
            theaterInformation(stage);
        });
        btReport.setOnAction((javafx.event.ActionEvent e) -> {
            filmInformation(stage);
        });
        btSave.setOnAction((javafx.event.ActionEvent e) -> {
            saveFile(stage);
        });
    }
    // 2 - optional. Record (Write) a file to save current data for employee.
    private void saveFile(javafx.stage.Stage stage) {
        java.io.File file = new java.io.File("saveFile.txt");
        try {
            if (!file.exists()) {
                // PrintWriter Object Definition (File Creation, text I/O)
                java.io.PrintWriter outputFile = new java.io.PrintWriter(file);
                saveProcess(outputFile);
                // Close
                outputFile.close();
            }
            else {
                // ================== JavaFX Event Source ==================
                // Buttons
                javafx.scene.control.Button btYes = new javafx.scene.control.Button("Yes");
                btYes.setPadding(new javafx.geometry.Insets(10));
                btYes.setMaxSize(50, 50);
                javafx.scene.control.Button btNo = new javafx.scene.control.Button("No");
                btNo.setPadding(new javafx.geometry.Insets(10));
                btNo.setMaxSize(50, 50);
                // Parent (Pane) - Top
                javafx.scene.control.Label top = new javafx.scene.control.Label(
                        "(!) You already have a saved file.\nDo you want to replace the file data?");
                // Parent (Pane) - Bottom
                javafx.scene.layout.HBox bottom = new javafx.scene.layout.HBox();
                bottom.setAlignment(javafx.geometry.Pos.CENTER);
                bottom.setSpacing(30);
                bottom.setPadding(new javafx.geometry.Insets(10));
                bottom.getChildren().addAll(btYes, btNo);
                // Parent of Parent (Pane)
                javafx.scene.layout.GridPane pane = new javafx.scene.layout.GridPane();
                pane.setAlignment(javafx.geometry.Pos.CENTER);
                pane.setPadding(new javafx.geometry.Insets(0));
                pane.setHgap(5);
                pane.setVgap(5);
                pane.add(top, 0, 0);
                pane.add(bottom, 0, 1);
                // Scene **********************************
                javafx.scene.Scene scene = new javafx.scene.Scene(pane, 300, 200);
                // Stage
                stage.setTitle("Save File");
                stage.setScene(scene);
                stage.setResizable(false);
                stage.show();
                // ================== JavaFX Event Handler =================
                btYes.setOnAction((javafx.event.ActionEvent e) -> {
                    try {
                        // PrintWriter Object Definition (File Creation, text I/O)
                        java.io.PrintWriter outputFile = new java.io.PrintWriter(file);
                        saveProcess(outputFile);
                        // Close
                        outputFile.close();
                    } catch (java.io.IOException exeption) {
                        System.out.println("Output Error");
                    }
                    menu(stage);
                });
                btNo.setOnAction((javafx.event.ActionEvent e) -> {
                    menu(stage);
                });
            }
        }
        catch (java.io.IOException exeption) {
            System.out.println("Output Error");
        }
    }
    private void saveProcess(java.io.PrintWriter outputFile) {
        // Write (MyFilmPane - ticketsSold)
        for (int i = 0; i < films.length; i++) {
            outputFile.println(new String() + films[i].getTicketsSold());
        }
        // Write (MyTheater - MyFilmPane - filmIndex)
        for (int i = 0; i < theaters.length; i++) {
            if (theaters[i].hasFilm())
                outputFile.println(new String() + theaters[i].getFilm().getFilmIndex());
            else
                outputFile.println(new String() + (-1));
        }
        // Write (MyTheater - seatsClicked[], seatsBooked[], and seatsAvailable)
        for (int i = 0; i < theaters.length; i++) {
            theaters[i].writeOn(outputFile);
        }
    }
    
    // 3-1. Ticketing Modules (Methods)
    private void ticket1(javafx.stage.Stage stage) {
        // ================== JavaFX Event Source ==================
        // Parent (Pane) - 1
        javafx.scene.layout.GridPane pane = new javafx.scene.layout.GridPane();
        pane.setAlignment(javafx.geometry.Pos.CENTER);
        pane.setPadding(new javafx.geometry.Insets(5));
        pane.setHgap(5);
        pane.setVgap(5);
        int index = 0;
        for (int col = 0; col < 4; col++) {
            for (int row = 0; row < 3; row++) {
                pane.add(btTheaters[index], row, col);
                index++;
            }
        }
        pane.add(btBack, 0, 6);
        // Parent (Pane) - 2
        javafx.scene.layout.VBox vPane = new javafx.scene.layout.VBox();
        javafx.scene.text.Text textForNotification = new javafx.scene.text.Text(400, 400, "Choose one of the options");
        textForNotification.setFont(javafx.scene.text.Font.font("Arial", javafx.scene.text.FontWeight.EXTRA_LIGHT, 15));
        textForNotification.setStroke(javafx.scene.paint.Color.GREEN);
        vPane.setAlignment(javafx.geometry.Pos.CENTER);
        vPane.getChildren().addAll(pane, textForNotification);
        
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(vPane, 800, 600);
        // Stage
        stage.setTitle("Theater by Show-Time");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btTheaters[0].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[0].hasFilm())
                ticket2(stage, 0);
            else
                changeText(textForNotification);
        });
        btTheaters[1].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[1].hasFilm())
                ticket2(stage, 1);
            else
                changeText(textForNotification);
        });
        btTheaters[2].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[2].hasFilm())
                ticket2(stage, 2);
            else
                changeText(textForNotification);
        });
        btTheaters[3].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[3].hasFilm())
                ticket2(stage, 3);
            else
                changeText(textForNotification);
        });
        btTheaters[4].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[4].hasFilm())
                ticket2(stage, 4);
            else
                changeText(textForNotification);
        });
        btTheaters[5].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[5].hasFilm())
                ticket2(stage, 5);
            else
                changeText(textForNotification);
        });
        btTheaters[6].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[6].hasFilm())
                ticket2(stage, 6);
            else
                changeText(textForNotification);
        });
        btTheaters[7].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[7].hasFilm())
                ticket2(stage, 7);
            else
                changeText(textForNotification);
        });
        btTheaters[8].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[8].hasFilm())
                ticket2(stage, 8);
            else
                changeText(textForNotification);
        });
        btTheaters[9].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[9].hasFilm())
                ticket2(stage, 9);
            else
                changeText(textForNotification);
        });
        btTheaters[10].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[10].hasFilm())
                ticket2(stage, 10);
            else
                changeText(textForNotification);
        });
        btTheaters[11].setOnAction((javafx.event.ActionEvent e) -> {
            if (theaters[11].hasFilm())
                ticket2(stage, 11);
            else
                changeText(textForNotification);
        });
        btBack.setOnAction((javafx.event.ActionEvent e) -> {
            menu(stage);
        });
    } 
    private void changeText(javafx.scene.text.Text textForNotification) {
        textForNotification.setStroke(javafx.scene.paint.Color.RED);
        textForNotification.setText("(!) Sorry, the film is not assigned");
    }
    private void ticket2(javafx.stage.Stage stage, int theaterIndex) {
        // ================== JavaFX Event Source ==================
        // Parent (Pane) - right
        
        // Parent (Pane) - Top
        javafx.scene.control.Label legend = new javafx.scene.control.Label("Seat Status");
        legend.setFont(javafx.scene.text.Font.font(STYLESHEET_MODENA, javafx.scene.text.FontWeight.EXTRA_BOLD, 30));
        javafx.scene.shape.Rectangle rec1 = new javafx.scene.shape.Rectangle(0, 0, 100, 50);
        javafx.scene.text.Text text1 = new javafx.scene.text.Text(15, 30, "AVAILIABLE");
        text1.setFont(javafx.scene.text.Font.font(STYLESHEET_MODENA, javafx.scene.text.FontWeight.EXTRA_BOLD, 12));
        rec1.setStroke(javafx.scene.paint.Color.BLACK);
        rec1.setFill(javafx.scene.paint.Color.WHITE);
        javafx.scene.shape.Rectangle rec2 = new javafx.scene.shape.Rectangle(110, 0, 100, 50);
        javafx.scene.text.Text text2 = new javafx.scene.text.Text(135, 30, "SELECTED");
        text2.setFont(javafx.scene.text.Font.font(STYLESHEET_MODENA, javafx.scene.text.FontWeight.EXTRA_BOLD, 12));
        rec2.setStroke(javafx.scene.paint.Color.BLACK);
        rec2.setFill(javafx.scene.paint.Color.GREEN);
        javafx.scene.shape.Rectangle rec3 = new javafx.scene.shape.Rectangle(220, 0, 100, 50);
        javafx.scene.text.Text text3 = new javafx.scene.text.Text(250, 30, "SOLD");
        text3.setFont(javafx.scene.text.Font.font(STYLESHEET_MODENA, javafx.scene.text.FontWeight.EXTRA_BOLD, 12));
        rec3.setStroke(javafx.scene.paint.Color.BLACK);
        rec3.setFill(javafx.scene.paint.Color.RED);
        javafx.scene.Group group = new javafx.scene.Group();
        group.getChildren().addAll(rec1,rec2,rec3, text1, text2, text3);
        javafx.scene.layout.VBox vbox = new javafx.scene.layout.VBox();
        vbox.getChildren().addAll(legend, group);
        vbox.setAlignment(javafx.geometry.Pos.CENTER);
        vbox.setPadding(new javafx.geometry.Insets(5));
        vbox.setStyle("-fx-border-color: black");
        javafx.scene.layout.Pane topPane = new javafx.scene.layout.StackPane(vbox);
        
        // Parent (Pane) - Bottom
        javafx.scene.layout.HBox bottomPane = new javafx.scene.layout.HBox();
        bottomPane.getChildren().addAll(btOk, btBack);
        bottomPane.setPadding(new javafx.geometry.Insets(5));
        bottomPane.setSpacing(10);
        bottomPane.setAlignment(javafx.geometry.Pos.CENTER);
        
        // Parent of Parent (Pane)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(theaters[theaterIndex]);
        pane.setBottom(bottomPane);
        pane.setTop(topPane);
        pane.setRight(theaters[theaterIndex].getFilm());
        
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Ticketing: " + theaterTime[theaterIndex]);
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btBack.setOnAction((javafx.event.ActionEvent e) -> {
            ticket1(stage);
        });
        btOk.setOnAction((javafx.event.ActionEvent e) -> {
            theaters[theaterIndex].bookSeat();
        });
        theaters[theaterIndex].getSeat(1).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(1));
        theaters[theaterIndex].getSeat(2).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(2));
        theaters[theaterIndex].getSeat(3).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(3));
        theaters[theaterIndex].getSeat(4).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(4));
        theaters[theaterIndex].getSeat(5).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(5));
        theaters[theaterIndex].getSeat(6).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(6));
        theaters[theaterIndex].getSeat(7).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(7));
        theaters[theaterIndex].getSeat(8).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(8));
        theaters[theaterIndex].getSeat(9).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(9));
        theaters[theaterIndex].getSeat(10).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(10));
        theaters[theaterIndex].getSeat(11).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(11));
        theaters[theaterIndex].getSeat(12).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(12));
        theaters[theaterIndex].getSeat(13).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(13));
        theaters[theaterIndex].getSeat(14).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(14));
        theaters[theaterIndex].getSeat(15).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(15));
        theaters[theaterIndex].getSeat(16).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(16));
        theaters[theaterIndex].getSeat(17).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(17));
        theaters[theaterIndex].getSeat(18).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(18));
        theaters[theaterIndex].getSeat(19).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(19));
        theaters[theaterIndex].getSeat(20).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(20));
        theaters[theaterIndex].getSeat(21).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(21));
        theaters[theaterIndex].getSeat(22).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(22));
        theaters[theaterIndex].getSeat(23).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(23));
        theaters[theaterIndex].getSeat(24).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(24));
        theaters[theaterIndex].getSeat(25).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(25));
        theaters[theaterIndex].getSeat(26).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(26));
        theaters[theaterIndex].getSeat(27).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(27));
        theaters[theaterIndex].getSeat(28).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(28));
        theaters[theaterIndex].getSeat(29).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(29));
        theaters[theaterIndex].getSeat(30).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(30));
        theaters[theaterIndex].getSeat(31).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(31));
        theaters[theaterIndex].getSeat(32).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(32));
        theaters[theaterIndex].getSeat(33).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(33));
        theaters[theaterIndex].getSeat(34).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(34));
        theaters[theaterIndex].getSeat(35).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(35));
        theaters[theaterIndex].getSeat(36).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(36));
        theaters[theaterIndex].getSeat(37).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(37));
        theaters[theaterIndex].getSeat(38).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(38));
        theaters[theaterIndex].getSeat(39).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(39));
        theaters[theaterIndex].getSeat(40).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(40));
        theaters[theaterIndex].getSeat(41).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(41));
        theaters[theaterIndex].getSeat(42).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(42));
        theaters[theaterIndex].getSeat(43).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(43));
        theaters[theaterIndex].getSeat(44).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(44));
        theaters[theaterIndex].getSeat(45).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(45));
        theaters[theaterIndex].getSeat(46).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(46));
        theaters[theaterIndex].getSeat(47).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(47));
        theaters[theaterIndex].getSeat(48).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(48));
        theaters[theaterIndex].getSeat(49).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(49));
        theaters[theaterIndex].getSeat(50).setOnAction((javafx.event.ActionEvent e) -> theaters[theaterIndex].clickSeat(50));

    }
    // 3-2. Theater Information Modules (Methods)
    private void theaterInformation(javafx.stage.Stage stage) {
        // Parent (Control) - Left
        javafx.scene.control.ListView<String> lvLeft = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(theaterTitles));
        lvLeft.setPrefSize(160, 600);
        lvLeft.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        
        // Parent (Control) - Center
        javafx.scene.control.ListView<String> lvCenter1 = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(
                        new String[]{"Theater 1 - 10 a.m.", "Theater 1 - 3 p.m.", "Theater 1 - 8 p.m."}));
        lvCenter1.setPrefSize(160, 600);
        lvCenter1.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        javafx.scene.control.ListView<String> lvCenter2 = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(
                        new String[]{"Theater 2 - 10 a.m.", "Theater 2 - 3 p.m.", "Theater 2 - 8 p.m."}));
        lvCenter2.setPrefSize(160, 600);
        lvCenter2.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        javafx.scene.control.ListView<String> lvCenter3 = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(
                        new String[]{"Theater 3 - 10 a.m.", "Theater 3 - 3 p.m.", "Theater 3 - 8 p.m."}));
        lvCenter3.setPrefSize(160, 600);
        lvCenter3.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        javafx.scene.control.ListView<String> lvCenter4 = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(
                        new String[]{"Theater 4 - 10 a.m.", "Theater 4 - 3 p.m.", "Theater 4 - 8 p.m."}));
        lvCenter4.setPrefSize(160, 600);
        lvCenter4.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        
        // Parent (Pane) - Bottom
        javafx.scene.layout.HBox bottomPane = new javafx.scene.layout.HBox();
        bottomPane.getChildren().addAll(btBack);
        bottomPane.setPadding(new javafx.geometry.Insets(10));
        bottomPane.setSpacing(10);
        bottomPane.setAlignment(javafx.geometry.Pos.CENTER);
        
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setLeft(lvLeft);
        pane.setBottom(bottomPane);
        
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Theater Information");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btBack.setOnAction((javafx.event.ActionEvent e) -> {
            menu(stage);
        });
        lvLeft.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lvLeft.getSelectionModel().getSelectedIndices()) {
                if (i == 0)
                    pane.setCenter(lvCenter1);
                else if (i == 1)
                    pane.setCenter(lvCenter2);
                else if (i == 2)
                    pane.setCenter(lvCenter3);
                else if (i == 3)
                    pane.setCenter(lvCenter4);
            }
        });
        // Parent (Pane) - Right (Conditional)
        lvCenter1.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lvCenter1.getSelectionModel().getSelectedIndices()) {
                if (theaters[i].hasFilm()) {
                    pane.setRight(getTheaterInformation(i));
                }
                else
                    pane.setRight(theaters[i].getFilm());
            }
        });
        lvCenter2.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lvCenter2.getSelectionModel().getSelectedIndices()) {
                if (theaters[i+3].hasFilm()) {
                    pane.setRight(getTheaterInformation(i + 3));}
                else
                    pane.setRight(theaters[i+3].getFilm());
            }
        });
        lvCenter3.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lvCenter3.getSelectionModel().getSelectedIndices()) {
                if (theaters[i+6].hasFilm()){
                    pane.setRight(getTheaterInformation(i + 6));
                }
                else
                    pane.setRight(theaters[i+6].getFilm());
            }
        });
        lvCenter4.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lvCenter4.getSelectionModel().getSelectedIndices()) {
                if (theaters[i+9].hasFilm()){
                    pane.setRight(getTheaterInformation(i + 9));}
                else
                    pane.setRight(theaters[i+9].getFilm());
            }
        });
                                
    }
    private javafx.scene.layout.VBox getTheaterInformation(int theaterIndex) {
        javafx.scene.layout.VBox rightPane = new javafx.scene.layout.VBox();
        rightPane.getChildren().add(theaters[theaterIndex].getFilm());
        javafx.scene.control.Label numSeatsAvailable = new javafx.scene.control.Label(
                "Number of Seats Available: " + theaters[theaterIndex].getSeatsAvailable());
        numSeatsAvailable.setFont(javafx.scene.text.Font.font("Arial", 15));
        numSeatsAvailable.setPadding(new javafx.geometry.Insets(5));
        numSeatsAvailable.setAlignment(javafx.geometry.Pos.CENTER);
        rightPane.getChildren().add(numSeatsAvailable);
        return rightPane;
    }
    // 3-3. Film Information Modules (Methods)
    private void filmInformation(javafx.stage.Stage stage) {
        // Parent (Control)
        javafx.scene.control.ListView<String> lv = 
                new javafx.scene.control.ListView<>(javafx.collections.FXCollections.observableArrayList(filmTitles));
        lv.setPrefSize(160, 600);
        lv.getSelectionModel().setSelectionMode(javafx.scene.control.SelectionMode.MULTIPLE);
        
        // Parent (Pane) - Bottom
        javafx.scene.layout.HBox bottomPane = new javafx.scene.layout.HBox();
        bottomPane.getChildren().addAll(btBack);
        bottomPane.setPadding(new javafx.geometry.Insets(10));
        bottomPane.setSpacing(10);
        bottomPane.setAlignment(javafx.geometry.Pos.CENTER);
        
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setLeft(lv);
        pane.setBottom(bottomPane);
        
        // Scene **********************************
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 800, 600);
        // Stage
        stage.setTitle("Film Information");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
        // ================== JavaFX Event Handler =================
        btBack.setOnAction((javafx.event.ActionEvent e) -> {
            menu(stage);
        });
        lv.getSelectionModel().selectedItemProperty().addListener(ov -> { 
            for (Integer i: lv.getSelectionModel().getSelectedIndices()) {
                pane.setCenter(films[i]);
                // display description
                int numOfChar = 40;
                int numPartition = 1;
                int length = films[i].getFilmDescription().length();
                while (length > numOfChar) {
                    numPartition++;
                    length -= numOfChar;
                }
                javafx.scene.layout.VBox rightPane = new javafx.scene.layout.VBox();
                rightPane.getChildren().add(new javafx.scene.control.Label("Description: "));
                for (int subindex = 0; subindex < numPartition - 1; subindex++) {
                    int beginnigIndex = subindex * numOfChar;
                    String temp = films[i].getFilmDescription().substring(beginnigIndex, beginnigIndex + numOfChar);
                    rightPane.getChildren().add(new javafx.scene.control.Label(temp));
                } rightPane.getChildren().add(new javafx.scene.control.Label(films[i].getFilmDescription().substring((numPartition - 1) * numOfChar, films[i].getFilmDescription().length())));
                rightPane.setPadding(new javafx.geometry.Insets(10));
                rightPane.setStyle("-fx-background-color: white; -fx-border-color: black");
                // total tickets sold by film 
                javafx.scene.control.Label numTicketsSold = new javafx.scene.control.Label("\n\nNumber of Tickets Sold: " + films[i].getTicketsSold());
                numTicketsSold.setFont(javafx.scene.text.Font.font("Arial", 15));
                rightPane.getChildren().add(numTicketsSold);
                pane.setRight(rightPane);
            }
        });
    }
}