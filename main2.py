import sys

def greet(name):
    return f"Hello, {name}!"

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(greet(name))

if __name__ == "__main__":
    main()
