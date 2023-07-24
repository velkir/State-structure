from Economy.AdvancedEconomy import AdvancedEconomy


class FullEconomy(AdvancedEconomy):
    def __init__(self, households, firms, banks, pension_funds, government, central_bank, markets, economic_policy, international_trade, investments):
        super().__init__(households, firms, banks, pension_funds, government, central_bank, markets, economic_policy)
        self.international_trade = international_trade
        self.investments = investments
