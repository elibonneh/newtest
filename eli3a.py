# class 3
# x = open("c:\eli\Eli.txt", 'r', encoding='UTF-8')
# content = x.read()
# x.close()
# print(content)

try:
    x = open("c:\eli\Eli1.txt", 'r+', encoding='UTF-8')
    content = x.write("and Inbar too yes")
    x.close()
    print(content)
    c = 5
except (IOError, ZeroDivisionError) as a:
    print(a)
    print('could not open file')
finally:
    print('this will run anyway')
x = open("c:\eli\Eli1.txt", 'r', encoding='UTF-8')
content = x.read()
x.close()
print(content)



# a = append
# w = write
# r+ = read + write דורס את הקובץ
# encoding='utf-8' לציין את סוג הקובץ

