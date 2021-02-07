<?php
require('dbconnect.php');
include("authorization.php");
session_start();
$status = "";
if(isset($_POST['new']) && $_POST['new']==1){
    $trn_date = date("Y-m-d H:i:s");
    $name =$_REQUEST['name'];
    $username =$_REQUEST['username'];
    $email = $_REQUEST['email'];
    $foodcontent = $_REQUEST['foodcontent'];
    $Pickupaddress = $_REQUEST['Pickupaddress'];
    $estimatednoofpeople = $_REQUEST['estimatednoofpeople'];
    $Phonenumber =$_REQUEST['Phonenumber'];
    $ins_query="INSERT into `Appointments`
    (`trn_date`,`name`,`username`,`email`,`foodcontent`,`Pickupaddress`,`estimatednoofpeople`, `Phonenumber`)values
    ('$trn_date','$name','$username','$email','$foodcontent','$Pickupaddress','$estimatednoofpeople','$Phonenumber')";
    $result = mysqli_query($con,$ins_query)
    or die(mysql_error());
    $_SESSION["username"] = $username;
    $status = "New Record Inserted Successfully.
    </br></br><a href='view.php'>View Inserted Record</a>";
}
?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
  font-size: 17px;
}

#myVideo {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
}
.form {
position: fixed;
top: 0%;
left: 40%;

  background: rgba(0, 0, 0, 0.5);
  color: #f1f1f1;
  width: 100%;
height: 900px;
padding: 20px;
}
</style>
</head>
<html>
<head>
<meta charset="utf-8">
<title>Insert New Record</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<video autoplay muted loop id="myVideo">
<source src="https://player.vimeo.com/external/220260309.sd.mp4?s=6ba5ae83e887a8a9cb4f72097b3404f68b519f99&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
<div class="form">
<p><a href="index.php">Home</a>
| <a href="view.php">View Appointments</a>
| <a href="logout.php">Logout</a></p>
<div>
<h1>Insert New Record</h1>
<form name="form" method="post" action="">
<input type="hidden" name="new" value="1" />
<p><input type="text" name="name" placeholder="Enter Name" required /></p>
<p><input type="text" name="username" placeholder="Enter Username" required /></p>
<p><input type="email" name="email" placeholder="Enter email address" required /></p>
<p><input type="text" name="foodcontent" placeholder="Enter the food content" required /></p>
<p><input type="text" name="Pickupaddress" placeholder="Enter the Pickup address" required /></p>
<p><input type="text" name="estimatednoofpeople" placeholder="Enter no of people to eat" required /></p>
<p><input type="text" name="Phonenumber" placeholder="Enter Phonenumber" required /></p>
<p><input name="submit" type="submit" value="Submit" /></p>
</form>
<p style="color:#FF0000;"><?php echo $status; ?></p>
</div>
</div>
</body>
</html>
