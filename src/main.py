from user import User

people = [User("Andrey", 21), User("Tom", 16), User("Niko", 35)]

for i in range(len(people)):
    if (people[i].is_adult() == True):
        people[i].greet()