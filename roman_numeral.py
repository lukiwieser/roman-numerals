import re

RE_ALLOWED_SYMBOLS = r"^[IVXLCDM]*$"
RE_STANDARD_FORM = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
RE_STANDARD_FORM_RELAXED = r"^M*(CM|CD|D?C*)(XC|XL|L?X*)(IX|IV|V?I*)$"  # M,C,X,I can occur more often

VALUE_OF_SYMBOLS: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def determine_form(text: str) -> str:
    """
    Determines the "form" of the roman number. I.e. if the number follows the standard, some relaxed versions of the
    standard, or contains invalid characters.

    :param text: roman number e.g. MMXXII
    :return: "form" of the roman number e.g. STANDARD_FORM
    """
    if re.match(RE_STANDARD_FORM, text):
        return "STANDARD_FORM"
    if re.match(RE_STANDARD_FORM_RELAXED, text):
        return "STANDARD_FORM_RELAXED"
    if re.match(RE_ALLOWED_SYMBOLS, text):
        return "ARBITRARY_ORDER"
    return "INVALID"


def roman_to_int(text: str) -> int:
    """
    Converts a roman number to integer

    :param text: roman number e.g. MMXXII
    :return: integer value of roman number e.g. 2022
    """
    if not re.match(RE_ALLOWED_SYMBOLS, text):
        raise ValueError(f"unknown symbols used")

    sum = 0
    buffer = 0
    for idx, symbol in enumerate(text):
        value = VALUE_OF_SYMBOLS.get(symbol)
        buffer += value

        # if last character we don't care about possible subtracting
        if idx + 1 == len(text):
            sum += buffer
            break

        # check next char to know if we add, subtract or wait (buffer)
        nextValue = VALUE_OF_SYMBOLS.get(text[idx + 1])

        if value < nextValue:
            sum -= buffer
            buffer = 0

        if value > nextValue:
            sum += buffer
            buffer = 0

    return sum
