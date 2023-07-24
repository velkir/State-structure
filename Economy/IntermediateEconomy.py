from Economy.BasicEconomy import BasicEconomy


class IntermediateEconomy(BasicEconomy):
    def __init__(self, households, firms, banks, pension_funds):
        super().__init__(households, firms)
        self.banks = banks
        self.pension_funds = pension_funds
