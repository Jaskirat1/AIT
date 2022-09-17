class fruits:
    def __init__(self, fname, fquality):
        self.fname = fname
        self.fquality = fquality


    def printfname(self):
        print(self.fname, self.fquality )



#chid class

class myapple(fruits):
    print("my fav fruits is apple")
    pass


obj = myapple("apple", "good")
