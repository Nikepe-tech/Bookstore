"""
Moduł zarządzania klientami (dodawanie, usuwanie, wczytywanie z pliku CSV).
"""

import csv
import os
from random import randint

customers = []


def load_customers():
    """
    Wczytuje klientów z pliku customers.csv do globalnej listy customers.

    Returns:
        None
    """

    global customers
    customers = []
    if not os.path.exists("customers.csv"):
        return
    try:
        with open("customers.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(row["name"])
    except FileNotFoundError:
        customers = []


def add_customer(name):
    """
    Dodaje klienta do pliku customers.csv, jeśli nie istnieje.

    Args:
        name (str): Imię i nazwisko klienta.

    Returns:
        bool: True jeśli dodano nowego klienta, False jeśli klient już istnieje.
    """

    if not os.path.exists("customers.csv"):
        with open("customers.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name"])

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
    """
    Usuwa klienta z pliku customers.csv na podstawie imienia.

    Args:
        name (str): Imię klienta do usunięcia.

    Returns:
        bool: True, jeśli klient został usunięty. False, jeśli nie znaleziono.
    """

    if not os.path.exists("customers.csv"):
        return False

    updated = []
    removed = False

    try:
        with open("customers.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] != name:
                    updated.append(row)
                else:
                    removed = True
    except FileNotFoundError:
        return False

    if removed:
        with open("customers.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            writer.writeheader()
            writer.writerows(updated)

    return removed
