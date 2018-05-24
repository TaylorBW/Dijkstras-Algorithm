#Taylor Woehrle
#Homework from Chapter 7 (1 and 3)
#3/6/16
#This program has two parts. 
#Part 1) finds a path between the vertices start and end
#and prints the sequence of vertives that must be travered
#in the path between the two vertices.
#
#Part 2) uses Dikistra's algorithm to finds the minimum cost
#of visiting all other vertices from specified vertex of the graph
#
#Limitations: the graph must be an XML file, it must have a posssible path from
#the start node to the end vertex, and must have correct form of input data in the xml file
#
#This is the driver module of the program. It calls Part_I_Find_Path.py and Part_II_DijkistraAlg.py for Part1 and
# Part2 that are described above after parsing a graph in an xml file and putting the data
# into the data structures defined under Graph.py and Edge.py

import xml.dom.minidom
import Vertex
import Edge
import Graph
from Part_II_DijkistraAlg import Part_II_DijkistraAlg 
from Part_I_Find_Path import Part_I_Find_Path 
import sys, traceback

#this function calls all others
def main():
    g = getGraph()  #G = (v,e)
    visited = []    #visitied initializes as empty for part 1
    #get start and end values
    try:
        startVal = int(input("enter the start node label: "))
        endVal = int(input("enter the end node label: "))
    except:
        print("\n========INVALID NODE, NODE MUST BE AN INTEGER========n")
        sys.exit
    
    #call search w/ start and end w/ graph
    Part_I_Find_Path.findPath(Part_I_Find_Path, g, startVal, endVal, visited)
    Part_II_DijkistraAlg.Dijikstra(Part_II_DijkistraAlg,g, startVal, endVal)
    
#This function gets a graph from an xml file
def getGraph():
    try:
        filename = input("Enter the xml gile name for the graph: ")
        xmldoc = xml.dom.minidom.parse(filename)    #get file name
    except:
        print("\n========FILE NOT FOUND, SYSTEM EXITING========\n")
        sys.exit()
    
    #create lists to hold vertices and edges
    vertexList = []
    edgeList = []
    #create graph to hold edges and vertices
    graph = dict() #empty dictionary
    
    try:
        graph = xmldoc.getElementsByTagName("Graph") [0] #get elements under graphs
        #get vertex elements from xml file
        verticesEle = graph.getElementsByTagName("Vertices")[0]   #get vertices element
        vertices = verticesEle.getElementsByTagName("Vertex")    #get individual vertices
        #get edges elements from elements in xml file
        edgesEle = graph.getElementsByTagName("Edges")[0]   #get edges element
        edges = edgesEle.getElementsByTagName("Edge")    #get individual edges
    except:
        print("\n========BAD EXML FILE SYSTEM EXITING========\n")
        sys.exit()
    
    
        #put vertices into new list
    try:
        for element in vertices:
            #get all attributes for vertices and put them into a Vertex object
            vertexId = element.attributes["vertexId"].value
            x = element.attributes["x"].value
            y = element.attributes["y"].value
            label = element.attributes["label"].value
            newVertex = Vertex.Vertex(vertexId, x, y, label)
            vertexList.append(newVertex)    #add  vertex obj to list
            
        for element in edges:
            #get all attributes for edges and put them into an Edge object
            weight = element.attributes["weight"].value
            tail = element.attributes["tail"].value
            head = element.attributes["head"].value
            newEdge = Edge.Edge(head, tail, weight)
            edgeList.append(newEdge)    #add edge obj to list

        #get adjacent nodes for vertices
        for i in range (len(edgeList)):
            #get head and tail of first edge
            currTail = edgeList[i].tail  #!!!!currtail = vertexID NOT label!!!!
            currHead = edgeList[i].head
            #adjacent to head/tail them to each vertex w/ id == head/tail
            for j in range (len(vertexList)):
                if vertexList[j].vertexId == currTail:
                    tailNode = vertexList[j]
                if vertexList[j].vertexId == currHead:
                    headNode = vertexList[j]
                    
            tailNode.adjacent.append(headNode.label)     #append tail node adjacent
            headNode.adjacent.append(tailNode.label)    #append head node adjacent
            
        newGraph = Graph.Graph(vertexList, edgeList) #put vertices and edges into graph
        return newGraph #return G(V,E)
    except:
        print("\n========INVALID DATA SYSTEM EXITING========\n")
        sys.exit()

        
if __name__ == "__main__":
    main()