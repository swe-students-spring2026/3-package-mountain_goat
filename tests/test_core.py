import pytest
from barkpy import puppy_eyes_translator


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