# do not change the method name
def main():
    text_message = input("Enter a message: ")
    text_message = text_message[0].upper() + text_message[1:]
    print(f"Original message ({len(text_message)} chars): {text_message}")
    text_replace = text_message.replace("with", "w/").replace("for", "4").replace("to", "2").replace("and", "&").replace("at", "@")
    if len(text_replace)  > 160:
        shortened = text_replace[:157] + "..."
        print(f"Shortened message ({len(shortened)} chars): {shortened}")
    else:
        shortened = text_replace
        print(f"Shortened message ({len(shortened)} chars): {shortened}")
    print(f"You saved {len(text_message) - len(shortened)} characters!")
    
    
# do not change the following lines:
main()
