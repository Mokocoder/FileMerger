import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class AutoScrollbar(tk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)

class FileMerger(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("파일 합성기")
        self.geometry("400x265")
        self.minsize(400, 265)
        self.resizable(True, True)
        self.files = []

        self.listbox_frame = tk.Frame(self)
        self.listbox_frame.grid(sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.vscrollbar = AutoScrollbar(self.listbox_frame, orient="vertical")
        self.vscrollbar.grid(row=0, column=1, sticky='ns')

        self.hscrollbar = AutoScrollbar(self.listbox_frame, orient="horizontal")
        self.hscrollbar.grid(row=1, column=0, sticky='ew')

        self.listbox = tk.Listbox(self.listbox_frame, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar.set)
        self.listbox.grid(row=0, column=0, sticky='nsew', pady=5, padx=5)

        self.listbox_frame.grid_rowconfigure(0, weight=1)
        self.listbox_frame.grid_columnconfigure(0, weight=1)

        self.vscrollbar.config(command=self.listbox.yview)
        self.hscrollbar.config(command=self.listbox.xview)

        self.add_button = tk.Button(self, text="파일 추가", bg='#dae9e4' ,command=self.add_files)
        self.add_button.grid(sticky='ew', pady=5, padx=45)

        self.merge_button = tk.Button(self, text="파일 합치기", bg='#dae9e4', command=self.merge_files)
        self.merge_button.grid(sticky='ew', pady=5, padx=45)

    def add_files(self):
        filenames = filedialog.askopenfilenames()
        for filename in filenames:
            self.files.append(filename)
            self.listbox.insert(tk.END, filename)

    def merge_files(self):
        if len(self.files) >= 2:
            messagebox.showwarning("안내", "파일을 저장하기 위한 이름 밎 확장자를 하단 '파일 이름' 에 기입한 후 저장하세요.\n\nex) final.gguf")
            output_file = filedialog.asksaveasfilename()

            if output_file != '':
                with open(output_file, 'wb') as outfile:
                    for file in self.files:
                        with open(file, 'rb') as infile:
                            outfile.write(infile.read())
                messagebox.showinfo("안내", "파일이 합쳐졌습니다.")
        else:
            messagebox.showerror("안내", "합칠 수 있는 파일이 2개 이상 존재하지 않습니다.\n파일을 추가해주세요.")

if __name__ == "__main__":
    FileMerger().mainloop()