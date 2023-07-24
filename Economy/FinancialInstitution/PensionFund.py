class PensionFund:
    def __init__(self, name, total_assets, contributing_members, retired_members, average_payout):
        self.name = name
        self.total_assets = total_assets
        self.contributing_members = contributing_members  # люди, которые сейчас вносят вклады
        self.retired_members = retired_members  # люди, которые получают пенсию
        self.average_payout = average_payout  # средняя выплата на одного пенсионера