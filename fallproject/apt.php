<?php
require('dbconnect.php');
include("authorization.php");
session_start();
echo "Hello, your user name is: " . $_SESSION['username'];
if(!isset($_SESSION["username"])){
header("Location: loginpage.php");
exit(); }
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
text-align: center;
top: 25%;
left: 40%;
background: rgba(0, 0, 0, 0.5);
color: #f1f1f1;
width: 25%;
height: 520px;
padding: 20px;
font family: monospace;
top: 150px;
}
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
<title>Dashboard - Secured Page</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<video autoplay muted loop id="myVideo">
  <source src="https://player.vimeo.com/external/220260309.sd.mp4?s=6ba5ae83e887a8a9cb4f72097b3404f68b519f99&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
<div class="form">
<h1>LET'S BAND TOGETHER AGAINST HUNGER</h1>
<p>37 million people face hunger in the U.S. today — including more than 11 million children and nearly 5.4 million seniors. Hunger knows no boundaries — it touches every community in the U.S., including your own</p>
<h2><a href="index.php">Home</a></h2>
<h3><a href="insert.php">Create a new appointment</a></h3>
<h4><a href="view.php">View Appointments</a></h4>
<h5><a href="logout.php">Logout</a></h5>
</div>
</body>
</html>
