import RomanNumeral as RN

# contains input (key), expected output ()
testcases = [
    #symbols
    ("I",1),	
    ("V",5), 
    ("X",10), 	
    ("L",50),	
    ("C",100), 
    ("D",500), 	
    ("M",1000),
    # standart forms examples
    ("IV",4),
    ("MCM",1900),
    ("MMXXII",2022),
    ("MLXVI",1066),
    # other additive forms
    ("IIII",4),
    ("XLIIII",44),
    # other subtractive forms
    ("CDXCIX",499 ),
    ("LDVLIV",499 ),
    ("XDIX",499 ),
    ("VDIV",499 ),
    ("ID",499),
    ("IIX",8),
    ("IIIXX",17),
    ("XIIX",18),
    ("XXIIX",28),
    ("IIIC",97),
    ("IIC",98),
    ("IC",99),
]

for (input, output_expect) in testcases:
    output = RN.romanToInt(input)
    is_success = (output_expect == output)
    print(str(is_success) + " / " + input + " / " + str(output) + " / " + str(output_expect))