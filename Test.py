import math

var = []

position = 3
print(f"Position is {position} on file: {(position - 1) % 8 + 1} and on rank: {math.ceil(position / 8)} ")

positionColumn = (position - 1) % 8 + 1
positionRow = math.ceil(position / 8)

# works
x = 0
print((position - ((x+1)*8)) - (1+x))

if position % 8 != 0:
    while position + ((x+1)*8) + (1+x) <= 64:
        var.append(position + ((x+1)*8) + (1+x))
        if (position + ((x+1)*8) + (1+x)) % 8 == 0:
            break
        x += 1





print(var)

