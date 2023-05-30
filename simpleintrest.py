from tkinter import *
window= Tk()

window.title('Simple Intrest Calculator')
window.geometry("380*400")
window.configure(bg="lightpurple")

def calculate_intrest():
    p = int(input("Enter principal : "))
    r = int(input("Enter rate : "))
    t = int(input("Enter time : "))

si = (p*r*t)/100
print("Simple Intrest is : ",si)
