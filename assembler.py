import assemblerParser, symbolTable, code
    
# First pass to build the symbol table.
filename = 'test.asm'
Parser = assemblerParser.parser(filename)
Table = symbolTable.table()
romCounter = 0
while Parser.hasMoreCommands():
    Parser.advanceCommand()
    if Parser.commandType() == Parser.L_COMMAND:
        Table.addEntry(Parser.symbol(), romCounter)
    else:
        romCounter += 1


newFilename = filename.split('.')[0] + '.hack'
outputFile = open(newFilename, 'w')

#Second pass to create code

WORD_SIZE = 16
currentMemoryLocation = 16
Parser = assemblerParser.parser(filename)

while Parser.hasMoreCommands():
    Parser.advanceCommand()
    output = ''
    if Parser.commandType() == Parser.C_COMMAND:
        output = '111' + code.comp(Parser.comp()) + code.dest(Parser.dest()) + code.jump(Parser.jump()) + '\n'
        outputFile.write(output)
    elif Parser.commandType() == Parser.A_COMMAND:
        symbol = Parser.symbol()
        try:
            symbol = int(symbol)
        except:
            pass
        
        if type(symbol) is int:
            binVal = bin(int(symbol))[2:]
        elif Table.contains(symbol):
            binVal = bin(Table.getAddress(symbol))[2:]
        else:
            Table.addEntry(symbol, currentMemoryLocation)
            binVal = bin(currentMemoryLocation)[2:]
            currentMemoryLocation += 1
        output = "0" * (WORD_SIZE - len(binVal)) + binVal
        outputFile.write(output + "\n")
    elif Parser.commandType() == Parser.L_COMMAND:
        pass
    else:
        print('An error has occurred:\t', Parser.commands[Parser.counter], '\tLine: ', Parser.counter)
        
print(Table.symbolTable)
'''
Created on Apr 15, 2012

@author: harvey
'''
