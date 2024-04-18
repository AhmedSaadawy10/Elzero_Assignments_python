import re
#1
my_string = re.findall(r"\w{1}\s","eeeeE llllLl lllzzZzzzz eroe operationr pollo ")
print(''.join(my_string))

#================================================================
#2
print("-"*30)

my_search=re.search(r"(El\w{4})","EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111")
print((my_search))

#________________________________________________________________
#3
print("-"*30)

phones='''
+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12
'''
my_phone=re.findall(r"(\+?\(\d{4}\))\s+\d+\-(\d{4})",phones)

# print((my_phone))
for ph in my_phone:
    print(''.join(ph))

#================================================================
#4
print("-"*30)

emails='''
http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net'''

my_emails=re.findall(r"(https?)(://)(www)?(\.)?[A-z0-9]+\.(org|com)\:?(\d+)?/?(.+)",emails)

for counter,email in enumerate(my_emails,1):
    print(f"{counter}=>{''.join(email)}")

#================================================================
#5
print("-"*30)   

protocols='''

http
https
abcd
abcd'''

my_protocols=re.findall(r"(https?)",protocols) 

for protocol in my_protocols:
    print(f"protocol => {protocol}")