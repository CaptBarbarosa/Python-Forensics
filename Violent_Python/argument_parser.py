import argparse
# Argparse is used to create CLI applications and parse arguments. For example, consider the 'grep' command in Linux. It provides a warning about its usage. This is where argparse comes in.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-Welcome', help='This is the welcoming message')  # If the user uses the -h (help) option, they will see positional arguments: "Welcome     This is the welcoming message". The code doesn't work if you don't provide a message after running 'python3 argument_parser.py'. However, if you add a "-" at the beginning of 'Welcome', then it becomes optional.
    parser.add_argument('-n', '--numbers', type=float, nargs=2)  # If you provide the code with -n OR --numbers, you have to provide 2 float values. To allow an infinite number of floats, you just need to use "nargs='*'". Moreover, with the double dash, we name the attribute 'numbers'.
    parser.add_argument('-o', '--operation', type=str, choices=['+', '-', '*', '/'], help='Allows you to select operations')
    
    arguments = parser.parse_args()
    if arguments.operation == '*' and arguments.numbers is not None:
        print(arguments.numbers[0] * arguments.numbers[1])
    # Etc., etc. I'm also well aware that this is an easy example, but I did it to explore the options of argparse.

