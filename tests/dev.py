import spydagram as spy

# top level encassement
sk = spy.sketch("sketch.svg")

graph = spy.template.graph.d2([0,1,2,3])

print(sk.stamp(graph))

sk.print()