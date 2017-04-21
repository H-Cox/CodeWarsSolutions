# Best practice solution from CodeWars by dgtlsoul
"""
class Automaton(object):

    def __init__(self):
        self.automata = {('q1', '1'): 'q2', ('q1', '0'): 'q1', 
                         ('q2', '0'): 'q3', ('q2', '1'): 'q2',
                         ('q3', '0'): 'q2', ('q3', '1'): 'q2'}
        self.state = "q1"

    def read_commands(self, commands):
        for c in commands:
            self.state = self.automata[(self.state, c)]
        return self.state=="q2"

my_automaton = Automaton()
"""


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
        return self.state==self.states[1]
            
my_automaton = Automaton()

print(my_automaton.read_commands(["1","0","0"]))
# Do anything necessary to set up your automaton's states, q1, q2, and q3.
