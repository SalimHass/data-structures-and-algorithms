import pytest
from graph import Graph


def test_graph_empty():
    g1=Graph()

    with pytest.raises(KeyError):
        g1.add_edge("T","z")

def test_graph_not_exist():
    g1=Graph()
    f=g1.add_node("F")
    g=g1.add_node("G")

    g1.add_edge(f,g)


    with pytest.raises(KeyError):
        g1.add_edge(f,"z")

def test_graph_add():
    g2=Graph()
    a=g2.add_node("a")
    actual = g2.get_nodes()
    expected = ["a"]
    assert actual == expected


def test_tree_nighbores1():
    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    actual = graph.get_neighbors(a)
    expected = [['D', 1], ['C', 1], ['B', 1]]
    assert actual == expected

def test_tree_nighbores2():
    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    actual = graph.get_neighbors(d)
    expected = []
    assert actual == expected

def test_tree_nighbores3():
    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    actual = graph.get_neighbors(f)
    expected = [['G', 1], ['E', 1]]
    assert actual == expected


def test_tree_nodes1():
    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    actual = graph.get_nodes()
    expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert actual == expected


def test_tree_nodes2():
    graph = Graph()

    actual = graph.get_nodes()
    expected = []
    assert actual == expected

def test_tree_size1():
    graph=Graph()
    actual = graph.size()
    expected = 0
    assert actual == expected
def test_tree_size2():
    graph = Graph()
    a= graph.add_node("a")

    actual = graph.size()
    expected = 1
    assert actual == expected

def test_tree_size3():
    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    actual = graph.size()
    expected = 7
    assert actual == expected



