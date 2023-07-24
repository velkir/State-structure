class Government:
    def __init__(self, type_of_government, executive_branch, legislative_branch, judicial_branch, economic_policy):
        self.type_of_government = type_of_government  # тип правительства (например, демократия, монархия, республика и т.д.)
        self.executive_branch = executive_branch  # исполнительная власть (может быть объектом класса "ExecutiveBranch")
        self.legislative_branch = legislative_branch  # законодательная власть (может быть объектом класса "LegislativeBranch")
        self.judicial_branch = judicial_branch  # судебная власть (может быть объектом класса "JudicialBranch")
        self.economic_policy = economic_policy
