<!DOCTYPE html>
<?php
function checkPasswords(){
        if(isset($_POST['password']) && isset($_POST['confirm'])){
                if($_POST['password'] == $_POST['confirm']){
                        echo "<br>Passwords Matched!<br>";
                }
                else{
                        echo "<br>Password Didn't match<br>";
                        return true;
                }
        }
}
?>
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
height: 420px;  
padding: 20px;
}
.form1{
position: fixed;
top: 0%;
left: 30%;
color: #f1f1f1;
font-size: 20px;
font-weight: 100;
letter-spacing: 5px;
margin-bottom: 30px;
}
.form1 h3
{
font-size: 20px;
font-weight: 100;
letter-spacing: 5px;
margin-bottom: 30px;
}
.form1 h4:hover
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
.form1 h5
{
font-size: 20px;
font-weight: 100;
letter-spacing: 5px;
margin-bottom: 30px;
}
.form1 h6
{
font-size: 20px;
font-weight: 100;
letter-spacing: 5px;
margin-bottom: 30px;
}
.form1 h7:hover
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
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="style.css" />
<script>
function validate(){
	var form = document.forms[0];
	var password = form.password.value;
	var conf = form.confirm.value;
	console.log(password);
	console.log(conf);
	let pv = document.getElementById("validation.password");
	let succeeded = true;
	if(password == conf){
		
		pv.style.display = "none";
	
	}
	else{
		pv.style.display = "block";
		pv.innerText = "Passwords don't match";
		
		succeeded = false;
	}
}
</script>
</head>
<body>
<video autoplay muted loop id="myVideo">
  <source src="https://player.vimeo.com/external/220260309.sd.mp4?s=6ba5ae83e887a8a9cb4f72097b3404f68b519f99&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

<?php
require('dbconnect.php');
// If form submitted, insert values into the database.
if (isset($_REQUEST['username'])){
        // removes backslashes
	$username = stripslashes($_REQUEST['username']);
        //escapes special characters in a string
	$username = mysqli_real_escape_string($con,$username); 
	$email = stripslashes($_REQUEST['email']);
	$email = mysqli_real_escape_string($con,$email);
	$password = stripslashes($_REQUEST['password']);
	$password = mysqli_real_escape_string($con,$password);
	$trn_date = date("Y-m-d H:i:s");
       
	if(checkPasswords() === true ){
	echo "<div class='form1'>
        <h6>Password doesn't match. Try again.</h6>
	<h7>Click here to <a href='loginpage.php'>Login</a></h7></div>";
	}

        else{
	    $query = "INSERT into `users2` (username, password, email, trn_date)
        VALUES ('$username', '".md5($password)."', '$email', '$trn_date')";
        $result = mysqli_query($con,$query);
$to = "$email";
$subject = "Test mail";
$message = "Hello! $username, Welcome to Left4Good. Thank you for registering and helping community.";
$from = "shubhamgohela5@gmail.com";
$headers = "From:" . $from;

mail($to,$subject,$message,$headers);

//        header("Location: index.php");           
           echo" <div class='form1'>
            <h3>You are registered successfully.</h3>
            <h4><a href='loginpage.php'>Login</a></h4>
           <h5>Enter your information below  to register</h5>
            </div>";
        }
    }
?>
<div class="form">
<h1>Registration</h1>
<form name="registration" action="" method="post">
<input type="text" name="username" placeholder="Username" required />
<input type="email" name="email" placeholder="Email" required />
<input type="password" name="password" placeholder="Password" required />
<input type="password" name="confirm" placeholder="Re-Enter password"/>
<span style="display:none;" id="validation.password"></span>
<input type="submit" name="submit" value="Register" />
</form>
</div>
<?php ?>
</body>
</html>
