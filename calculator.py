# from operation import add

# value1 = int(input("Enter the 1st Number :- "))
# value2 = int(input("Enter the 2nd Number :-"))

# if __name__ == "__main__":
    
#     while True:
#         choice = input(""" Enter Your Number
#                    0. Exit:-
#                    1. Addition
#                    2. Substraction
#                    3. Multiplcation
#                    4. Divion
#                    5. Moduls
                    
#                    """)
#         if "choice" == "choice":
#             if choice == "1":
#                 Number = value1 + value2
#                 print("Addition of Two Number :- ", Number)
            
#             elif choice == "2":
#                 Number = value1 - value2
#                 print("Addition of Two Number :- ", Number)
                    
#             elif choice == "3":
#                 Number = value1 * value2
#                 print("Addition of Two Number :- ", Number)
                    
#             elif choice == "4":
#                 Number = value1 / value2
#                 print("Addition of Two Number :- ", Number)

#             elif choice == "5":
#                 Number = value1 % value2
#                 print("Addition of Two Number :- ", Number)

#             elif choice == "6":
#                 break      
#         # else:
#         #     print("do you want to contiune :-")
#         # break

history = []
answer  = []

def addition(value1, value2):
    Ans = value1 + value2
    answer.append(Ans)
    return Ans

def subtraction(value1, value2):
    Ans = value1 - value2
    answer.append(Ans)
    return Ans

def multiplication(value1, value2):
    Ans = value1 * value2
    answer.append(Ans)
    return Ans

def division(value1, value2):
    Ans = value1 / value2
    answer.append(Ans)
    return Ans

def moduls(value1, value2):
    Ans = value1 % value2
    answer.append(Ans)
    return Ans


# Fib Seq with cache
fib = [0,1]
def fib_seq(value):
    while len(fib) < value:
        fib.append(fib[-1] + fib[-2])
    print(fib)
    return fib

def prime_number(value):
    for i in range(2, int(value/2)+1):
        if (value % i) == 0 :
            print(f"{value} Number is Not Prime")
            break
    else:
        print(f"This is prime Number {value}")
import math
def Armstrong(value):
    sum = 0
    t1 = value
    while t1 > 0:
        digit = t1 % 10
        sum += digit ** 3
        t1 //= 10
    if value == sum:
        print(f"{value} is an Armstrong number")
    else:
        print(f"{value} is not an Armstrong number")

def numIssqre(value):
    val = int(math.sqrt(value))
    return ((val*val) == value)
 
# Pythagoras Triplet Generator
def triplet(value1,value2):
    v1 = value1 * value1 
    v2 = value2 * value2 
    c3 = v1 + v2
    d1 = math.sqrt(c3)
    return int(d1)
# Average Calculator
# Percentage increase/decrease
# Splitwise

def other():
    userchoice = input("You want to calculation Yes and Other operation No :-")
    print(userchoice)
    if userchoice == "yes":
        userinpt = input("""Enter you are choice
                    1.fibonacci series:-
                    2.Prime Number Checker:- 
                    3.Armstrong number:-
                    4.Is this a Square:-
                    5.Percentage increase/decrease:-
                    6.Splitwise:-
                    """)
        val1 = int(input("enter you are number :-"))
        if userinpt == "1":
            fib = fib_seq(val1)
            history.append(fib)
        elif userinpt == "2":
            prime = prime_number(val1)
            history.append(prime)
        elif userinpt == "3":
            armstrong = Armstrong(val1)
            history.append(armstrong)
        elif userinpt == "4":
            sqr = numIssqre(val1)
            if sqr == True:
                print(f"{val1} Number is IsSquare")
            else:
                print(f"{val1} Number is Not IsSquare")
            history.append(val1)    
    else:
        exit()

def main():
    print(" |....... Welcome User Use Calculator ..........|")
    value1 = int(input("Enter the your First Number :- "))
    choice = input(""" Enter Your choice
                    0. exit :-
                    1. Addition + :-
                    2. Substraction - :-
                    3. Multiplcation *:-
                    4. Divion / :-
                    5. Moduls  % :-
                    6.Pythagoras Triplet Generator
                    """)
    value2 = int(input("Enter the your second  Number :-"))
    if 'choice' == 'choice':
        if choice == '0':
            exit()        
        if choice == "+":
            ans = addition(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        if choice == "-":
            ans = subtraction(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        if choice == "*":
            ans = multiplication(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        if choice == "/":
            ans = division(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        if choice == "%":
            ans = moduls(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        # history.append(his)
        if choice == "6":
            ans = triplet(value1,value2)
            his = f"{value1} + {value2} =", ans
            print(his)
        history.append(his)
    
def secondvalue():
    i = 0
    while True:
        users = input("do you want to continue Yes / No :- ")
        choice = input(""" Enter Your Number \n0. Exit:-\n1. Addition +\n2. Substraction - \n3. Multiplcation * \n4. Divion / \n5. Moduls % \n 6. history \n 7.clear history\n\t:-""")
        if choice == '6':
            print(history)
        elif choice == '7':
            history.clear()
        else:
            newval = int(input("enter you 2nd value:-"))

        oldvalue = answer[i]
        i+=1    
        if users == "yes":
            if choice == '0':
                break
            if choice == '+':
                res = addition(oldvalue , newval)
                his = f"{oldvalue} + {newval} =", res
                history.append(his)
                print(f"{oldvalue} + {newval} =", res)
            if choice == "-":
                res = oldvalue - newval
                his = f"{oldvalue} - {newval} =", res
                history.append(his)
                print(f"{oldvalue} - {newval} =", res)
                    
            if choice == "*":
                res = oldvalue*newval
                his = f"{oldvalue} * {newval} =", res
                history.append(his)
                print(f"{oldvalue} * {newval} =", res)
                    
            if choice == "/":
                res = oldvalue / newval
                his = f"{oldvalue} / {newval} =", res
                history.append(his)
                print(f"{oldvalue} / {newval} =", res)

            if choice == "%":
                res = oldvalue % newval
                his = f"{oldvalue} % {newval} =", res
                history.append(his)
                print(f"{oldvalue} % {newval} =", res)
            
            answer.append(res)
        else:
            exit()

if __name__ == "__main__":
    while True:
        other()
        main()
        secondvalue()
    
        
# def calculator(value1,choice,value2):
    
#     if 'choice' == "choice":
#         if choice == "1":
#             ans = value1 + value2
#             his = f"{value1} + {value2} =", ans
#             print(f"{value1} + {value2} =", ans)
#         if choice == "2":
#             ans = value1 - value2
#             his = f"{value1} - {value2} =", ans
#             print(f"{value1} - {value2} =", ans)
                
#         if choice == "3":
#             ans = value1 * value2
#             his = f"{value1} * {value2} =", ans
#             print(f"{value1} * {value2} =", ans)
                
#         if choice == "4":
#             ans = value1 / value2
#             his = f"{value1} / {value2} =", ans
#             print(f"{value1} / {value2} =", ans)

#         if choice == "5":
#             ans = value1 % value2
#             his = f"{value1} % {value2} =", ans
#             print(f"{value1} % {value2} =", ans)
#         history.append(his)
#         users = input("do you want to continue Yes / No :- ")
#         choice = input(""" Enter Your Number \n0. Exit:-\n1. Addition\n2. Substraction\n3. Multiplcation\n4. Divion\n5. Moduls  \n\t:-""")
#         newval = int(input("enter you 2nd value:-"))
#         if choice == "1":
#             res = ans + newval
#             his = f"{ans} + {newval} =", res
#             history.append(his)
#             print(f"{ans} + {newval} =", res)
#         if choice == "2":
#             res = ans - newval
#             his = f"{ans} - {newval} =", res
#             history.append(his)
#             print(f"{ans} - {newval} =", res)
                
#         if choice == "3":
#             res = ans*newval
#             his = f"{ans} * {newval} =", res
#             history.append(his)
#             print(f"{ans} * {newval} =", res)
                
#         if choice == "4":
#             res = ans / newval
#             his = f"{ans} / {newval} =", res
#             history.append(his)
#             print(f"{ans} / {newval} =", res)

#         if choice == "5":
#             res = ans % newval
#             his = f"{ans} % {newval} =", res
#             history.append(his)
#             print(f"{ans} % {newval} =", res)     
#         else:
#             # return exit()
#             pass
#     elif choice == "0":
#         # return exit()
#         pass

# if __name__ == "__main__":
    
#     value1 = int(input("Enter the 1st Number :- "))
#     choice = input(""" Enter Your Number
#                     0. Exit:-
#                     1. Addition
#                     2. Substraction
#                     3. Multiplcation
#                     4. Divion
#                     5. Moduls  
#                     """)
#     value2 = int(input("Enter the 2nd Number :-"))
#     while True:
#         calculator(value1,choice,value2)
#         print(history)