def dest(s):
    dests = [None, 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    return str(bin(dests.index(s))[2:]).zfill(3)
    
def comp(s):
    import re
    result = ''
    if 'M' in s:
        result += '1'
    else:
        result += '0'
        
    secondVar = "(A|M)"
    plusOneRegex = "\s*\+\s*1"
    minusOneRegex = "\s*-\s*1"
    if "0" == s:
        result += "101010"
    elif "1" == s:
        result += "111111"
    elif "-1" == s:
        result += "111010"
    elif "D" == s:
        result += "001100"
    elif re.match(secondVar + "$", s):
        result += "110000"
    elif "!D" == s:
        result += "001101"
    elif re.match("!" + secondVar, s):
        result += "110001"
    elif "-D" == s:
        result += "001111"
    elif re.match("-" + secondVar, s): 
        result += "110011"
    elif re.match("D" + plusOneRegex, s): #D+1
        result += "011111"
    elif re.match(secondVar + plusOneRegex, s):
        result += "110111"
    elif re.match("D" + minusOneRegex, s):
        result += "001110"
    elif re.match(secondVar + minusOneRegex, s):
        result += "110010"
    elif re.match("D\s*\+\s*" + secondVar, s):
        result += "000010"
    elif re.match("D\s*-\s*" + secondVar, s):
        result += "010011"
    elif re.match(secondVar + "\s*-\s*D", s):
        result += "000111"
    elif re.match("D\s*&\s*" + secondVar, s):
        result += "000000"
    elif re.match("D\s*\|\s*" + secondVar, s):
        result += "010101"
    else:
        result = '0000000'
    return result

def jump(s):
    jumps = [None, 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
    return str(bin(jumps.index(s))[2:]).zfill(3)

'''
Created on Apr 15, 2012

@author: harvey
'''
