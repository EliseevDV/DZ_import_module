from time import sleep
from aplication.salary import calculate_salary
from aplication.db.people import get_employees


names = ['Федоренко', 'Киселев', 'Игнатьев', 'Проскурякова', 'Михеева']
box = [1000, 3000, 4000, 5000, 8000, 10000, 1000000]


def happy_roulette():
    print(f'Дополнительную премию в этом месяце получает....')
    sleep(20)
    print(get_employees(names))
    print(f'В этом месяце доплнительная премия составит.....')
    sleep(30)
    print(calculate_salary(box))











if __name__ == '__main__':
    happy_roulette()
