"""
Moduł zarządzania książkami (dodawanie, usuwanie, wczytywanie z pliku CSV).
"""

import csv
import os

books = []


def load_books():
    """
Wczytuje wszystkie książki z pliku books.csv do zmiennej globalnej books.

Returns:
    None
"""

    global books
    books = []
    if not os.path.exists("books.csv"):
        return
    try:
        with open("books.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append({
                    "id": row["id"],
                    "title": row["title"],
                    "author": row["author"]
                })
    except FileNotFoundError:
        books = []


def add_book(title, author):
    """
    Dodaje nową książkę do pliku books.csv i zwraca jej ID.

    Args:
        title (str): Tytuł książki.
        author (str): Autor książki.

    Returns:
        str: Nowy unikalny identyfikator książki.
    """

    global books

    if not os.path.exists("books.csv"):
        with open("books.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "title", "author"])

    load_books()
    new_id = str(max([int(book["id"]) for book in books] + [0]) + 1)

    with open("books.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, title, author])

    return new_id


def remove_book_by_id(book_id):
    """
    Usuwa książkę z books.csv na podstawie ID.

    Args:
        book_id (str): Identyfikator książki do usunięcia.

    Returns:
        bool: True, jeśli książka została usunięta. False, jeśli nie znaleziono.
    """

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
