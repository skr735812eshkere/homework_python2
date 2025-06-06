#pragma once
#include <string>

class Task {
public:
    int id;
    std::string name;
    int priority;
    bool done;
    bool getStatus() const;
    
    Task(int id, const std::string& name, int priority);
    void setPriority(int p);
    std::string toString() const;
};
