import argparse
# Argparse is used to create a CLI applications and parse arguments. Let's say you just said grep in linux. It gives you a warning about it's usage. This is argparse. 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('Welcome', help = 'This is the welcoming message')
    arguments = parser.parse_args()
