from typing import Tuple
from inspect import stack
import tracemalloc
import time
import os
import subprocess
import random


def get_calling_file_path():
    file_path = stack()[2].filename
    return os.path.abspath(file_path)


def read(filename: str = r'../txtf/input.txt', type_convert: type = int):
    """
    Чтение файла построчно с преобразованием типов
    :param filename: имя файла, с которого нужно прочитать данные
    :param type_convert: все данные в файле будут конвертироваться в списки с данными этого типа
    :return: генератор списков строк
    """
    filename = fr'{os.path.dirname(get_calling_file_path())}/{filename}'

    with open(filename) as file:
        while True:
            line = file.readline().split()
            if not line:
                break

            if type_convert != str:
                line = list(map(type_convert, line))

            yield line


def write(*values, sep: str = " ", end: str = "\n", filename: str = r'../txtf/output.txt',
          to_end: bool = False) -> None:
    """
    Запись в файл списка values
    :param values: данные, которые необходимо записать
    :param sep: разделитель данных
    :param end: строка, которая будет записана в конец данных
    :param filename: имя файла, куда будут записываться данные
    :param to_end: определяет, файл будет перезаписан или данные запишутся в конец файла
    """
    filename = fr'{os.path.dirname(get_calling_file_path())}/{filename}'

    mode = 'w'
    if to_end:
        mode = 'a'

    with open(filename, mode) as file:
        print(*values, sep=sep, end=end, file=file)


def time_data(func) -> float:
    """
    Запускает функцию func и возвращает время ее выполнения в секундах
    :param func: функция, время которой нужно проверить
    :return: время выполнения func
    """
    time_start = time.perf_counter()
    func()
    return time.perf_counter() - time_start


def memory_data(func) -> Tuple[float, float]:
    """
    Запускает функцию func и возвращает данные о памяти, затраченной при ее выполнении, в Mб
    :param func: функция, память которой нужно проверить
    :return: занятая и пиковая память соотв.
    """
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    return current / 1024 ** 2, peak / 1024 ** 2


def run_tasks(working_dir, root_dir):
    for file in os.listdir(working_dir):
        if file.startswith('task'):
            src_dir = os.path.join(working_dir, file, 'src')
            for root, _, files in os.walk(src_dir):
                for fl in files:
                    run_path = os.path.relpath(os.path.join(root, fl), root_dir)
                    if fl.endswith('.py'):
                        print('—————————————————————————————————————————————')
                        print(f'RUNNING {run_path}')
                        subprocess.run(['python', run_path], cwd=root_dir)

            txtf_dir = os.path.join(working_dir, file, 'txtf')
            if not os.path.exists(txtf_dir):
                continue
            input_file = os.path.join(txtf_dir, 'input.txt')
            if not os.path.exists(input_file):
                continue
            print('---------------------------------------------')
            print(f'ВХОДНЫЕ ДАННЫЕ')
            for line in read(os.path.relpath(input_file, root_dir), type_convert=str):
                print(*line)

            print('---------------------------------------------')
            print(f'ВЫХОДНЫЕ ДАННЫЕ')
            output_file = os.path.join(working_dir, file, 'txtf', 'output.txt')
            if not os.path.exists(output_file):
                continue
            for line in read(os.path.relpath(output_file, root_dir), type_convert=str):
                print(*line)


def generate_random_array(n, left, right):
    array = [random.randint(left, right+1) for _ in range(1, n+1)]
    return array
