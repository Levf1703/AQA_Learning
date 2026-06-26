import random

def main():
    spisok = []
    for i in range(10):
        spisok += [random.randint(1, 100)]
    count = 0

    for i in range(len(spisok)):
        if (spisok[i] % 2 == 0):
            print(spisok[i])
        if (spisok[i] > 90):
            count += 1
    
    if (count >= 1):
        print("Есть рекорд!")
    else:
        print("Без рекордов")