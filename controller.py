from views import MainView
from model import Tournament, Player, Tour, Match
from datetime import datetime


class MainMenuController:

    def __init__(self):
        self.view = MainView

    def bienvenue(self):
        self.view.bienvenue()

    def start_menu(self):
        ok = True
        while ok:
            try:
                choice_menu = self.view.welcome_menu()
                if choice_menu == 1:
                   self.start_tournament()
                elif choice_menu == 2:
                    ok = False
                elif choice_menu == 3:
                    ok = False
                elif choice_menu == 4:
                    print()
                    print("A bientôt!")
                    print()
                    self.exit_tournament()
                else:
                    raise ValueError
            except ValueError:
                print("veuillez entrer des caractères valides")

    def start_tournament(self):
        # demander les information du tournoi
        self.view.start_new_tournament()
        """
            infos sur le tournois
        """
        nom, lieu, date, nb_tour, day, time, description = self.view.get_data_tournament()
        Tournament(nom=nom, lieu=lieu, date=date, nb_tour=nb_tour, day=day, time=time, description=description)
        """
            type de tournoi
        """
        self.view.type_tournament()
        """
            infos sur le joueur
        """
        first_name, last_name, date_birth, gender, ranking = self.view.player_info()
        Player(first_name, last_name, date_birth, gender, ranking)
        # Créer le tournoi

        # Créer autant de joueurs qu'il y à de nb_players
        for player in range(9):
            player = self.view.player_info()
            print("Vous avez défini le nombre maximum de joueurs ")

        # Réaliser autant de rounds qu'il y à de nb_rounds
        #   - Créer un round
        #   - Définir les matchs pour le round (qui contre qui)
        #   - Afficher les matchs
        #   - pour chaque match, demander qui est le gagnant (mise à jours du classement)

    def exit_tournament(self):
        print("Voulez vous sauvegarder et quitter le tournoi en cours ? Y / N")
        valid_choice = True
        while valid_choice:
            choice = input("--->")
            if choice == 'Y':
                break
            if choice == 'N':
                pass
