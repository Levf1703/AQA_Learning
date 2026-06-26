from user import User

def run_demo():
    people = [User("Andrey", 21), User("Tom", 16), User("Niko", 35)]

    for person in people:
        if (person.is_adult()):
            person.greet()

if __name__ == "__main__":
    run_demo()