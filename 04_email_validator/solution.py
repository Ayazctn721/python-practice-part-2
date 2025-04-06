# do not change the method name
def main():
    email_input = input("Enter an email address: ")
    if " " in email_input:
        print("Email cannot contain spaces")
    elif "@" not in email_input:
        print("Email must contain an @ symbol")    
    elif email_input.count("@") > 1:
        print("Email must contain only one @ symbol")
    else:
        username, domain = email_input.split("@")    

        if len(username) == 0:
            print("Email must have characters before the @ symbol")
        elif "." not in domain:
            print("Email must have a domain with a period after the @ symbol")  
        else:
            print("Valid email address!")          

# do not change the following lines:
main()