
"""Model"""


class Player:

    """ méthode """

    def __init__(self, name, first_name, birthday, sex, ranking):

        """ attributs d'instances """
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking


    """ méthode d'instance(accessor: accéder a l'objet) """

    def get_name(self):
       return self.name

    def get_first_name(self):
       return self.first_name

    def get_birthday(self):
       return self.birthday

    def get_sex(self):
       return self.sex

    def get_ranking(self):
       return self.ranking

    def __repr__(self):
        """ méthode renvoie la représentation sous forme de chaîne de l'objet (lisibles) """
        return repr(self.name + self.first_name + self.birthday + self.sex + self.ranking)


class Tour:
    """ méthode avec constructeur """

    def __init__(self, name, start_date, start_time, end_date, end_time):
        """ attributs d'instances """
        self.name = name
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.matches = []

    """ méthode d'instance(accessor: accéder à l'objet) """

    def get_tour(self):
        return [self.name, self.start_date, self.start_time, self.end_date, self.end_time, self.matches]


class Match:

    def __int__(self, player1, player2):
        self.score1 = 0
        self.score2 = 0
        self.player1 = player1
        self.player2 = player2
        self.single_match = ([self.player1.nom, self.score1], [self.player2.nom, self.score2])

    def get_score(self):
        return self.score1

    def get_player1(self):
        return self.player1

    def get_player2(self):
        return self.player2

    def get_unique_match(self):
        return self.single_match


class Tournament:

    def __init__(self, nom, lieu, date, nb_tour, tour, day, time, description):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tour = 4
        self.tour = tour
        self.day = day
        self.time = time
        self.description = description

    def get_nom(self):
        return self.nom

    def get_lieu(self):
        return self.lieu

    def get_date(self):
        return self.date

    def get_nb_tour(self):
        return self.nb_tour

    def get_tour(self):
        return self.tour

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time

    def get_description(self):
        return self.description


"""VUE"""


class MainMenuView:

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
        return int(input("quel est votre choix ? "))

    @classmethod
    def display_tournament(cls):
        print("ok")


class TournamentView:

    @classmethod
    def input_informations_tournament(cls):
        print()
        name = input("Quel nom souhaitez-vous donner au tournois ? ")
        print()
        lieu = input("Dans quel lieu souhaitez-vous faire le tournois ?")
        print()
        date = input("Quand souhaitez-vous le faire ?")
        return name, lieu, date

    @classmethod
    def print_informations_tournament(cls, informations):
        print()
        print("le nom du tournois sera" + informations.name)
        print()
        print("le tournois se déroulera à " + informations.lieu)
        print()
        print("il se déroulera le " + informations.date)


class PlayersView:

    @classmethod
    def input_player(cls, player):
        print()
        player.name = input("Quel est votre nom ?")
        print()
        player.first_name = input("Quel est votre prénom ? ")
        print()
        player.birthday = input(int("quel est votre âge ? "))
        print()
        player.sex = input("genre ? (M ou F")
        print()

    @classmethod
    def print_player(cls, players):
        nb_player = 1
        for player in players:
            print("nom du joueur : " + player.name)
            print("prénom du joueur : " + player.first_name)
            print("âge du joueur : " + player.birthday)
            print("genre du joueur : " + player.sex)
            nb_player += 1


"""controller"""


class MainMenuController:

    def __init__(self):
        self.view = MainMenuView

    def bienvenue1(self):
        self.view.bienvenue()

    def accueil_du_menue(self):
        self.view.welcome_menu()

    def start_tournament(self):
        self.view.display_tournament()


    def menu(self):
        while True:
            try:
                choice_menu = self.view.welcome_menu()
                if choice_menu == 1:
                   self.start_tournament()

                elif choice_menu == 2:
                    print()
                    print("Ravie de vous revoir")
                    print()
                    return choice_menu
                elif choice_menu == 3:
                    print()
                    print("Menu des rapports")
                    print()
                    return choice_menu

                elif choice_menu == 4:
                    print()
                    print("A bientôt!")
                    print()
                    return choice_menu
                else:
                    raise ValueError
            except ValueError:
                print("veuillez entrer des caractères valides")


class TournamentController:

    def __init__(self):
        self.view = TournamentView()

    def inf1(self):
        self.view.input_informations_tournament()

    def inf2(self):
        self.view.print_informations_tournament()


class PlayerController:

    def __init__(self, players):
        self.view = PlayersView
        self.view = players

    def question(self):
        self.view.input_player(self)

    def reponse(self):
        self.view.print_player(self, players="players")







