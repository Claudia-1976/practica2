   
def print_score(score_players):

    ranking_round = dict(sorted(score_players.items(), key=lambda item: item[1]['pt_final'],reverse=True))
    
    print("{0} {1} {2} {3} {4} {5} ".format('Jugador','Kills','Asistencias','Muertes','MPVs','Puntos'))
    for elem in ranking_round:
        print(f"{elem:<8}{ranking_round[elem]['kills']:<6}{ranking_round[elem]['assists']:<12}{ranking_round[elem]['deaths']:<8}{ranking_round[elem]['MPV']:<5}{ranking_round[elem]['pt_final']}")
    