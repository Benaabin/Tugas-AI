var = '''!()-[];:'"\,<>./?@#$%^&*_~'''

str = "Hello!!!,  whatsssup-#@?s>  pe,@#mede@$%#k"

str_new = ""
for kata in str:
    if kata not in var:
        str_new= str_new + kata

print(str_new)