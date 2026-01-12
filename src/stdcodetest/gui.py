import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .manager import TestManager
from .registry import ModeRegistry

class StdTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("stdcodetest - Configuration GUI")
        self.root.geometry("500x350")
        
        # UI Elements
        ttk.Label(root, text="Standardized Test Creator", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Mode Selection
        ttk.Label(root, text="Select Mode:").pack(anchor="w", padx=20)
        self.mode_var = tk.StringVar(value="default")
        self.mode_cb = ttk.Combobox(root, textvariable=self.mode_var, values=ModeRegistry.list_modes())
        self.mode_cb.pack(fill="x", padx=20, pady=5)
        
        # Test Name
        ttk.Label(root, text="Test Case Name:").pack(anchor="w", padx=20)
        self.name_entry = ttk.Entry(root)
        self.name_entry.insert(0, "new_test_case")
        self.name_entry.pack(fill="x", padx=20, pady=5)
        
        # Target Path
        ttk.Label(root, text="Tests Root Location:").pack(anchor="w", padx=20)
        path_frame = ttk.Frame(root)
        path_frame.pack(fill="x", padx=20, pady=5)
        self.path_var = tk.StringVar(value="TEST_SUITE")
        ttk.Entry(path_frame, textvariable=self.path_var).pack(side="left", expand=True, fill="x")
        ttk.Button(path_frame, text="Browse", command=self.browse_path).pack(side="right", padx=5)
        
        # Action Button
        ttk.Button(root, text="Generate Test Structure", command=self.generate).pack(pady=20)

    def browse_path(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    def generate(self):
        try:
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Test name cannot be empty")
                
            manager = TestManager(tests_root=self.path_var.get(), mode=self.mode_var.get())
            path = manager.create_std_test(name, replace=True)
            messagebox.showinfo("Success", f"Test structure created at:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def gui_main():
    root = tk.Tk()
    app = StdTestGUI(root)
    root.mainloop()