from tkinter import *
from tkinter import filedialog
#from tkmacosx import *
import pathlib

CONVERSION_CODE = {

    # Uppercase Alphabets
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
    'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
    'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
    'Y': 'B', 'Z': 'A',

    # Lowercase Alphabets
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'F', 'v': 'e', 'w': 'd', 'x': 'c',
    'y': 'b', 'z': 'a'
}


def encode_and_decode_text(txt):
    converted_txt = ""

    for i in range(0, len(txt)):
        if txt[i] in CONVERSION_CODE.keys():
            converted_txt += CONVERSION_CODE[txt[i]]
        else:
            converted_txt += txt[i]
    return converted_txt


def open_file():

    # Get absolute Path
    abspath = pathlib.Path().absolute()

    absolute_path_str = str(abspath)
    tf = filedialog.askopenfilename(
        initialdir=absolute_path_str,
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    PATH.insert(END, tf)
    tf = open(tf)
    file_cont = tf.read()
    decoded_text = encode_and_decode_text(file_cont)
    txtarea.insert(END, str(decoded_text))
    tf.close()


def save_file():
    tf = filedialog.asksaveasfile(
        mode='w',
        title="Save file",
        defaultextension=".txt"
    )

    PATH.insert(END, tf)
    data = str(txtarea.get(1.0, END))
    encoded_text = encode_and_decode_text(data)
    tf.write(encoded_text)
    tf.close()


ws = Tk()
ws.title("Alpha Encrypt Password v0.1")
ws.geometry("1500x750")
ws['bg'] = '#e5f3f3'

# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars
ver_sb = Scrollbar(frame, orient=VERTICAL)
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=80, height=30)
txtarea.pack(side=LEFT)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

# adding path showing box
PATH = Entry(ws)
PATH.pack(expand=True, fill=X, padx=10)

# adding buttons
Button(
    ws,
    text="Open File",
    command=open_file
).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Save File",
    command=save_file
).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Clear File Text",
    command=lambda: txtarea.delete(1.0, END)
).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Clear Path Text",
    command=lambda: PATH.delete(0, END)
).pack(side=LEFT, expand=True, fill=X, padx=20)


Button(
    ws,
    text="Exit",
    command=lambda: ws.destroy()
).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)


ws.mainloop()
