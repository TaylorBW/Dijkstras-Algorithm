#Taylor Woehrle
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
#This is the module for part 1 (finding a path)
import Vertex
import sys, traceback

class Part_I_Find_Path:
    def findPath(self, G, start, end, visited):
        print("\n--------\nPart 1\n--------\n")
        self.start = start
        self.end = end
        #create boolean values to see if start and end are in list
        startFound = False
        endFound = False 
        currentNode = Vertex.Vertex(1, 1, 1, 1)   #initial current node as null since it is found in a loop and will check to see if exists
        
        
        #find node for start and end
        vertexList = G.v        
        for i in range(len(G.v)):
            if int(G.v[i].label) == int(start):    #see if found start node
                startNode = G.v[i]
                currentNode = startNode
                startFound = True
            if int(G.v[i].label) == int(end):  #see if found end node
                endNode = G.v[i]
                endFound = True
        #if not found terminate and print error message
        
        if(startFound == False):
            print("\n=======THERE IS NO NODE ",start," SYSTEM EXITING=======\n")
            sys.exit()
            return False
        
        if(endFound == False):
            print("\n=======THERE IS NO NODE ",end," SYSTEM EXITING=======\n")
            sys.exit()
            return False
        
        visited = [start]
        adjI = 0 #adjacent index
        backtoStartCounter = 0  #used to see how many adj have been checked of the starting node
        whileCounter =0    #used in error detection
        
        while backtoStartCounter <= len(startNode.adjacent):    #keep looping until all options have been exhausted
            whileCounter +=1 #used in error detection
            if whileCounter > 50000:#used in error detection
                print("\n==========INFINITE LOOP HAS OCCURED, NO PATH CAN BE FOUND\n==========")
                sys.exit()
                break #used in error detection
            #if current is deisred node
            if int(currentNode.label) == int(end):
                print("path has been found to node", currentNode.label)
                return True
            #else search list
            #if adjacent has not been visitied, set it as current node
            elif not currentNode.adjacent[adjI] in visited:
                #get adjacent node
                #append adjacent to visitied
                for i in range(len(G.v)):
                    if int(G.v[i].label) == int(currentNode.adjacent[adjI]):    #see if found start node
                        visited.append(currentNode.adjacent[adjI]) #add to visitied list
                        tempNode = currentNode      #save as temp to set as previous
                        currentNode = G.v[i]
                        currentNode.previous = tempNode
                        print("At node",currentNode.label)
                        adjI = 0
                        break
                
                
            #However, if adjacent has been visited, increment adjI #(if adjI is max go back)
            elif currentNode.adjacent[adjI] in visited:
                adjI = adjI+1
                if adjI >= len(currentNode.adjacent):#(if adjI is max go back)
                    if not currentNode.previous == None:
                        currentNode = currentNode.previous
                        print("Went back to node ",currentNode.label)
                        adjI = 0 #reset adjacent index (vistied adj will be stored in visited)
                        if currentNode.label == start: #if all the way back to start increment b2start
                            backtoStartCounter +=1
                            if backtoStartCounter >= len(startNode.adjacent): #if all adj of start node have been searched no path can be found
                                print("No path can be found")
                                return False
                        
            #used for debug
            else:
                print("ERROR")
        