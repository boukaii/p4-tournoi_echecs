class Boat:

    def __init__(self, name):
        self.name = name
        self.crew = list()

    def add_sailor(self, sailor):
        self.crew.append(sailor)
        sailor.wallet -= 2
        sailor.boat = self


class Sailor:

    def __init__(self, first_name, wallet):
        self.first_name = first_name
        self.wallet = wallet
        self.boat = None


# VIEWS

class MainView:

    @staticmethod
    def display_create_boat():
        print('#' * 79)
        print("# Création d'un bateau")
        print('#' * 79)

        names = input('Nom du bateau: ')
        return names

    @staticmethod
    def display_boat(boat):
        print('#' * 79)
        print("# Affichage d'un bateau")
        print('#' * 79)

        print('Nom du bateau: ' + boat.name)


# CONTROLLERS

class MainController:

    def __init__(self):
        self.view = MainView

    def create_boat(self):
        name = self.view.display_create_boat()
        boat = Boat(name=name)
        self.view.display_boat(boat)


# MAIN

ctrl = MainController()
ctrl.create_boat()





#
#
#
#
#
#
#
#
#
#
#
# class Boat:
#
#     def __init__(self, name):
#         self.name = name
#         self.crew = list()
#
#     def add_sailor(self, sailor):
#         self.crew.append(sailor)
#         sailor.wallet -= 2
#         # print('Le marin %s à été ajouté au bateau %s' % (sailor.first_name, self.name))
#         # print('Le marin {sailor_name} à été ajouté au bateau {boat_name}'.format(
#         #     sailor_name=sailor,
#         #     boat_name=self.name
#         # ))
#         sailor.boat = self
#
#
# class Sailor:
#
#     def __init__(self, first_name, wallet):
#         self.first_name = first_name
#         self.wallet = wallet
#         self.boat = None
#
#
# barque = Boat('barque')
# tintin = Sailor('Tintin', 10)
# haddock = Sailor('CPT Haddock', 30)
#
# barque.add_sailor(tintin)
# barque.add_sailor(haddock)
#
# for sailor in barque.crew:
#     print(sailor.first_name)
#
# print(tintin.boat.name)


# var_1 = 'VAR 1'
# var_2 = 'VAR 2'
# pattern = 'Le marin {sailor_name} à été ajouté au bateau {boat_name}'
# to_display = pattern.format(sailor_name=var_1, boat_name=var_2)
# print(to_display)











