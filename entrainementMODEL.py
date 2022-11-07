class Player:

    """ méthode """

    def __init__(self, names, first_names, birthdays, sexs):

        """ attributs d'instances """
        self.name = names
        self.first_name = first_names
        self.birthday = birthdays
        self.sex = sexs
        self.ranking = ""

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

    # def __repr__(self):
    #     """ méthode renvoie la représentation sous forme de chaîne de l'objet (lisibles) """
    #     return repr(self.name + self.first_name + self.birthday + self.sex + self.ranking)
    #


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

    # def __init__(self, nom, lieu, date, nb_tour, tour, day, time, description):
    def __init__(self, names, lieus, dates):
        self.name = names
        self.lieu = lieus
        self.date = dates
        self.nb_tour = ""
        self.tour = ""
        self.day = ""
        self.time = ""
        self.description = ""

    def get_nom(self):
        return self.name

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