from datetime import datetime, timedelta
from typing import List, Annotated

from pydantic import EmailStr
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from . import Base


intpk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True, nullable=False)]

recipes_products = Table(
    "recipes_products", Base.metadata,
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)


class BaseModel(Base):
    __abstract__ = True
    
    id: Mapped[intpk]
    create_at: Mapped[datetime] = Column(DateTime, default=func.now())
    update_at: Mapped[datetime] = Column(DateTime, default=func.now(), onupdate=func.now())


class Users(BaseModel):
    """User entities"""

    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(50), unique=True, index=True, nullable=False)
    is_activated: Mapped[bool] = mapped_column(nullable=False, default=True)
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    accounts: Mapped[List["Recipes"]] = relationship("Accounts", back_populates="user")
    token: Mapped[List["Tokens"]] = relationship("Tokens", back_populates="user")
    secret_key: Mapped[List["SecretKeys"]] = relationship("SecretKeys", back_populates="user")


class Products(BaseModel):
    """Product entities"""

    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    calories: Mapped[int] = mapped_column(Integer, nullable=False)
    is_activated: Mapped[bool] = mapped_column(nullable=False, default=False)
    recipes: Mapped[List["recipes_products"]] = relationship("Payments", secondary=recipes_products, 
                                                             back_populates="products")


class Recipes(BaseModel):
    """Recipe entities"""

    __tablename__ = "recipes"

    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String)
    calories: Mapped[int] = mapped_column(Integer, nullable=False)
    is_activated: Mapped[bool] = mapped_column(nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["Users"] = relationship(back_populates="recipes")
    products: Mapped[List["recipes_products"]] = relationship("Payments", secondary=recipes_products, 
                                                              back_populates="recipes")


class SecretKeys(Base):
    """Secret Key entities"""

    __tablename__ = "secret_keys"

    id: Mapped[intpk]
    secret_key: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["Users"] = relationship(back_populates="secret_key")


class Tokens(Base):
    """Token entities"""

    __tablename__ = "tokens"

    id: Mapped[intpk]
    access_token: Mapped[str] = mapped_column(String(300), unique=True, nullable=False)
    refresh_token: Mapped[str] = mapped_column(String(300), unique=True, nullable=False)
    expires: Mapped[datetime] = mapped_column(DateTime, default=datetime.now() + timedelta(weeks=1), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["Users"] = relationship(back_populates="token")
