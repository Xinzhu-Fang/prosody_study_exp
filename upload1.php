<!-- by cam fox form is&t
As for securing the upload script, I've made it so that the webserver can't access and run the files, and that the file names can't do stuff like "../../whatever". The files may still contain anything anyone gives you, so it is up to you to handle it carefully until you've validated it (and your wav player may even be subject to buffer overruns if it gets a sufficiently malformatted wav file). The fact that the whole virtual machine has nothing but this thing on it adds a lot, as there's no collateral damage. -->

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
