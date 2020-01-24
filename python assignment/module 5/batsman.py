players = {'batsmen':{'Virat Kohli':{'matches':'206','runs':'8010','average':'47.4','highest_score':'264'},
                      'shikhar Dhawan':{'matches':'128','runs':'5355','average':'44.62','highest_score':'143'},
                      'Rohit sharma':{'matches':'227','runs':'10843','average':'59.58','highest_score':'183'}},
           'bowler':{'sainee':{'matches':'206','runs':'8010','average':'47.4','highest_score':'262'}},
           'wicket_keeper':{'MS Dhoni':{'matches':'206','runs':'5366','average':'47.4','highest_score':'200'}}}
print(players)
l1=[players['bowler']['sainee']['highest_score'],
    players['batsmen']['Virat Kohli']['highest_score'],
    players['batsmen']['shikhar Dhawan']['highest_score'],
    players['batsmen']['Rohit sharma']['highest_score'],
    players['wicket_keeper']['MS Dhoni']['highest_score']]
print('highest score=',max(l1))
