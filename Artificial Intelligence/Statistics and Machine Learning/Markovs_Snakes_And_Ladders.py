# Enter your code here. Read input from STDIN. Print output to STDOUT

# numpy doen's work
import random 
def roll(p):
    r = random.random()
    for i in range(6):
        if r <= p[i]: return i+1

def ladder_snake(cur, ladders, snakes):
    # in case there's a chain
    prev = -1
    while prev != cur:
        prev = cur
        if cur in ladders: cur = ladders[cur]
        if cur in snakes: cur = snakes[cur]
    return cur

if "__main__" == __name__:
    nTests = int(input())
    
    for _ in range(nTests):
        # read the inputs
        p = [float(x) for x in input().split(",")]
        # skip the ladder and snake count
        input()
        # read the ladders
        ladders = {int(s.split(",")[0]):int(s.split(",")[1]) for s in input().split()}
        # read the snakes
        snakes = {int(s.split(",")[0]):int(s.split(",")[1]) for s in input().split()}

        # start the simulation
        for i in range(1, 6): p[i] += p[i-1] # make cumulative
        total_steps = 0
        successful_games = 0

        for _ in range(5000): # 5000 simulations for each board
            
            cur, n_moves = 1, 0
            # check if ladder is in first cell
            cur = ladder_snake(cur, ladders, snakes)
            
            while n_moves < 1000:
                n_moves += 1
                m = roll(p)    
                cur += m
                if cur == 100: break
                
                if cur > 100:
                    cur -= m 
                    continue
                # move throught ladders and snakes
                cur = ladder_snake(cur, ladders, snakes)

            if cur != 100: continue # game didn't end

            # successfully ended a simulation
            total_steps += n_moves
            successful_games += 1

        print(total_steps // successful_games)
    
