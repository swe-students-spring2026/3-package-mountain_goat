import pytest
from barkpy import puppy_eyes_translator, good_boy_generator


class Tests:
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
            good_boy_generator("TestName" , 11)
        
    def test_good_boy_generator_raises_value_error_name_not_string(self):
        with pytest.raises(ValueError, match="name must be a string"):
            good_boy_generator(20, 5)
    
    def test_good_boy_generator_raises_value_roughness_not_int(self):
        with pytest.raises(ValueError, match="roughness must be an integer"):
            good_boy_generator("TestName", "one")    
    
    def test_good_boy_generator_roughness_effect(self):
        roughness = 7
        actual = good_boy_generator("Riley", roughness)
        assert actual.count("*scritch*") == roughness, (
            f'Expected good_boy_generator() to return {roughness} "Who\'s a good developer?!" repetitions. '
            f'Instead, it returned {actual.count("Who\'s a good developer?!")}'
        )

        assert actual.count("*scritch*") == roughness, (
            f"Expected good_boy_generator() to return {roughness} belly rubs."
            f"Instead, it returned {actual.count('*scritch*')}"
        )


        