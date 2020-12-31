# Import testing clause
def _init_True():
    return True

def spydagram_helloWorld():
    print("Hellow Spydagram!")

class sketch:
    """Sketch object, called to build and output a sketch-style freehand image
    :param size: The canvas size in arbitrary integer units, defaults to (100, 100)
    :type size: coordinate
    """

    # Define coordinate as a tuple of integers
    from typing import Tuple
    coordinate = Tuple[int, int]

    def __init__(self, size: coordinate = (100, 100)):
        self.size = size
    
    def _helloWorld(self):
        return "Hello Sketch!"

class diagram:
    """Diagram object, called to build and output an assembled diagram image
    :param size: The canvas size in arbitrary integer units, defaults to (100, 100)
    :type size: coordinate
    """

    # Define coordinate as a tuple of integers
    from typing import Tuple
    coordinate = Tuple[int, int]

    def __init__(self, size: coordinate = (100, 100)):
        self.size = size
    
    def _helloWorld(self):
        return "Hello Diagram!"