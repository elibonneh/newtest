name = "EliB"
size = 10
# print(size)
print("hello",name)
# this print the name plus the size value
print(name + str(size))
# print(name)
# print("Eli Bonneh")

# if example:
a = 101
b = 101
if a > b:
        print("a is bigger")
        if a > 5:
            print("a big then 5")
if b > a:
        print("b is bigger")
if a == b:
        print("a is equal to b")

# example for if with and with elif
if ( a > b and a > 5 ):
        print("big a")
elif a == b:
        print("equal")
        if a < 100:
            print("bigger than 100")
        elif a >= 101:
            print("it is 101")
elif a != b:
        print("not equal")
else:
        print("small a")

# oparator
print(1 + 1 * 5)
print(12 % 2)
# input
y = input("please insert y value...")
print("very good")
z = int(input ("pls insert Z value..."))
if z >1000:
    print("z value")
    print("big than 1000")
