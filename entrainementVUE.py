class MainMenu:

    @classmethod
    def bienvenue(cls):
        print("#" * 28 + " " + "Bienvenue au tournois d'échecs" + " " + "#" * 28)
        print()
        welcome = input("#" * 20 + "(appuyer sur n'importe quel touche pour continuer: )" + "#" * 20)
        print()
        return welcome

    @classmethod
    def welcome_menu(cls):
        print()
        print("Taper '1' pour créer un nouveau tournoi")
        print("Taper '2' pour reprendre un tournoi")
        print("Taper '3' pour accéder aux rapports")
        print("Taper '4' pour quitter")
        return int(input("Que souhaitez-vous faire ? "))

    @staticmethod
    def start_new_tournament():
        print("Création d'un nouveau tournoi")

    @staticmethod
    def display_continue_tournament():
        print("Vous reprenez un tournoi")

    @staticmethod
    def display_rapports_tournament():
        print("Rapports")


class NewTournament:

    @classmethod
    def tournament_input(cls):
        """
            Entrer des informations tournoi
        """
        name = input("Quel sera le nom du nouveau tournoi ?")
        place = input("A quel endroit ?")
        tour_date = input("A quel date ? ")
        return name, place, tour_date

    @classmethod
    def tournament_info(cls, tournament):
        """
           Sortie des informations tournoi
        """
        print("Name : {}".format(tournament.name))
        print("Place : {}".format(tournament.place))
        print("Date : {}".format(tournament.tour_date))

    @classmethod
    def player_info(cls):
        """
            Entrer des informations des joueurs
        """
        first_name = str(input("Nom du joueur ?"))
        last_name = str(input("Prénom du joueur ?"))
        date_birth = int(input("Age ?"))
        gender = str(input("Genre ?"))
        return first_name, last_name, date_birth, gender

    @classmethod
    def players_info(cls, players):
        """
            Sortie des informations des joueurs
        """
        counter = 1
        for player in players:
            print("\n*******PLAYER N°{}******".format(counter))
            print("Nom : {}".format(player.first_name))
            print("Prénom : {}".format(player.last_name))
            print("Genre : {}".format(player.gender))
            print("Age : {}".format(player.date_birth))
            print("Classement : {}".format(player.ranking))
            counter += 1

    @staticmethod
    def type_tournament():
        """
            Choisir le type d'échecs
        """
        print()
        print("#" * 28 + " " + "Veuillez choisir un type d'échecs" + "#" * 28 + " ")
        print()
        print("tapez 1 pour le mode Bullet")
        print("tapez 2 pour le mode Blitz")
        print("tapez 3 pour le mode Speed")
        return int(input("Que souhaitez-vous faire ? "))

#
# class ExitTournament:
#
#     def exit_tournament(self):
#         print("Voulez vous sauvegarder et quitter le tournoi en cours ? Y / N")
#         valid_choice = True
#         while valid_choice:
#             choice = input("--->")
#             if choice == 'Y':
#                 break
#             if choice == 'N':
#                 pass
#
#
# class ResumeTournament:
#
#     @staticmethod
#     def resum_T():
#         print("------------------------------------------------\n"
#               "--------------Reprendre un tournoi--------------\n"
#               "------------------------------------------------\n")
#
#
# class ReportTournament:
#  @classmethod
#     def display_tournament_info(cls, tournament):
#         """
#            Sortie des informations tournoi
#         """
#         print("Name : {}".format(tournament.name))
#         print("Place : {}".format(tournament.place))
#         print("Date : {}".format(tournament.tour_date))

