import re

reAllowedSymbols = r"^[IVXLCDM]*$"

valueOfSymbols:dict[str, int] = {
    "I":1, 	
    "V":5, 
    "X":10, 	
    "L":50,	
    "C":100, 
    "D":500, 	
    "M":1000
}

def RomanToInt(text:str) -> int: 
    if not re.match(reAllowedSymbols,text):
        raise ValueError(f"unknown symbols used")
    
    sum = 0
    buffer = 0
    for idx, symbol in enumerate(text):
        value = valueOfSymbols.get(symbol)            
        buffer += value

        # if last charachter we dont care about possible subtracting
        if idx+1 == len(text):
            sum += buffer
            break
        
        # check next char to know if we add, substract or wait (buffer)
        nextValue = valueOfSymbols.get(text[idx+1])

        if value < nextValue:
            sum -= buffer
            buffer = 0

        if value > nextValue:
            sum += buffer
            buffer = 0

    return sum