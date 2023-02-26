# Roman Numerals

A small program to convert roman symbols to integers.

Example: `MMXXII` → `2022`

## Usage

You can simply use the functions by importing the file `roman_numeral.py`:

```python
import roman_numeral as rn

print(rn.roman_to_int("MMXXII"))
print(rn.determine_form("MMXXII"))
```

Or you can use the command line like this:

```console
python .\test_input.py IIIIIV
```

## More

We try our best to convert the symbols to a number, even if they do not follow the standard form.

There are multiple ways to handle roman numbers. For more information take a look at their [Wikipedia article](https://en.wikipedia.org/wiki/Roman_numerals).
