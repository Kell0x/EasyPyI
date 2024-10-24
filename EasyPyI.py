import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def select_project_directory():
    directory = filedialog.askdirectory()
    if directory:
        project_dir_entry.delete(0, tk.END)
        project_dir_entry.insert(0, directory)

def select_main_file():
    file = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file:
        main_file_entry.delete(0, tk.END)
        main_file_entry.insert(0, file)

def run_command(command, project_dir):
    process = subprocess.Popen(command, cwd=project_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def read_output(pipe):
        while True:
            line = pipe.readline()
            if not line:
                break
            console_output.insert(tk.END, line)
            console_output.yview(tk.END)  # Scroll automatique à la fin

    # Threads pour lire stdout et stderr en parallèle sans bloquer l'interface
    stdout_thread = threading.Thread(target=read_output, args=(process.stdout,))
    stderr_thread = threading.Thread(target=read_output, args=(process.stderr,))

    stdout_thread.start()
    stderr_thread.start()

    stdout_thread.join()
    stderr_thread.join()

    process.wait()  # Attendre la fin de la commande
    if process.returncode == 0:
        messagebox.showinfo("Succès", "Compilation réussie !")
    else:
        messagebox.showerror("Erreur", f"Erreur lors de la compilation (code {process.returncode})")

def compile_project():
    project_dir = project_dir_entry.get()
    main_file = main_file_entry.get()

    if not project_dir or not main_file:
        messagebox.showwarning("Erreur", "Veuillez sélectionner le répertoire du projet et le fichier principal.")
        return

    # Construction de la commande PyInstaller avec les options
    command = f'pyinstaller "{main_file}"'

    # Gestion des options
    if onefile_var.get():
        command += " --onefile"
    if windowed_var.get():
        command += " --windowed"
    if noupdate_var.get():
        command += " --noconfirm"
    if clean_var.get():
        command += " --clean"
    if noupx_var.get():
        command += " --noupx"
    if name_entry.get():
        command += f' --name "{name_entry.get()}"'
    if icon_entry.get():
        command += f' --icon "{icon_entry.get()}"'
    if additional_files_entry.get():
        command += f' --add-data "{additional_files_entry.get()};."'
    if hidden_imports_entry.get():
        command += f' --hidden-import "{hidden_imports_entry.get()}"'
    if extra_files_entry.get():
        command += f' --add-binary "{extra_files_entry.get()};."'
    if distpath_entry.get():
        command += f' --distpath "{distpath_entry.get()}"'
    if workpath_entry.get():
        command += f' --workpath "{workpath_entry.get()}"'
    if specpath_entry.get():
        command += f' --specpath "{specpath_entry.get()}"'

    # Vidage du contenu de la console
    console_output.delete(1.0, tk.END)

    # Lancer la commande dans un thread pour ne pas bloquer l'interface
    threading.Thread(target=run_command, args=(command, project_dir)).start()

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Compilateur PyInstaller")

# Répertoire du projet
tk.Label(root, text="Répertoire du projet :").grid(row=0, column=0, sticky="w")
project_dir_entry = tk.Entry(root, width=50)
project_dir_entry.grid(row=0, column=1)
tk.Button(root, text="Sélectionner", command=select_project_directory).grid(row=0, column=2)

# Fichier principal
tk.Label(root, text="Fichier principal (.py) :").grid(row=1, column=0, sticky="w")
main_file_entry = tk.Entry(root, width=50)
main_file_entry.grid(row=1, column=1)
tk.Button(root, text="Sélectionner", command=select_main_file).grid(row=1, column=2)

# Nom de l'exécutable
tk.Label(root, text="Nom de l'exécutable :").grid(row=2, column=0, sticky="w")
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=2, column=1)

# Icône
tk.Label(root, text="Icône (.ico) :").grid(row=3, column=0, sticky="w")
icon_entry = tk.Entry(root, width=50)
icon_entry.grid(row=3, column=1)
tk.Button(root, text="Sélectionner", command=lambda: icon_entry.insert(0, filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")]))).grid(row=3, column=2)

# Options PyInstaller
onefile_var = tk.IntVar()
windowed_var = tk.IntVar()
noupdate_var = tk.IntVar()
clean_var = tk.IntVar()
noupx_var = tk.IntVar()

tk.Checkbutton(root, text="Créer un seul fichier exécutable (--onefile)", variable=onefile_var).grid(row=4, columnspan=3, sticky="w")
tk.Checkbutton(root, text="Fenêtre sans console (--windowed)", variable=windowed_var).grid(row=5, columnspan=3, sticky="w")
tk.Checkbutton(root, text="Pas de demande de confirmation (--noconfirm)", variable=noupdate_var).grid(row=6, columnspan=3, sticky="w")
tk.Checkbutton(root, text="Nettoyage avant compilation (--clean)", variable=clean_var).grid(row=7, columnspan=3, sticky="w")
tk.Checkbutton(root, text="Désactiver UPX (--noupx)", variable=noupx_var).grid(row=8, columnspan=3, sticky="w")

# Fichiers additionnels
tk.Label(root, text="Fichiers additionnels (e.g., .ui, ; séparateur) :").grid(row=9, column=0, sticky="w")
additional_files_entry = tk.Entry(root, width=50)
additional_files_entry.grid(row=9, column=1)

# Importations cachées
tk.Label(root, text="Imports cachés (--hidden-import) :").grid(row=10, column=0, sticky="w")
hidden_imports_entry = tk.Entry(root, width=50)
hidden_imports_entry.grid(row=10, column=1)

# Fichiers binaires supplémentaires
tk.Label(root, text="Fichiers binaires supplémentaires :").grid(row=11, column=0, sticky="w")
extra_files_entry = tk.Entry(root, width=50)
extra_files_entry.grid(row=11, column=1)

# Chemin de distribution
tk.Label(root, text="Chemin de sortie (--distpath) :").grid(row=12, column=0, sticky="w")
distpath_entry = tk.Entry(root, width=50)
distpath_entry.grid(row=12, column=1)

# Chemin de travail
tk.Label(root, text="Chemin de travail (--workpath) :").grid(row=13, column=0, sticky="w")
workpath_entry = tk.Entry(root, width=50)
workpath_entry.grid(row=13, column=1)

# Chemin du fichier spec
tk.Label(root, text="Chemin fichier .spec (--specpath) :").grid(row=14, column=0, sticky="w")
specpath_entry = tk.Entry(root, width=50)
specpath_entry.grid(row=14, column=1)

# Zone de texte pour afficher la sortie de la console
tk.Label(root, text="Console :").grid(row=15, column=0, sticky="w")
console_output = scrolledtext.ScrolledText(root, width=80, height=10)
console_output.grid(row=16, column=0, columnspan=3)

# Bouton pour compiler
tk.Button(root, text="Compiler", command=compile_project).grid(row=17, columnspan=3)

root.mainloop()
