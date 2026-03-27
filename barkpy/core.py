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

def zoomie_timer(sitting_hours: float, has_backyard: bool) -> str:
    """
    Calculates the perfect Zoomie break based on how long you've been sitting.

    Arguments:
        sitting_hours (float): How long you've been sitting in hours.
        has_backyard (bool): Whether you have a backyard to sprint in.

    Returns:
        str: A suggested zoomie activity.
    
    Raises:
        ValueError: If sitting_hours is not a positive number or has_backyard is not a bool.
    """
    if not isinstance(sitting_hours, (int, float)):
        raise ValueError("sitting_hours must be a number")
    if sitting_hours <= 0:
        raise ValueError("sitting_hours must be greater than 0")
    if not isinstance(has_backyard, bool):
        raise ValueError("has_backyard must be a boolean")

    spins = max(1, int(sitting_hours))
    sprints = max(1, int(sitting_hours / 0.5))

    if has_backyard:
        return (
            f"You've been sitting for {sitting_hours} hours! "
            f"Time for {sprints} wind sprints around the backyard! "
            f"*zooms at full speed* 🐾"
        )
    else:
        return (
            f"You've been sitting for {sitting_hours} hours! "
            f"Time for {spins} spins in the kitchen and a quick bark at the mailman. "
            f"*zooms down the hallway* 🐾"
        )