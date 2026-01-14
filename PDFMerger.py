import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

# --- CONFIGURATION ---
VERSION = "1.0.0"
APP_NAME = "PDF Merger Utility"

def show_about():
    """Displays a popup with app information."""
    messagebox.showinfo(
        "About",
        f"{APP_NAME}\n"
        f"Version: {VERSION}\n\n"
        "A simple tool to merge PDFs in your preferred order.\n"
        "Licensed under MIT."
    )

# --- GUI Setup ---
root = tk.Tk()
# This adds the version to the top bar of the window
root.title(f"{APP_NAME} - v{VERSION}")
root.geometry("500x450")

# --- ADDING A MENU BAR ---
menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# --- Functions ---
def add_files():
    """Allows user to select multiple files and adds them to the list."""
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    for file in files:
        listbox.insert(tk.END, file)


def move_up():
    """Moves the selected item up one spot."""
    try:
        # Get the index of the selected item
        selection = listbox.curselection()
        if not selection:
            return
        pos = selection[0]

        # If it's already at the top, stop
        if pos == 0:
            return

        # Get the text of the item
        text = listbox.get(pos)

        # Delete it and re-insert it one spot higher
        listbox.delete(pos)
        listbox.insert(pos - 1, text)

        # Keep it selected so user can click 'Up' again quickly
        listbox.selection_set(pos - 1)
    except Exception as e:
        pass


def move_down():
    """Moves the selected item down one spot."""
    try:
        selection = listbox.curselection()
        if not selection:
            return
        pos = selection[0]

        # If it's already at the bottom, stop
        if pos == listbox.size() - 1:
            return

        text = listbox.get(pos)
        listbox.delete(pos)
        listbox.insert(pos + 1, text)
        listbox.selection_set(pos + 1)
    except:
        pass


def remove_selected():
    """Removes the selected item from the list."""
    try:
        selection = listbox.curselection()
        if selection:
            listbox.delete(selection[0])
    except:
        pass


def merge_pdfs():
    """Reads the list in order and merges them."""
    # Get all items from the Listbox
    files = listbox.get(0, tk.END)

    if len(files) == 0:
        messagebox.showwarning("Warning", "Please add some PDF files first!")
        return

    # Ask where to save
    save_path = filedialog.asksaveasfilename(
        title="Save Merged File As...",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not save_path:
        return

    # Merge Logic
    merger = PdfWriter()
    try:
        for pdf in files:
            merger.append(pdf)

        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge: {e}")


# --- GUI Setup ---
root = tk.Tk()
root.title("PDF Merger Utility")
root.geometry("500x400")

# 1. The Listbox (The "Staging Area")
frame_list = tk.Frame(root)
frame_list.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame_list, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# 2. Control Buttons (Right below the list)
frame_controls = tk.Frame(root)
frame_controls.pack(fill="x", padx=10, pady=5)

btn_add = tk.Button(frame_controls, text="Add Files...", command=add_files, width=15)
btn_add.pack(side="left", padx=5)

btn_remove = tk.Button(frame_controls, text="Remove Selected", command=remove_selected, width=15)
btn_remove.pack(side="left", padx=5)

# Move Up/Down Buttons
btn_up = tk.Button(frame_controls, text="Move Up ↑", command=move_up, width=10)
btn_up.pack(side="right", padx=5)

btn_down = tk.Button(frame_controls, text="Move Down ↓", command=move_down, width=10)
btn_down.pack(side="right", padx=5)

# 3. The Big Merge Button
btn_merge = tk.Button(root, text="MERGE PDFS", command=merge_pdfs, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_merge.pack(fill="x", padx=10, pady=10)

root.mainloop()