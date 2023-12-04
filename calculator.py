value1 = int(input("Enter the 1st Number :- "))
value2 = int(input("Enter the 2nd Number :-"))

if __name__ == "__main__":
    
    while 1 >= 0:
        choice = input(""" Enter Your Number
                   1. Addition
                   2. Substraction
                   3. Multiplcation
                   4. Divion
                   5. Moduls
                   0. Exit:- 
                   """)
        if "choice" == "choice":
            if choice == "1":
                Number = value1 + value2
                print("Addition of Two Number :- ", Number)
            
            elif choice == "2":
                Number = value1 - value2
                print("Addition of Two Number :- ", Number)
                    
            elif choice == "3":
                Number = value1 * value2
                print("Addition of Two Number :- ", Number)
                    
            elif choice == "4":
                Number = value1 / value2
                print("Addition of Two Number :- ", Number)

            elif choice == "5":
                Number = value1 % value2
                print("Addition of Two Number :- ", Number)

            elif choice == "6":
                continue      
        else:
            print("do you want to contiune :-")
        break