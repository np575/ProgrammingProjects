<?php
require('dbconnect.php');
include("authorization.php");
session_start();
$id=$_REQUEST['id'];
$query = "SELECT * from Appointments where id='".$id."'";
$result = mysqli_query($con, $query) or die ( mysqli_error());
$row = mysqli_fetch_assoc($result);
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
height: 750px;
padding: 20px;}
.form h1
{
font-size: 20px;
font-weight: 100;
letter-spacing: 5px;
margin-bottom: 30px;
}
.form h2:hover
{
font-size: 20px;
color: #fff;
padding: 7px 22px;
text-decoration: none;
border: 1px solid coral;
border-radius: 25px;
font-weight: 100;
letter-spacing: 5px;
background: coral;
margin-bottom: 30px;
transition: .5s;
}
.form h3:hover
{
font-size: 20px;
color: #fff;
padding: 7px 22px;
text-decoration: none;
border: 1px solid coral;
border-radius: 25px;
font-weight: 100;
letter-spacing: 5px;
background: coral;
margin-bottom: 30px;
transition: .5s;
}
.form h4:hover
{
font-size: 20px;
color: #fff;
padding: 7px 22px;
text-decoration: none;
border: 1px solid coral;
border-radius: 25px;
font-weight: 100;
letter-spacing: 5px;
background: coral;
margin-bottom: 30px;
transition: .5s;
}
.form h5:hover
{
font-size: 20px;
color: #fff;
padding: 7px 22px;
text-decoration: none;
border: 1px solid coral;
border-radius: 25px;
font-weight: 100;
letter-spacing: 5px;
background: coral;
margin-bottom: 30px;
transition: .5s;
}

</style>
</head>

<html>
<head>
<meta charset="utf-8">
<title>Update Record</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<video autoplay muted loop id="myVideo">
  <source src="https://player.vimeo.com/external/220260309.sd.mp4?s=6ba5ae83e887a8a9cb4f72097b3404f68b519f99&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
<div class="form">
<p><a href="index.php">Home</a>
| <a href="insert.php">Create New Appointment</a>
| <a href="logout.php">Logout</a></p>
<h1>Update Record</h1>
<?php
session_start();
$status = "";
if(isset($_POST['new']) && $_POST['new']==1)
{
$id=$_REQUEST['id'];
$trn_date = date("Y-m-d H:i:s");
$name =$_REQUEST['name'];
$email =$_REQUEST['email'];
$foodcontent=$_REQUEST['foodcontent'];
$Pickupaddress =$_REQUEST['Pickupaddress'];
$estimatednoofpeople =$_REQUEST['estimatednoofpeople'];
$Phonenumber =$_REQUEST['Phonenumber'];

$update="update Appointments set trn_date='".$trn_date."',
name='".$name."', email='".$email."',foodcontent='".$foodcontent."',Pickupaddress='".$Pickupaddress."',
estimatednoofpeople='".$estimatednoofpeople."',Phonenumber='".$Phonenumber."' where id='".$id."'";
mysqli_query($con, $update) or die(mysqli_error());
$status = "Record Updated Successfully. </br></br>
<a href='view.php'>View Updated Record</a>";
echo '<p style="color:#FF0000;">'.$status.'</p>';
}else {
?>
<div>
<form name="form" method="post" action="">
<input type="hidden" name="new" value="1" />
<input name="id" type="hidden" value="<?php echo $row['id'];?>" />

<p><input type="text" name="name" placeholder="Enter Name"
required value="<?php echo $row['name'];?>" /></p>

<p><input type="text" name="username" placeholder="Enter username"
required value="<?php echo $row['username'];?>" /></p>

<p><input type="email" name="email" placeholder="Enter Email"
required value="<?php echo $row['email'];?>" /></p>


<p><input type="text" name="foodcontent" placeholder="Enter food-content"
required value="<?php echo $row['foodcontent'];?>" /></p>

<p><input type="text" name="Pickupaddress" placeholder="Enter pickup address"
required value="<?php echo $row['Pickupaddress'];?>" /></p>

<p><input type="text" name="estimatednoofpeople" placeholder="Enter No. of people to eat"
required value="<?php echo $row['estimatednoofpeople'];?>" /></p>

<p><input type="text" name="Phonenumber" placeholder="Enter Phonenumber"
required value="<?php echo $row['Phonenumber'];?>" /></p>

<p><input name="submit" type="submit" value="Update" /></p>

</form>
<?php } ?>
</div>
</div>
</body>
</html>
