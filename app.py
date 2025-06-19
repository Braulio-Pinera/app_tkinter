import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Personalizada")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        
        self.crear_widgets()
        self.aplicar_layout_responsive()

    def crear_widgets(self):
        self.entrada = tk.Entry(self.root, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        botones = [
            ("7", self.insertar), ("8", self.insertar), ("9", self.insertar), ("/", self.insertar),
            ("4", self.insertar), ("5", self.insertar), ("6", self.insertar), ("*", self.insertar),
            ("1", self.insertar), ("2", self.insertar), ("3", self.insertar), ("-", self.insertar),
            ("0", self.insertar), (".", self.insertar), ("%", self.porcentaje), ("+", self.insertar),
            ("C", self.limpiar), ("←", self.borrar), ("=", self.calcular), ("km->m", self.convertir_km_a_m)
        ]

        fila = 1
        col = 0
        for texto, comando in botones:
            b = tk.Button(self.root, text=texto, font=("Arial", 16), command=lambda t=texto, c=comando: c(t))
            b.grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                fila += 1

    def aplicar_layout_responsive(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def insertar(self, valor):
        self.entrada.insert(tk.END, valor)

    def limpiar(self, _=None):
        self.entrada.delete(0, tk.END)

    def borrar(self, _=None):
        actual = self.entrada.get()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, actual[:-1])

    def porcentaje(self, _=None):
        try:
            valor = float(self.entrada.get())
            resultado = valor / 100
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except:
            messagebox.showerror("Error", "Entrada inválida")

    def convertir_km_a_m(self, _=None):
        try:
            valor = float(self.entrada.get())
            resultado = valor * 1000
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, f"{resultado} m")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    def calcular(self, _=None):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except:
            messagebox.showerror("Error", "Operación inválida")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()