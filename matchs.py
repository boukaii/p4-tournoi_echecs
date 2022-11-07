
class Matchs:

    def __int__(self, player1, player2):
        # self._player = Player(nom="guigui", prenom="lol")
        self.score = 0
        self.player1 = player1
        self.player2 = player2
        self._unique_match = ([self.player1, self.score], [self.player2, self.score])


        # self.unique_match = ([self.nom, self.prenom, self.score], [self.nom, self.prenom, self.score])
        # print(self.prenom)



"""
un match > dans un TUPLE dans 2 listes, chacune contenant deux élèments
instance de joueur
instance de score

player 1 = Nom + prenom + score 
player 2 = Nom + prenom + score


Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour
"""

