#Python gives us a method to remove elements at a specific index using a method called .pop().
#The .pop() method takes an optional single input:
    #The index for the element you want to remove.


data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()   #Due to me not setting an index within the Pop, this will remove the last item within the list, 'Python 3'
print(data_science_topics)