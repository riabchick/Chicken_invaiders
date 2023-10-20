import PyInstaller.__main__

# Путь к основному файлу вашего проекта (ваш скрипт)
main_script = 'shooter_game.py'

# Опции сборки PyInstaller
build_options = [
    main_script,
    '--onefile',  # Создать один исполняемый файл
    '--name', 'my_app_name',  # Имя выходного файла
    '--distpath', 'dist',  # Каталог для сохранения результата
]

# Запустите сборку PyInstaller
PyInstaller.__main__.run(build_options)