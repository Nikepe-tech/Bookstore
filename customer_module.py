"""
Moduł zarządzania klientami (dodawanie, usuwanie, wczytywanie z pliku CSV).
"""

import csv
import os
from random import randint

customers = []

def load_customers():
    """Wczytuje klientów z pliku customers.csv do listy."""
    global customers
    customers = []
    if not os.path.exists("customers.csv"):
        return
    with open("customers.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row["name"])

def add_customer(name):
    """Dodaje klienta do customers.csv (jeśli nie istnieje)."""
    if not os.path.exists("customers.csv"):
        with open("customers.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name"])

    # Sprawdź, czy klient już istnieje
    with open("customers.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] == name:
                return False

    new_id = str(randint(1000, 9999))

    with open("customers.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name])

    return True

def remove_customer(name):
    """Usuwa klienta po imieniu z customers.csv."""
    if not os.path.exists("customers.csv"):
        return False

    updated = []
    removed = False

    with open("customers.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] != name:
                updated.append(row)
            else:
                removed = True

    if removed:
        with open("customers.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            writer.writeheader()
            writer.writerows(updated)

    return removed
