
# do not change the method name
def main():
    import sys
    # your solution goes here
    num = input("Enter a 10-digit phone number, no spaces, special characters or spaces: ")
    (len(num) == 10 and num.isdigit()) or (print("Error: Please enter exactly 10 digits.\nNo spaces, special characters and alphabetical characters.") or sys.exit())    
    print(f"Formatted Phone Number: ({num[:3]}) {num[3:6]}-{num[6:]}")
# do not change the code below
if __name__ == "__main__":
    main()