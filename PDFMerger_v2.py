import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pypdf import PdfWriter
import os

# --- CONFIGURATION ---
VERSION = "2.0.0"
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

# --- LOGIC ---

def add_files():
    """Manual selection of files via button."""
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    for file in files:
        listbox.insert(tk.END, file)


def drop_files(event):
    """Handles dragging and dropping files into the listbox."""
    # The event.data returns a string of filenames.
    # We need to clean curly braces {} which Windows adds to paths with spaces.
    raw_files = event.data

    # This logic splits the dropped items into individual paths
    # Note: TkinterDnD can be tricky with spaces, this is a basic parser
    if raw_files.startswith('{'):
        paths = raw_files[1:-1].split('} {')
    else:
        paths = raw_files.split()

    for path in paths:
        if path.lower().endswith('.pdf'):
            listbox.insert(tk.END, path)


def move_up():
    """Moves selected item up."""
    try:
        selection = listbox.curselection()
        if not selection or selection[0] == 0: return
        pos = selection[0]
        text = listbox.get(pos)
        listbox.delete(pos)
        listbox.insert(pos - 1, text)
        listbox.selection_set(pos - 1)
    except:
        pass


def move_down():
    """Moves selected item down."""
    try:
        selection = listbox.curselection()
        if not selection or selection[0] == listbox.size() - 1: return
        pos = selection[0]
        text = listbox.get(pos)
        listbox.delete(pos)
        listbox.insert(pos + 1, text)
        listbox.selection_set(pos + 1)
    except:
        pass


def remove_selected():
    """Removes selected item."""
    try:
        selection = listbox.curselection()
        if selection: listbox.delete(selection[0])
    except:
        pass


def merge_pdfs():
    """Merges files and auto-opens the folder."""
    files = listbox.get(0, tk.END)

    if len(files) == 0:
        messagebox.showwarning("Warning", "No files to merge!")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save Merged File",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not save_path: return

    merger = PdfWriter()
    try:
        for pdf in files:
            merger.append(pdf)

        merger.write(save_path)
        merger.close()

        # --- FEATURE: AUTO-OPEN FOLDER ---
        folder_path = os.path.dirname(save_path)
        os.startfile(folder_path)

        messagebox.showinfo("Success", f"Saved to:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")


# --- GUI SETUP ---
# We use TkinterDnD.Tk instead of tk.Tk
root = TkinterDnD.Tk()
root.title(f"{APP_NAME} - v{VERSION}")
root.geometry("600x450")

# --- ADDING A MENU BAR ---
menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# 1. Header with Instructions
lbl_instruct = tk.Label(root, text="Drag & Drop PDF files here", font=("Arial", 10, "italic"), fg="gray")
lbl_instruct.pack(pady=(10, 0))

# 2. The Listbox (With Drag & Drop Enabled)
frame_list = tk.Frame(root)
frame_list.pack(fill="both", expand=True, padx=15, pady=5)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame_list, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=("Consolas", 9))
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# ENABLE DRAG AND DROP ON LISTBOX
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', drop_files)

# 3. Control Buttons
frame_controls = tk.Frame(root)
frame_controls.pack(fill="x", padx=15, pady=5)

btn_add = tk.Button(frame_controls, text="➕ Add Manually", command=add_files)
btn_add.pack(side="left")

btn_remove = tk.Button(frame_controls, text="❌ Remove", command=remove_selected)
btn_remove.pack(side="left", padx=5)

btn_down = tk.Button(frame_controls, text="↓", command=move_down, width=3)
btn_down.pack(side="right")

btn_up = tk.Button(frame_controls, text="↑", command=move_up, width=3)
btn_up.pack(side="right", padx=5)

# 4. Merge Button
btn_merge = tk.Button(root, text="MERGE NOW", command=merge_pdfs, bg="#007ACC", fg="white", font=("Arial", 11, "bold"),
                      height=2)
btn_merge.pack(fill="x", padx=15, pady=10)

# 5. Version Badge (Bottom Right)
lbl_version = tk.Label(root, text=f"v{VERSION}", font=("Arial", 8), fg="#999")
lbl_version.pack(side="bottom", anchor="se", padx=5, pady=2)

root.mainloop()