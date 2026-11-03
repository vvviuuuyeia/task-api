from fastapi import FastAPI

app = FastAPI()

# 测试接口
@app.get("/")
def hello():
    return {"msg": "项目运行成功！"}

# 任务CRUD示例
tasks = []
next_id = 1

@app.post("/tasks", status_code=201)
def create_task(title: str):
    global next_id
    new_task = {"id": next_id, "title": title}
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.get("/tasks")
def get_all_tasks():
    return tasks
