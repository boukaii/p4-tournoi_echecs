from entrainementVUE import MainMenu, NewTournament
from model import Tournament, Player, Tour, Match


class MainMenuController:

    def __init__(self):
        self.view1 = MainMenu
        self.view2 = NewTournament
        self.view3 = TournamentController

    def test(self):
        self.view3.inf_tournament(self)

    def bienvenue1(self):
        self.view1.bienvenue()

    def start1_tournament(self):
        self.view1.display_continue_tournament()

    def start2_tournament(self):
        self.view1.display_rapports_tournament()

    def start_menu(self):
        ok = True
        while ok:
            try:
                choice_menu = self.view1.welcome_menu()
                if choice_menu == 1:
                    self.start_tournament()
                    # ok = False
                elif choice_menu == 2:
                    self.start1_tournament()
                    ok = False
                elif choice_menu == 3:
                    self.start2_tournament()
                    ok = False
                elif choice_menu == 4:
                    print()
                    print("A bientôt!")
                    print()
                else:
                    raise ValueError
            except ValueError:
                print("veuillez entrer des caractères valides")


class TournamentController:

    def __init__(self):
        self.view2 = NewTournament

    @staticmethod
    def inf_tournament(self):
        name, lieu, date = self.view2.tournament_input()
        info1 = Tournament(names=name, lieus=lieu, dates=date)
        self.view2.player_info()
        # self.view2.start_new_tournament()





    # @staticmethod
    # def inf_players(self):
    #     test5 = self.view2.player_info()
    #
    #     # name, first_name, birthday, sex = self.view3.input_player(player="name")
    #     # name, first_name, birthday, sex = self.view2.player_info()
    #     # info2 = Player(names=name, first_names=first_name, birthdays=birthday, sexs=sex)
    #     # self.view2.players_info()
    #
    #     first_name, last_name, date_birth, gender = self.view2.player_info()
    #     test = Player(names=first_name, first_names=last_name, birthdays=date_birth, sex=gender)
    #     self.view2.player_info(test)
    #
    def test3(self):
        self.view2.player_info()
#
#
# ctrl = MainMenuController()
# ctrl.bienvenue1()
# ctrl.start_menu()
#



# class ControllerType:
#
#     def __init__(self):
#         self.view = TypeTournament
#
#     def test(self):
#         self.view.type_tournament()
#
#     def types_tournaments(self):
#         while True:
#             try:
#                 choice = self.test()
#                 if choice not in [1, 2, 3]:
#
#                     print("veuillez entrer des caractères valides")
#                 else:
#                     raise ValueError
#             except ValueError:
#                 print("ERREUR")
#
#
# ctrl = ControllerType()
# ctrl.types_tournaments()

