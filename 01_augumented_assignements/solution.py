# do not change the method name
def main():
    balance = 5000
    print("================== BALANCE ====================", end="\n")
    print("")
    print(f"Current Balance: ${balance:.1f}")
    # write your code here with 4 space intentation
    deposit = float(input("How much do you want to deposit: $"))
    balance += deposit
    print(f"Balance Successfully Updated: ${balance:.1f}")
    withdraw = float(input("How much do you want to withdraw: $"))
    balance -= withdraw
    print(f"There is a 3% transaction fee on the withdrawal.")
    balance -= (withdraw*0.03)
    print(f"Withdrawal: ${withdraw} - Fee: ${withdraw*0.03:.1f}")
    print(f"Balance Successfully Updated: ${balance:.1f}")
    print("")
    print("============ TRANSACTION COMPLETED ============")
# do not change the following lines:    
if __name__ == "__main__":
    main()