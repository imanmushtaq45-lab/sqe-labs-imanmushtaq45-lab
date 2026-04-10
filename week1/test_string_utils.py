import pytest
from string_utils import (
    count_vowels, reverse_string, is_palindrome, 
    word_count, capitalise_words, remove_duplicates
)

# C5: Naming Convention test_<function>_<condition>
# C2 & C3: 18+ Tests with Edge Cases

# --- count_vowels Tests ---
def test_count_vowels_regular_string():
    """Test with normal lowercase words."""
    assert count_vowels("hello") == 2

def test_count_vowels_case_insensitive():
    """Test with uppercase vowels."""
    assert count_vowels("AEIOU") == 5

def test_count_vowels_empty_string():
    """Edge case: Empty string."""
    assert count_vowels("") == 0

# --- reverse_string Tests ---
def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_character():
    """Edge case: Single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

# --- is_palindrome Tests ---
def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_with_spaces_and_caps():
    """Edge case: Complex palindrome."""
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false_case():
    assert is_palindrome("hello") is False

# --- word_count Tests ---
def test_word_count_simple():
    assert word_count("Hello World") == 2

def test_word_count_multiple_spaces():
    """Edge case: String with extra spaces."""
    assert word_count("  spaces  only  ") == 2

def test_word_count_empty_string():
    assert word_count("") == 0

# --- capitalise_words Tests ---
def test_capitalise_words_lowercase():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_mixed_case():
    assert capitalise_words("sOftwAre qUality") == "Software Quality"

def test_capitalise_words_single_word():
    assert capitalise_words("python") == "Python"

# --- remove_duplicates Tests ---
def test_remove_duplicates_consecutive():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_long_sequence():
    """Edge case: Long duplicates (> 3)."""
    assert remove_duplicates("aaaaaa") == "a"

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("abcd") == "abcd"

# --- Exception Handling Test (Requirement 10.3) ---
def test_string_utils_none_input_raises_error():
    """Verifies TypeError is raised when input is None."""
    with pytest.raises(TypeError):
        count_vowels(None)