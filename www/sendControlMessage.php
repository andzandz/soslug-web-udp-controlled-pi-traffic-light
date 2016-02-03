<?php
### Extract the desired colour from the AJAX POST request coming in: ###
$msg = $_POST["message"];

$destIp = $_POST["dest"];

$port = 5005;

print "Sending $msg to IP $destIp, port $port... ";

### Make a UDP socket to send the message: ###
if ($socket = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP)) {
  ### Try to send the UDP message to the correct IP and port number: ###
  socket_sendto($socket, $msg, strlen($msg), 0, $destIp, $port);
  echo "Send successful";
} else {
  echo "Can't create socket\n";
}

?>
