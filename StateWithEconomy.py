from State import State


class StateWithEconomy(State):
    def __init__(self, territory, population, government, economy):
        super().__init__(territory, population, government)
        self.economy = economy

