from cs50 import get_float
import sys

def main():
    while True:
        cents = get_float('Change owed in cents: ')
        cents = round(cents * 100)
        if cents < 0:
            True
        else:
            break

    calculate_quarters(cents)
    calculate_dimes(cents)
    calculate_nickels(cents)
    calculate_pennies(cents)

    coins = count

    print(f'{coins}')

def calculate_quarters(cents):
    # how many quarters do a dollar have until dollar is less than 0,25 return number of quarters
    while True:
        if cents >= 25:
            cents = cents - 25
            count += 1
            True
        else:
            break
         return count


def calculate_dimes(cents):
    while True:
        if cents >= 10:
            cents = cents - 10
            count += 1
            True
        else:
            break
        return count


def calculate_nickels(cents):
    while True:
        if cents >= 5:
            cents = cents - 5
            count += 1
            True
        else:
            break
        return count


def calculate_pennies(cents):
    while True:
        if cents >= 1:
            cents = cents - 1
            count += 1
            True
        else:
            break
        return count

if __name__ == "__main__":
    global count
    main()
