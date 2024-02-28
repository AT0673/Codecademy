# An elif statement checks another condition after the previous if statements conditions aren’t met. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.


#Write an if/elif/else statement that:

    #If grade is 90 or higher, print "A"
    #Else if grade is 80 or higher, print "B"
    #Else if grade is 70 or higher, print "C"
    #Else if grade is 60 or higher, print "D"
    #Else, print "F"

grade = 86
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")