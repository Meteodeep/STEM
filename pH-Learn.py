from time import sleep
while True:

    value=input("Please enter the pH value between 1 and 14......")

    if value == "7":
        print("Neutral e.g Distilled Water")

    elif value <= "6":
        print(" Acid e.g Lemon Juice")

    elif value >= "8":
        print("Base e.g Toothpaste")

    else:
        print("ERROR") 

#Using another if function, greater and less than!!!!!
#Some chatter and sleep at the end!!!!!

    print("Thank You for using this pH scale!!!!")
    sleep(3)
    print("More Info: https://en.wikipedia.org/wiki/PH#/media/File:216_pH_Scale-01.jpg")
