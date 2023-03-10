import os
import shutil

folder_downloads = 'E:\Downloads'

folders = {'.mp3': 'E:\Downloads\Новая папка\Музыка',
           '.pdf': 'E:\Downloads\Новая папка\PDF',
           '.torrent': 'E:\Downloads\Новая папка\Torrent',
           '.jpg': 'E:\Downloads\Новая папка\Картинки',
           '.jpeg': 'E:\Downloads\Новая папка\Картинки',
           '.png': 'E:\Downloads\Новая папка\Картинки',
           '.doc' : 'E:\Downloads\Новая папка\Документы',
           '.docx': 'E:\Downloads\Новая папка\Документы',
           '.zip' : 'E:\Downloads\Новая папка\Архивы',
           '.rar' : 'E:\Downloads\Новая папка\Архивы',
           '.xls' : 'E:\Downloads\Новая папка\Документы',
           '.xlsx': 'E:\Downloads\Новая папка\Документы',
           '.exe': 'E:\Downloads\Новая папка\Приложения'
           }
# Перебираем все файлы в папке загрузок
for filename in os.listdir(folder_downloads):
    file_path = os.path.join(folder_downloads, filename)
    # Проверяем, является ли файл файлом (а не папкой) и имеет ли он расширение
    if os.path.isfile(file_path) and "." in filename:
        file_ext = os.path.splitext(filename)[1]
        # Проверяем, есть ли для данного расширения соответствующая папка
        if file_ext in folders:
            # Если есть, перемещаем файл в эту папку
            dest_folder = folders[file_ext]
            shutil.move(file_path, dest_folder)
            print(f"Файл {filename} перемещен в папку {dest_folder}.")
        else:
            # Если нет, выводим сообщение об ошибке
            print(f"Не найдено соответствующей папки для файла {filename}.")