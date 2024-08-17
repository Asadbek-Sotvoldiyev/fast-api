from database import Base, engine
from models import Order, User, Product

Base.metadata.create_all(bind=engine)
