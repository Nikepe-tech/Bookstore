"""Временный модуль управления klientami (только для тестов GUI)."""

# Список клиентов
customers = []

def load_customers():
    """Загружает список клиентов из файла customers.csv."""
    global customers
    customers = []

    if not os.path.exists("customers.csv"):
        return

    with open("customers.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row["name"])

import csv
import os

def add_customer(name):
    """Добавляет клиента в файл customers.csv, если его там ещё нет."""
    # Проверка: если файл не существует — создаём с заголовком
    if not os.path.exists("customers.csv"):
        with open("customers.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name"])

    # Чтение всех текущих имён
    with open("customers.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"].strip().lower() == name.strip().lower():
                return False  # уже существует

    # Генерация ID
    import random
    customer_id = random.randint(1000, 9999)

    # Запись в файл
    with open("customers.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, name])

    return True  # клиент успешно добавлен

def remove_customer(name):
    """Удаляет клиента по имени из файла customers.csv."""
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
