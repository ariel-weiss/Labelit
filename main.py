import tkinter as tk

def clear(self):
    pass

def export(self):
    pass


def main():
    _root = tk.Tk()
    _root.title("Labelit!")
    _root.geometry("800x150")
    _root.resizable(0,0)
    _root.configure(background="#f2eb22")

    text_frame = tk.Frame(_root, bg="red")
    text_frame.pack()

    btn_frame = tk.Frame(_root, bg="#f2eb22")
    btn_frame.pack()


    # Horizontal (x) Scroll bar
    xscrollbar = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
    xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Text Widget
    text = tk.Text(text_frame, wrap=tk.NONE,height = 5,
                xscrollcommand=xscrollbar.set)
    text.pack()

    # Configure the scrollbars
    xscrollbar.config(command=text.xview)
    # yscrollbar.config(command=text.yview)

    ref_btn = tk.Button(btn_frame,text="It's a REF!" ,command=export)
    ref_btn.pack(padx=5, pady=10, side=tk.LEFT)

    no_ref_btn = tk.Button(btn_frame,text="No REF.", command=clear)
    no_ref_btn.pack(padx=5, pady=10, side=tk.LEFT)

    _root.mainloop()


if __name__ == "__main__":
    main()