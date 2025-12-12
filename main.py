print("Hello the world")


class Damn:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def Point(self):
    return (self.x,self.y,self.z)
a = Damn(1,2,3)
print(a.Point())
