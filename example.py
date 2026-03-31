from barkpy import (
    good_boy_generator,
    mailman_alert,
    puppy_eyes_translator,
    zoomie_timer,
    paw_selector
)

def demo_puppy_eyes_translator():
    print("=== puppy_eyes_translator ===")
    print()

    print("Input: puppy_eyes_translator('Can you review my PR?', 7)")
    print("Output:", puppy_eyes_translator("Can you review my PR?", 7))

    print("Input: puppy_eyes_translator('Please check my code', 3)")
    print("Output:", puppy_eyes_translator("Please check my code", 3))

    print("Input: puppy_eyes_translator('Help me', 5)")
    print("Output:", puppy_eyes_translator("Help me", 5))

    print("Input: puppy_eyes_translator('Help', 10)")
    print("Output:", puppy_eyes_translator("Help", 10))


def demo_paw_selector():
    print("=== paw_selector ===")
    print()

    print("Input: paw_selector(['React', 'Vue', 'Angular'], 'tennis ball')")
    print("Output:", paw_selector(['React', 'Vue', 'Angular'], 'tennis ball'))

    print("Input: paw_selector(['Python', 'JavaScript', 'Go', 'Rust'], 'squeaky toy')")
    print("Output:", paw_selector(['Python', 'JavaScript', 'Go', 'Rust'], 'squeaky toy'))

    print("Input: paw_selector(['AWS', 'GCP'], 'chew bone')")
    print("Output:", paw_selector(['AWS', 'GCP'], 'chew bone'))

    print("Input: paw_selector(['merge', 'rebase'], 'frisbee')")
    print("Output:", paw_selector(['merge', 'rebase'], 'frisbee'))

def demo_good_boy_generator():
    print("=== good_boy_generator ===")
    print("Input: good_boy_generator('Alice', 1)")
    print("Output:", good_boy_generator('Alice', 1))

    print("Input: good_boy_generator('Bob', 3)")
    print("Output:", good_boy_generator('Bob', 3))

    print("Input: good_boy_generator('Joe', 5)")
    print("Output:", good_boy_generator('Joe', 5))

    print("Input: good_boy_generator('Rebecca', 10)")
    print("Output:", good_boy_generator('Rebecca',10))

def demo_mailman_alert():
    print("=== mailman_alert ===")
    print()

    print("Input: mailman_alert('Critical Bug in Production', 5)")
    print("Output:", mailman_alert("Critical Bug in Production", 5))

    print("Input: mailman_alert('ASAP Jira Deadline', 3)")
    print("Output:", mailman_alert("ASAP Jira Deadline", 3))

    print("Input: mailman_alert('Urgent Production Issue', 1)")
    print("Output:", mailman_alert("Urgent Production Issue", 1))

    print("Input: mailman_alert('Critical ASAP Bug', 4)")
    print("Output:", mailman_alert("Critical ASAP Bug", 4))

def demo_zoomie_timer():
    print("=== zoomie_timer ===")
    print()

    print("Input: zoomie_timer(3.5, False)")
    print("Output:", zoomie_timer(3.5, False))

    print("Input: zoomie_timer(2.0, True)")
    print("Output:", zoomie_timer(2.0, True))

    print("Input: zoomie_timer(1.0, False)")
    print("Output:", zoomie_timer(1.0, False))

    print("Input: zoomie_timer(4.0, True)")
    print("Output:", zoomie_timer(4.0, True))

def main():
    demo_puppy_eyes_translator()
    print()
    demo_zoomie_timer()
    print()
    demo_paw_selector()
    print()
    demo_good_boy_generator()
    print()
    demo_mailman_alert()



if __name__ == "__main__":
    main()
