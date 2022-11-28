# Roman Numerals

A small program to convert roman symbols to integers.

## Usage

You can simply use the functions by importing the file:

```python
import RomanNumeral as RN
print(RN.romanToInt("MMXXII"))
print(RN.determineForm("MMXXII"))
```

Or you can use the commandline like this:

```console
python .\test_input.py IIIIIV
```

## More

We try our best to convert the symbols to a number, even if it does not follow standard form.

There are multiple ways to handle roman numbers. For more information take a look at their [Wikipedia article](https://en.wikipedia.org/wiki/Roman_numerals).
