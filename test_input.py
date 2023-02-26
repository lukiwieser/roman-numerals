import sys

import roman_numeral as rn

text = sys.argv[1]
form = rn.determine_form(text)
print(form)
if form != "INVALID":
    print(rn.roman_to_int(text))