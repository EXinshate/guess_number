import random

def main():
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    mynumber = random.randint(smaller, larger)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guess: "))
        if userNumber < mynumber:
            print("Too small")
        elif userNumber > mynumber:
            print("Too large")
        else:
            print("You're got it in", count, "Tries")
            break

if __name__ == "__main__":
    main()