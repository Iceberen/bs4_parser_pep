## Проект парсинга pep
#### Описание проекта:
Учебный проект по созданию парсеров документации на Python.   
#### Функционал:
- Парсинг новых версий Python;
- Парсинг статусов версий и PEP;
- Загрузка архива с документацией;
- Вывод в формате PrettyTable или CSV.
   
#### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
  ```
  git clone https://github.com/Iceberen/bs4_parser_pep.git
  cd bs4_parser_pep
  ```
- Cоздать и активировать виртуальное окружение:
  - Windows
    ```
    python -m venv venv
    source venv/Scripts/activate
    ```
  - Linux
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
- Установить зависимости из файла requirements.txt:
  - Windows
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
  - Linux
    ```
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
- Пример для запуска проекта:
  - Windows:
    ```
    python main.py pep -o pretty
    ```
  - Linux:
    ```
    python3 main.py pep -o pretty
    ```

####  Справка:
  - Windows:
    ```
    python main.py -h
    ```
  - Linux:
    ```
    python3 main.py -h
    ```

#### Режимы работы:
- ```whats-new```	(Ссылки на список изменений в версиях Python);
- ```latest-versions```	(Ссылки на документацию Python);
- ```download```	(Загрузка документации последней версии Python);
- ```pep```	(Вывод статусов документов PEP).

#### Дополнительные параметры:
- ```-output pretty```	(Вывод в PrettyTable в консоль);
- ```-output file```	(Вывод в файл CSV).