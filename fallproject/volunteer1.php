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
    $Availability =$_REQUEST['Availability'];
    $Phonenumber =$_REQUEST['Phonenumber'];
    $ins_query="INSERT into `vol2`
    (`trn_date`,`name`,`username`, `email`,`Availability`,`Phonenumber`)values
    ('$trn_date','$name','$username','$email','$Availability','$Phonenumber')";
    $result = mysqli_query($con,$ins_query)
    or die(mysql_error());
    $_SESSION["username"] = $username;
    $status = "New Record Inserted Successfully.
    </br></br><a href='view1.php'>View and Edit Availability</a>";
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
position: absolute;
top: 0%;
margin: auto;
left: 40%;
background-color: rgba(0,0,0,0.6);
width: 300px;
height: 600px;
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
| <a href="logout.php">Logout</a></p>
<div>
<form name="form" method="post" action="">
<input type="hidden" name="new" value="1" />
<p><input type="text" name="name" placeholder="Enter Name" required /></p>
<p><input type="text" name="username" placeholder="Enter username" required /></p>
<p><input type="email" name="email" placeholder="Enter email address" required /></p>
<p><input type="text" name="Phonenumber" placeholder="Enter Phonenumber" required /></p>
<p><textarea type="text" name="Availability" row="7" cols="35" placeholder="Enter Availability" required /></textarea></p>
<p><input name="submit" type="submit" value="Submit" /></p>
</form>
<p style="color:#FF0000;"><?php echo $status; ?></p>
</div>
</div>
</body>
</html>
