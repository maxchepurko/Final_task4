Задание 4. Создание Docker-контейнера с Pandas
Цель: Научиться создавать Docker-контейнер с Python-приложением, которое выполняет анализ данных с использованием библиотеки Pandas. В этом приложении будет произведен расчет средней зарплаты и выборка сотрудников старше 30 лет.

Описание задания:
  Создайте директорию для проекта и необходимые файлы.
  Создайте файл data.csv с примерными данными о сотрудниках. Убедитесь, что в файле не менее 20 строк.
  Пример содержимого data.csv:
name,age,salary
Alice,30,70000
Bob,25,50000
Charlie,35,100000
David,40,120000
Eve,28,60000
Frank,50,150000
Grace,33,80000
Hank,29,55000
Ivy,42,110000
Jack,31,90000
Kathy,36,95000
Leo,24,48000
Mona,34,87000
Nina,26,65000
Oscar,45,140000
Paul,38,102000
Quinn,37,98000
Rachel,27,62000
Steve,32,93000
Tom,41,113000

  В файле app.py создайте Python-скрипт, который будет:
    Загружать данные из data.csv.
    Вычислять среднюю зарплату всех сотрудников.
    Отбирать и выводить только тех сотрудников, которым больше 30 лет.
  Создайте Dockerfile для сборки образа вашего Python-приложения, использующего Pandas.
  После запуска контейнера вы должны увидеть в терминале вывод с:
    Средней зарплатой всех сотрудников.
    Списком сотрудников, которым больше 30 лет.

Результат задания — после выполнения задания у вас будет Docker-образ, который при запуске выполняет анализ данных с использованием Pandas. Скрипт выводит среднюю зарплату сотрудников и список сотрудников старше 30 лет. 


## Docker Image
Docker образ доступен на Docker Hub: [mchepurko/docker-pandas-app](https://hub.docker.com/r/mchepurko/docker-pandas-app)
