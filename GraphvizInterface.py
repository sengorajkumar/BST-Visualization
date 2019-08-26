from graphviz import Source, Graph
import math
import random

class GraphvizInterface:
    def __init__(self):
        self._graphdata=''

    def clearGraphData(self):
        self._graphdata =''

    def createGraphData(self, node):

        if node :
            if node._left is not None:
                self._graphdata += str(node._key) + "--" + str(node._left._key) + "[angle=240]" + "\n"
            else:
                nullLabel = str("null") + str(math.trunc(node._key))
                self._graphdata += str(node._key) + "--" + nullLabel + "[style=dotted]"+ "\n"
                self._graphdata += nullLabel + "[shape=point]" + "\n"

            if node._right is not None:
                self._graphdata += str(node._key) + "--" + str(node._right._key) + "[angle=110]" + "\n"
            else:
                nullLabel = str("null") + str(math.trunc(node._key)) + "1"
                self._graphdata += str(node._key) + "--" + nullLabel + "[style=dotted]"+ "\n"
                self._graphdata += nullLabel + "[shape=point]" + "\n"

            self.createGraphData(node._left)
            self.createGraphData(node._right)

    def generateGrap(self,filename = ""):
        #print(self._root._key)
        if filename =="":
            filename = "InitialBST"
        temp = """
             graph { 
        	node [shape=circle];
        	nodesep=0.5
        	splines="line"
        """ + self._graphdata +  """   } 
         """
        s = Source(temp, filename, format="png")
        s.view()


