import spydagram as spy

# top level encassement
sk = spy.sketch("sketch.svg")

graph = spy.template.graph.d2("Andrews", "Luke", "Extra")

print(sk.stamp(graph))

sk.print()