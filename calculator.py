from operation import add

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
while True:
        history = []
        value1 = int(input("Enter the 1st Number :- "))
        choice = input(""" Enter Your Number
                        0. Exit:-
                        1. Addition
                        2. Substraction
                        3. Multiplcation
                        4. Divion
                        5. Moduls  
                        """)
        value2 = int(input("Enter the 2nd Number :-"))
        if "choice" == "choice":
            if choice == "1":
                ans = value1 + value2
                his = f"{value1} + {value2} =", ans
                history.append(his)
                print(f"{value1} + {value2} =", ans)
            
            elif choice == "2":
                ans = value1 - value2
                his = f"{value1} - {value2} =", ans
                history.append(his)
                print(f"{value1} - {value2} =", ans)
                    
            elif choice == "3":
                ans = value1 * value2
                his = f"{value1} * {value2} =", ans
                history.append(his)
                print(f"{value1} * {value2} =", ans)
                    
            elif choice == "4":
                ans = value1 / value2
                his = f"{value1} / {value2} =", ans
                history.append(his)
                print(f"{value1} / {value2} =", ans)

            elif choice == "5":
                ans = value1 % value2
                his = f"{value1} % {value2} =", ans
                history.append(his)
                print(f"{value1} % {value2} =", ans)


        print(history)