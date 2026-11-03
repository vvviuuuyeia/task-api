from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False

class TaskUpdate(BaseModel):
    # 两个字段都是可选，传哪个就改哪个
    title: str | None = Field(default=None, min_length=1)
    completed: bool | None = None