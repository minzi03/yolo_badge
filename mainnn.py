import sys
import time

def greet(name):
    return f"Hello, {name}! Welcome to our program."

def get_user_input():
    name = input("Enter your name: ")
    return name.strip() if name.strip() else "World"

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = get_user_input()
    
    print("Processing...")
    time.sleep(1)
    print(greet(name))
    
    print("\nThank you for using our program!")
    time.sleep(1)

if __name__ == "__main__":
    main()
