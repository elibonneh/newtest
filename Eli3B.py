
try:
    a = 1/0

except (ZeroDivisionError) as a:
    print(a)
    print('could not Dividing by Zero')
finally:
    print('this will run anyway')

try:
    x = 1
except (SyntaxError) as b:
    print(b)
finally :
    print('finally')

# Answer 5:
print("Answer 5: we will have an errors in the code but we will not know or pound about them")
# Answer 6:
print("except IOError - Input Output error  except ZeroDivisionError - dividing by Zero error")

x = open("c:\eli\words.txt", 'w', encoding='UTF-8')
content = x.write("Eli")
x.close()
print(content)
x = open("c:\eli\words.txt", 'a+')
content = x.write("BONNEH")
x.close()
print(content)
x = open("c:\eli\words.txt", 'a+')
content = x.write("מה נשמע")
x.close()
print(content)

