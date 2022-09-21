from random import randint, shuffle

move = []
win = False
field = [[0,0,0],[0,0,0],[0,0,0]]
player_count = [int(x+1) for x in range(2)]
shuffle(player_count)
field_simbol = {0 : ' ', player_count[0] : '✖', player_count[1] : '◯'}







def can_win(a1,a2,a3):
    global move
    if (str(a1)+str(a2)+str(a3)).count('0') == 1:
        if a1 == a2 or a2 == a3 or a1 == a3:
            if a1 == 0: 
                move = [0,1,1]
                return True 
            elif a2 == 0:
                move = [1,0,1]
                return True 
            else: 
                move = [1,1,0]
                return True 
    return False
            

def ai_turn():
    global move
    move = []
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2]):
            move = [n, move.index(0)]
        if can_win(field[0][n], field[1][n], field[2][n]):
            move = [move.index(0),n]
    if can_win(field[0][0], field[1][1], field[2][2]):
        if field[0][0] == 0: move = [0,0]
        elif field[1][1] == 0: move = [1,1]
        else: move = [2,2]
    if can_win(field[2][0], field[1][1], field[0][2]):
        if field[2][0] == 0: move = [0,0]
        elif field[1][1] == 0: move = [1,1]
        else: move = [0,2]
    
    if move != []:
        return move
    else:
        while True:
            move = [randint(0, 2), randint(0, 2)]
            if field[move[0]][move[1]] == 0:
                return move






def check_win():
    # win = list(filter(lambda x: not 0 in x, field))
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2])
        check_line(field[0][n], field[1][n], field[2][n])
    check_line(field[0][0], field[1][1], field[2][2])
    check_line(field[2][0], field[1][1], field[0][2])

def check_line(a1,a2,a3):
    global win
    if a1 + a2 + a3 != 0:
        if a1 == a2 and a2 == a3:
            win = True
        if a1 == a2 or a2 == a3 or a1 == a3:
            return True
        else: return False

    

def prin_field(field):
    for i in field:
        print (field_simbol[i], end = ' | ')
    print()



while not win:

    list(map(lambda x: prin_field(x), field))
    player_count.insert(0, player_count.pop())

    print (player_count[0])

    if player_count[0] == 1:
        temp = [int(i) for i in input ('Ваш ход. Введите через пробел строку и колонку: ').split()]
        field[temp[0]-1][temp[1]-1] = 1

    if player_count[0] == 2:
        temp = ai_turn()
        field[temp[0]][temp[1]] = 2

    check_win()
    