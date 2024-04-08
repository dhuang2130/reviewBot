import tkinter as tk
from tkinter import filedialog, messagebox
from review_bot import CodeReviewBot

class CodeReviewGUI:
    def __init__(self, root):
        self.root = root
        self.bot = CodeReviewBot()

        self.file_label = tk.Label(root, text="")
        self.file_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.analyze_button = tk.Button(root, text="Analyze", command=self.analyze_code)
        self.analyze_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        message = self.bot.select_file(file_path)
        self.file_label.config(text=message)

    def analyze_code(self):
        message = self.bot.review_code()
        messagebox.showinfo("Pylint Output", message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Code Review Bot")
    root.geometry("400x300")

    app = CodeReviewGUI(root)

    root.mainloop()
