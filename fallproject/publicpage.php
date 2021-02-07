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
top: 25%;
left: 40%;
background: rgba(0, 0, 0, 0.5);
color: #f1f1f1;
width: 100%;
height: 520px;
padding: 20px;
}
.form h1:hover
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
</style>
</head>
<html>
<head>
<meta charset="utf-8">
<title>Welcome Home</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<video autoplay muted loop id="myVideo">
  <source src="https://player.vimeo.com/external/220260309.sd.mp4?s=6ba5ae83e887a8a9cb4f72097b3404f68b519f99&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
<div class="form">
<p>Welcome to left4good</p>
<p>An overview on what we do</p>
<p> 
 Left4good is a non-profit food rescue organization,operating in different cities in NJ, that provides solutions to prevent excess wholesome cuisine from being wasted.
 It provides services such as food waste consulting,excess food delivery, co-branding services.
</p>
<p> request now or join us today </p>
<h1><a href="register.php">Register</a></h1>
<h2> <a href="loginpage.php">login</a></h2>
<h3> <a href="question.html">FAQs</a></h3>
</div>
</body>
</html>
