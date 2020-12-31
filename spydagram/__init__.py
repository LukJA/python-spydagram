import cairo

# Import testing clause
def _init_True():
    return True

def spydagram_helloWorld():
    print("Hellow Spydagram!")

class _coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class sketch:
    """Sketch object, called to build and output a sketch-style freehand image
    :param size: The canvas size in arbitrary integer units, defaults to (100, 100)
    :type size: coordinate
    """

    if not cairo.HAS_SVG_SURFACE:
        raise SystemExit('cairo was not compiled with SVG support')

    # Define coordinate as a tuple of integers for input
    # we will use the 
    from typing import Tuple
    coordinate = Tuple[int, int]

    # Collect the drawing libraries

    def __init__(self, filename: str, size: coordinate = (100, 100)):
        filename = filename.split('.')[0] + ".svg"
        self.size = _coord(size[0], size[1])
        self._surface = cairo.SVGSurface(filename, self.size.x , self.size.y)
        self._ctx = cairo.Context(self._surface)

        self._ctx.scale(self.size.x , self.size.y)  # Normalizing the canvas

    def print(self):
        return self._surface.finish()

    def _tutorial_sketch(self):
        self._ctx.scale(self.size.x , self.size.y)
        self._ctx.set_line_width(0.04)

        x, y = 0.1, 0.5
        x1, y1 = 0.4, 0.9
        x2, y2 = 0.6, 0.1
        x3, y3 = 0.9, 0.5

        self._ctx.move_to(x, y)
        self._ctx.curve_to(x1, y1, x2, y2, x3, y3)
        self._ctx.stroke()

        self._ctx.set_source_rgba(1, 0.2, 0.2, 0.6)
        self._ctx.set_line_width(0.03)

        self._ctx.move_to(x, y)
        self._ctx.line_to(x1, y1)
        self._ctx.move_to(x2, y2)
        self._ctx.line_to(x3, y3)
        self._ctx.stroke()
    

    
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