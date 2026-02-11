import re

# ref is lesson 194
# USE regular expressions 101(regex.com) for this
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
username = 'Gian'
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = "kujweafkawee%8"
# can change username and password to input as "username=input('what is name?')"

a = pattern.search(username)
check = pattern2.fullmatch(password)
print(check)