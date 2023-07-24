class Demographics:
    def __init__(self, age_distribution, gender_distribution, marital_status, fertility_rate, mortality_rate):
        self.age_distribution = age_distribution  # Распределение по возрасту, например словарь: {'0-14': 20%, '15-24': 15%, '25-64': 50%, '65+': 15%}
        self.gender_distribution = gender_distribution  # Распределение по полу, например словарь: {'Male': 49%, 'Female': 51%}
        self.marital_status = marital_status  # Состояние в браке, например словарь: {'Single': 35%, 'Married': 50%, 'Divorced': 10%, 'Widowed': 5%}
        self.fertility_rate = fertility_rate  # Коэффициент рождаемости
        self.mortality_rate = mortality_rate  # Коэффициент смертности