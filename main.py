import tkinter as tk
from tkinter import messagebox


def show_text():
    text = str(text_tf.get())
    messagebox.showinfo(title="Very USEFUL message", message=text)


window = tk.Tk()
window.title("VUP. Very USEFUL program")
window.geometry("500x100")

frame = tk.Frame(
    window,
    padx=10,  # отступ по горизонтали
    pady=10  # отступ по вертикали
)
frame.pack(expand=True)

text_lb = tk.Label(
    frame,
    text="Введите фразу, которую хотите вывести на экран:"
)
text_lb.grid(row=0, column=0, padx=(0, 10))

text_tf = tk.Entry(
    frame
)
text_tf.grid(row=0, column=1, ipadx=30)

cal_btn = tk.Button(
    frame,
    text="Жмяк",  # надпись на кнопке
    command=show_text
)
cal_btn.grid(row=1, column=0, columnspan=2, pady=(10, 0), ipadx=40)

window.mainloop()
