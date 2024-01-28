from sqlalchemy import create_engine, Column, Integer, String, Date, Enum

engine = create_engine("sqlite:///tasks.db", echo=True)

class Task(engine.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    date = Column(Date)
    status = Column(Enum("pendente", "executando", "concluida"))

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, description={self.description}, date={self.date}, status={self.status})"
