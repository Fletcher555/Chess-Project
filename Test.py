
def possibleMoves(position):
    possibleMoveList = []
    # Calculate the king moves.
    for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        print(x * 8 + y + 1)
        if 0 <= x < 8 and 0 <= y < 8:
            possibleMoveList.append(x * 8 + y + 1)
        else:
            break

    return possibleMoveList


print(possibleMoves(5))