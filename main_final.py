import os
import shutil


# в данном проекте была добавлена функция проверки выхода из директории
# a также исправлено action == 9

def create_directory(name):
    os.mkdir(name)


def remove_directory(name):
    os.rmdir(name)


def change_directory(action):
    if action == 'up':
        os.chdir('../')
    else:
        os.chdir(action)


def create_file(name):
    with open(os.path.join(os.getcwd(), name), 'w') as f:
        f.write("")


def write_file(name, text):
    with open(os.path.join(os.getcwd(), name), "a+") as f:
        f.write(text)


def read_file(name):
    with open(os.path.join(os.getcwd(), name), 'r') as f:
        for line in f:
            print(line, end="")


def remove_file(name):
    os.rmdir(name)


def recursive_way_to_dirs(dir1, f1, dir2):
    full_dir1 = None
    fill_dir2 = None
    for dirpath, dirnames, filenames in os.walk(home_directory):
        if dir1 in dirnames:
            full_dir1 = os.path.join(dirpath, dir1, f1)
        if dir2 in dirnames:
            full_dir2 = os.path.join(dirpath, dir2, f1)
        check_directory()
    return full_dir1, full_dir2


def copy_file(dir1, f1, dir2):
    full_dir1, full_dir2 = recursive_way_to_dirs(dir1, f1, dir2)
    try:
        shutil.copy2(full_dir1, full_dir2)
    except:
        print('Данной папки или файла не существует')


def move_file(dir1, f1, dir2):
    full_dir1, full_dir2 = recursive_way_to_dirs(dir1, f1, dir2)
    try:
        shutil.move(full_dir1, full_dir2)
    except:
        print('Данной папки или файла не существует')


def rename_file(name1, name2):
    old_file = os.path.join(os.getcwd(), name1)
    new_file = os.path.join(os.getcwd(), name2)
    os.rename(old_file, new_file)


def check_directory():
    if os.path.getsize(os.getcwd()) < os.path.getsize(home_directory):
        raise IsADirectoryError('Вы вышли из директории')


def body():
    print('1.	Создание папки (с указанием имени);')
    print('2.	Удаление папки по имени;')
    print(
        '3.	Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;')
    print('4.	Создание пустых файлов с указанием имени;')
    print('5.	Запись текста в файл;')
    print('6.	Просмотр содержимого текстового файла;')
    print('7.	Удаление файлов по имени;')
    print('8.	Копирование файлов из одной папки в другую;')
    print('9.	Перемещение файлов;')
    print('10.	Переименование файлов.')
    print('11.  Выход из программы')
    action = int(input('Введите нужное действие:\n'))
    return action


home_directory = None
with open("directory.txt", "r") as f:
    home_directory = f.readline()
print(home_directory)

while True:
    action = body()
    if action == 1:
        create_directory(input("Введите имя папки:\n"))
    elif action == 2:
        remove_directory(input('Введите имя папки:\n'))
    elif action == 3:
        change_directory(input('Введите up - чтобы подняться на уровень вверх, либо укажите имя папки:\n'))
    elif action == 4:
        create_file(input('Введите имя файла:\n'))
    elif action == 5:
        write_file(input('Введите имя файла:\n'), input('Введите текст для записи в файл:\n'))
    elif action == 6:
        read_file(input('Введите имя файла:\n'))
    elif action == 7:
        remove_file(input('Введите имя файла:\n'))
    elif action == 8:
        dir1 = input('Введите название папки, из которой будет выполняться копирование:\n')
        f1 = input('Введите имя файла, который нужно скопировать:\n')
        dir2 = input('Введите название папки, куда нужно скопировать файл\n')
        copy_file(dir1, f1, dir2)
    elif action == 9:
        dir1 = input('Введите название папки, из которой будет браться файл:\n')
        f1 = input('Введите имя файла, который нужно взять:\n')
        dir2 = input('Введите название папки, куда нужно переместить файл\n')
        move_file(dir1, f1, dir2)
    elif action == 10:
        rename_file(input('Введите первое имя файла:\n'), input('Введите второе имя файла:\n'))
    elif action == 11:
        print('Работа с файловым менеджером завершена')
        break
    print("Текущая директория: ", os.getcwd())
