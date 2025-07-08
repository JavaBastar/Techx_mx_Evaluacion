import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models import Book

def scrape_and_store(url: str, db: Session):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception as e:
        return {"status": "error", "message": f"No se pudo acceder a la URL: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.product_pod")

    if not articles:
        return {"status": "warning", "message": "No se encontraron productos en la página."}

    books = []
    for article in articles:
        print(article)
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text
        category = "Default"

        # Evita duplicados
        if not db.query(Book).filter(Book.title == title).first():
            db_book = Book(title=title, price=price, category=category)
            db.add(db_book)
            books.append({"title": title, "price": price, "category": category})

    db.commit()

    return {"status": "success", "message": f"{len(books)} libros guardados.", "books": books}
