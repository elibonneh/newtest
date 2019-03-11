# answerA
x = 10
y = 20
if x > y:
    print("BIG")
else:
    print("SMALL")

# answerB loops
for x in range(5):
    print(x)

# answerC
a = 1
b = 2
c = 3
d = 4
if a > b:
    print("summer")
elif a < b:
    print("winter")
elif c == d:
    print("fall")
else:
    print("spring")

# answerD
count = 1
while count < 11:
    print(count)
    count = count+1

# answerE
name1 = input("Enter your age:")
name2 = input("Enter your first latter of your last name:")
name3 = input("Enter current shekel-dollar currancy:")
name4 = input("Did you flew abtoad?")
name5 = input("my appartment number is:")
print("my age is:", name1)
print("my first latter of my last name is:", name2)
print("current Shekel-Dollar currency is:", name3)
print("I flew aboard:", name4)
print("my appartment number is:", name5)
x = name1+name3
print(name1 + name3)



# answerF
name = input("enter your phone number:")
print("phone number", name)

# answerG

def run(PrintHello):
    print("HELLO")
if __name__ == '__main__':
    run(1)

def calculate(x,y):
   print(x + y)
if __name__ == '__main__':
   calculate(5, 3.2)


# answerH
name = input("Enter your Name:")
print("your name is:", name)

def divide_by_2():
    number = input("enter the number: ")
    print(int(number) / 2)

if __name__ == '__main__':
    divide_by_2()

# answerI
def plus(num1, num2):
    print(num1 + num2)
if __name__ == '__main__':
    plus(5, 6)

def strings_connector(str_1, str_2):
    print((str_1) + " " + (str_2))

if __name__ == '__main__':
    strings_connector("Hi", "Eli")




# answer J:
import array as arr

a = arr.array("i", [1, 3, 6, 9])
print(a)

# answer K:
for x in range(1):
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
# answer L:

    print("*" + " " + " " + " " + " " + " " + "*")
    print(" " + "*" + " " + " " + " " + "*" + " ")
    print(" " + " " + "*" + " " + "*" + " " + " ")
    print(" " + " " + " " + "*" + " " + " " + " ")
    print(" " + " " + "*" + " " + "*" + " " + " ")
    print(" " + "*" + " " + " " + " " + "*" + " ")
    print("*" + " " + " " + " " + " " + " " + "*")
# answer M:




def computes_the_sum():
    number = input("enter the number: ")
    print(int(number))
    print((int(int(number) /10)) + (int(number) - ((int(int(number) /10)  *10))))


if __name__ == '__main__':
    computes_the_sum()
