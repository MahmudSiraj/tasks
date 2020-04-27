from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import DATE, BOOLEAN

engine = create_engine('sqlite:///tasks', echo=True)
Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    due_date = Column(DATE)
    high_priority = Column(BOOLEAN)
    completed = Column(BOOLEAN)

    subtasks = relationship("subtasks", back_populates="task")

    def __repr__(self):
        return f'<Task(id={self.id}, description={self.description}, due_date={self.due_date},' \
               f'high_priority={self.high_priority}, completed={self.completed})>'


class SubTasks(Base):
    __tablename__ = 'subtasks'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    description = Column(String)
    due_date = Column(DATE)
    high_priority = Column(BOOLEAN)
    completed = Column(BOOLEAN)

    task = relationship("tasks", back_populates="subtasks")

    def __repr__(self):
        return f'<Task(task={self.task_id}, id={self.id}, description={self.description}, ' \
               f'due_date={self.due_date}, high_priority={self.high_priority}, completed={self.completed})>'


Base.metadata.create_all(engine)
