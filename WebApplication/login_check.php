<?php
session_start();
include('conn.php');

<?php
/* Redirect browser */
header("location:login.php");

/* Make sure that code below does not get executed when we redirect. */
exit;
?>


<?php

if(count($_POST)>0)
{   

    $result = mysql_query("SELECT * FROM admin WHERE username='".$_POST["username"]."' and password = '".$_POST["password"]."'");
    $row  = mysql_fetch_array($result);

if(is_array($row)) 
{
    $_SESSION["username"] = $row[username];
    $session_register["username"] = $row[username];
} 
else 
{
   $_SESSION['msg']="Invalid Username or Password";
   header("location:login.php");
}
}

if(isset($_SESSION["user_id"]))
{
    header("Location:index.php");
}

?>