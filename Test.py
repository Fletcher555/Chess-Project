from dataForChessGame import gameScale as gs
import math

myX = [22, 81, 122, 194, 234, 278, 346, 381]
# var = math.ceil(x / gs * 8)
myY = [141, 168, 219, 267, 320, 377, 429, 485]
# var = math.ceil((y - (gs / 2)) / gs * 8) + 2


for y in myY:
    var = math.ceil((y - (gs / 2)) / gs * 8) + 2
    print(var)


# pixelValues = [((((self.position - 1) % 8) + 1) * (self.gameScale / 8)) - (self.gameScale / 16),
#                      ((int((self.position - 1) / 8)) * (self.gameScale / 8)) - (3 * self.gameScale / 16) + (
#                               self.gameScale / 2)]