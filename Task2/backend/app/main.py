from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app import models
from app.database import SessionLocal, engine
from app.scraper import scrape_and_store
from app.models import Book
from fastapi.middleware.cors import CORSMiddleware

# Crear las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS para frontend en React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de entrada para /scrape
class ScrapeRequest(BaseModel):
    url: str

@app.get("/")
def root():
    return {"message": "Backend listo"}

@app.post("/scrape")
def scrape_url(request: ScrapeRequest, db: Session = Depends(get_db)):
    result = scrape_and_store(request.url, db)
    return result


# Nuevo endpoint con filtros
@app.get("/books")
def get_books(
    category: str = None,
    title_contains: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Book)
    if category:
        query = query.filter(Book.category.ilike(f"%{category}%"))
    if title_contains:
        query = query.filter(Book.title.ilike(f"%{title_contains}%"))
    return query.all()
