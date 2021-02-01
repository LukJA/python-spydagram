import cairo

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

    def __init__(self,  filename: str = None, 
                        size: coordinate = (1000, 1000)):
 
        self.size = _coord(size[0], size[1])
        self.filename = filename
        self._surface = cairo.SVGSurface(filename, self.size.x , self.size.y) # None -> no output by default
        self._ctx = cairo.Context(self._surface)
        self._ctx.save()

        self._ctx.scale(self.size.x , self.size.y)  # Normalizing the canvas

    def print(self):
        self._ctx.restore()
        self._ctx.show_page()
        return self._surface.finish()

    def _tutorial_sketch(self):
        self._ctx.set_line_width(0.04)
        xc = 0.5
        yc = 0.5
        radius = 0.4
        angle1 = 45.0 * (pi / 180.0)  # angles are specified
        angle2 = 180.0 * (pi / 180.0)  # in radians
        self._ctx.arc(xc, yc, radius, angle1, angle2)
        self._ctx.stroke()
        # draw helping lines
        self._ctx.set_source_rgba(1, 0.7, 0.2, 0.6)
        self._ctx.arc(xc, yc, 0.05, 0, 2 * pi)
        self._ctx.fill()
        self._ctx.set_line_width(0.03)
        self._ctx.arc(xc, yc, radius, angle1, angle1)
        self._ctx.line_to(xc, yc)
        self._ctx.arc(xc, yc, radius, angle2, angle2)
        self._ctx.line_to(xc, yc)
        self._ctx.stroke()
    

    
    def _helloWorld(self):
        return "Hello Sketch!"

    def stamp(self, stamp):
        return stamp.seal()

class stamp:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def seal(self):
        return True


def svgToPng():
    print("TODO")