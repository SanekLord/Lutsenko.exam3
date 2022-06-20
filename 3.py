class Tomato:
    # States tomato
    states = {0: "empty", 1: "sprout", 2: "green tomato", 3: "ripe tomato"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    #up states
    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f"\t * Tomato {self._index + 1}: {Tomato.states[self._state]}")

    #Examination tomato
    def is_ripe(self):
        if self._state == 3:
            return True
        return False


#class TomatoBush
class TomatoBush:
    # new object class Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    #up states
    def grow_all(self):
        for j in self.tomatoes:
            j.grow()

    #Examination tomato
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    #harvesting
    def give_away_all(self):
        self.tomatoes = []


#new class Gardener
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    #work
    def work(self):
        print("\n|*|*|*| Watering tomatoes |*|*|*|")
        self._plant.grow_all()

    #harvesting
    def harvest(self):
        if self._plant.all_are_ripe():
            print("--- Hooray! Everything is ripe, we are harvesting! ---")
            self._plant.give_away_all()
            print("$$$ Harvest is harvested! Let's go sell! $$$")
        else:
            print("*** It's too early! Need to water! ***")

    #info
    @staticmethod
    def knowledge_base():
        print("_______ Information _______ \n"
              "\t1. Water more often!\n"
              "\t2. Green is not good!\n"
              "\t3. Red is ripe!\n"
              "___________________________")


#Test
Gardener.knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener("Alibaba", great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()