import sys

class FASTAReader(object): #making a new type of 'thing'
    def __init__(self, file): #initilizes the state of the object, always pass self
        self.file = file
        self.last_sid = None
    def next(self):
        if self.last_sid is None:    
            line = sys.stdin.readline()
            assert line.startswith(">") #make sure it is a file that we expect
            sid = line[1:].rstrip("\r\n") #take the first character off of the string and at the end of the string 
        else:
            sid = self.last_sid
        
        sequences = []
        while True:
            line = sys.stdin.readline()
            if line == "" and not sequences:
                raise StopIteration
            if line.startswith(">") or line == "":
                self.last_sid = line[1:].rstrip("\r\n")
                break
            else:
                sequences.append( line.strip() ) #stripping whitespace from both ends

        sequence = "".join(sequences)  #adding the sequences together without any whitespace
        return sid, sequence
    def __iter__(self):
        return self    