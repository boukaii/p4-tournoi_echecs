class Tour:
    """ méthode avec constructeur """
    def __init__(self, name, date_debut, heure_debut, date_fin, heure_fin):
        """ attributs d'instances """
        self.name = name
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
        self.matches = []
    """ méthode d'instance(accessor: accéder à l'objet) """
    def get_tour(self):
        return [self.name, self.date_debut, self.heure_debut, self.date_fin, self.heure_fin, self.matches]


