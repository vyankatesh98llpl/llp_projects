# def add():
#     num  = a+b
#     return num
# from calculator import history

# print(history)

u1 = int(input("enter the number:- "))
old = [0,1]
while len(old) < u1:
    old.append(old[-1] + old[-2])
print(old)