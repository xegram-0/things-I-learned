def collatz(number:int):
    if number % 2 == 0:
        return number // 2
    else:
        return number*3 + 1

def main():
    while True:
        try:
            number:int = int(input("Enter a number: "))
            break
        except ValueError:
            print("Wrong type of input")
        
    while True:
        number:int = collatz(number)
        print(number)
        if number == 1:
            break

if __name__ == "__main__":
    main()