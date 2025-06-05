# Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q on the keyboard
print("Haji Karyana Store:")
total = 0
prices = []
while(True):
    UserInput = input("Enter the item price or press q to quit: \n")
    if (UserInput!='q'):
        price = int(UserInput)
        prices.append(price)
        total = total + price
        print(f"Order total so far {total}")
    else:
        print("Haji Kryana Store:")
        for i, price in enumerate(prices, start=1):
            print(f"{i}. {price}")
        print(f"Your total bill is {total}. Thanks for shopping with us.")
        break
