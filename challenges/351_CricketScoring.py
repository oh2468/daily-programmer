## https://old.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/

def score(balls):
    team_scores = [0] * 12
    all_players = [i for i in range(3, 12)]
    players = [1, 2]
    curr_p = 0
    player = players[curr_p]
    valid_balls = 0
    
    for ball in balls:
        valid_balls += 1
        if valid_balls % 6 == 0:
            curr_p += 1
            player = players[curr_p % 2]
        match ball:
            case ".":
                pass
            case "b":
                team_scores[0] += 1
                curr_p += 1
            case "w":
                team_scores[0] += 1
                valid_balls -= 1
            case "W":
                if not all_players:
                    break
                players[curr_p % 2] = all_players.pop(0)
            case _:
                runs = int(ball)
                team_scores[player] += runs
                if runs % 2 == 1:
                    curr_p += 1
        player = players[curr_p % 2]

    for p, score in enumerate(team_scores):
        if p == 0 or score == 0:
            continue
        print(f"P{p}: {score}")
    if team_scores[0]:
        print(f"Extras: {team_scores[0]}")
    print()

score("1.2wW6.2b34")
score("WWWWWWWWWW")
score("1..24.w6")

"""
challenge input:
challenge 1:
WWWWWWWWWW

challenge 2:
1..24.w6

challenge output:
challenge 1:
<NOTHING>

challenge 2:
P1: 7
P2: 6
Extras: 1
"""
