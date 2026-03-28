#Turn a normal request into a puppy-eyes request
def puppy_eyes_translator(request_text: str, sadness_multiplier: int) -> str:
    if not isinstance(request_text, str) or request_text.strip() == "":
        raise ValueError("request_text must be a non-empty string")

    if not isinstance(sadness_multiplier, int):
        raise ValueError("sadness_multiplier must be an integer")

    if sadness_multiplier < 1 or sadness_multiplier > 10:
        raise ValueError("sadness_multiplier must be between 1 and 10")

    words = request_text.strip().split()

    if len(words) >= 3:
        result = "*whimper* " + words[0] + " *tilts head* " + " ".join(words[1:-1]) + " *big round eyes* " + words[-1]
    elif len(words) == 2:
        result = "*whimper* " + words[0] + " *tilts head* " + words[1] + " *big round eyes*"
    else:
        result = "*whimper* " + words[0] + " *big round eyes*"

    if sadness_multiplier >= 7:
        result += " *sad tail thump*"

    return result


def mailman_alert(ticket_title, annoyance_level):
    if not isinstance(ticket_title, str):
        raise TypeError("ticket_title must be a string")
    if not ticket_title.strip():
        raise ValueError("ticket_title cannot be empty")
    if not isinstance(annoyance_level, int):
        raise TypeError("annoyance_level must be an integer")
    if annoyance_level < 1 or annoyance_level > 5:
        raise ValueError("annoyance_level must be between 1 and 5")

    stress_words = {
        "critical": {
            1: "woof",
            2: "WOOF",
            3: "WOOF WOOF",
            4: "BARK BARK",
            5: "BARK BARK! *snarl*",
        },
        "asap": {
            1: "woof soon",
            2: "WOOF soon",
            3: "WOOF WOOF soon",
            4: "BARK BARK soon",
            5: "BARK BARK NOW! *growl*",
        },
        "urgent": {
            1: "woof",
            2: "WOOF",
            3: "WOOF! WOOF!",
            4: "BARK! BARK!",
            5: "BARK BARK! *snarl*",
        },
        "production": {
            1: "yard",
            2: "YARD",
            3: "BIG YARD",
            4: "BIG YARD!",
            5: "BIG YARD! *protective growl*",
        },
        "deadline": {
            1: "walk time",
            2: "WALK TIME",
            3: "WALK TIME!",
            4: "WALK TIME NOW!",
            5: "WALK TIME NOW! *whine*",
        },
        "jira": {
            1: "mailman note",
            2: "MAILMAN NOTE",
            3: "MAILMAN ALERT",
            4: "MAILMAN ALERT!",
            5: "MAILMAN ALERT! *bark bark*",
        },
    }

    words = ticket_title.split()
    translated_words = []

    for word in words:
        clean_word = word.strip(".,!?;:").lower()
        punctuation = ""
        if word and word[-1] in ".,!?;:":
            punctuation = word[-1]

        if clean_word in stress_words:
            replacement = stress_words[clean_word][annoyance_level]
            translated_words.append(replacement + punctuation)
        else:
            translated_words.append(word)

    if annoyance_level == 1:
        prefix = "woof... "
        suffix = ""
    elif annoyance_level == 2:
        prefix = "WOOF! "
        suffix = ""
    elif annoyance_level == 3:
        prefix = "WOOF WOOF! "
        suffix = " *tail wag*"
    elif annoyance_level == 4:
        prefix = "BARK BARK! "
        suffix = " *guard dog stance*"
    else:
        prefix = "BARK BARK! *snarl* "
        suffix = " *protective growl*"

    return prefix + " ".join(translated_words) + suffix


def good_boy_generator(name: str, roughness: int):
    if not isinstance(name, str):
        raise ValueError("name must be a string")
    
    if not isinstance(roughness, int):
        raise ValueError("roughness must be an integer")
    
    if roughness < 1 or roughness > 10:
        raise ValueError("roughness must be an integer between 1 and 10 inclusive")
    
    repeats = "Who's a good developer?! " * roughness
    belly_rubs = "*scritch*" * roughness

    return (f"{repeats}\n" +
            f"You are, {name}, you are!\n" +
            f"*wag wag* {belly_rubs}\n" +
            "Have a treat! 🦴"
    )

