g++ -std=c++17 -Wall -Wextra -Iinclude src/*.cpp -o taskmanager

if [ $? -eq 0 ]; then
    echo "Сборка успешна! Запускаем приложение..."
    ./taskmanager
else
    echo "Ошибка сборки!"
fi
