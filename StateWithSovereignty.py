from State import State


class StateWithSovereignty(State):
    def __init__(self, territory, population, sovereignty):
        super().__init__(territory, population)
        self.sovereignty = sovereignty
