import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox, Canvas
from PIL import Image, ImageTk

# Funkcia na generovanie čísel a výpočet priemeru
def generate_numbers():
    try:
        min_val = int(min_range.get())
        max_val = int(max_range.get())
        if min_val >= max_val:
            raise ValueError("Minimálna hodnota musí byť menšia ako maximálna hodnota.")
        global random_numbers, mean_value
        random_numbers = np.random.randint(min_val, max_val + 1, size=14)
        mean_value = np.mean(random_numbers)
        messagebox.showinfo("Výsledky",
                            f"Rozsah: {min_val} až {max_val}\n"
                            f"Vygenerované čísla: {random_numbers}\n"
                            f"Aritmetický priemer: {mean_value:.2f}")
    except ValueError as e:
        messagebox.showerror("Chyba", f"Neplatný vstup: {e}")

# Funkcia na vykreslenie grafu
def plot_graph():
    if random_numbers is None:
        messagebox.showwarning("Upozornenie", "Najprv vygenerujte čísla!")
        return
    negative_numbers = -random_numbers
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, 15), negative_numbers, color='skyblue')
    plt.title("Graf záporných hodnôt")
    plt.xlabel("Index čísla")
    plt.ylabel("Hodnota čísel")
    plt.xticks(range(1, 15))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # Nastavenie názvu okna grafu
    plt.gcf().canvas.manager.set_window_title("Graf")
    plt.show()

# Inicializácia GUI
root = Tk()
root.title("Zadanie č.14")
root.geometry("600x400")

# Nastavenie obrázku ako pozadia
try:
    background_image = Image.open("pozadie.jpg")
    background_image = background_image.resize((600, 400))
    bg_image = ImageTk.PhotoImage(background_image)

    canvas = Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
except FileNotFoundError:
    messagebox.showerror("Chyba", "Obrázok 'pozadie.jpg' nebol nájdený. Uistite sa, že sa nachádza v rovnakom priečinku ako tento skript.")
    root.destroy()

# Globálne premenné na uloženie hodnôt
random_numbers = None
mean_value = None

# Prvky GUI na pozadí s bielym podfarbením
canvas.create_rectangle(180, 20, 420, 100, fill="white", outline="")
canvas.create_text(300, 30, text="Oliver Kovaľ", font=("Arial", 14), fill="black")
canvas.create_text(300, 60, text="Programovacie techniky", font=("Arial", 14), fill="black")
canvas.create_text(300, 90, text="Zadanie úlohy: č. 14", font=("Arial", 14), fill="black")

# Rámec pre rozsah čísel
range_frame = Label(root, bg="#f0f0f0")
canvas.create_window(300, 150, window=range_frame)

Label(range_frame, text="Minimálna hodnota:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
min_range = StringVar(value="1000")
Entry(range_frame, textvariable=min_range, font=("Arial", 12), width=10).grid(row=0, column=1, padx=5)

Label(range_frame, text="Maximálna hodnota:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5)
max_range = StringVar(value="10000")
Entry(range_frame, textvariable=max_range, font=("Arial", 12), width=10).grid(row=1, column=1, padx=5)

# Tlačidlá
generate_button = Button(root, text="Generovať čísla", command=generate_numbers, font=("Arial", 12))
canvas.create_window(300, 230, window=generate_button)

plot_button = Button(root, text="Vykresliť graf", command=plot_graph, font=("Arial", 12))
canvas.create_window(300, 280, window=plot_button)

exit_button = Button(root, text="Zatvoriť", command=root.quit, font=("Arial", 12))
canvas.create_window(300, 330, window=exit_button)

# Spustenie hlavnej slučky
root.mainloop()
