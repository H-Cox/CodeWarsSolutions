class Automaton(object):

    def __init__(self):
        self.states = ['q1','q2','q3']
        self.state = self.states[0]
        
    # method to perform a command and change state
    def do_command(self,command):
        
        if self.state == self.states[2]:
            self.state = self.states[1]
        elif command == '1':
            self.state = self.states[1]
        elif self.state == self.states[0]:
            self.state = self.states[0]
        else:
            self.state = self.states[2]
            
    # method to read commands and report output
    def read_commands(self, commands):
        # loop through commands
        for command in commands:
            self.do_command(command)
        return self.state    
        # decide output
        if self.state == self.states[1]:
            return True
        else:
            return False
            
my_automaton = Automaton()

print(my_automaton.read_commands(["1","0","0"]))
# Do anything necessary to set up your automaton's states, q1, q2, and q3.
