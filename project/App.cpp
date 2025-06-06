#include "App.hpp"
#include <iostream>

void App::printMenu() const {
    std::cout << "\nМеню:\n"
              << "1. Добавить задачу\n"
              << "2. Показать все задачи\n"
              << "3. Удалить задачу по ID\n"
              << "4. Задача выполнена\n"
              << "5. Показать выполненные задачи\n"
              << "6. Показать невыполненные задачи\n"
              << "7. Сортировать по приоритету\n"
              << "8. Изменить приоритет задачи\n"
              << "0. Выход\n";
}

void App::addTask() {
    std::string name;
    int priority;
    std::cout << "Название: ";
    std::cin.ignore();
    std::getline(std::cin, name);
    std::cout << "Приоритет (1-5): ";
    std::cin >> priority;
    manager.addTask(name, priority);
}

void App::deleteTask() {
    int id;
    std::cout << "ID: ";
    std::cin >> id;
    if (manager.deleteTask(id)) {
            std::cout << "Задача [" << id << "] удалена\n";
        } else {
            std::cout << "Задача с таким ID не найдена\n";
        }
}

void App::changeStatus() {
    int id;
    std::cout << "ID: ";
    std::cin >> id;
    if (manager.toggleStatus(id)) {
        bool done = false;
        for (const auto& task : manager.getTasks()) {
            if (task.id == id) {
                done = task.getStatus();
                break;
            }
        }
        std::cout << "Задача [" << id << "] помечена как "
                  << (done ? "выполненная\n" : "невыполненная\n");
    } else {
        std::cout << "Задача с таким ID не найдена\n";
    }
}

void App::showAll() {
    manager.printAllTasksSortedById();
}

void App::showByStatus(bool done) {
    manager.printByStatus(done);
}

void App::sortTasks() {
    manager.sortByPriority();
    std::cout << "Отсортировано!\n";
}

void App::changePriority(){
    int id, newPrio;
    std::cout << "Введите ID задачи: ";
    std::cin >> id;
    std::cout << "Введите новый приоритет (1-5): ";
    std::cin >> newPrio;
    if (manager.changePriority(id, newPrio)) {
        std::cout << "Приоритет изменён.\n";
    } else {
        std::cout << "Задача с таким ID не найдена.\n";
    }
}

void App::handleChoice(int choice) {
    switch (choice) {
        case 1: addTask(); break;
        case 2: showAll(); break;
        case 3: deleteTask(); break;
        case 4: changeStatus(); break;
        case 5: showByStatus(true); break;
        case 6: showByStatus(false); break;
        case 7: sortTasks(); break;
        case 8: changePriority(); break;
        case 0: break;
        default: std::cout << "Неверный выбор\n";
    }
}

void App::run() {
    int choice;
    do {
        printMenu();
        std::cout << "Выбор: ";
        std::cin >> choice;
        handleChoice(choice);
    } while (choice != 0);
}
