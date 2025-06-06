#include "TaskManager.hpp"
#include <iostream>
#include <algorithm>

TaskManager::TaskManager() : nextId(1) {}

void TaskManager::addTask(const std::string& name, int priority) {
    tasks.emplace_back(nextId++, name, priority);
}

bool TaskManager::deleteTask(int id) {
    auto it = std::remove_if(tasks.begin(), tasks.end(),
        [id](const Task& t) { return t.id == id; });
    if (it != tasks.end()) {
        tasks.erase(it, tasks.end());
        return true;
    }
    return false;
}

bool TaskManager::toggleStatus(int id) {
    for (auto& task : tasks) {
        if (task.id == id) {
            task.done = !task.done;
            return true;
        }
    }
    return false;
}

bool TaskManager::changePriority(int id, int newPriority) {
    for (auto& task : tasks) {
        if (task.id == id) {
            task.setPriority(newPriority);
            return true;
        }
    }
    return false;
}

void TaskManager::printAllTasksSortedById() const {
    std::vector<Task> sorted = tasks;
    std::sort(sorted.begin(), sorted.end(), [](const Task& a, const Task& b) {
        return a.id < b.id;
    });

    for (const auto& task : sorted) {
        std::cout << task.toString() << '\n';
    }
}

void TaskManager::printAllTasks() const {
    for (const auto& task : tasks)
        std::cout << task.toString() << '\n';
}

void TaskManager::printByStatus(bool done) const {
    int count = 0;
    for (const auto& task : tasks) {
        if (task.done == done) {
            std::cout << task.toString() << '\n';
            count++;
        }
    }
    if (count == 0) {
        if (done) {
            std::cout << "Нет выполненных задач\n";
        } else {
            std::cout << "Все задачи выполнены!\n";
        }
    }
}

void TaskManager::sortByPriority() {
    std::sort(tasks.begin(), tasks.end(),
              [](const Task& a, const Task& b) {
        return a.priority > b.priority;
              });

    std::cout << "Список отсортирован по приоритету:\n";
    printAllTasks();
}

const std::vector<Task>& TaskManager::getTasks() const {
    return tasks;
}
