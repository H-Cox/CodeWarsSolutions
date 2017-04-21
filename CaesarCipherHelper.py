# Best practice solution by r24
'''
class CaesarCipher(object):
    
    def __init__(self, shift):
        self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
        self.newalpha = self.alpha[shift:] + self.alpha[:shift]
        

    def encode(self, str):
        t = maketrans(self.alpha, self.newalpha)
        return str.upper().translate(t)
            
            
        
    def decode(self, str):
        t = maketrans(self.newalpha, self.alpha)
        return str.upper().translate(t)
'''

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift;

    # method to encode                 
    def encode(self, str):
        # initialise output
        output = ''
        # loop through characters to encode
        for letter in str.lower():
            
            # check if it is in range a - z
            if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
                
                # shift character using ascii values
                ordout = ord(letter)+self.shift

                # correct if it has gone out of a-z range
                if ordout > ord('z'):
                    ordout -= 26

                # append to output
                output += chr(ordout)

            # if not a - z, just append
            else:
                output += letter
        # return capitalised output
        return output.upper()

    # method to decode is very similar to encode but shift is taken away rather than added.    
    def decode(self, str):
        output = ''
        for letter in str.lower():
            if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
                ordout = ord(letter)-self.shift
                if ordout < ord('a'):
                    ordout += 26
                output += chr(ordout)
            else:
                output += letter
        return output.upper()

c = CaesarCipher(5)

print(c.encode(' AA '))
print(c.decode('BFKKQJX'))
