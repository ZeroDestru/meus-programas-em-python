from random import randint

tabu = []
res = 's'
pl1 = [0,0]
pl1s = 'X'
pl2 = [0,0]
pl2s = 'O'
conf1 = 0
conf2 = 0
conf3 = 0

for i in range(3):
    tabu.append([])
    for j in range(3):
        tabu[i].append(' ')


while(res == 's'):
    while(True):
        pl1[0] = int(input("player 1 digite a posição desejada 1 (1,2,3): "))-1
        pl1[1] = int(input("player 1 digite a posição desejada 2 (1,2,3): "))-1
    
        tabu[pl1[0]][pl1[1]] = pl1s
    
        for i in range(3):
            for j in range(3):
                print(f"[{tabu[i][j]}]",end=' ')
            print()

        for i in range(3):
            if(tabu[0][i] == pl1s):
                conf1 += 1

            if(tabu[1][i] == pl1s):
                conf2 += 1
        
            if(tabu[2][i] == pl1s):
                conf3 += 1

        if(conf1 == 3) or (conf2 == 3) or (conf3 == 3):
            print("player 1 ganhou")
            break

        conf1 = 0
        conf2 = 0
        conf3 = 0

        for i in range(3):
            if(tabu[i][0] == pl1s):
                conf1 += 1

            if(tabu[i][1] == pl1s):
                conf2 += 1
        
            if(tabu[i][2] == pl1s):
                conf3 += 1

        if(conf1 == 3) or (conf2 == 3) or (conf3 == 3):
            print("player 1 ganhou")
            break

        conf1 = 0
        conf2 = 0
        conf3 = 0

        for i in range(3):
            if(tabu[i][i] == pl1s):
                conf1 += 1

            if(tabu[i][2-i] == pl1s):
                conf2 += 1

        if(conf1 == 3) or (conf2 == 3):
            print("player 1 ganhou")
            break

        conf1 = 0
        conf2 = 0
        
        for i in range(3):
            for j in range(3):
                if(tabu[i][j] == pl1s) or (tabu[i][j] == pl2s):
                    conf1 += 1
        
        if(conf1 == 9):
            print("nenhum vencedor, empate")
            break
        conf1 = 0

        pl2[0] = int(input("player 2 digite a posição desejada 1 (1,2,3): "))-1
        pl2[1] = int(input("player 2 digite a posição desejada 2 (1,2,3): "))-1
    
        tabu[pl2[0]][pl2[1]] = pl2s
    
        for i in range(3):
            for j in range(3):
                print(f"[{tabu[i][j]}]",end=' ')
            print()

        for i in range(3):
            if(tabu[0][i] == pl2s):
                conf1 += 1

            if(tabu[1][i] == pl2s):
                conf2 += 1
        
            if(tabu[2][i] == pl2s):
                conf3 += 1

        if(conf1 == 3) or (conf2 == 3) or (conf3 == 3):
            print("player 2 ganhou")
            break

        conf1 = 0
        conf2 = 0
        conf3 = 0

        for i in range(3):
            if(tabu[i][0] == pl2s):
                conf1 += 1

            if(tabu[i][1] == pl2s):
                conf2 += 1
        
            if(tabu[i][2] == pl2s):
                conf3 += 1

        if(conf1 == 3) or (conf2 == 3) or (conf3 == 3):
            print("player 2 ganhou")
            break

        conf1 = 0
        conf2 = 0
        conf3 = 0

        for i in range(3):
            if(tabu[i][i] == pl2s):
                conf1 += 1
            if(tabu[i][2-i] == pl2s):
                conf2 += 1

        if(conf1 == 3) or (conf2 == 3):
            print("player 2 ganhou")
            break

        conf1 = 0
        conf2 = 0

        for i in range(3):
            for j in range(3):
                if(tabu[i][j] == pl1s) or (tabu[i][j] == pl2s):
                    conf1 += 1
        
        if(conf1 == 9):
            print("nenhum vencedor, empate")
            break
        conf1 = 0

    print("deseja jogar novamente ? (s/n)")
    res = input()

    for i in range(3):
        for j in range(3):
            tabu[i][j] = ' '
    conf1 = 0
    conf2 = 0
    conf3 = 0