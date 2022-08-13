import time

def slow_print(text):
    """Prints text slowly to add character to the game"""
    for character in text:
        print(character, end="")
        if character == ".":
            time.sleep(1)
        else:
            time.sleep(0.025)
    print('')