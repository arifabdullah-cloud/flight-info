from app.db.database import Base
from app.db.database import engine

from app.models.flight import Flight

Base.metadata.create_all(bind=engine)

print("Database tables created.")
