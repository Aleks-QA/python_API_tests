FROM python
#WORKDIR — эта директива устанавливает текущий рабочий каталог для инструкций RUN , CMD , ENTRYPOINT , COPY и ADD .
WORKDIR /test_project/
#COPY — аналогично ADD но источником может быть только локальный файл или каталог.
COPY / .
#RUN - команды, которые будут выполняться в процессе сборки.
RUN pip install -r requirements.txt
#ENV - позволяет определить переменную среды.
ENV ENV=dev
#CMD - команда, которая будет выполняться при запуске контейнера.
CMD python -s -m pytest --alluredir=test_results/ /test_project/tests/









#   docker build -t pytest_runner .       # создать образ
#   docker run --rm --mount type=bind,src=C:\Test\python_API_tests,target=/tests_project/ pytest_runner     #запуск

