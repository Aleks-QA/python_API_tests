FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
#CMD python -s -m pytest --alluredir=test_results/ /test_project/tests/
CMD where
CMD python -m pytest -s --alluredir=test_results/ /tests/
#RUN allure serve test_results/


#   docker build -t pytest_runner .       # создать образ
#   docker run --rm --mount type=bind,src=C:\Test\python_API_tests,target=/tests_project/ pytest_runner     #запуск

