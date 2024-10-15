#!/bin/run.sh

# Установка зависимостей
pip install -r requirements.txt

# Сборка исполняемого файла
pyinstaller --onefile --windowed main.py

# Переход в папку с исполняемым файлом
cd dist

# Проверка операционной системы и запуск соответствующей команды
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    chmod +x main
    ./main
else
    # Windows
    main.exe
fi
