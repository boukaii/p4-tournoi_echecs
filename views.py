class MainView:

    @classmethod
    def bienvenue(cls):
        print("#" * 28 + " " + "Bienvenue" + " " + "#" * 28)
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
        return int(input("Quel choix voulez vous faire ? "))

    @staticmethod
    def start_new_tournament():
        print("Création d'un nouveau tournoi")

    @staticmethod
    def display_continue_tournament():
        print("Vous reprenez un tournoi")

    @staticmethod
    def display_rapports_tournament():
        print("Rapports")

    @classmethod
    def get_data_tournament(cls):
        """
            Entrer des informations tournoi
        """
        nom = input("Quel sera le nom du nouveau tournoi ?")
        lieu = input("A quel endroit ?")
        date = input("A quel date ? ")
        day = input("Quel jour ? ")
        time = input("A quel heure ? ")
        nb_tour = 4
        print("le nombre de tour est définie par défault sur 4 ")
        description = input("Description du tournoi :")
        return nom, lieu, date, nb_tour, day, time, description

    @classmethod
    def type_tournament(cls):
        """
            Choisir le type d'échecs
        """
        print()
        print("#" * 28 + " " + "Veuillez choisir un type d'échecs" + "#" * 28 + " ")
        print()
        print("tapez 1 pour le mode Bullet")
        print("tapez 2 pour le mode Blitz")
        print("tapez 3 pour le mode Speed")
        return int(input("Quel mode avez-vous choisi ?"))

    @classmethod
    def player_info(cls):
        """
            Entrer des informations des joueurs
        """
        print("Entrer les informations des joueurs")
        first_name = str(input("Nom du joueur ?"))
        last_name = str(input("Prénom du joueur ?"))
        date_birth = int(input("Age ?"))
        gender = str(input("Genre ?"))
        ranking = int(input("Le classement ?"))
        return first_name, last_name, date_birth, gender, ranking


class StartTournament:

    @staticmethod
    def the_tournament_start():
        print("Début du Tournois")


# démarre le premier round
# saisie des scores et affichages des résultats

    @classmethod
    def result_tour(cls):
        print("Veuillez entrer les résultats des jours")




















    # @classmethod
    # def tournament_info(cls, tournament):
    #     """
    #        Sortie des informations tournoi
    #     """
    #     print("Name : {}".format(tournament.name))
    #     print("Place : {}".format(tournament.place))
    #     print("Date : {}".format(tournament.tour_date))

    # @classmethod
    # def players_info(cls, players):
    #     """
    #         Sortie des informations des joueurs
    #     """
    #     counter = 1
    #     for player in players:
    #         print("\n*******PLAYER N°{}******".format(counter))
    #         print("Nom : {}".format(player.first_name))
    #         print("Prénom : {}".format(player.last_name))
    #         print("Genre : {}".format(player.gender))
    #         print("Age : {}".format(player.date_birth))
    #         print("Classement : {}".format(player.ranking))
    #         counter += 1

