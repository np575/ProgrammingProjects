<?php
#turn error reporting on
ini_set('display_errors',1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
//pull in config.php so we can access the variables from it
require('dbconnect.php');
$conn_string = "mysql:host=$host;dbname=$database;charset=utf8mb4";

try{
        $db = new PDO($conn_string, $username, $password);
        echo "Connected";
        //create table
        $query ="CREATE TABLE IF NOT EXISTS `vol2` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `name` varchar(50) NOT NULL,
                 `username` varchar(50) NOT NULL,
		`email` varchar(50) NOT NULL,
                `Availability` varchar(400) NOT NULL,
		`Phonenumber` int(10) NOT NULL,
                `trn_date` datetime NOT NULL,
                PRIMARY KEY (`id`)
                )CHARACTER SET utf8 COLLATE utf8_general_ci";
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
        $stmt = $db->prepare($query);
        print_r($stmt->errorInfo());
        $r = $stmt->execute();
        echo "<br>" . ($r>0?"Created table or already exists":"Failed to create table") . "<br>";
        unset($r);
        //simple insert
        //TODO/homework make values variables bindable
        $insert_query = "INSERT INTO `vol2`( 'name', 'id','username','Availability', 'email', 'trn_date', 'Phonenumber')
                         VALUES (?, ?, ?, ?, ?, ?, ?)";
        $stmt = $db->prepare($insert_query);
        //TODO catch error from DB

        //TODO select query using bindable :username is where clause
        //select * from TestUsers where username =
}
catch(Exception $e){
        echo $e->getMessage();
        exit("Something went wrong");
}
?>

