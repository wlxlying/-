# -*- coding: utf-8 -*-
# 在"TODO:" 下方编写代码，完成后删除下方的 pass
import copy

# --- 练习 1：引用与陷阱 ---
def list_copy_practice():
    """
    理解引用关系，并创建一个不随原列表变化的独立副本。
    """
    a = [1, 2, 3]
    b = a
    # TODO: 请在下方写出一行代码获取 a 的独立副本 c
    # 提示：完成后请删除 pass
    c = a[:]
    
    return a, b, c

# --- 练习 2：Student 类构建 ---
class Student:
    def __init__(self, name, student_id):
        # TODO: 初始化属性 name 和 student_id
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        # TODO: 返回格式如 Student(name='Alice', id='101')
        # 在下方编写输出结果
        return f"Student(name='{self.name}', id='{self.student_id}')"

    def __str__(self):
        # TODO: 返回格式如 Student: Alice (ID: 101)
        # 在下方编写输出结果
        return f"Student: {self.name} (ID: {self.student_id})"

# --- 练习 3：Task 任务排序 ---
class Task:
    def __init__(self, title, priority=3):
        # TODO: 初始化 title, priority (1-5), 以及 done (默认为 False)
        self.title = title
        if 1 <= priority <= 5:
            self.priority = priority
        else:
            self.priority = 3 
        self.done = False

    def mark_done(self):
        # TODO: 将 self.done 设为 True
        self.done = True

    def __lt__(self, other):
        # TODO: 实现基于 priority 的比较逻辑 (priority 值越小，优先级越高)
        # 初始返回 False 以支持基础的比较操作
        if isinstance(other, Task):
            return self.priority < other.priority
        return False

    def __str__(self):
        # TODO: 根据完成状态返回 "[ ] 标题 (Priority: n)" 或 "[V] 标题 (Priority: n)"
        status = "[V]" if self.done else "[ ]"
        return f"{status} {self.title} (Priority: {self.priority})"

# --- 练习 4：任务字典管理器 ---
class TaskManager:
    def __init__(self):
        # TODO: 初始化一个空字典 self.tasks
        self.tasks = {}

    def add_task(self, title, priority=3):
        """
        提示：在此方法中实例化 Task 对象并存入 self.tasks
        """
        # TODO: 实现添加逻辑
        self.tasks[title] = Task(title, priority)

    def get_task(self, title):
        """
        安全查找任务。如果不存在则返回 None。
        """
        # TODO: 实现查找逻辑
        return self.tasks.get(title)

    def delete_task(self, title):
        """
        安全删除任务。如果不存在则直接跳过。
        """
        # TODO: 实现删除逻辑
        if title in self.tasks:
            del self.tasks[title]

    def update_priority(self, title, new_priority):
        """
        安全修改任务优先级。
        """
        # TODO: 实现修改逻辑
        task = self.get_task(title)
        if task:
            if 1 <= new_priority <= 5:
                task.priority = new_priority
            else:
                task.priority = 3

if __name__ == "__main__":
    tm = TaskManager()
    
    tm.add_task("写作业", 2)
    tm.add_task("游戏", 4)
    
    task1 = tm.get_task("写作业")
    print("查找写作业任务：", task1)  
    
    tm.update_priority("写作业", 1)
    print("修改后写作业任务：", tm.get_task("写作业")) 
    
    tm.delete_task("游戏")
    print("删除后查找游戏任务：", tm.get_task("游戏"))  
