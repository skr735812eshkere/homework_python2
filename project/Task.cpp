#include "Task.hpp"
#include <sstream>

Task::Task(int id, const std::string& name, int priority)
    : id(id), name(name), priority(priority), done(false) {}
void Task::setPriority(int p) {
    if (p >= 1 && p <= 5) {
        this->priority = p;
    }
}

std::string Task::toString() const {
    std::ostringstream ss;
    ss << "[" << id << "] " << name << " | Приоритет: " << priority << " | Статус: ";
    ss << (done ? "Выполнено" : "Не выполнено");
    return ss.str();
}

bool Task::getStatus() const {
    return done;

}
