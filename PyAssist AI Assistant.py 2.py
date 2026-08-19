def main():
    print("================================")
    print("    PyAssist AI Assistant")
    print("================================")
    print("Type 'exit' to close PyAssist. \n")
    
    while True:
        user_input = input ("You: ")
        
        if user_input.lower() == "exit":
            print("PyAssist: Goodbye!")
            break
        
        if user_input.lower() == "hello":
            print("PyAssist: Hello! How can I help you?")
        
        elif user_input.lower() == "what is python":
            print("PyAssist: Python is a programming language.")
        
        elif user_input.lower() == "calculate 25 * 4":
            print("PyAssist: Result: 100")
            
        else:
            print("PyAssist: I don't understant that command yet.")
             
        

if __name__ == "__main__":
    main()
