# Convert Roman numerals to integers

ROMAN_NUMERALS = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def roman_to_int(roman_numerals: str) -> int:
    """Convert Roman numerals to integers."""
    result = 0
    for i in range(len(roman_numerals)):
        if i > 0 and ROMAN_NUMERALS[roman_numerals[i]] > ROMAN_NUMERALS[roman_numerals[i - 1]]:
            result += ROMAN_NUMERALS[roman_numerals[i]] - 2 * ROMAN_NUMERALS[roman_numerals[i - 1]]
        else:
            result += ROMAN_NUMERALS[roman_numerals[i]]
    return result

TEST_CASES = [
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('MCMXCIV', 1994),
    ('X', 10)
]

for test_input, expected in TEST_CASES:
    assert roman_to_int(test_input) == expected