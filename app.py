tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
if __name__=="__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài thực hành ở nhà")
def delete_task(task_name):
    """Xóa một công việc khỏi danh sách"""
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"Đã xóa công việc: '{task_name}'")
