import re

email='abc@xxx.com'
match_string=re.match(r'[a-z]+@[a-z]+\.[a-z]+',email)

print(match_string)

print(match_string.start())
print(match_string.end())
print(match_string.span())
print(match_string.group())



email='abc@xxx.com'
match_list=re.findall(r'[a-z]+@[a-z]+\.[a-z]+',email)

print(match_list)


email='abc@xxx.com'
replace_string=re.sub(r'[a-z]+@','ABC@',email)
print(replace_string)


text='【重要です！】明日、必ず連絡を下さい'
result=re.sub(r'[【】！]',' ',text)
print(result)