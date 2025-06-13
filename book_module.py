import csv
import os


def add_book(title, author):
    """Добавляет новую книгу в файл books.csv"""
    global books

    if not os.path.exists("books.csv"):
        with open("books.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "title", "author"])

    # Загружаем текущие книги, чтобы найти максимальный ID
    books = []
    with open("books.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)

    new_id = str(max([int(book["id"]) for book in books] + [0]) + 1)

    with open("books.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, title, author])

    return new_id

books = []

def load_books():
    """Загружает книги из файла books.csv в глобальный список."""
    global books
    books = []

    if not os.path.exists("books.csv"):
        return

    with open("books.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append({
                "id": row["id"],
                "title": row["title"],
                "author": row["author"]
            })

def remove_book_by_id(book_id):
    """Удаляет книгу по ID из файла books.csv."""
    if not os.path.exists("books.csv"):
        return False

    updated = []
    removed = False

    with open("books.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] != str(book_id):
                updated.append(row)
            else:
                removed = True

    if removed:
        with open("books.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "author"])
            writer.writeheader()
            writer.writerows(updated)

    return removed
