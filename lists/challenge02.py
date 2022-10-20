#!/usr/bin/env python3

def main():

    wordbank = ["indentation", "spaces"]

    tlgstudent = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)
    num = input("choose between 0-18:")
    
    student_name = tlgstudent[int(num)]

    print(f'{student_name} always uses {wordbank[2]} {wordbank[1]}  to indent.')
  
main()
