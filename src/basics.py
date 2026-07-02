import random

def main():
    numbers = [random.randint(1, 100) for i in range(10)]
    count = 0

    for number in numbers:
        if (number % 2 == 0):
            print(number)
        
    for number in numbers:
        if (number > 90):
            count += 1
    
    if (count > 0):
        print("Есть рекорд!")
    else:
        print("Без рекордов")

if __name__ == "__main__":
    main()