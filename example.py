from barkpy import (
    good_boy_generator,
    mailman_alert,
    puppy_eyes_translator,
    zoomie_timer,
    paw_selector
)

def main():

    print("Testing puppy_eyes_translator")
    print()

    print("Input: puppy_eyes_translator('Can you review my PR?', 7)")
    print("Output:", puppy_eyes_translator("Can you review my PR?", 7))

    print("Input: puppy_eyes_translator('Please check my code', 3)")
    print("Output:", puppy_eyes_translator("Please check my code", 3))
    
    print("Input: puppy_eyes_translator('Help me', 5)")
    print("Output:", puppy_eyes_translator("Help me", 5))

    print("Input: puppy_eyes_translator('Help', 10)")
    print("Output:", puppy_eyes_translator("Help", 10))

if __name__ == "__main__":
    main()