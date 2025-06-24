# 📚 Projekt – Księgarnia internetowa (Python GUI)

**ENGLISH BELOW ↓**

---

## 🇵🇱 Opis (Polski)

Aplikacja stworzona w ramach projektu zespołowego na zajęcia z języka Python.  
Umożliwia zarządzanie e-bookami, klientami oraz realizację zakupów poprzez prosty interfejs graficzny.

---

### 👨‍💻 Autorzy

- **Mikita Kryvenia** – GUI (Tkinter), integracja modułów, obsługa zakupów, dekoratory, dokumentacja, obsługa wyjątków, system logów  
- **Jakub Kadaj** – logika i moduł obsługi książek (`book_module.py`)  
- **Paweł Zarzecki** – logika i moduł obsługi klientów (`customer_module.py`)

---

### 🧩 Struktura projektu

bookstore_project/
├── main.py             # Uruchamia program
├── gui_module.py       # Interfejs graficzny
├── book_module.py      # Obsługa książek
├── customer_module.py  # Obsługa klientów
├── purchase_module.py  # Obsługa zakupów
│
├── books.csv           # Baza książek
├── customers.csv       # Baza klientów
├── purchases.csv       # Historia zakupów
├── actions.log         # Dziennik działań
├── README.md           # Ten plik



---

### ▶️ Jak uruchomić

1. Zainstaluj Pythona (3.11+)
2. Pobierz projekt lub sklonuj repozytorium
3. Uruchom:

```bash
python main.py
🇬🇧 Description (English)
This application was created as a team project for Python programming classes.
It allows you to manage e-books, customers, and purchases via a graphical user interface.

👨‍💻 Authors
Mikita Kryvenia – GUI (Tkinter), module integration, purchase logic, decorators, documentation, error handling, logging

Jakub Kadaj – logic and book handling module (book_module.py)

Paweł Zarzecki – logic and customer handling module (customer_module.py)

🧩 Project Structure

bookstore_project/
│
├── main.py                # Starts the app
├── gui_module.py          # GUI logic
├── book_module.py         # Book handling
├── customer_module.py     # Customer handling
├── purchase_module.py     # Purchase system
│
├── books.csv              # Book database
├── customers.csv          # Customer database
├── purchases.csv          # Purchase records
├── actions.log            # Action logs
├── README.md              # This file
▶️ How to run
Install Python (3.11+)

Download the ZIP or clone the repository

Run the program:

python main.py
🔧 Technologies
Python 3.11+

Tkinter (GUI)

CSV data handling

Functional programming

Decorators

Exception handling

Google-style docstrings (visible in IDE)

