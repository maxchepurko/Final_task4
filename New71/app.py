import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('data.csv')

# Вычисление средней зарплаты
average_salary = df['salary'].mean()

# Отбор сотрудников старше 30 лет
older_than_30 = df[df['age'] > 30]

# Вывод результатов
print(f"Средняя зарплата сотрудников: {average_salary:.2f}\n")
print("Сотрудники старше 30 лет:\n")
print(older_than_30[['name', 'age', 'salary']].to_string(index=False))