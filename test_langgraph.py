# test_langgraph.py
from langgraph.graph import StateGraph, END

def test_node(state):
    return state

graph = StateGraph(dict)
graph.add_node("test", test_node)
graph.add_edge("test", END)

inputs = {}
output = graph.run(inputs)
for item in output:
    print(item)