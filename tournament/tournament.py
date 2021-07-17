def tally(rows):

    scores = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    score_tab = []
    teams = {}

    for res in rows:
        # First time in scoreboard
        if not res.split(";")[0] in teams:
            teams[res.split(";")[0]] = [res.split(";")[0],'0','0','0','0','0']
        if not res.split(";")[1] in teams:
            teams[res.split(";")[1]] = [res.split(";")[1],'0','0','0','0','0']

        # Matchs played
        teams[res.split(";")[0]][1] = str(int(teams[res.split(";")[0]][1])+1)
        teams[res.split(";")[1]][1] = str(int(teams[res.split(";")[1]][1])+1)

        # Wins
        if res.split(";")[2] == "win":
            teams[res.split(";")[0]][2] = str(int(teams[res.split(";")[0]][2])+1)
            teams[res.split(";")[1]][4] = str(int(teams[res.split(";")[1]][4])+1)

        # Loss
        elif res.split(";")[2] == "loss":
            teams[res.split(";")[1]][2] = str(int(teams[res.split(";")[1]][2])+1)
            teams[res.split(";")[0]][4] = str(int(teams[res.split(";")[0]][4])+1)

        # Draws
        elif res.split(";")[2] == "draw":
            teams[res.split(";")[1]][3] = str(int(teams[res.split(";")[1]][3])+1)
            teams[res.split(";")[0]][3] = str(int(teams[res.split(";")[0]][3])+1)

    # Scores
    for v in teams.values():
        v[5] = str(int(v[2])*3+int(v[3]))

    # Header
    score_tab.append(['Team','MP','W','D','L','P'])

    for t in sorted(sorted(teams.values()), key=lambda point: point[5], reverse = True):
        score_tab.append(t)

    return [scores.format(*row) for row in score_tab]
