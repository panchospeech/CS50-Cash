from cs50 import get_float

# ask for change owed and verify if its not a negative number, otherwise prompt again
while True:
    cents = get_float('Change: ')
    if cents > 0:
        break

# convert the change in dollars to cent for easier management
cents = round(cents * 100)

# set the counter of coins to 0
count = 0

# QUARTERS: verify if the cents are greater or equal to 25, if it is reduce 25 and add 1 to count, otherwise break the loop
while True:
    if cents >= 25:
        cents = cents - 25
        count += 1
    else:
        break

# DIMES: verify if the cents are greater or equal to 10, if it is reduce 10 and add 1 to count, otherwise break the loop
while True:
    if cents >= 10:
        cents = cents - 10
        count += 1
    else:
        break

# NICKELS: verify if the cents are greater or equal to 5, if it is reduce 5 and add 1 to count, otherwise break the loop
while True:
    if cents >= 5:
        cents = cents - 5
        count += 1
    else:
        break
# PENNIES: verify if the cents are greater or equal to 1, if it is reduce 1 and add 1 to count, otherwise break the loop
while True:
    if cents >= 1:
        cents = cents - 1
        count += 1
    else:
        break

# Print the count that represent the number of coins owed
print(f'{count}')

# the else statement its not necesary, but logical correct

