from node import Node
from edge import Edges
import numpy as np


class Graph:

    def __init__(self):
        '''
        Clase Grafo
        :atrib nodes: Diccionario los nodos del grafo
        :atrib edges: Lista de aristas del grafo
        '''
        self.nodes = {}
        self.edges = []

    def addNode(self, name):
        '''
        Agrega el nodo y sus atributos al diccionario
        :param name: nombre del nodo 
        '''
        node = self.nodes.get(name) 

        if node is None:
            self.nodes[name] = vars(Node())

   
    def addEdge(self, source, target, directed = False, auto = False, weight = None):
        '''
        Agrega el nodo a la lista
        :param source: nodo origen
        :param target: nodo destino
        :param directed: dirigido
        :param auto: ciclos
        :param weight: peso
        '''
        if auto is False:
            buc = source == target
        else:
            buc = False
        if weight == None:
            name = Edges(source, target, np.random.randint(1,100))
        else:
            name = Edges(source, target, weight)
        for edge in self.edges:
            if directed is False:
                comp = name != edge
            else:
                comp = False
            if name == edge or buc or comp:
                return False
        self.edges.append((name))
        self.nodes[source]['edges'].append([source, target])
        self.nodes[target]['edges'].append([target, source])

    def write(self, title, graph, nodes):
        '''
        Genera archivo de grafo con formato GraphViz 
        :param title: titulo del archivo
        :param nodes: numero de nodos
        '''
        with open(f"{title}_{nodes}.gv", "w") as f:
            f.write('Graph = {\n')
            #f.write('layout=circo;\n')
            for node in graph.nodes.keys():
                f.write(f'{node} [label="{node}"];\n')
            for edge in graph.edges:
                arista = list(edge)
                f.write(f'{arista[0]} -> {arista[1]} [label="{edge.weight}"];\n')
            f.write('}\n')
    
    def getDegree(self, node):
        '''
        Obtiene el número de aristas conectadas a un nodo 
        param: node: nodo
        :return grado del nodo
        '''
        deg = 0
        if len(self.edges) > 0:
            for nodes in self.edges:
                if list(nodes)[0] == node or list(nodes)[1] == node:
                    deg += 1
        return deg

    def getWeight(self, edge):
        '''
        Obtiene el peso de la arista 
        :param arista
        :return peso de la arista
        '''
        name = Edges(edge[0],edge[1], 0)
        for edges in self.edges:
            if (edges == name) | (edges != name):
                return edges.weight

    def writeDijkstra(self, title, graph, nodes, pesos):
        '''
        Genera archivo de grafo Dijkstra con formato GraphViz 
        :param title: titulo del archivo
        :param nodes: numero de nodos
        :pesos pesos: pesos calculados de cada nodo
        '''
        with open(f"{title}_{nodes}.gv", "w") as f:
            f.write('Graph = {\n')
            f.write('layout=sfdp\n')
            i=0
            for node in graph.nodes.keys():
                f.write(f'{node} [label="Nodo{node}_{pesos[i]}"];\n')
                i+=1
            for edge in graph.edges:
                arista = list(edge)
                f.write(f'{arista[0]} -> {arista[1]} \n')
            f.write('}\n')

