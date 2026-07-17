from app.database.database import Base, engine

# Import all models here
from app.models import MenuItem

Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")