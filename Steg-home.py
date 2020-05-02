import tkinter as tk

HEIGHT = 500
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

head_label = tk.Label(frame, bg='#80c1ff', text='Steganography', font=('nexa rust', 15), justify='center', bd=4)
head_label.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

body_label = tk.Label(lower_frame, bg='white', font=('courier', 15), anchor='nw', justify='left', bd=4)
body_label.place(relwidth=1, relheight=1)

body_label1 = tk.Label(body_label, text='LOGIN PAGE:', bg='#80c1ff', font=('courier', 15), anchor='n', justify='center')
body_label1.place(relwidth=1, relheight=0.1)

body_label2 = tk.Label(body_label, text='USER-NAME:', font=('courier', 15), anchor='n', bg='white')
body_label3 = tk.Label(body_label, text='PASS-WORD:', font=('courier', 15), anchor='n', bg='white')
body_label4 = tk.Label(body_label, anchor='n', bg='white')
body_label5 = tk.Label(body_label, anchor='n', bg='white')
body_label2.place(relx=0.1, rely=0.3)
body_label3.place(relx=0.1, rely=0.5)
body_label4.place(relx=0.4, rely=0.3, relwidth=0.3, relheight=0.1)
body_label5.place(relx=0.4, rely=0.5, relwidth=0.3, relheight=0.1)

body_entry1 = tk.Entry(body_label4, bg='#80c1ff', bd=1, justify='left')
body_entry2 = tk.Entry(body_label5, show='*', bg='#80c1ff', bd=1)
body_entry1.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)
body_entry2.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)

body_button1 = tk.Button(lower_frame, bg='#fd7558', text='Login', font=15)
body_button2 = tk.Button(lower_frame, bg='#fd7558', text='Register', font=15)
body_button1.place(relx=0.43, rely=0.7, relwidth=0.2, relheight=0.1)
body_button2.place(relx=0.65, rely=0.7, relwidth=0.2, relheight=0.1)


root.mainloop()
