import re # import regular expression

# pattern and sequence are important


pattern=r'\w+@\w+\.\w+'# raw so that we can skip unnecessary steps

sequence="this@gmail.com that@gmail.com whatever@whatever.com whisdfisai@fsdlkjfldksj.comd"


# to match pattern and sequence


print(re.match(pattern,sequence))#shows only first
email="this@gamil.com"


if re.match(pattern, email):
    print('email is valid')
else:
    print('this is not valid')

print(re.search(pattern,sequence)) #finds one then stops working

print(re.findall(pattern,sequence))