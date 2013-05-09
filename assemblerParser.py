class parser():

    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3
    JMP_COMMANDS = [None, 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
    def __init__(self, filename):
        self.counter = 0
        import re
        f = open(filename, 'r')
        self.commands = ['']
        for line in f:
            if not re.match('//', line.strip()) and len(line.strip()) != 0:
                self.commands.append(line.strip())
                
    def hasMoreCommands(self):
        return self.counter + 1 < self.commands.__len__()
    
    def advanceCommand(self):
        self.counter += 1
        self.current = self.commands[self.counter]
        
    def commandType(self):
        import re
        current = self.current
        if current[0] == '(' and re.search('\)', current):
            return self.L_COMMAND
            print('Debug')
        elif current[0] == '@':
            return self.A_COMMAND
        else:
            return self.C_COMMAND
        
    def symbol(self):
        if self.commandType() == self.A_COMMAND:
            return self.current.split('@')[1]
        elif self.commandType() == self.L_COMMAND:
            return self.current[1:(len(self.current) -1)]
        else:
            raise TypeError('You must have inputted a C_COMMAND.')
    
    def dest(self):
        current = self.current
        i = current.find('=')
        if i > -1:
            return current[:i]
        else:
            return None
        
    def comp(self):
        import re
        current = self.current
        index = current.find(';')
        if index > -1:
            current = current[:index]
        index = current.find('=')
        if index > -1:
            current = current[index + 1:]
        result = re.search("[^/]*", current)
        return result.group(0).strip()
    
    def jump(self):
        current = self.current
        for jmp in self.JMP_COMMANDS:
            if jmp == current:
                return jmp
            
                    
'''
Created on Mar 15, 2012

@author: harvey
'''
