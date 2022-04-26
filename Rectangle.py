class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = x
    if x < 0:
        self.x = 0
    self.y = y
    if y < 0:
        self.y = 0
    self.height = h
    if h < 0:
        self.height = 0
    self.width = w
    if w < 0:
        self.width = 0

  def __str__(self):
    return '(x: ' + str(self.x) + ',' + 'y: ' + str(self.y) + ') width: ' + str(self.width) + ', height: ' + str(self.height)