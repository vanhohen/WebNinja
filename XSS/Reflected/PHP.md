# Vulnerable Code 1
This code will get a user input with "name" parameter and reflect result to user. 

```php

<?php

header ("X-XSS-Protection: 0");

// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Feedback for end user
    echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
}

?>
```

## Abuse

## Payload

## Result


# Vulnerable Code 2

## Abuse

## Payload

## Result



# Vulnerable Code 3

## Abuse

## Payload

## Result

