from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyttsx3

USER_ID = "1"
PASSWORD = "1"
indian_languages = ["hindi", "bengali", "tamil", "telugu", "marathi", "urdu", "gujarati", "malayalam", "kannada", "punjabi","english"]
all_languages = sorted(list(LANGUAGES.values()))
languages_sorted = indian_languages + [lang for lang in all_languages if lang not in indian_languages]

lang_map = {v.lower(): k for k, v in LANGUAGES.items()}

engine = pyttsx3.init()

def login():
    if user_id.get() == USER_ID and password.get() == PASSWORD:
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password!")

def Translate():
    translator = Translator()
    input_text = Input_text.get(1.0, END).strip()
    source_lang = src_lang.get().strip().lower()
    target_lang = dest_lang.get().strip().lower()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return

    if source_lang not in lang_map or target_lang not in lang_map:
        messagebox.showerror("Error", "Invalid languages selected! Please choose from the dropdown.")
        return

    try:
        translated = translator.translate(text=input_text, src=lang_map[source_lang], dest=lang_map[target_lang])
        Output_text.config(state=NORMAL)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
        Output_text.config(state=DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}")
def speak_output():
    Output_text.config(state=NORMAL)
    text = Output_text.get(1.0, END).strip()
    Output_text.config(state=DISABLED)
    
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showinfo("No Text", "There is no translated text to speak!")
def main_window():
    global root, src_lang, dest_lang, Input_text, Output_text

    root = Tk()
    root.geometry('1080x500')
    root.minsize(800, 400)
    root.title("Language Translator")
    root.config(bg='#2C3E50')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='#1ABC9C', fg='white', pady=8).grid(row=0, column=0, columnspan=2, sticky="ew")
    Label(root, text="Infotact Internship Project", font='arial 15 bold', bg='white smoke', width='25').grid(row=3, column=0, columnspan=2, pady=5)
    frame1 = Frame(root, bg='#2C3E50')
    frame1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)

    Label(frame1, text="Enter Text", font='arial 13 bold', bg='#2C3E50', fg='white').grid(row=0, column=0, sticky='w')
    Input_text = Text(frame1, font='arial 12', wrap=WORD, padx=5, pady=5, bg='#ECF0F1', fg='#2C3E50')
    Input_text.grid(row=1, column=0, sticky="nsew")
    frame2 = Frame(root, bg='#2C3E50')
    frame2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    frame2.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)

    Label(frame2, text="Output", font='arial 13 bold', bg='#2C3E50', fg='white').grid(row=0, column=0, sticky='w')
    Output_text = Text(frame2, font='arial 12', wrap=WORD, padx=5, pady=5, bg='#BDC3C7', fg='#2C3E50')
    Output_text.grid(row=1, column=0, sticky="nsew")
    Output_text.config(state=DISABLED)

    lang_frame = Frame(root, bg='#2C3E50')
    lang_frame.grid(row=2, column=0, columnspan=2, pady=5)

    Label(lang_frame, text="From Language:", font="arial 12 bold", bg="#2C3E50", fg="white").grid(row=0, column=0, padx=5)
    src_lang = ttk.Combobox(lang_frame, values=languages_sorted, width=30, state="readonly")
    src_lang.grid(row=0, column=1, padx=5)
    src_lang.set("Select Input Language")

    Label(lang_frame, text="To Language:", font="arial 12 bold", bg="#2C3E50", fg="white").grid(row=0, column=2, padx=5)
    dest_lang = ttk.Combobox(lang_frame, values=languages_sorted, width=30, state="readonly")
    dest_lang.grid(row=0, column=3, padx=5)
    dest_lang.set("Select Output Language")

    # Buttons for Translate and Speak
    trans_btn = Button(lang_frame, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='#E74C3C', fg='white', activebackground='red')
    trans_btn.grid(row=0, column=4, padx=10)

    speak_btn = Button(lang_frame, text='🔊 Speak', font='arial 12 bold', pady=5, command=speak_output, bg='#3498DB', fg='white', activebackground='skyblue')
    speak_btn.grid(row=0, column=5, padx=10)

    root.mainloop()

login_window = Tk()
login_window.geometry('400x300')
login_window.resizable(0, 0)
login_window.title("Login")
login_window.config(bg='#87CEFA')

Label(login_window, text="Login", font="arial 20 bold", fg='black').pack(pady=20)

Label(login_window, text="Username:", font="arial 12").place(x=50, y=80)
user_id = Entry(login_window, font="arial 12")
user_id.place(x=150, y=80)

Label(login_window, text="Password:", font="arial 12").place(x=50, y=120)
password = Entry(login_window, font="arial 12", show="*")
password.place(x=150, y=120)

login_btn = Button(login_window, text="Login", font="arial 12 bold", command=login, bg="dark blue", fg="white")
login_btn.place(x=170, y=180)

login_window.bind('<Return>', lambda event: login())

login_window.mainloop()

