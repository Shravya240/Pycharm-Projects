print("Tic Tac Toe")
ttt = [
    ["X  |  O  |  O"],
    ["O  |  X  |  X"],
    ["X  |  O  |  O"]
]

for row in ttt:
    print(*row)
    print("-" * 13)






print("Tic Tac Toe with Loops")
ttt = [
    ["X  |  O  |  O"],
    ["O  |  X  |  X"],
    ["X  |  O  |  O"]
]

for i in range(3):
    print(ttt[i][0])
    if i < 2:
        print("-" * 13)
