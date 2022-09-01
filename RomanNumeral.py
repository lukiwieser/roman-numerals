from pickletools import read_long1
import re

reAllowedSymbols = r"^[IVXLCDM]*$"
reStandartForm = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
reStandartFormRelaxed = r"^M*(CM|CD|D?C*)(XC|XL|L?X*)(IX|IV|V?I*)$" # M,C,X,I can occur more often

valueOfSymbols:dict[str, int] = {
    "I":1, 	
    "V":5, 
    "X":10, 	
    "L":50,	
    "C":100, 
    "D":500, 	
    "M":1000
}

def determineForm(text:str):
    if re.match(reStandartForm, text):
        return "STANDART_FORM"
    if re.match(reStandartFormRelaxed, text):
        return "STANDART_FORM_RELAXED"
    if re.match(reAllowedSymbols, text):
        return "ARBITRARY_ORDER"
    return "INVALID"

# text: string consiting of roman symbols
def romanToInt(text:str) -> int: 
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