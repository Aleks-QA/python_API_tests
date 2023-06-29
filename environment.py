import os

""" ЗАПУСК ТЕСТОВ НА РАЗНЫХ ОКРУЖЕНИЯХ
# Определить окружение для запуска(прописать переменную "ENV" в систему, нужно будет сменить терминал 
                                                                                            и ввести команду cmd(win))
set ENV=prod         # win,
export ENV=prod      # linux или mac

# Проверить что переменная окружения корректна
echo %ENV%

# Запуск с отчетом Allure
python -s -m pytest --alluredir=test_results/   

# Открыть отчеты Allure
allure serve test_results/
"""

class Environment:
    DEV = "dev"
    PROD = "prod"

    URLS = {
        DEV: "https://playground.learnqa.ru/api_dev",
        PROD: "https://playground.learnqa.ru/api"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


ENV_OBJECT = Environment()
