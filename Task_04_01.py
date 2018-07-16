import configuration
import json
# output = json
# interval = 5
import psutil
import time

class Simple(object):

    @staticmethod
    def cpu_load(self):
        # self - обязательный аргумент, содержащий в себе экземпляр
        # класса, передающийся при вызове метода,
        # поэтому этот аргумент должен присутствовать
        # во всех методах класса.
        return psutil.cpu_percent(0.5, True)

    @staticmethod
    def memory_use(self):
        return psutil.disk_usage('/')

    @staticmethod
    def virt_memory(self):
        return psutil.virtual_memory().used / (1024 * 1024)

    @staticmethod
    def io_check(self):
        return psutil.disk_io_counters().write_count

    @staticmethod
    def network(self):
        return psutil.net_if_addrs()["eno1"][0][1]


# print(network())

    @staticmethod
    def out(self):
        print(' CPU load: ', Simple.cpu_load(),
          ' Memory use: ', Simple.memory_use(),
          ' Virtual memory: ', Simple.virt_memory(),
          ' IO check: ', Simple.io_check(),
          ' Network: ', Simple.network())


interval = configuration.interval

output = configuration.output

listOfparam = list()
if output == 'json':
    for i in range(configuration.num):
        j = i + 1
        json_p = {
            'Snapshot ': j,
            'Time': time.strftime('%H:%M:%S'),
            'CPU': Simple.cpu_load(),
            'Memory': Simple.memory_use(),
            'Virtual memory': Simple.virt_memory(),
            'IO check': Simple.io_check(),
            'Network': Simple.network(),
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
# json изначально по умолчанию не поддерживает UTF-8 =>
# => использование ключевого параметра
# ensure_ascii (американская стандартная кодировка обмена информации)

# Вывод информации в txt:
if output == 'txt':
    for i in range(configuration.num):
        j = i + 1
        print('Snapshot ', j, ': ',
              ' Time :', time.strftime('%H:%M:%S'),
              ' CPU: ', Simple.cpu_load(),
              ' Memory: ', Simple.memory_use(), 'Mb',
              ' Virtual memory: ', Simple.virt_memory(), 'Mb',
              ' IO: ', Simple.io_check(),
              ' Network: ', Simple.network(),
              file=open('output.txt', 'a'))
        time.sleep(interval)
