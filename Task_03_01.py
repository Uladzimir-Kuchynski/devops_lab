import configuration
import json
# output = json
# interval = 5
import psutil
import time


def cpu_load():
    return psutil.cpu_percent(0.5, True)

def memory_use():
    return psutil.disk_usage('/')

def virt_memory():
    return psutil.virtual_memory().used / (1024*1024)

def io_check():
    return psutil.disk_io_counters().write_count


def network():
    return psutil.net_if_addrs()["eno1"][0][1]
# print(network())

def out():
    print(' CPU load: ', cpu_load(),
          ' Memory use: ', memory_use(),
          ' Virtual memory: ', virt_memory(),
          ' IO check: ', io_check(),
          ' Network: ', network())


interval = configuration.interval

output = configuration.output

listOfparam = list()
if output == 'json':
    for i in range(configuration.num):
        j = i + 1
        json_p = {
            'Snapshot ': j,
            'Time': time.strftime('%H:%M:%S'),
            'CPU': cpu_load(),
            'Memory': memory_use(),
            'Virtual memory': virt_memory(),
            'IO check': io_check(),
            'Network': network(),
        }
        with open('json_file.json', 'a') as file:
            json.dump(listOfparam, file, indent=2, ensure_ascii=False)
        print('OK')

        time.sleep(interval)

# Запись данных в JSON файл:
# with - это контекстный менеджер;
# open()- это функция;
# 'json_file'.json - это имя файла;
# 'w' - это флаг записи для файла;
# file - это переменная, куда сохраняется json_file.json

# json - это модуль;
# dump - это метод, который осуществляет запись объектов в файл;
# listOfparam - это список, который наполняется;
# indent - это ключевой параметр для отступов
# json изначально по умолчанию не поддерживает UTF-8 => использование ключевого параметра ensure_ascii (американская стандартная кодировка обмена информации)


# Вывод информации в txt:
if output == 'txt':
    for i in range(configuration.num):
        j = i + 1
        print('Snapshot ', j, ': ',
        ' Time :', time.strftime('%H:%M:%S'),
        ' CPU: ', cpu_load(),
        ' Memory: ', memory_use(), 'Mb',
        ' Virtual memory: ', virt_memory(),'Mb',
        ' IO: ', io_check(),
        ' Network: ', network(),
        file=open('output.txt', 'a'))
        time.sleep(interval)
