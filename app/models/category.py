import sqlalchemy as sa
from app._core.models import Base


class Category(Base):
    __tablename__ = "categories"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100), nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey("categories.id"), nullable=True)
