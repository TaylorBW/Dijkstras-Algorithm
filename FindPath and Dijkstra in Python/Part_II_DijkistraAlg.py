#Taylor Woehrle
#Homework from Chapter 7 (1 and 3)
#3/6/16
#This program has two parts. 
#Part 1) finds a path between the vertices 9 and 29
#and prints the sequence of vertives that must be travered
#in the path between the two vertices.
#
#Part 2) uses Dikistra's algorithm to fine the minimum cose
#of visiting all other vertices from vertex 9 of the graph
#
#Limitations: the graph must be an XML file, it must have a posssible path from
#9 to the searched vertex, must have a vertices 9 and 29, and must have correct
#form of input data in the xml file
#
#This is the module for part 2 (question 3)
import sys, traceback

class Part_II_DijkistraAlg:
    def __init__(self):
            self.dunvisited = dunvisited
            self.dvisited = dvisited
    
    def Dijikstra(self, G, start, end):
        print("\n--------------------\npart 2 start\n--------------------")
        #step 1 initialize sets
        self.dunvisited = []
        self.dvisited = []
        
        #step 2, make sure start and end exit
        startFound = False
        endFound = False
        vertexList = G.v
        edgeList = G.e
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
            print("\n============START NODE DNE, EXITING PROGRAM===========")
            sys.exit()
            return False
        if(endFound == False):
            print("\n============END NODE DNE, EXITING PROGRAM===========")
            sys.exit() 
            
        #step 3 create loop for as long as there is more than 1 node in univisited and add startNode to unvisited
        currentNode = startNode
        currentNode.cost = 0
        visited = [start]
        adjI = 0 #adjacent index
        backtoStartCounter = 0  #used to see how many adj have been checked of the starting node
        whileCounter =0    #used in debug
        self.dijCalc(self, currentNode, G, self.dvisited) #calc cost from start
        
        #**********************************************
        while backtoStartCounter <= len(startNode.adjacent):    #keep looping until all options have been exhausted
            whileCounter +=1 #used in debug
            if whileCounter > 50000:#used in debug
                print("\n==========INFINITE LOOP HAS OCCURED, NO PATH CAN BE FOUND\n==========")
                sys.exit()
                break#used in debug
            #if current is deisred node
            if int(currentNode.label) == int(end):
                print("path found")
                print("min value to node ",start," from ",currentNode.label, " is ",currentNode.cost)
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
                        self.dijCalc(self, currentNode, G, self.dvisited)  #calculate all paths from current
                        adjI = 0
                        break
                
                
            #However, if adjacent has been visited, increment adjI #(if adjI is max go back)
            elif currentNode.adjacent[adjI] in visited:
                adjI = adjI+1
                if adjI >= len(currentNode.adjacent):#(if adjI is max go back)
                    if not currentNode.previous == None:
                        currentNode = currentNode.previous
                        self.dijCalc(self, currentNode, G, self.dvisited)  #calculate all paths from current
                        adjI = 0 #reset adjacent index (vistied adj will be stored in visited)
                        if currentNode.label == start: #if all the way back to start increment b2start
                            backtoStartCounter +=1
                            if backtoStartCounter >= len(startNode.adjacent): #if all adj of start node have been searched no path can be found
                                print("No path can be found")
                                return False
                        
            #used for debug and testing
            else:
                print("ERROR") 
            #*********************************************************
            
    def dijCalc(self,startNode, G, dvisited):
        self.dunvisited.append(startNode)
        currentNode = startNode
        ###########################################################
        while len(self.dunvisited) > 0:
            #print("calculating cost of adjacent for ",currentNode.label)
            #step 4 add current to visited and popped from unvisited
            self.dunvisited.pop()
            self.dvisited.append(currentNode)
            
            #step 5 for every adj see if adj is visited or not and compute costs
            #if in visited do nothing
            for i in range (len(currentNode.adjacent)):
                if currentNode.adjacent[i] in self.dvisited:
                    # print("already in dvisited") #used during testing
                    pass#i += i    #if in visited do nothing, but increment adjacent index
                
                elif not currentNode.adjacent[i] in self.dvisited:
                    #find adj node
                    for k in range(len(G.v)):
                        if int(G.v[k].label) == int(currentNode.adjacent[i]):    #see if found
                            adjacentNode = G.v[k]
                            #print("currentNode: ",currentNode.label," Adj Node:", int(adjacentNode.label)) #used for debug
                            #compute cost of arriving at adjacent
                            for j in range(len(G.e)):
                                #print("j", G.e[j].weight," tail",G.e[j].tail," Head",G.e[j].head)
                                if (int(currentNode.vertexId) == int(G.e[j].head)) and (int(adjacentNode.vertexId) == int(G.e[j].tail)):
                                    tempCost = float(currentNode.cost) + float(G.e[j].weight)
                                    #print("new tempCost")  #used for debug
                                    if tempCost < adjacentNode.cost or adjacentNode.cost == 0.00: #if better cost update
                                        adjacentNode.cost = tempCost
                                        #print("cost of ",adjacentNode.label," is ",adjacentNode.cost)
                                        self.dvisited.append(adjacentNode.label)
                                    #break #break for loop (edge found)
                                if (int(currentNode.vertexId) == int(G.e[j].tail)) and (int(adjacentNode.vertexId) == int(G.e[j].head)):
                                    tempCost = currentNode.cost + float(G.e[j].weight)
                                    if tempCost < adjacentNode.cost or adjacentNode.cost == 0.00: #if better cost update
                                        adjacentNode.cost = tempCost
                                        #print("cost of ",adjacentNode.label," is ",adjacentNode.cost)
                                        self.dvisited.append(adjacentNode.label)
                                    #break #break for loop (edge found)
        ###################################################                           