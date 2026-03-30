import pytest
from barkpy import puppy_eyes_translator, good_boy_generator, mailman_alert, zoomie_timer, paw_selector

class TestPuppyEyesTranslator:
    def test_puppy_eyes_translator_returns_string(self):
        '''
        Verify puppy_eyes_translator() returns a string for valid input.
        '''
        actual = puppy_eyes_translator("Can you review my PR?", 7)
        assert isinstance(actual, str), (
            f"Expected puppy_eyes_translator() to return a string. "
            f"Instead, it returned {actual}"
        )
        assert len(actual) > 0, (
            f"Expected puppy_eyes_translator() not to be empty. "
            f"Instead, it returned a string with {len(actual)} characters"
        )
        assert actual.startswith("*whimper*"), (
            f"Expected output to start with '*whimper*'. Instead, it returned {actual}"
        )

    def test_puppy_eyes_translator_adds_required_phrases(self):
        '''
        Verify puppy_eyes_translator() adds the puppy-eyes phrases.
        '''
        actual = puppy_eyes_translator("Can you review my PR?", 7)
        assert "*whimper*" in actual, (
            f"Expected output to include '*whimper*'. Instead, it returned {actual}"
        )
        assert "*tilts head*" in actual, (
            f"Expected output to include '*tilts head*'. Instead, it returned {actual}"
        )
        assert "*big round eyes*" in actual, (
            f"Expected output to include '*big round eyes*'. Instead, it returned {actual}"
        )

    def test_puppy_eyes_translator_high_sadness_adds_extra_phrase(self):
        '''
        Verify puppy_eyes_translator() adds extra sadness text when sadness_multiplier is high.
        '''
        actual = puppy_eyes_translator("Can you review my PR?", 9)
        assert "*sad tail thump*" in actual, (
            f"Expected output to include '*sad tail thump*'. Instead, it returned {actual}"
        )
        assert "*tiny puppy sigh*" in actual, (
            f"Expected output to include '*tiny puppy sigh*'. Instead, it returned {actual}"
        )
        assert isinstance(actual, str), (
            f"Expected puppy_eyes_translator() to return a string. "
            f"Instead, it returned {actual}"
        )

    def test_puppy_eyes_translator_low_sadness_does_not_add_extra_phrase(self):
        '''
        Verify puppy_eyes_translator() does not add extra sadness text when sadness_multiplier is low.
        '''
        actual = puppy_eyes_translator("Help me", 3)
        assert "*sad tail thump*" not in actual, (
            f"Did not expect '*sad tail thump*' in output. Instead, it returned {actual}"
        )
        assert "*tiny puppy sigh*" not in actual, (
            f"Did not expect '*tiny puppy sigh*' in output. Instead, it returned {actual}"
        )
        assert "*whimper*" in actual, (
            f"Expected output to include '*whimper*'. Instead, it returned {actual}"
        )

    def test_puppy_eyes_translator_raises_error_for_empty_text(self):
        '''
        Verify puppy_eyes_translator() raises ValueError for empty request_text.
        '''
        with pytest.raises(ValueError, match="request_text must be a non-empty string"):
            puppy_eyes_translator("", 5)

    def test_puppy_eyes_translator_raises_error_for_invalid_multiplier_type(self):
        '''
        Verify puppy_eyes_translator() raises ValueError when sadness_multiplier is not an integer.
        '''
        with pytest.raises(ValueError, match="sadness_multiplier must be an integer"):
            puppy_eyes_translator("Can you help?", "7")

    def test_puppy_eyes_translator_raises_error_for_invalid_multiplier_range(self):
        '''
        Verify puppy_eyes_translator() raises ValueError when sadness_multiplier is outside 1 to 10.
        '''
        with pytest.raises(ValueError, match="sadness_multiplier must be between 1 and 10"):
            puppy_eyes_translator("Can you help?", 15)


class TestZoomieTimer:
    def test_zoomie_timer_returns_string(self):
        '''
        Verify zoomie_timer() returns a string for valid input.
        '''
        actual = zoomie_timer(3.5, False)
        assert isinstance(actual, str), (
            f"Expected zoomie_timer() to return a string. "
            f"Instead, it returned {actual}"
        )
        assert len(actual) > 0, (
            f"Expected zoomie_timer() not to return an empty string. "
            f"Instead, it returned a string with {len(actual)} characters"
        )

    def test_zoomie_timer_no_backyard(self):
        '''
        Verify zoomie_timer() suggests kitchen spins when has_backyard is False.
        '''
        actual = zoomie_timer(3.5, False)
        assert "spins in the kitchen" in actual, (
            f"Expected output to include 'spins in the kitchen'. Instead, it returned {actual}"
        )
        assert "zooms down the hallway" in actual, (
            f"Expected output to include 'zooms down the hallway'. Instead, it returned {actual}"
        )
        assert "3.5" in actual, (
            f"Expected output to include the sitting hours '3.5'. Instead, it returned {actual}"
        )

    def test_zoomie_timer_has_backyard(self):
        '''
        Verify zoomie_timer() suggests backyard sprints when has_backyard is True.
        '''
        actual = zoomie_timer(2.0, True)
        assert "wind sprints around the backyard" in actual, (
            f"Expected output to include 'wind sprints around the backyard'. Instead, it returned {actual}"
        )
        assert "zooms at full speed" in actual, (
            f"Expected output to include 'zooms at full speed'. Instead, it returned {actual}"
        )
        assert "2.0" in actual, (
            f"Expected output to include the sitting hours '2.0'. Instead, it returned {actual}"
        )

    def test_zoomie_timer_sprint_count_increases_with_hours(self):
        '''
        Verify zoomie_timer() increases sprint/spin count with more sitting hours.
        '''
        short = zoomie_timer(1.0, True)
        long = zoomie_timer(4.0, True)
        short_num = int(short.split("Time for ")[1].split(" wind")[0])
        long_num = int(long.split("Time for ")[1].split(" wind")[0])
        assert long_num > short_num, (
            f"Expected more sprints for longer sitting time. "
            f"Got {short_num} for 1.0 hours and {long_num} for 4.0 hours"
        )

    def test_zoomie_timer_raises_error_for_invalid_hours_type(self):
        '''
        Verify zoomie_timer() raises ValueError when sitting_hours is not a number.
        '''
        with pytest.raises(ValueError, match="sitting_hours must be a number"):
            zoomie_timer("three", False)

    def test_zoomie_timer_raises_error_for_negative_hours(self):
        '''
        Verify zoomie_timer() raises ValueError when sitting_hours is 0 or negative.
        '''
        with pytest.raises(ValueError, match="sitting_hours must be greater than 0"):
            zoomie_timer(-1, True)
        with pytest.raises(ValueError, match="sitting_hours must be greater than 0"):
            zoomie_timer(0, True)

    def test_zoomie_timer_raises_error_for_invalid_backyard_type(self):
        '''
        Verify zoomie_timer() raises ValueError when has_backyard is not a boolean.
        '''
        with pytest.raises(ValueError, match="has_backyard must be a boolean"):
            zoomie_timer(2.0, "yes")
        with pytest.raises(ValueError, match="has_backyard must be a boolean"):
            zoomie_timer(2.0, 1)


class TestGoodBoyGenerator:
    def test_good_boy_generator_returns_string(self):
        actual = good_boy_generator("TestName", 5)
        assert isinstance(actual, str), ("Expected good_boy_generator() to return a string."
                                        f"Instead, it returned {actual}")
        assert len(actual) > 0, (
            "Expected good_boy_generator() not to be empty. "
        )

    def test_good_boy_generator_returns_expected_text(self):
        actual = good_boy_generator("TestName", 5)
        assert "Who's a good developer?!" in actual, (
            f"Expected output to include 'Who's a good developer?!'. Instead, it returned {actual}"
        )
        assert 'You are, TestName, you are!' in actual, (
            f"Expected output to include 'You are, TestName, you are!'. Instead, it returned {actual}"
        )
        assert "*scritch*" in actual, (
            f"Expected output to include '*scritch*'. Instead, it returned {actual}"
        )

    def test_good_boy_generator_raises_value_error_out_of_range(self):
        with pytest.raises(ValueError, match="roughness must be an integer between 1 and 10 inclusive"):
            good_boy_generator("TestName", 11)

    def test_good_boy_generator_raises_value_error_name_not_string(self):
        with pytest.raises(ValueError, match="name must be a string"):
            good_boy_generator(20, 5)

    def test_good_boy_generator_raises_value_roughness_not_int(self):
        with pytest.raises(ValueError, match="roughness must be an integer"):
            good_boy_generator("TestName", "one")

    def test_good_boy_generator_roughness_effect(self):
        roughness = 7
        actual = good_boy_generator("TestName", roughness)
        phrase = "Who's a good developer?!"
        assert actual.count(phrase) == roughness, (
            f'Expected good_boy_generator() to return {roughness} "{phrase}" repetitions. '
            f'Instead, it returned {actual.count(phrase)}'
        )
        assert actual.count("*scritch*") == roughness, (
            f"Expected good_boy_generator() to return {roughness} belly rubs."
            f"Instead, it returned {actual.count('*scritch*')}"
        )


class TestMailmanAlert:
    def test_mailman_alert_returns_string(self):
        result = mailman_alert("Critical Bug in Production", 5)
        assert isinstance(result, str)
        assert "Bug" in result
        assert "BARK" in result or "WOOF" in result

    def test_mailman_alert_replaces_stress_words(self):
        result = mailman_alert("Critical ASAP Deadline", 4)
        assert "Critical" not in result
        assert "ASAP" not in result
        assert "Deadline" not in result

    def test_mailman_alert_empty_title_raises(self):
        with pytest.raises(ValueError):
            mailman_alert("", 3)

    def test_mailman_alert_invalid_title_type_raises(self):
        with pytest.raises(TypeError):
            mailman_alert(123, 3)

    def test_mailman_alert_invalid_annoyance_type_raises(self):
        with pytest.raises(TypeError):
            mailman_alert("Critical Bug", "5")

    def test_mailman_alert_out_of_range_raises(self):
        with pytest.raises(ValueError):
            mailman_alert("Critical Bug", 0)


class TestPawSelector:
    def test_paw_selector_returns_string(self):
        '''
        Verify paw_selector() returns a string for valid input.
        '''
        actual = paw_selector(["React", "Vue", "Svelte"], "Squeaky Ball")
        assert isinstance(actual, str), (
            f"Expected paw_selector() to return a string. "
            f"Instead, it returned {actual}"
        )
        assert len(actual) > 0, (
            f"Expected paw_selector() not to return an empty string. "
            f"Instead, it returned a string with {len(actual)} characters"
        )

    def test_paw_selector_chosen_option_in_output(self):
        '''
        Verify paw_selector() includes the chosen option in its output.
        '''
        options = ["React", "Vue", "Svelte"]
        actual = paw_selector(options, "Squeaky Ball")
        assert any(option in actual for option in options), (
            f"Expected output to contain one of {options}. "
            f"Instead, it returned {actual}"
        )

    def test_paw_selector_favorite_toy_in_output(self):
        '''
        Verify paw_selector() includes the favorite_toy in its output.
        '''
        actual = paw_selector(["React", "Vue", "Svelte"], "Squeaky Ball")
        assert "Squeaky Ball" in actual, (
            f"Expected output to include 'Squeaky Ball'. "
            f"Instead, it returned {actual}"
        )

    def test_paw_selector_output_contains_tail_wag(self):
        '''
        Verify paw_selector() always ends with the tail wag signature.
        '''
        actual = paw_selector(["Python", "Java"], "Rope Toy")
        assert "*tail wag*" in actual, (
            f"Expected output to include '*tail wag*'. "
            f"Instead, it returned {actual}"
        )

    def test_paw_selector_single_option(self):
        '''
        Verify paw_selector() works correctly when only one option is given.
        '''
        actual = paw_selector(["Svelte"], "Frisbee")
        assert "Svelte" in actual, (
            f"Expected output to contain 'Svelte'. "
            f"Instead, it returned {actual}"
        )
        assert "Frisbee" in actual, (
            f"Expected output to contain 'Frisbee'. "
            f"Instead, it returned {actual}"
        )

    def test_paw_selector_raises_error_for_empty_list(self):
        '''
        Verify paw_selector() raises ValueError when options list is empty.
        '''
        with pytest.raises(ValueError, match="options list cannot be empty"):
            paw_selector([], "Squeaky Ball")

    def test_paw_selector_raises_error_for_invalid_options_type(self):
        '''
        Verify paw_selector() raises TypeError when options is not a list.
        '''
        with pytest.raises(TypeError, match="options must be a list"):
            paw_selector("React", "Squeaky Ball")

    def test_paw_selector_raises_error_for_invalid_toy_type(self):
        '''
        Verify paw_selector() raises TypeError when favorite_toy is not a string.
        '''
        with pytest.raises(TypeError, match="favorite_toy must be a string"):
            paw_selector(["React", "Vue"], 42)

    def test_paw_selector_deterministic_with_seed(self):
        '''
        Verify paw_selector() picks consistently when random seed is fixed.
        '''
        import random
        random.seed(42)
        first = paw_selector(["React", "Vue", "Svelte"], "Bone")
        random.seed(42)
        second = paw_selector(["React", "Vue", "Svelte"], "Bone")
        assert first == second, (
            f"Expected same result with same random seed. "
            f"Got '{first}' and '{second}'"
        )
