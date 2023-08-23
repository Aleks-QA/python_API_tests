<h3 tabindex="-1" dir="auto">Проект по автоматизации тестирования learnQA</h3>
<hr>
<h4 dir="auto"><em>В процессе тестов происходит:</em></h4>
<ul>
    <li>Создание нового пользователя, авторизация, редактирование и удаление</li>
    <li>Тестирование регистрации с некорректными данными</li>
    <li>Проверка определения сервером параметров клиента по строке заголовка User Agent</li>
     <li>Тесты авторизации пользователя с использованием токена и cookie</li>
</ul>
<hr>
<h4 dir="auto"><em>Для запуска тестов необходимо:</em></h4>
<ol>
     <li>Скачать проект с удаленного репозитория на свой локальный, с помощью команды:<br>     <code>git clone https://github.com/Aleks-QA/python_API_tests.git</code></li>
     <li>Открыть проект на установленной заранее IDE</li>
</ol>  

<h5><em>Запуск тестов:</em></h5>
<ol>
     <li>Создать и активировать виртуальное окружение:<br><code>python -m venv venv</code><br>
     <code>venv\Scripts\activate</code></li>
     <li>Установить все зависимости: <br>          <code>python -m pip install -r requirements.txt</code> </li>
     <li>Запустить тесты командой:<br><code>python -s -m pytest --alluredir=test_results</code> </li>
     <li>Открыть отчет о прохождении тестов командой:<br>          <code>allure serve test_results/ </code></li>
</ol>

<h5><em>Запуск тестов в Docker:</em></h5>
<ol>
    <li>Развернуть контейнеры с помощью команды:<br><code>docker-compose up --build</code></li>
    <li>Открыть отчет о прохождении тестов командой:<br>          <code>allure serve test_results/ </code></li>
</ol>
<hr>          
<h5>Добавлено краткое описание работы проекта в <a href="https://github.com/Aleks-QA/python_API_tests/blob/main/project_description.py" target="_blank">project_description.py</a></h5>
