import json
import requests
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from pprint import pformat

class JSONManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Manager")
        self.root.geometry("1200x600")
        self.root.minsize(800, 400)

        # Initialize JSON data
        self.json_data = None
        self.original_json_data = None  # To preserve the original JSON

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # PanedWindow for side-by-side layout
        self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        # Left side - Original/Uploaded JSON
        self.left_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.left_frame, width=600)

        tk.Label(self.left_frame, text="Original/Uploaded JSON", font=("Arial", 12, "bold")).pack(pady=5)
        self.original_json_text = scrolledtext.ScrolledText(self.left_frame, wrap=tk.WORD, width=70, height=20)
        self.original_json_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Right side - Formatted JSON
        self.right_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.right_frame, width=600)

        tk.Label(self.right_frame, text="Formatted JSON", font=("Arial", 12, "bold")).pack(pady=5)
        self.formatted_json_text = scrolledtext.ScrolledText(self.right_frame, wrap=tk.WORD, width=70, height=20)
        self.formatted_json_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Buttons and Search
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, pady=10)

        tk.Button(self.button_frame, text="Open JSON File", command=self.open_file).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Format JSON", command=self.format_json).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Download Formatted JSON", command=self.download_formatted_json).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Upload JSON", command=self.upload_json).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Clear Results", command=self.clear_results).pack(side=tk.LEFT, padx=5)

        # Search Frame
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(fill=tk.X, pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(self.search_frame, text="Search", command=self.search_json).pack(side=tk.LEFT, padx=5)
        self.search_count_label = tk.Label(self.search_frame, text="Occurrences: 0")
        self.search_count_label.pack(side=tk.LEFT, padx=5)

    def open_file(self):
        """Open a JSON file and display its content."""
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as f:
                    self.json_data = json.load(f)  # Load JSON data
                    self.original_json_data = self.json_data  # Preserve original JSON
                    self.original_json_text.delete(1.0, tk.END)
                    self.original_json_text.insert(tk.END, json.dumps(self.json_data, indent=4))
                    self.format_json()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load JSON file: {e}")

    def format_json(self):
        """Format the JSON data and display it in the formatted text area."""
        try:
            # Get JSON data from the original text area
            json_text = self.original_json_text.get(1.0, tk.END).strip()
            if not json_text:
                messagebox.showerror("Error", "No JSON data to format!")
                return

            # Parse JSON from the text area
            self.json_data = json.loads(json_text)
            formatted_json = json.dumps(self.json_data, indent=4)  # Format JSON
            self.formatted_json_text.delete(1.0, tk.END)
            self.formatted_json_text.insert(tk.END, formatted_json)
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"Invalid JSON data: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to format JSON: {e}")

    def search_json(self):
        """Search for a keyword in the formatted JSON and highlight it."""
        keyword = self.search_entry.get()
        if not keyword:
            return

        # Clear previous highlights
        self.formatted_json_text.tag_remove("highlight", 1.0, tk.END)

        # Search and highlight
        formatted_json = self.formatted_json_text.get(1.0, tk.END)
        occurrences = formatted_json.count(keyword)
        self.search_count_label.config(text=f"Occurrences: {occurrences}")

        if occurrences == 0:
            messagebox.showinfo("Search Result", f"Keyword '{keyword}' not found.")
            return

        start_index = 1.0
        while True:
            start_index = self.formatted_json_text.search(keyword, start_index, stopindex=tk.END)
            if not start_index:
                break
            end_index = f"{start_index}+{len(keyword)}c"
            self.formatted_json_text.tag_add("highlight", start_index, end_index)
            start_index = end_index

        self.formatted_json_text.tag_config("highlight", background="seagreen")

    def download_formatted_json(self):
        """Download the formatted JSON as a file."""
        formatted_json = self.formatted_json_text.get(1.0, tk.END)
        if not formatted_json.strip():
            messagebox.showerror("Error", "No formatted JSON to download!")
            return

        # File type options
        file_types = [
            ("JSON Files", "*.json"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=file_types)
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write(formatted_json)
                messagebox.showinfo("Success", "Formatted JSON downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def upload_json(self):
        """Upload JSON to a server."""
        if self.json_data is None:
            messagebox.showerror("Error", "No JSON data to upload!")
            return

        url = tk.simpledialog.askstring("Upload JSON", "Enter URL to upload JSON:")
        if url:
            try:
                headers = {'Content-Type': 'application/json'}
                # Ensure JSON is properly serialized with double quotes
                json_data = json.dumps(self.json_data, indent=4, ensure_ascii=False)
                response = requests.post(url, data=json_data, headers=headers)
                response.raise_for_status()
                messagebox.showinfo("Upload Success", "JSON uploaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload JSON: {e}")

    def clear_results(self):
        """Clear all results and reset the UI."""
        self.original_json_text.delete(1.0, tk.END)
        self.formatted_json_text.delete(1.0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.search_count_label.config(text="Occurrences: 0")
        self.formatted_json_text.tag_remove("highlight", 1.0, tk.END)
        self.json_data = None
        self.original_json_data = None

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONManagerApp(root)
    root.mainloop()
