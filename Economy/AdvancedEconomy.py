from Economy.IntermediateEconomy import IntermediateEconomy


class AdvancedEconomy(IntermediateEconomy):
    def __init__(self, households, firms, banks, pension_funds, government, central_bank, markets, economic_policy):
        super().__init__(households, firms, banks, pension_funds)
        self.government = government
        self.central_bank = central_bank
        self.markets = markets
        self.economic_policy = economic_policy
