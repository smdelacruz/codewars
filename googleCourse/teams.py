teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if away_team != home_team:
            print(away_team)