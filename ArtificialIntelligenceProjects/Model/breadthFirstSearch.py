#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
from collections import deque
#==============================================================================


#==============================================================================
#=============================Breadth First Search=============================
#==============================================================================
class BreadthFirstSearch(object):

    def __init__(self,startPosition,costPosition,maze):
        self.startPosition=startPosition
        self.costPosition=costPosition
        self.maze=maze
        self.createdNodes=0
        self.searchCost=0
        self.treeDepth=0
        self.costValue=5
        self.nodeList=self.searchPath()

    def getCreatedNodes(self):
        return(self.createdNodes)

    def getSearchCost(self):
        return(self.searchCost)

    def getTreeDepth(self):
        return(self.treeDepth)

    def getPath(self):
        path=[]
        while(self.nodeList!=None):
            path.append((self.nodeList[0],self.nodeList[1]))
            self.nodeList=self.nodeList[2]
        path.reverse()
        self.searchCost=self.getCost(path)-1
        self.treeDepth=len(path)-1
        return(path)

    def getCost(self,path):
        cost=0
        counter=0
        for i in range(len(path)):
            for j in range(len(self.costPosition)):
                if([path[i][0],path[i][1]]==[self.costPosition[j][0],self.costPosition[j][1]]):
                    cost+=self.costValue
                    counter+=1
        cost+=len(path)-counter
        return(cost)

    def searchPath(self):
        queue=deque([(self.startPosition[0],self.startPosition[1],None)]) #create queue
        while(len(queue)>0): #make sure there are nodes to check left
            nodeList=queue.popleft() #grab the first node
            x=nodeList[0] #get x
            y=nodeList[1] #get y
            if(self.maze[x][y]=="M"): #check if it's an meta
                self.reconstructMaze() #reconstruct the maze
                return(nodeList) #if it is then return the path
            if(self.maze[x][y]!="0"): #if it's not a path, we can't try this spot
                if((self.maze[x][y]=="S")or(self.maze[x][y]=="C")): #discard the starting point and the cost
                    pass #continue executing the algorithm
                else: #does not meet the condition
                    continue #return to the beginning of the loop
            self.maze[x][y]="explored" #make this spot explored so we don't try again
            for i in ([x,y-1],[x,y+1],[x-1,y],[x+1,y]): #new spots to try
                self.createdNodes+=1 #count the number of nodes created
                queue.append((i[0],i[1],nodeList)) #create the new spot, with node as the parent
        return([]) #return the empty list since we couldn't find any paths from here

    def reconstructMaze(self):
        self.maze[self.startPosition[0]][self.startPosition[1]]="S"
        for row in range(len(self.maze)):
            for column in range(len(self.maze)):
                if (self.maze[row][column]=="explored"):
                    self.maze[row][column]="0"
        for index in range(len(self.costPosition)):
            self.maze[self.costPosition[index][0]][self.costPosition[index][1]]="C"
#==============================================================================