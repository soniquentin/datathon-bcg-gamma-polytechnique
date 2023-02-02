import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
from datetime import datetime
import cv2
import shutil
import matplotlib.pyplot as plt

class App_CE(tk.Tk):
    def __init__(self, file_path = "livrable_alpha_team.csv"):
        super().__init__()
        self.file_path = file_path
        self.title("Afficher les résultats")

        # Charger l'image
        self.image = ImageTk.PhotoImage(master = self, file = "asset/champselysees02.png")
        # PhotoImage(master=Fenetre, file='FONDM.gif')
        self.generate_graph()
        # Créer un canvas pour afficher l'image
        self.canvas = tk.Canvas(self, width=self.image.width(), height=self.image.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

        # Créer une molette pour régler la valeur entre 0 et 100
        self.var = tk.IntVar(master = self)
        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.var)
        self.scale.pack()

        self.date_label = tk.Label(self)
        self.date_label.pack()

        # Charger l'image ce
        self.image_ce = Image.open("result.png")
        self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")

        # Créer un canvas pour afficher l'image ce
        self.canvas_ce = tk.Canvas(self, width=self.image_ce.width(), height=self.image_ce.height())
        # self.canvas_ce.place(x=self.image.width(), y=0)
        self.canvas_ce.create_image(0, 0, image=self.image_ce, anchor=tk.NW)

        self.canvas_ce.pack()
        self.geometry("500x1000")
        # Appeler la fonction update_line lorsque la valeur de la molette change
        self.var.trace("w", self.update_line)
        self.after(100, self.update_image)

    def update_image(self):
        # Modifier l'image en utilisant un fichier différent pour chaque appel de la fonction
        #file_path = "result.png".format(self.update_image.counter)
        #self.update_image.counter = (self.update_image.counter + 1) % 3  # Pour changer d'image toutes les secondes
        self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")
        self.canvas_ce.configure(width=self.image_ce.width(), height=self.image_ce.height())
        self.canvas_ce.create_image(0, 0, image=self.image_ce, anchor=tk.NW)

        self.after(100, self.update_image)

    def generate_graph(self):
        df = pd.read_csv(self.file_path)
        df["Taux d'occupation"].plot()
        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()/2)
        plt.savefig("result.png", dpi=100)

    def generate_graph2(self, abs):
        df = pd.read_csv(self.file_path)
        fig, ax = plt.subplots()

        df["Taux d'occupation"].plot(ax=ax)

        ax.scatter([abs, ], [df.at[abs, "Taux d'occupation"], ], 50, color='red')

        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()/2)
        plt.savefig("result.png", dpi=100)
        fig.clf()


    def getText(self, *args):
        value = self.var.get()
        df = pd.read_csv(self.file_path)
        date = df.at[value, "Datetime"]
        date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')

        # Formater la date en utilisant strftime
        formatted_date = date_time_obj.strftime("%d %B %Y a %Hh%M")
        return formatted_date

    def get_val(self, i, seuil_max = 40):
        df = pd.read_csv(self.file_path)
        occupancy_rate = df.at[i, "Taux d'occupation"]
        date = df.at[i, "Datetime"]
        max_occupancy = df["Taux d'occupation"].max()
        min_occupancy = df["Taux d'occupation"].min()
        if occupancy_rate > seuil_max:
            val = 100
        else : val = int((occupancy_rate-min_occupancy)/(max_occupancy-min_occupancy)*100)
        return val, date

    def update_line(self, *args):
        # Récupérer la valeur de la molette
        val = self.var.get()
        value, date = self.get_val(val)
        # Supprimer l'ancien trait s'il existe
        self.canvas.delete("line")
        self.canvas_ce.delete("line_result")

        # Calculer les couleurs de dégradé en fonction de la valeur de la molette
        green = int(255 * (100 - value) / 100)
        red = int(255 * value / 100)
        color = "#{:02x}{:02x}00".format(red, green)

        self.date_label.config(text = self.getText())
        self.value_looking = value
        # Dessiner le trait
        gauche = 40
        haut = 10
        bas = self.image.width()
        droite = self.image_ce.width()-gauche
        #self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")
        self.generate_graph2(val)
        #self.canvas_ce.image = img
        self.canvas.create_line(91, 95, 360, 221, width=5, fill=color, tags="line")
       # print(value)


class App_convention(tk.Tk):
    def __init__(self, file_path = "livrable_alpha_team.csv"):
        super().__init__()
        self.file_path = file_path
        self.title("Afficher les résultats")

        # Charger l'image
        self.image = ImageTk.PhotoImage(master = self, file = "asset/convention.png")
        # PhotoImage(master=Fenetre, file='FONDM.gif')
        self.generate_graph()
        # Créer un canvas pour afficher l'image
        self.canvas = tk.Canvas(self, width=self.image.width(), height=self.image.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

        # Créer une molette pour régler la valeur entre 0 et 100
        self.var = tk.IntVar(master = self)
        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.var)
        self.scale.pack()

        self.date_label = tk.Label(self)
        self.date_label.pack()

        # Charger l'image ce
        self.image_ce = Image.open("result.png")
        self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")

        # Créer un canvas pour afficher l'image ce
        self.canvas_ce = tk.Canvas(self, width=self.image_ce.width(), height=self.image_ce.height())
        # self.canvas_ce.place(x=self.image.width(), y=0)
        self.canvas_ce.create_image(0, 0, image=self.image_ce, anchor=tk.NW)

        self.canvas_ce.pack()
        self.geometry("500x1000")
        # Appeler la fonction update_line lorsque la valeur de la molette change
        self.var.trace("w", self.update_line)
        self.after(100, self.update_image)

    def update_image(self):
        # Modifier l'image en utilisant un fichier différent pour chaque appel de la fonction
        #file_path = "result.png".format(self.update_image.counter)
        #self.update_image.counter = (self.update_image.counter + 1) % 3  # Pour changer d'image toutes les secondes
        self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")
        self.canvas_ce.configure(width=self.image_ce.width(), height=self.image_ce.height())
        self.canvas_ce.create_image(0, 0, image=self.image_ce, anchor=tk.NW)

        self.after(100, self.update_image)

    def generate_graph(self):
        df = pd.read_csv(self.file_path)
        df["Taux d'occupation"].plot()
        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()/2)
        plt.savefig("result.png", dpi=100)

    def generate_graph2(self, abs):
        df = pd.read_csv(self.file_path)
        fig, ax = plt.subplots()

        df["Taux d'occupation"].plot(ax=ax)

        ax.scatter([abs, ], [df.at[abs, "Taux d'occupation"], ], 50, color='red')

        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()/2)
        plt.savefig("result.png", dpi=100)
        fig.clf()


    def getText(self, *args):
        value = self.var.get()
        df = pd.read_csv(self.file_path)
        date = df.at[value, "Datetime"]
        date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')

        # Formater la date en utilisant strftime
        formatted_date = date_time_obj.strftime("%d %B %Y a %Hh%M")
        return formatted_date

    def get_val(self, i, seuil_max = 40):
        df = pd.read_csv(self.file_path)
        occupancy_rate = df.at[i, "Taux d'occupation"]
        date = df.at[i, "Datetime"]
        max_occupancy = df["Taux d'occupation"].max()
        min_occupancy = df["Taux d'occupation"].min()
        if occupancy_rate > seuil_max:
            val = 100
        else : val = int((occupancy_rate-min_occupancy)/(max_occupancy-min_occupancy)*100)
        return val, date

    def update_line(self, *args):
        # Récupérer la valeur de la molette
        val = self.var.get()
        value, date = self.get_val(val)
        # Supprimer l'ancien trait s'il existe
        self.canvas.delete("line")
        self.canvas_ce.delete("line_result")

        # Calculer les couleurs de dégradé en fonction de la valeur de la molette
        green = int(255 * (100 - value) / 100)
        red = int(255 * value / 100)
        color = "#{:02x}{:02x}00".format(red, green)

        self.date_label.config(text = self.getText())
        self.value_looking = value
        # Dessiner le trait
        gauche = 40
        haut = 10
        bas = self.image.width()
        droite = self.image_ce.width()-gauche
        #self.image_ce = ImageTk.PhotoImage(master = self, file= "result.png")
        self.generate_graph2(val)
        #self.canvas_ce.image = img
        self.canvas.create_line(40, 56, 273, 217, width=5, fill=color, tags="line")
        self.canvas.create_line(273, 217, 426, 283, width=5, fill=color, tags="line")
       # print(value)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rues")

        self.b1 = tk.Button(self, text="Avenue des Champs Elysées", command=self.run_app_ce)
        self.b1.pack()

        self.b2 = tk.Button(self, text="Rue de la Convention", command=self.run_app_convention)
        self.b2.pack()

        self.upload_button = tk.Button(self, text="Upload", command=self.upload_csv)
        self.upload_button.pack()

    def run_app_ce(self):
        try :
            app = App_CE(self.file_name)
            app.mainloop()
        except:
            app = App_CE()
            app.mainloop()

    def run_app_convention(self):
        try :
            app = App_convention(self.file_name)
            app.mainloop()
        except:
            app = App_convention()
            app.mainloop()

    def upload_csv(self):
        filename = filedialog.askopenfilename()
        self.file_name = filename
        if filename:
            # Copier le fichier sélectionné à la racine du projet
            shutil.copy(filename, "result.csv")

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
