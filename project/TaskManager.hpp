#pragma once
#include "Task.hpp"
#include <vector>

class TaskManager {
private:
    std::vector<Task> tasks;
    int nextId;

public:
    TaskManager();

    void addTask(const std::string& name, int priority);
    bool deleteTask(int id);
    bool toggleStatus(int id);
    bool changePriority(int id, int newPriority);
    void printAllTasksSortedById() const;
    void printAllTasks() const;
    void printByStatus(bool done) const;
    void sortByPriority();
    const std::vector<Task>& getTasks() const;
};
