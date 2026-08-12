#ATM SIMULATOR

balance = 1000

print("1. Check account balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Exit")

while True:
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your available balance is: ${balance}")

    elif choice == "2":
        deposit_request = int(input("How much do you want to deposit?: "))
        balance += deposit_request
        print(f"Deposit successful. Your new balance is: ${balance}")

    elif choice == "3":
        withdrawal_request = int(input("How much do you want to withdraw?: "))

        if withdrawal_request <= balance:
            balance -= withdrawal_request
            print(f"Withdrawal successful. Your new balance is: ${balance}")
        else:
            print("Insufficient funds")
        
    elif choice == "4":
        print("Thank you for banking with us, hope to see you soon")
        break
    else:
        print("Invalid option")



