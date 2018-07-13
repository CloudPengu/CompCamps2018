import random, enemy

descriptions = ["Deadly", "Dangerous", "Spooky", "Demonic"]
location_types = ["Cage", "Void", "Subway", "McDonalds"]


class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
