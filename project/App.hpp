#pragma once
#include "TaskManager.hpp"

class App {
private:
    TaskManager manager;

    void printMenu() const;
    void handleChoice(int choice);
    void addTask();
    void deleteTask();
    void changeStatus();
    void showAll();
    void showByStatus(bool done);
    void sortTasks();
    void changePriority();

public:
    void run();
};
