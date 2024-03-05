from models22 import *

query = (Employee.select(Employee.name, Department.name).join(Department).dict())

dep1 = Department.create(name='IT')
dep2 = Department.create(name='HR')
dep3 = Department.create(name='Finance')

emp1 = Employee.create(name='John Doe', department=dep1, salary=12000, experience=4)
emp2 = Employee.create(name='Alex Verb', department=dep2, salary=15000, experience=8)
emp3 = Employee.create(name='Nick Richards', department=dep1, salary=16000, experience=7)
emp4 = Employee.create(name='Nick Fury', department=dep2, salary=10000, experience=2)
emp5 = Employee.create(name='Stiven Williams', department=dep3, salary=20000, experience=7)
emp6 = Employee.create(name='Michail Lors', department=dep3, salary=7000, experience=1)



avg_salary = Employee.select(fn.AVG(Employee.salary)).scalar()
print(f'Средняя зарплата среди сотрудников {avg_salary}')

avg_salary_2 = Employee.select(fn.AVG(Employee.salary)).where(Employee.salary > 13000).scalar()
print(f'Средняя зарплата среди сотрудников выше 13000 {avg_salary_2}')

min_salary = Employee.select(fn.MIN(Employee.salary)).join(Department).where(Department.name == 'HR').scalar()
print(min_salary)

max_salary = Employee.select(fn.MAX(Employee.salary)).join(Department).where(Department.name == 'IT') & (Employee.name.startswith('J')).scalar()
print(max_salary)

employee_count = Employee.select().count
print(employee_count)

employee_count2 = Employee.select().where(Employee.experience > 5).count
print(employee_count2)

employee_count3 = Department.select().where(Department.fn.COUNT(Employee.id).alias('emlloyee_count')).join(Employee, JOIN.LEFT_outer).group_by(Department)
for department in employee_count3:
    print(department.name, department.employee_count)


salary_stddev = Employee.select((fn.STDDEV(Employee.salary)).scalar())
print(salary_stddev)

################################################################

# 1. Найти средний опыт работы всех сотрудников в отделе 'HR'.

avg_experience = Employee.select(fn.AVG(Employee.experience)).join(Department).where(Department.name == 'HR').scalar()
print(f'Средний опыт среди сотрудников отдела HR {avg_experience}')

# 2. Получить максимальную зарплату среди сотрудников со стажем более 5 лет.

max_salary = Employee.select(fn.MAX(Employee.salary)).where(Employee.experience > 5).scalar()
print(f'Максимальная зарплата среди сотрудников отдела со стажем болеее 5 лет {avg_experience}')

# 3. Подсчитать количество сотрудников в отделе 'IT'.

employee_count = Employee.select().join(Department).where(Department.name == 'IT').count()
print(f'Количество сотрудников в отделе IT {employee_count}')

# 4. Найти минимальную зарплату среди сотрудников со стажем менее 2 лет в отделе 'Sales'.

min_salary = Employee.select(fn.MIN(Employee.salary)).join(Department).where(Department.name == 'Sales') & (Employee.experience < 2).scalar()
print(f'Минимальная зарплата среди сотрудников отдела Sales со стажем менее 2 лет {min_salary}')

# 5. Определить средний опыт работы всех сотрудников с зарплатой выше $5000.

avg_experience = Employee.select(fn.AVG(Employee.experience)).where(Employee.salary > 5000).scalar()
print(f'Средний опыт среди сотрудников с зарплатой выше $5000 {avg_experience}')

# 6. Получить максимальную зарплату среди сотрудников с опытом работы более 10 лет в отделе 'IT'.

max_salary = Employee.select(fn.MAX(Employee.salary)).join(Department).where(Employee.experience > 10) & (Department.name == 'IT').scalar()
print(f'Максимальная зарплата среди сотрудников с опытом работы более 10 лет в отделе IT {max_salary}')

# 7. Подсчитать количество сотрудников с опытом работы более 3 лет и зарплатой менее $4000.

employee_count = Employee.select().where(Employee.experience > 3) & (Employee.salary < 4000).count()
print(f'Количество сотрудников с опытом работы более 3 лет и зарплатой менее $4000 {employee_count}')

# 8. Найти минимальный опыт работы среди сотрудников, у которых зарплата между 3000 и 4000.

min_experience = Employee.select(fn.MIN(Employee.experience)).where((Employee.salary > 3000) & (Employee.salary < 4000)).scalar()
print(f'Минимальный опыт работы среди сотрудников, у которых зарплата между 3000 и 4000 {min_experience}')

# 9. Получить среднюю зарплату сотрудников в отделе 'Finance' с опытом работы более 5 лет.

avg_salary = Employee.select(fn.AVG(Employee.salary)).join(Department).where(Department.name == 'Finance') & (Employee.experience > 5).scalar()
print(f'Средняя зарплата среди сотрудников в отделе Finance с опытом работы более 5 лет {avg_salary}')

# 10. Определить количество сотрудников в отделе 'HR' с зарплатой выше средней по всем сотрудникам.

avg_salary = Employee.select(fn.AVG(Employee.salary)).join(Department).where(Department.name == 'HR')
employee_count_avg = Employee.select().join(Department).where(Department.name == 'HR') & (Employee.salary > avg_salary).count()
print(f'Количество сотрудников в отделе HR с зарплатой выше средней по всем сотрудникам {employee_count_avg}')