#A simple Program that automically adds the variable on at the start of the calculation in the same unit
def variable(x):
    print(x+" is your Variable!!")                                  
    print("Now we will move onto the calculating unit")                               
    x = (float(x))
    number1=(float(input("Please enter your First Number")))
    number2=(float(input("Please enter your Second Number")))


    choice=input("Would you like to Add, Subtract, Multiply or Divide? (Use Symbols)")

    choice = choice.lower()

    if choice == "+":
        answer1 = x+number1+number2
        print (answer1)

    elif choice == "-":
        answer2 = x-number1-number2
        print (answer2)

    elif choice == "x":
        answer3 = x*number1*number2
        print (answer3)

    elif choice == "÷":
        answer4 = x/number1/number2
        print (answer4)

    else:
        print("ERROR")







variable2=(input("Please enter your Variable"))

variable(variable2)
