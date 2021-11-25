import math
import random
import numpy
import os #it's just for clear screen 



# every point(individual) hav a name and list of coordinates (params or features)
class Point:
    def __init__(self,name,coordinates ): 
        self.name=name
        self.coordinates =coordinates 

    def getNearestCluster (self,clusters):

        distClusters=[]  # list to store distances between point and each cluster
        for cluster  in clusters:
            distClusters.append(math.dist(cluster.coordinates,self.coordinates)) # calculate dist and appand it in distClusters list
        minDist= min(distClusters) # get min dist from distClusters list
        nearestCluster=clusters[distClusters.index(minDist)] # get the cluster that have min dist with the point 
        return nearestCluster
             


# every cluster (centroid ) have name and list of coordinates and list of points that belonge to this cluster
class Cluster: 
    def __init__(self,name,coordinates):
        self.name=name
        self.coordinates=coordinates
        self.oldCoordinates=coordinates.copy() # store old coordinates 
        self.points=[]
         
    def recalculateCoordinates(self):
         
        if not self.points : # in case the cluster is empty (no points)
            return
        listOfPointsCordinates=[] # list to store all points coordinates as a matrix 
        for point in  self.points :
            listOfPointsCordinates.append(point.coordinates)
        numberOfPoints=len(listOfPointsCordinates)# number of points in this cluslter
        newCoordinates=[coordinate /  numberOfPoints for coordinate in numpy.sum(listOfPointsCordinates, axis=0) ] # calculate the sum of eche coordinate of points  then divide by number of points 
                                                                                                                   #[1        , 2       , 3        , 3.3        ]  p1
                                                                                                                   #[1        , 3       , 0        , 3.7        ]  p2 
                                                                                                                   #[(1+1)/2  ,(2+3)/2  , (3+0)/2  , (3.3+3.7)/2]
                                                                                                                   #[1        ,2.5      , 1.5      , 3.6        ]   new coordinates of cluster
        self.oldCoordinates=self.coordinates 
        self.coordinates=newCoordinates

    @staticmethod
    def generateRandomClusters(clustersNumber,points): # static method to generate initial clusters positions 
                                                       # how this work  it take random point than change in there coordinates(in range of -10 and 10 from there original values) to get random clusters 
        randomPoints=random.sample(points,clustersNumber) # this method will not work in case of  number of clusters > points
        # for randomPoint in randomPoints:
        #     print(randomPoint.name)
        clusters=[]
        for i, point in enumerate(randomPoints):
            newCoordinates=[]
            for coordinate in point.coordinates:
                newCoordinates.append(random.uniform(coordinate-10,coordinate+10))
            clusters.append(Cluster("c"+str(i), newCoordinates)) 
        return clusters 
    @staticmethod
    def isCoordinatesChanged(clusters):# return true if any cluster change hes coordinates
        for cluster in clusters:
            if cluster.oldCoordinates != cluster.coordinates:  
                return True
        return False




def addPoints(pointes):
    pointes.clear()
    os.system('cls') # in lunix change cls with clear 
    print('this is a small implementation  for kmeans algorithm devloped by Akram Ayeb ')
    print('points= '+str(len(points)))
    numberOfCoordinates=int(input('number of coordinates for eche point: '))
    coun=0
    while True:
        os.system('cls') 
        print('this is a small implementation  for kmeans algorithm devloped by Akram Ayeb ')
        print('points= '+str(len(points)))
        coordinates=[]
        print('p'+str(coun)+' :')
        for i in range(numberOfCoordinates):
            coordinates.append(float(input(' add cordinate '+str(i)+' ')))
        pointes.append(Point('p'+str(coun), coordinates))# create point and add it to pointes list (dataset)
        coun+=1
        os.system('cls')
        print('this is a small implementation  for kmeans algorithm devloped by Akram Ayeb ')
        print('points= '+str(len(points)))
        print('p'+str(i)+str(coordinates)+' add seccesfoly')
        print('1 for add new point ')
        print('2 for go back')
        choice =int( input())
        if choice==2:
            break



     






def kMeans(clustersNumber,points):
    clusters=Cluster.generateRandomClusters(clustersNumber, points) # get random clusters
    count=1
    while True:
        print('--- itiration'+str(count)+' ---')
        count +=1
        for point in points:# go to each point and get nearest cluster then appand it to theme
            nearestCluster=point.getNearestCluster(clusters)# get nearest cluster for this point
            nearestCluster.points.append(point)# appent this point to the  cluster  
        for cluster in clusters: # recalculate Coordinates of all clusters
            cluster.recalculateCoordinates()
            print(cluster.name)
            for point in cluster.points:
                print(' '+point.name, end = ' || ')
            print(' ')    
         
        if not Cluster.isCoordinatesChanged(clusters):
            break
        else:
            for cluster in clusters:
                cluster.points.clear() # if the coordinates chenged clrear the pointes belogne to eche cluster to start regroup agean
         



 
     
points=[] # data set
clustersNumber =1

 
# menu 
while True:
    os.system('cls') # in lunix change cls with clear 
    print('this is a small implementation  for kmeans algorithm devloped by Akram Ayeb ')
    print('clusters= '+str(clustersNumber)+' points= '+str(len(points)))
    print('1 for add points')
    print('2 change number of clusters')
    print('3 for start k-means algorithm')
    print('4 for exit')
    choice=int(input())

    if choice==1:
      addPoints(points)
    elif choice==2:
        clustersNumber=int(input('number of clusters '))
    elif choice==3:
        os.system('cls') 
        print('this is a small implementation  for kmeans algorithm devloped by Akram Ayeb ')
        if clustersNumber>0 and points:
            kMeans(clustersNumber, points)
        else:
            print('number of clusters or points is <1')
        input("click enter to countine")
    else  :
        break


 




 



 

