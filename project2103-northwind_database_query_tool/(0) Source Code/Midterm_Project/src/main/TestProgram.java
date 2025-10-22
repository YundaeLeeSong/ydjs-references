package main;

public class TestProgram extends javafx.application.Application { 
    /*
        Attributes (for Window Control)
    */
    private javafx.scene.control.Button backButton;
    private javafx.scene.control.Button task1Button;
    private javafx.scene.control.Button task2Button;
    private javafx.scene.control.Button task3Button;
    private javafx.scene.control.Button task4Button;
    /*
        Attributes (for Program Works)
    */
    private javafx.scene.control.ComboBox<String> cboTableName;     // for database
    private javafx.scene.control.Button btShowContents;
    private javafx.scene.control.TextArea taContents;
    private javafx.scene.control.TextArea taResult;                 // for tasks
    private javafx.scene.control.Label caution;                 
    private javafx.scene.control.TextField tfOrderID1;
    private javafx.scene.control.Button btShow1;
    private javafx.scene.control.TextField tfOrderID2;
    private javafx.scene.control.Button btShow2;
    private javafx.scene.control.TextField tfState3;
    private javafx.scene.control.Button btShow3;
    private javafx.scene.control.TextField tfYear4;
    private javafx.scene.control.Button btShow4;
    private java.sql.Statement stmt;
    
    /*
        Constructor (Initialization)
    */
    public TestProgram() {
        backButton = new javafx.scene.control.Button("Back");
        backButton.setAlignment(javafx.geometry.Pos.CENTER_RIGHT);
        task1Button = new javafx.scene.control.Button("#1 - ******* Order Total *******");
        task2Button = new javafx.scene.control.Button("#2 - ****** Order Details ******");
        task3Button = new javafx.scene.control.Button("#3 - ** Customers Information **");
        task4Button = new javafx.scene.control.Button("#4 - *** Employees Birthday ****");
        task1Button.setMinSize(200, 50);
        task2Button.setMinSize(200, 50);
        task3Button.setMinSize(200, 50);
        task4Button.setMinSize(200, 50);
        cboTableName = new javafx.scene.control.ComboBox<>();
        btShowContents = new javafx.scene.control.Button("Show Contents");
        taContents = new javafx.scene.control.TextArea();
        taContents.setPrefSize(600, 400);
        taContents.setEditable(false);
        taContents.setFont(javafx.scene.text.Font.font("Arial", 12));
        taResult = new javafx.scene.control.TextArea();
        taResult.setPrefSize(500, 400);
        taResult.setEditable(false);
        caution = new javafx.scene.control.Label();
        caution.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        tfOrderID1 = new javafx.scene.control.TextField();  
        btShow1 = new javafx.scene.control.Button("Task #1 Execute");
        tfOrderID2 = new javafx.scene.control.TextField();
        btShow2 = new javafx.scene.control.Button("Task #2 Execute");
        tfState3 = new javafx.scene.control.TextField();
        btShow3 = new javafx.scene.control.Button("Task #3 Execute");
        tfYear4 = new javafx.scene.control.TextField();
        btShow4 = new javafx.scene.control.Button("Task #4 Execute");
        try {
            // 1. Load the JDBC driver
            java.lang.Class.forName("oracle.jdbc.driver.OracleDriver");
        } 
        catch (java.lang.ClassNotFoundException ex) { 
            System.out.println("(!) ClassNotFoundException"); 
        }        
        try {
            // 2. Establish a connection
            java.sql.Connection connection = java.sql.DriverManager.getConnection(
                    "jdbc:oracle:thin:@localhost:1521:XE",
                    "SYSTEM", "2232");
            // 3. Create a statement and metadata
            stmt = connection.createStatement();
            java.sql.DatabaseMetaData dbMetaData = connection.getMetaData();            
            java.sql.ResultSet rsTables 
                    = dbMetaData.getTables(null, null, null, new String[] {"TABLE"});
            while (rsTables.next()) {
                String tableName = new String(rsTables.getString("TABLE_NAME"));
                if (tableName.substring(0, 3).compareTo("JDB") == 0)
                    cboTableName.getItems().add(tableName);
            } 
            cboTableName.getSelectionModel().selectFirst();
        } 
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    }
    
    /*
        Methods (Windows)
    */
    @Override // Override the start method in the Application class
    public void start(javafx.stage.Stage primaryStage) {   
        // Parent (Pane for panes)
        javafx.scene.layout.VBox pane 
                = new javafx.scene.layout.VBox(10, new javafx.scene.control.Label(
                        "< Midterm Project >"), task1Button, task2Button, 
                        task3Button, task4Button);
        pane.setPadding(new javafx.geometry.Insets(10));
        pane.setAlignment(javafx.geometry.Pos.CENTER);
        // Scene
        javafx.scene.Scene scene = new javafx.scene.Scene(pane, 600, 400);
        // Stage
        primaryStage.setTitle("Midterm_Project");
        primaryStage.setScene(scene); 
        primaryStage.show();
        // ================== JavaFX Event Handler =================
        task1Button.setOnAction(e -> task1(primaryStage));  
        task2Button.setOnAction(e -> task2(primaryStage));
        task3Button.setOnAction(e -> task3(primaryStage));
        task4Button.setOnAction(e -> task4(primaryStage));
    }
    public void task1(javafx.stage.Stage primaryStage) {   
        // Starting Set Up
        String explain = "The program will ask the user for an order number, "
                + "and then print out the total for all products in the order, "
                + "considering quantities and discounts.";
        caution.setText(explain);
        taContents.setText("You can look up the Northwind database here. \n"
                + "Use the combo box on the top!");
        taResult.setText("You will check your answer here.");
        
        // ======================== JavaFX ========================
        // Parent (Pane)
        javafx.scene.layout.HBox hBox = new javafx.scene.layout.HBox(5);
        hBox.getChildren().addAll(new javafx.scene.control.Label("Table Name"), 
                cboTableName, btShowContents);
        hBox.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        hBox.setPadding(new javafx.geometry.Insets(10));
        javafx.scene.layout.HBox child = new javafx.scene.layout.HBox(5,
                new javafx.scene.control.Label("Enter an order ID: "),
                tfOrderID1,
                btShow1); 
        child.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.HBox buttonSet = new javafx.scene.layout.HBox(backButton); 
        buttonSet.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.VBox task1 = new javafx.scene.layout.VBox(20, caution, child, buttonSet);
        task1.setPadding(new javafx.geometry.Insets(10));
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(new javafx.scene.control.ScrollPane(taContents));
        pane.setRight(new javafx.scene.control.ScrollPane(taResult));
        pane.setTop(hBox);
        pane.setBottom(task1);
        pane.setPadding(new javafx.geometry.Insets(10));
        // Scene
        javafx.scene.Scene scene = new javafx.scene.Scene(pane);
        // Stage
        primaryStage.setTitle("Midterm_Project_Task#1");
        primaryStage.setScene(scene); 
        primaryStage.show();
        // ================== JavaFX Event Handler =================
        btShowContents.setOnAction(e -> showContents());  
        backButton.setOnAction(e -> {
            deleteContents(); 
            start(primaryStage);
        });
        btShow1.setOnAction(e -> showTask1(explain));
    }
    public void task2(javafx.stage.Stage primaryStage) {   
        // Starting Set Up
        String explain = "The program will ask the user for an order number, "
                + "and then print the order date, freight charge, "
                + "and all products and their quantity, unit price, "
                + "and discount for the order.";
        caution.setText(explain);
        taContents.setText("You can look up the Northwind database here. \n"
                + "Use the combo box on the top!");
        taResult.setText("You will check your answer here.");
        
        // ======================== JavaFX ========================
        // Parent (Pane)
        javafx.scene.layout.HBox hBox = new javafx.scene.layout.HBox(5);
        hBox.getChildren().addAll(new javafx.scene.control.Label("Table Name"), 
                cboTableName, btShowContents);
        hBox.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        hBox.setPadding(new javafx.geometry.Insets(10));
        javafx.scene.layout.HBox child = new javafx.scene.layout.HBox(5,
                new javafx.scene.control.Label("Enter an order ID: "),
                tfOrderID2,
                btShow2); 
        child.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.HBox buttonSet = new javafx.scene.layout.HBox(backButton); 
        buttonSet.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.VBox task1 = new javafx.scene.layout.VBox(20, caution, child, buttonSet);
        task1.setPadding(new javafx.geometry.Insets(10));
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(new javafx.scene.control.ScrollPane(taContents));
        pane.setRight(new javafx.scene.control.ScrollPane(taResult));
        pane.setTop(hBox);
        pane.setBottom(task1);
        pane.setPadding(new javafx.geometry.Insets(10));
        // Scene
        javafx.scene.Scene scene = new javafx.scene.Scene(pane);
        // Stage
        primaryStage.setTitle("Midterm_Project_Task#2");
        primaryStage.setScene(scene); 
        primaryStage.show();
        // ================== JavaFX Event Handler =================
        btShowContents.setOnAction(e -> showContents());  
        backButton.setOnAction(e -> {
            deleteContents(); 
            start(primaryStage);
        });
        btShow2.setOnAction(e -> showTask2(explain));
    }
    public void task3(javafx.stage.Stage primaryStage) {   
        // Starting Set Up
        String explain = "The program will ask the user for a state, "
                + "and then print out the contact names and cities of "
                + "all customers in this state in order by city.";
        caution.setText(explain);
        taContents.setText("You can look up the Northwind database here. \n"
                + "Use the combo box on the top!");
        taResult.setText("You will check your answer here.");
        
        // ======================== JavaFX ========================
        // Parent (Pane)
        javafx.scene.layout.HBox hBox = new javafx.scene.layout.HBox(5);
        hBox.getChildren().addAll(new javafx.scene.control.Label("Table Name"), 
                cboTableName, btShowContents);
        hBox.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        hBox.setPadding(new javafx.geometry.Insets(10));
        javafx.scene.layout.HBox child = new javafx.scene.layout.HBox(5,
                new javafx.scene.control.Label("Enter a state: "),
                tfState3,
                btShow3); 
        child.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.HBox buttonSet = new javafx.scene.layout.HBox(backButton); 
        buttonSet.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.VBox task1 = new javafx.scene.layout.VBox(20, caution, child, buttonSet);
        task1.setPadding(new javafx.geometry.Insets(10));
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(new javafx.scene.control.ScrollPane(taContents));
        pane.setRight(new javafx.scene.control.ScrollPane(taResult));
        pane.setTop(hBox);
        pane.setBottom(task1);
        pane.setPadding(new javafx.geometry.Insets(10));
        // Scene
        javafx.scene.Scene scene = new javafx.scene.Scene(pane);
        // Stage
        primaryStage.setTitle("Midterm_Project_Task#3");
        primaryStage.setScene(scene); 
        primaryStage.show();
        // ================== JavaFX Event Handler =================
        btShowContents.setOnAction(e -> showContents());  
        backButton.setOnAction(e -> {
            deleteContents(); 
            start(primaryStage);
        });
        btShow3.setOnAction(e -> showTask3(explain));
    }
    public void task4(javafx.stage.Stage primaryStage) {   
        // Starting Set Up
        String explain = "The program will ask the user for a year, "
                + "and then print out the first names and last names "
                + "(in alphabetical order by last name) of all employees "
                + "who were born during that year.";
        caution.setText(explain);
        taContents.setText("You can look up the Northwind database here. \n"
                + "Use the combo box on the top!");
        taResult.setText("You will check your answer here.");
        // ======================== JavaFX ========================
        // Parent (Pane)
        javafx.scene.layout.HBox hBox = new javafx.scene.layout.HBox(5);
        hBox.getChildren().addAll(new javafx.scene.control.Label("Table Name"), 
                cboTableName, btShowContents);
        hBox.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
        hBox.setPadding(new javafx.geometry.Insets(10));
        javafx.scene.layout.HBox child = new javafx.scene.layout.HBox(5,
                new javafx.scene.control.Label("Enter an year: "),
                tfYear4,
                btShow4); 
        child.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.HBox buttonSet = new javafx.scene.layout.HBox(backButton); 
        buttonSet.setAlignment(javafx.geometry.Pos.TOP_RIGHT);
        javafx.scene.layout.VBox task1 = new javafx.scene.layout.VBox(20, caution, child, buttonSet);
        task1.setPadding(new javafx.geometry.Insets(10));
        // Parent (Pane for panes)
        javafx.scene.layout.BorderPane pane = new javafx.scene.layout.BorderPane();
        pane.setCenter(new javafx.scene.control.ScrollPane(taContents));
        pane.setRight(new javafx.scene.control.ScrollPane(taResult));
        pane.setTop(hBox);
        pane.setBottom(task1);
        pane.setPadding(new javafx.geometry.Insets(10));
        // Scene
        javafx.scene.Scene scene = new javafx.scene.Scene(pane);
        // Stage
        primaryStage.setTitle("Midterm_Project_Task#4");
        primaryStage.setScene(scene); 
        primaryStage.show();
        // ================== JavaFX Event Handler =================
        btShowContents.setOnAction(e -> showContents());  
        backButton.setOnAction(e -> {
            deleteContents(); 
            start(primaryStage);
        });
        btShow4.setOnAction(e -> showTask4(explain));
    }
    
    /*
        Methods (Internal Works for Attributes Modification)
    */
    private void showContents() {    
        try {
            taContents.clear();
            // 4..... SQL command
            String tableName = cboTableName.getValue();
            String queryString = "select * from " + tableName;
            // 4. Execute a statement
            java.sql.ResultSet resultSet = stmt.executeQuery(queryString);
            java.sql.ResultSetMetaData rsMetaData = resultSet.getMetaData();
            // 5. Iterate through the result
            
            ///******* Settings
            java.util.ArrayList<Integer> maxLengths = new java.util.ArrayList<>();
            String nullString = new java.lang.String("(null)");
            if (resultSet.next()) {
                for (int i = 1; i <= rsMetaData.getColumnCount(); i++) {
                    if (resultSet.getString(i) != null) {
                        maxLengths.add(resultSet.getString(i).length());
                    }
                    else {
                        maxLengths.add(nullString.length());
                    }
                }
            } resultSet = stmt.executeQuery(queryString);
            while (resultSet.next()) {
                for (int i = 1; i <= rsMetaData.getColumnCount(); i++) {
                    if (resultSet.getString(i) != null) {
                        if (maxLengths.get(i-1) < resultSet.getString(i).length())
                            maxLengths.set(i-1, resultSet.getString(i).length());
                    }
                    else {
                        if (maxLengths.get(i-1) < nullString.length())
                            maxLengths.set(i-1, nullString.length());
                    }
                }
            } resultSet = stmt.executeQuery(queryString);
            
            ///******* Header
            String command;
            for (int i = 1; i <= rsMetaData.getColumnCount(); i++) {    
                command = "%-" + (maxLengths.get(i-1).intValue() + 2) +"s\t|\t";
                taContents.appendText(java.lang.String.format(command, 
                        rsMetaData.getColumnName(i).toLowerCase())
                );
            }
            taContents.appendText("\n----------------------------------------------------------"
                    + "----------------------------------------------------------------------");
            
            ///******* Contents
            String text;
            String subtext1, subtext2;
            taContents.appendText("\n");
            while (resultSet.next()) {
                for (int i = 1; i <= rsMetaData.getColumnCount(); i++) {
                    // Format String
                    command = "%-" + (maxLengths.get(i-1).intValue() + 2) +"s\t|\t";
                    // Validation on Bad Data
                    text = resultSet.getString(i);
                    int newlineIndex;
                    if (text != null) {
                        for (int index = 0; index < text.length(); index++) {
                            if (text.charAt(index) == '\n') {
                                newlineIndex = index;
                                subtext1 = text.substring(0, newlineIndex);
                                subtext2 = text.substring(newlineIndex+1);
                                text = subtext1.trim() + ' ' + subtext2.trim();
                            }
                        }
                    }
                    taContents.appendText(java.lang.String.format(command, 
                            text)
                    );
                }
                taContents.appendText("\n");
            }
        }
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    } 
    private void deleteContents() {
        taContents.clear();
        taResult.clear();
        caution.setText("");
        caution.setTextFill(javafx.scene.paint.Color.BLACK);
        tfOrderID1.setText("");
        tfOrderID2.setText("");
        tfState3.setText("");
        tfYear4.setText("");
    } 
    private void showTask1(String explain) {    
        try {
            boolean isEmpty = true;
            taResult.clear();
            
            // 4..... SQL command
            String orderID = tfOrderID1.getText();
            String queryString 
                    = "SELECT unitprice * quantity * (1 - discount) "
                    + "FROM jdbc_orderdetails "
                    + "WHERE orderid = " + orderID;
            // 4. Execute a statement
            java.sql.ResultSet resultSet = stmt.executeQuery(queryString);
            java.sql.ResultSetMetaData rsMetaData = resultSet.getMetaData();
            // 5. Iterate through the result
            
            
            ///******* Header
            taResult.appendText(java.lang.String.format("%17s", "Total Price")
                );
            taResult.appendText("\n");
            taResult.appendText("---------------------------\n");
            ///******* Result
            java.util.ArrayList<Double> totals = new java.util.ArrayList<>();
            int counter = -1;
            taResult.appendText("Subtotals: \n");
            while (resultSet.next()) {
                counter++;
                isEmpty = false;
                totals.add(java.lang.Double.valueOf(resultSet.getString(1).trim()));
                taResult.appendText(java.lang.String.format("\t\t\t$ %-17.2f", totals.get(counter)));
                taResult.appendText("\n");          // total for each product
            }
            double accumulator = 0;
            if (counter >= 0) {
                for (int i = 0; i < totals.size();i++) { 
                    accumulator += totals.get(i);
                }
                taResult.appendText("---------------------------\n");
                taResult.appendText("Total Cost: \n");
                taResult.appendText(java.lang.String.format("\t\t\t$ %-17.2f", accumulator));
                taResult.appendText("\n");          // total for a single order id
            }
                
            
            
            
            
            if (isEmpty) {
                caution.setText("Sorry, data is not found. Have another try!");
                caution.setTextFill(javafx.scene.paint.Color.RED);
            }
            else {
                caution.setText(explain + " (Data Found)");
                caution.setTextFill(javafx.scene.paint.Color.GREEN);
            }
                
        }
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    } 
    private void showTask2(String explain) {    
        try {
            boolean isEmpty = true;
            taResult.clear();
            
            // 4..... SQL command
            String orderID = tfOrderID2.getText(); // Important ************
            String queryString 
                    = "SELECT jdbc_orders.orderdate, "
                    + "jdbc_orders.freight, "
                    + "jdbc_products.productname, "
                    + "jdbc_orderdetails.quantity, "
                    + "jdbc_orderdetails.unitprice, "
                    + "jdbc_orderdetails.discount "
                    + "FROM jdbc_orders, jdbc_products, jdbc_orderdetails "
                    + "WHERE (jdbc_orderdetails.orderid = jdbc_orders.orderid "
                    + "AND jdbc_products.productid = jdbc_orderdetails.productid "
                    + "AND jdbc_orders.orderid = "+ orderID +")";
            // 4. Execute a statement
            java.sql.ResultSet resultSet = stmt.executeQuery(queryString);
            java.sql.ResultSetMetaData rsMetaData = resultSet.getMetaData();
            // 5. Iterate through the result
            
            ///******* Header
            taResult.appendText(java.lang.String.format("%80s", "Order Details")
                );
            taResult.appendText("\n");
            taResult.appendText("-----------------------------"
                    + "-----------------------------------------"
                    + "---------------------------------------------------\n");
            taResult.appendText(java.lang.String.format("%-12s|\t%-16s|\t%-10s|"
                    + "\t%-12s|\t%-10s|\t%-40s", 
                    "Order Date", 
                    "Freight Charge", 
                    "Quantity", 
                    "Unit Price", 
                    "Discount",
                    "Product Name")
                );
            taResult.appendText("\n");
            taResult.appendText("-----------------------------"
                    + "-----------------------------------------"
                    + "---------------------------------------------------\n");
            
            ///******* Result 
            while (resultSet.next()) {
                isEmpty = false;
                taResult.appendText(java.lang.String.format("%-12s\t|\t$ "
                        + "%-14.2f|\t%-10d\t|\t$ %-10.2f\t|\t%9.0f%%\t|\t%-40s", 
                        resultSet.getString(1).trim().substring(0, 10), 
                        java.lang.Double.valueOf(resultSet.getString(2).trim()), 
                        java.lang.Integer.valueOf(resultSet.getString(4).trim()), 
                        java.lang.Double.valueOf(resultSet.getString(5).trim()), 
                        java.lang.Double.valueOf(resultSet.getString(6).trim())*100.0, 
                        resultSet.getString(3).trim())
                );
                taResult.appendText("\n");
            }
            
            if (isEmpty) {
                caution.setText("Sorry, data is not found. Have another try!");
                caution.setTextFill(javafx.scene.paint.Color.RED);
            }
            else {
                caution.setText(explain + " (Data Found)");
                caution.setTextFill(javafx.scene.paint.Color.GREEN);
            }
                
        }
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    } 
    private void showTask3(String explain) {    
        try {
            boolean isEmpty = true;
            taResult.clear();
            
            // 4..... SQL command
            String region = tfState3.getText(); // Important ************
            String queryString 
                    = "SELECT contactname, city "
                    + "FROM jdbc_customers "
                    + "WHERE(region = '" + region + "') "
                    + "ORDER BY city ASC NULLS LAST";
            // 4. Execute a statement
            java.sql.ResultSet resultSet = stmt.executeQuery(queryString);
            java.sql.ResultSetMetaData rsMetaData = resultSet.getMetaData();
            // 5. Iterate through the result
            
            ///******* Header
            taResult.appendText(java.lang.String.format("%-30s\t|%10s",
                    "Customer Name", 
                    "City")
            );
            taResult.appendText("\n");
            taResult.appendText("-----------------------------"
                    + "-------------------------\n");
            ///******* Result
            while (resultSet.next()) {
                isEmpty = false;
                taResult.appendText(java.lang.String.format("%-30s\t|%10s", 
                            resultSet.getString(1), 
                            resultSet.getString(2)));                  
                taResult.appendText("\n");
            }
            
            if (isEmpty) {
                caution.setText("Sorry, data is not found. Have another try!");
                caution.setTextFill(javafx.scene.paint.Color.RED);
            }
            else {
                caution.setText(explain + " (Data Found)");
                caution.setTextFill(javafx.scene.paint.Color.GREEN);
            }
        }
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    } 
    private void showTask4(String explain) {    
        try {
            boolean isEmpty = true;
            taResult.clear();
            
            // 4..... SQL command
            String year = tfYear4.getText();
            if (year.length() == 4)
                year = year.substring(2);
            else
                year = "a";
            String queryString 
                    = "SELECT firstname, lastname "
                    + "FROM jdbc_employees "
                    + "WHERE (birthdate LIKE '%" + year + "') "
                    + "ORDER BY lastname ASC NULLS LAST";
            // 4. Execute a statement
            java.sql.ResultSet resultSet = stmt.executeQuery(queryString);
            java.sql.ResultSetMetaData rsMetaData = resultSet.getMetaData();
            // 5. Iterate through the result
            
            ///******* Header
            taResult.appendText("Employee Name");
            taResult.appendText("\n");
            taResult.appendText("-----------------------------\n");
            ///******* Result
            while (resultSet.next()) {
                isEmpty = false;
                taResult.appendText(resultSet.getString(1) + " " + resultSet.getString(2));     
                // Contents
                taResult.appendText("\n");
            }

            if (isEmpty) {
                caution.setText("Sorry, data is not found. Have another try!");
                caution.setTextFill(javafx.scene.paint.Color.RED);
            }
            else {
                caution.setText(explain + " (Data Found)");
                caution.setTextFill(javafx.scene.paint.Color.GREEN);
            }
        }
        catch (java.sql.SQLException ex) { System.out.println("(!) SQLException"); }
    } 
    
    /*
        main Function
    */
    public static void main(String[] args) {
        launch(args);
    }
}