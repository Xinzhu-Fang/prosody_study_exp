<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, A$

$fileName = $_GET['file'];

if(preg_match('/^[a-zA-Z0-9-_]+.wav$/',$fileName)) {
  $fp = fopen( "uploads/$fileName", 'wb' );
  fwrite( $fp, file_get_contents("php://input") );
  fclose( $fp );
} else {
  echo 'Filename not accepted';
}


?>
