"""
PRIMM: 1+1 = 11
Program to add two variables together
Channing Moor - Spetember 27th
"""

def main():
    # Getting two numbers to add together in total
    num1: int = int(input("Enter a number: "))
    num2: int = int(input("Enter another number: "))
    total: int = num1+num2
    stotal: int = num1-num2
    mtotal: int = num1*num2
    sqtotal: int = num1**num2
    dtotal: int = num1/num2
    ddtotal: int = num1//num2
    mototal: int = num1%num2

    # Printing the total
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {stotal}")
    print(f"{num1} * {num2} = {mtotal}")
    print(f"{num1} ** {num2} = {sqtotal}")
    print(f"{num1} / {num2} = {dtotal}")
    print(f"{num1} // {num2} = {ddtotal}")
    print(f"{num1} % {num2} = {mototal}")

if __name__ == "__main__":
  main()
