import spydagram as spy

# top level encassement
sk = spy.sketch("sketch.svg")

graph2d = spy.template.graph.d2("Andrews", "Luke", "Extra")
graph3d = spy.template.graph.d2("Andrews", "Luke", "Bread")

graph2d.childFunc()
graph3d.childFunc()


print(sk.stamp(graph2d))

sk.print()