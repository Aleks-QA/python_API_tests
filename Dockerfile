FROM python
#WORKDIR — эта директива устанавливает текущий рабочий каталог для инструкций RUN , CMD , ENTRYPOINT , COPY и ADD .
WORKDIR /test_project/
#COPY — аналогично ADD но источником может быть только локальный файл или каталог.
COPY / .
#RUN - команды, которые будут выполняться в процессе сборки.
RUN pip install -r requirements.txt
#ENV - позволяет определить переменную среды.(prod or dev)
ENV ENV=prod
#CMD - команда, которая будет выполняться при запуске контейнера.
CMD python -s -m pytest --alluredir=test_results/ /test_project/tests/












#   docker-compose up --build           # запуск
#   allure serve test_results/          # отчет
