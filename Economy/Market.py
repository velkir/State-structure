class Market:
    def __init__(self, type, participants, commodities):
        self.type = type  # Тип рынка (товары и услуги, труд, финансы, недвижимость)
        self.participants = participants  # Участники на этом рынке (фирмы, домохозяйства, банки и т.д.)
        self.commodities = commodities  # Товары или услуги, которые обмениваются на этом рынке