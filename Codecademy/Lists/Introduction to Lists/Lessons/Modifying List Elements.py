garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"     #<----- We are selecting the 1st element in the index, and setting it equal to Calla. This therefore replaces Adam with Calla
print(garden_waitlist)

garden_waitlist[-1] = "Alex"     #<---- The negative index (-1) will select the last element on the list (Alisha) and by setting it equal to Alex, we replace Alisha with Alex.
print(garden_waitlist)