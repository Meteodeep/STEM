def trianglearea(base,height):
    print("Ok so you want the area of a triangle.....")
    answer = 0.5*base*height
    print(answer) 
    
def cylindervolume(radius,height):
    print("Ok so you want the volume of a cylinder.....")
    answer1 = 3.14*radius**2*height
    print(answer1)
    
def circlecircumfrence(radius):
    print("Ok so you want the circumfrence of a circle.....")
    answer2 = 2*3.14*radius
    print(answer2)     
    
def circlearea(radius):
    print("Ok so you want the area of a circle.....")
    answer3 = 3.14*radius**2
    print(answer3) 
    
while True:
from time import sleep

menu=input("Please Choose a Geometry Topic: 'Triangle Area', 'Cylinder Volume', 'Circle Circumfrence', 'Circle Area'")
sleep(5)
print("Please Edit this code and add the appropiate Function to the bottom of the Code!")
