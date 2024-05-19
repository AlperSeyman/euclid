
x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
y1 = int(input("Enter y1 : "))
y2 = int(input("Enter y2 : "))


points = [(x1,y1),(x2,y1),(x1,y2),(x2,y2)] # x1,y1  x2,y1  x1,y2   x2,y2


def euclideanDistance(cord1,cord2): 
    return pow(pow(cord1[0] - cord2[0],2) + pow(cord1[1] - cord2[1],2),0.5)


distance = []


for i  in range(len(points) -1):   
    for j in range(i+1,len(points)):
        distance.append(euclideanDistance(points[i],points[j]))
print("Distance : " , distance)


min = distance[0]

for i in range(len(distance)):
    if distance[i] < min:
        min = distance[i]

print("Minimum Distance : ",min)


        