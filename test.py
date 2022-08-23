from tkinter import messagebox, Toplevel, Label, Tk, Button


def pop(msg):  # This will be on top of the window which called this pop up
    messagebox.showinfo('message', msg)


def pop_always_on_top(msg):  # This will be on top of any other window
    msg_window = Toplevel()
    msg_window.title("Show Message")
    msg_window.attributes('-topmost', True)
    msg_label = Label(msg_window, text=msg)
    msg_label.pack(expand=1, fill='both')
    button = Button(msg_window, text="Ok", command=msg_window.destroy)
    button.pack()


if __name__ == '__main__':
    top = Tk()

    hello_btn = Button(top, text="Say Hello", command=lambda: pop('hello world!'))
    hello_btn.pack()
    hello_btn = Button(top, text="Say Hello and stay on top!", command=lambda: pop_always_on_top('hello world - on top!'))
    hello_btn.pack()
    top.mainloop()