"""
Moduł graficzny GUI dla księgarni internetowej.
Obsługuje interfejs użytkownika, interakcje z klientem i książkami.
"""

import csv
import tkinter as tk
from tkinter import messagebox
import book_module
import customer_module
import purchase_module


def log_action(func):
    """
    Dekorator zapisujący akcję do pliku logów z timestampem.

    Args:
        func (function): Funkcja, którą dekorujemy.

    Returns:
        function: Opakowana funkcja z logowaniem.
    """

    def wrapper(*args, **kwargs):
        from datetime import datetime
        with open("actions.log", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} \n")
        return func(*args, **kwargs)

    return wrapper


def run_gui():
    """Uruchamia graficzny interfejs księgarni internetowej."""

    root = tk.Tk()
    root.geometry("800x500")
    root.title("Księgarnia internetowa")

    label = tk.Label(root, text="Witamy w ksiegarni internetowej ")
    label.pack(pady=20)

    book_frame = tk.Frame(root)
    book_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    book_label = tk.Label(book_frame, text="Lista ksiazek: ")
    book_label.pack()

    book_listbox = tk.Listbox(book_frame, exportselection=False)
    book_listbox.pack(fill=tk.BOTH, expand=True)

    book_module.load_books()
    for book in book_module.books:
        book_listbox.insert(tk.END, f"{book['id']} - {book['title']} - {book['author']}")

    title_label = tk.Label(book_frame, text="Tytul:")
    title_label.pack(anchor="w")
    title_entry = tk.Entry(book_frame)
    title_entry.pack(fill=tk.X)

    author_label = tk.Label(book_frame, text="Autor: ")
    author_label.pack(anchor="w")
    author_entry = tk.Entry(book_frame)
    author_entry.pack(fill=tk.X)

    action_frame = tk.Frame(root)
    action_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    @log_action
    def add_book():
        """
        Dodaje nową książkę do listy i pliku CSV.

        Pobiera dane z pól tekstowych, wywołuje funkcję add_book() z book_module,
        a następnie aktualizuje Listbox.

        Returns:
            None
        """

        title = title_entry.get().strip()
        author = author_entry.get().strip()
        if title == "" or author == "":
            return

        book_id = book_module.add_book(title, author)
        book_listbox.insert(tk.END, f"{book_id} - {title} - {author}")
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        messagebox.showinfo("OK", "Ksiazka dodana")

    add_button = tk.Button(book_frame, text="Dodaj ksiazke", command=add_book)
    add_button.pack(pady=10)

    @log_action
    def remove_book():
        """
        Usuwa zaznaczoną książkę z interfejsu i pliku books.csv.

        Pobiera wybraną pozycję z listy, wyodrębnia ID,
        pyta o potwierdzenie, a następnie wywołuje funkcję
        remove_book_by_id() z book_module.

        Returns:
            None
        """

        selected_book = book_listbox.curselection()
        if not selected_book:
            messagebox.showwarning("Blad", "Wybierz ksiazke")
            return

        book_text = book_listbox.get(selected_book[0])
        book_id = book_text.split(" - ")[0]

        confirm = messagebox.askyesno("Potwierdz", f"Usunac '{book_text}'?")
        if not confirm:
            return

        try:
            result = book_module.remove_book_by_id(book_id)
            if result:
                book_listbox.delete(selected_book[0])
                messagebox.showinfo("OK", "Ksiazka usunieta")
            else:
                messagebox.showerror("Error", "Nie udalo sie")
        except Exception as e:
            messagebox.showerror("Error", f"Nie udalo sie: {e}")

    remove_book_button = tk.Button(book_frame, text="Usun ksiazke", command=remove_book)
    remove_book_button.pack(pady=5)

    customer_frame = tk.Frame(root)
    customer_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    customer_label = tk.Label(customer_frame, text="Lista klientow: ")
    customer_label.pack()

    customer_listbox = tk.Listbox(customer_frame, exportselection=False)
    customer_listbox.pack(fill=tk.BOTH, expand=True)

    customer_module.load_customers()
    for customer in customer_module.customers:
        customer_listbox.insert(tk.END, customer)

    name_label = tk.Label(customer_frame, text="Imie i nazwisko: ")
    name_label.pack(anchor="w")
    name_entry = tk.Entry(customer_frame)
    name_entry.pack(fill=tk.X)

    @log_action
    def add_customer():
        """
        Dodaje nowego klienta na podstawie wpisanego imienia i nazwiska.

        Sprawdza, czy pole nie jest puste, następnie wywołuje
        add_customer() z customer_module. W razie powodzenia
        dodaje klienta do listy GUI.

        Returns:
            None
        """

        name = name_entry.get().strip()
        if name == "":
            return

        result = customer_module.add_customer(name)
        if result:
            customer_listbox.insert(tk.END, name)
            name_entry.delete(0, tk.END)
            messagebox.showinfo("OK", "Klient dodan")
        else:
            messagebox.showwarning("Uwaga", "Klient istnieje")

    add_customer_button = tk.Button(customer_frame, text="Dodaj klienta", command=add_customer)
    add_customer_button.pack(pady=10)

    @log_action
    def remove_customer():
        """
        Usuwa wybranego klienta z listy i pliku customers.csv.

        Pobiera imię klienta z Listboxa, pyta o potwierdzenie
        i wywołuje remove_customer() z customer_module.

        Returns:
            None
        """

        selected_customer = customer_listbox.curselection()
        if not selected_customer:
            messagebox.showwarning("Uwaga", "Wybierz klienta")
            return

        name = customer_listbox.get(selected_customer[0])

        confirm = messagebox.askyesno("Podtwierdz", f"Usunac '{name}'?")
        if not confirm:
            return

        result = customer_module.remove_customer(name)
        if result:
            customer_listbox.delete(selected_customer[0])
            messagebox.showinfo("OK", "Klient usunat")
        else:
            messagebox.showwarning("Uwaga", "Nie udalo sie")

    remove_customer_button = tk.Button(action_frame, text="Usun klienta", command=remove_customer)
    remove_customer_button.pack(pady=5)

    @log_action
    def purchase_book():
        """
        Realizuje zakup książki przez wybranego klienta.

        Sprawdza zaznaczenia w obu listach, odczytuje ID z plików,
        a następnie wywołuje save_purchase() z purchase_module.
        Pokazuje komunikat z potwierdzeniem.

        Returns:
            None
        """

        selected_book = book_listbox.curselection()
        selected_customer = customer_listbox.curselection()

        if not selected_book or not selected_customer:
            messagebox.showerror("Error", "Wybierz ksiazke i klienta")
            return

        book_text = book_listbox.get(selected_book[0])
        customer_text = customer_listbox.get(selected_customer[0])

        book_id = book_text.split("-")[0]

        customer_id = None
        try:
            with open("customers.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == customer_text:
                        customer_id = row["id"]
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Brakuje pliku customers.csv")
            return
        if customer_id is None:
            messagebox.showerror("Error", "Nie ma klienta")
            return

        purchase_module.save_purchase(customer_id, book_id)

        messagebox.showinfo("Zakup", f"Klient '{customer_text}' kupil ksiazke '{book_text}'")

    purchase_button = tk.Button(action_frame, text="Kup ksiazke", command=purchase_book)
    purchase_button.pack(side=tk.LEFT)

    root.mainloop()
