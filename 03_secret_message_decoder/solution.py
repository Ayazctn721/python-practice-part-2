# do not change the method name
import sys
def main():
    sec_message = input("Enter the encoded message: ")
    step_size = input("Enter the step size: ")
    step_size.isdigit() and int(step_size) > 0  or (
        print("Error: Step size must be a positive integer") or sys.exit())
    step_size_input = int(step_size)
    decode_message = sec_message[:: step_size_input]
    print(f"Decoded Message: {decode_message}")

# do not change the following lines:    
if __name__ == "__main__":
    main()