class Point:

    def __init__(self,x,y):
        self.X=x
        self.Y=y
        
    def __str__(self):
        return f"X : {self.X} Y : {self.Y}"
    
    def show(self):
        print(f"X={self.X}, Y={self.Y}")
        
center=Point(23,34)
topLeft=Point(49,40)
rightBottom=Point(10,20)

print(center)