
def getGameFromInput(textFile):
    with open(textFile) as f:
        lines = f.readlines()
    # ID: {color: [x,y,z]}
    game = {}

    for line in lines:
        id_draws = line.split(":")
        id = int(id_draws[0].split(" ")[1])
        game[id] = {}

        draws = id_draws[1].split(";")
        for draw in draws:
            splitDraw = draw.split(",")

            for balls in splitDraw:
                colour = balls.strip().split(" ")[1]
                numberOfBalls = balls.strip().split(" ")[0]

                if colour not in game[id]:
                    game[id][colour] = []

                game[id][colour].append(int(numberOfBalls))
    return game


def solve1(textFile):
    constraint = {"red":12, "green":13, "blue":14}
    solution = 0
    game = getGameFromInput(textFile)

    for id, draws in game.items():
        valid = True
        for colour, qs in draws.items():
            for q in qs:
                if q > constraint[colour]:
                    valid = False

        if valid:
            solution += id
    
    return solution

def solve2(textFile):
    game = getGameFromInput(textFile)
    solution = 0
    
    for id, draws in game.items():
        gamePower = 1
        for _, qs in draws.items():
            gamePower *= max(qs)
    
        solution += gamePower
    return solution

if __name__=="__main__":
    testInput = "day2Test.txt"
    input = "day2Input.txt"
    assert solve1(testInput) == 8
    assert solve2(testInput) == 2286
    print(solve1(input))
    print(solve2(input))
