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

Since there is no input sanitizing we can add javascript code in our request and execute on client browser. To weponize it we can sent url to a user and redirect their session cookies or execute malicious javascript code on their browser. For simple demonstration we will make it pop-up a message

## Payload

```php
<script>alert(1)</script>
```

## Result

```php
<pre>Hello <script>alert(1)</script></pre>
```

# Vulnerable Code 2
This code will get a user input with "name" parameter and reflect result to user. 

```php
<?php

header ("X-XSS-Protection: 0");

// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Get input
    $name = str_replace( '<script>', '', $_GET[ 'name' ] );

    // Feedback for end user
    echo "<pre>Hello ${name}</pre>";
}

?>
```


## Abuse

There is filtering unlike code-1 but mechanism is not secure. The problem there any user input will be controlled and if there is "\<script>" inside of it, code will delete it. The issue here javascript can be executed with capital and lower case also so it is not case sensitive. Since code filters only "\<script>" with lower characters, we can make it like "\<ScRipT" and bypass filtering. 

## Payload

```php
<ScRipT>alert(1)</ScRipT>
```


## Result

# Vulnerable Code 3

This code will get a user input with "name" parameter and reflect result to user. 

```php
<?php

header ("X-XSS-Protection: 0");

// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Get input
    $name = preg_replace( '/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $_GET[ 'name' ] );

    // Feedback for end user
    echo "<pre>Hello ${name}</pre>";
}
```

## Abuse

In this code, unlike code-2 filter is NOT case sensitive, "preg_replace" function will filter any given user input that contains "script". We can still execute other javascript command without "\<sctipt>" tag. To abuse this, we will define an image tag and set source to an unknown location and force it get error. When error occurs we will make it to run our own javascript code

## Payload

```php
<IMG SRC=/ onerror="alert(1)"></img>
```

## Result

```php
<pre>Hello <img src="/" onerror="alert(1)"></pre>
```
