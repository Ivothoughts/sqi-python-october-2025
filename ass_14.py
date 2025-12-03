#1 Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

balance = int(input("Enter your balance: "))
atm_loop = True
while atm_loop:
    withdrwal_amt = int(input("Enter withdrawal amout: "))
    if withdrwal_amt > balance:
        print("Insufficient balance")
    else:
        balance -= withdrwal_amt
        print(f"Remaining balance: {balance}")
    
    while True:
        another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").lower().strip()
        if another_withdrawal == "no":
            print(f"Final balance: {balance}")
            atm_loop = False
            break

        if another_withdrawal == "yes":
            break

        print("Invalid input")




#2 Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48
 
# total_cost = 0
# while True:



#3 Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

#  4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.

#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


