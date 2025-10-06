import sqlalchemy as sa


from app._core.models import Base


class Task(Base):
    __tablename__ = "tasks"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100),nullable=False)
    description = sa.Column(sa.String(255),nullable=True)
    select_date = sa.Column(sa.DateTime, nullable=True)
    priority = sa.Column(sa.String(50), nullable=True)
    status = sa.Column(sa.String(50))


