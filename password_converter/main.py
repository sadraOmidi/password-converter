from password_hasher import PasswordHasher
import tkinter as tk
from tkinter import messagebox

instance = PasswordHasher()

text = '*** welcome ***\nThis system is designed to convert hashes to text. To use, just enter your hash\
and get the desired text output.'

window = tk.Tk()

window.title('Hash Converter!')
window.geometry('650x300')
window.resizable(0, 0)
window.configure(background='grey')

convert_password_to_hash_lable = tk.Label(text='convert hash to password : ', bg='grey', fg='white', height=3, width=25)
convert_password_to_hash_lable.place(x=5, y=50)
convert_password_to_hash_entry = tk.Entry(window, textvariable=tk.StringVar(), width=50)
convert_password_to_hash_entry.place(x=175, y=65)
# Button Convert from password to hash
result_convert_password_to_hash = tk.Button(text='convert', bg='black', fg='white', width=10,
                                            command=lambda: messagebox.showinfo('PASSWORD',
                                                                                instance.hash_converter(
                                                                                    convert_password_to_hash_entry.get()
                                                                                )))
result_convert_password_to_hash.place(x=515, y=65)

convert_hash_to_password_lable = tk.Label(text='convert password to hash : ', bg='grey', fg='white', height=3, width=25)
convert_hash_to_password_lable.place(x=5, y=130)
convert_hash_to_password_entry = tk.Entry(window, textvariable=tk.StringVar(), width=50)
convert_hash_to_password_entry.place(x=175, y=145)
# Button Convert from hash to password
result_convert_hash_to_password = tk.Button(text='convert', bg='black', fg='white', width=10,
                                            command=lambda: messagebox.showinfo('HASH', instance.password_converter(
                                                convert_hash_to_password_entry.get())))
result_convert_hash_to_password.place(x=515, y=145)

exit_program = tk.Button(text='exit', bg='black', fg='red', height=3, width=25, command=lambda: exit())
exit_program.place(x=250, y=210)

window.mainloop()
