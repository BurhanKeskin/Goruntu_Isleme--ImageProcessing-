class Rectangle():
    def __init__(self,centerX, centerY, size = [120,120], rectColor = (0,100,255)):
        self.centerX = centerX
        self.centerY = centerY
        self.size = size
        self.rectColor = rectColor
    
    def updatePosition(self, cursor):
    
        if (self.centerX - self.size[0]//2 < cursor[0] < self.centerX + self.size[0]//2)  and (self.centerY - self.size[1]//2 < cursor[1] < self.centerY + self.size[1]//2):
            self.centerX, self.centerY = cursor[0], cursor[1]
            self.rectColor = (200,15,21)
        else:
            self.rectColor = (0,100,255)
            

rectangleList = []

for i in range(5):
    rectangleList.append(Rectangle((i*200)+100, 100))

for rect in rectangleList:
    print(rect.centerX, rect.centerY)    