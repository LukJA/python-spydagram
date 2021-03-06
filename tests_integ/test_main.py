# Full package tests 
# ~ pip install -e . ~
import spydagram as spy

def test_spydagram_true():
    assert(spy._init_True())

def test_sketchImport():
    sk = spy.sketch(None)
    assert (sk._helloWorld() == "Hello Sketch!")

def test_diagramImport():
    sk = spy.diagram(None)
    assert (sk._helloWorld() == "Hello Diagram!")