tasks: list[dict] = []
next_id = 1

def create_task(payload) -> dict:
    global next_id
    task = {
        "id": next_id,
        "title": payload.title,
        "completed": payload.completed
    }
    next_id += 1
    tasks.append(task)
    return task

def find_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None

def update_task(task_id: int, payload):
    task = find_task(task_id)
    if task is None:
        return None
    for key, value in payload.model_dump(exclude_unset=True).items():
        task[key] = value
    return task

def delete_task(task_id: int) -> bool:
    task = find_task(task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True