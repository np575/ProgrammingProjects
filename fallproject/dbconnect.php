<?php
$host="sql1.njit.edu";//your msql host [sql1, sql2, sql3]
$database="np575";//ucid
$username="np575";//ucid
$password="wEgXLA9Ki";//mysql password (not ucid password)
// Enter your Host, username, password, database below.
// I left password empty because i do not set password on localhost.
$con = mysqli_connect("sql1.njit.edu","np575","wEgXLA9Ki","np575");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
?>
