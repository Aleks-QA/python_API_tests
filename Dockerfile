FROM python
WORKDIR /test_project/
#WORKDIR C:/Test/python_API_tests/test_project/
#COPY requirements.txt .
COPY / .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -s -m pytest --alluredir=test_results/ /test_project/tests/


#   docker build -t pytest_runner .
#   docker run --rm --mount type=bind,src=C:\Test\python_API_tests,target=/tests_project/ pytest_runner

