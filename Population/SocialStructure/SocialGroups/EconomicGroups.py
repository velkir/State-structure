class EconomicGroups:
    def __init__(self, income_brackets, employment_status, occupations, industries):
        self.income_brackets = income_brackets  # Разбивка по уровню дохода, скажем, 'низкий', 'средний', 'высокий'
        self.employment_status = employment_status  # Статус занятости, например, 'трудоустроен', 'безработный', 'нетрудоспособный'
        self.occupations = occupations  # Разбивка по видам профессий
        self.industries = industries  # Разбивка по отраслям, в которых работают люди