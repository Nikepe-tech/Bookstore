"""
Moduł obsługi zakupów (zapis do purchases.csv).
"""

import csv
import os
from datetime import datetime

def save_purchase(customer_id, book_id):
    """
    Zapisuje zakup książki przez klienta do pliku purchases.csv,
    wraz z datą i godziną zakupu.
    """
    if not os.path.exists("purchases.csv"):
        with open("purchases.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["customer_id", "book_id", "timestamp"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("purchases.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, book_id, timestamp])
