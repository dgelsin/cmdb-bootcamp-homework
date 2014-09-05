import sys 

class FASTAReader(object):
    #with class always want to fill with an object, an object has data and functionality (can have methods and strings), class is the same as type, you are creating a new type of thing with class
    def __init__(self, file):
    #dunder methods, init initializes the state of the object
        self.file = file
        self.last_sid = None
    def next(self):
        if self.last_sid is None:
            line = sys.stdin.readline()
            #read very first line of the file
            assert line.startswith(">")
            #saftey check to make sure it's the right part we're reading
            sid = line[1:].rstrip("\r\n")
            #don't want > in the line, so you must do a slice [1:]
        else:
            sid = self.last_sid
        #else means otherwise

        sequences = []
        #make a list
        while True:
            line = sys.stdin.readline()
            #reads one line, can either get a header or sequence
            if line == "" and not sequences:
                raise StopIteration
            elif line.startswith(">") or line == "":
                self.last_sid = line[1:].rstrip("\r\n")
                #saves the previous sid before going to the next sid
                break
            #if line starts with > aka a header, we stop and move to sequence
            else: 
                sequences.append(line.strip())
                #what to get ride of the end space (black space) from the end of the sequence lines

        sequence = "".join(sequences)
#join together the list I passed you using this string as a delimiter (string is an empty string )
        return sid, sequence
        #return gives back data to the caller
    def __iter__(self):
        return self