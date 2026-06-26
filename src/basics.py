import random

def main():
    numbers = [random.randint(1, 100) for i in range(10)]
    count = 0

    for number in range(len(numbers)):
        if (numbers[number] % 2 == 0):
            print(numbers[number])
        
    for number in range(len(numbers)):
        if (numbers[number] > 90):
            count += 1
    
    if (count >= 1):
        print("Есть рекорд!")
    else:
        print("Без рекордов")

if __name__ == "__main__":
    main()