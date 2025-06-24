"""
Moduł obsługi zakupów (zapis do purchases.csv).
"""

import csv
import os
from datetime import datetime

def save_purchase(customer_id, book_id):
    """
    Zapisuje zakup książki przez klienta do pliku purchases.csv.

    Args:
        customer_id (str): Identyfikator klienta.
        book_id (str): Identyfikator książki.

    Returns:
        None
    """

    if not os.path.exists("purchases.csv"):
        with open("purchases.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["customer_id", "book_id", "timestamp"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("purchases.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([customer_id, book_id, timestamp])
    except Exception as e:
        print(f"Błąd podczas zapisu zakupu: {e}")

