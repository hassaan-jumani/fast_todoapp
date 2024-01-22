from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = 'todos'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    description:Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<Todo {self.name}>"
    

engine: Engine = create_engine(
    f'postgresql://hassaan-jumani:xZ2kpnwgBm0J@ep-lucky-math-a5u8v0r3.us-east-2.aws.neon.tech/todoapp?sslmode=require',
    echo= True
)


Session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)