from spydagram.app import stamp 

class d2(stamp):
    def __init__(self, fname, lname, subparam):
        super().__init__(fname, lname)
        self.subparam = subparam
    
    def childFunc():
        print(self.subparam)