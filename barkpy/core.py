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