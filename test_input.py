import RomanNumeral as RN

import sys
text = sys.argv[1]

form = RN.determineForm(text)
print(form)
if(form != "INVALID"):
    print(RN.romanToInt(text))