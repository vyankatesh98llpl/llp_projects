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

def main():
    print(" |....... Welcome User Use Calculator ..........|")
    value1 = int(input("Enter the your First Number :- "))
    choice = input(""" Enter Your Number
                    0. exit :-
                    1. Addition + :-
                    2. Substraction - :-
                    3. Multiplcation *:-
                    4. Divion / :-
                    5. Moduls  % :-
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