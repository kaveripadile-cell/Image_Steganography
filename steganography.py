import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import font as tkFont
from PIL import ImageTk, Image
from stegano import lsb
from stegano import exifHeader as aaa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILETYPES = (("jpeg, png files", "*.jpg *.jpeg *.png"), ("all files", "*.*"))

main = Tk()
main.title('Enc & Dec Panel')
main.attributes("-fullscreen", True)
fontl = tkFont.Font(family='Algerian', size=32)

# keep references to PhotoImages so Tkinter does not garbage collect them
images = {}


def clear_screen():
	for widget in main.winfo_children():
		widget.destroy()


def set_background(name):
	bg = Image.open(os.path.join(BASE_DIR, name))
	bg = bg.resize((main.winfo_screenwidth(), main.winfo_screenheight()))
	images['bg'] = ImageTk.PhotoImage(bg)
	Label(main, image=images['bg']).place(x=0, y=0, relwidth=1, relheight=1)


def open_image(state):
	path = askopenfilename(initialdir=os.path.expanduser("~/Desktop"), title="select file", filetypes=FILETYPES)
	if not path:
		return
	try:
		preview = Image.open(path)
		preview.thumbnail((200, 200))
	except Exception as e:
		messagebox.showerror("popup", "Could not open image:\n" + str(e))
		return

	state['file'] = path
	images['preview'] = ImageTk.PhotoImage(preview)

	Label(main, text=path).place(relx=0.6, rely=0.25, height=21, width=450)
	Label(main, image=images['preview']).place(relx=0.7, rely=0.3, height=200, width=200)


def is_jpeg(path):
	return os.path.splitext(path)[1].lower() in ('.jpg', '.jpeg')


def encode():
	clear_screen()
	set_background("bg2.jpg")
	state = {'file': None}

	LabelTitle = Label(main, text="ENCODE", bg="red", fg="white", width=20)
	LabelTitle['font'] = fontl
	LabelTitle.place(relx=0.6, rely=0.1)

	Button(main, text="Openfile", command=lambda: open_image(state)).place(relx=0.7, rely=0.2, height=31, width=94)

	secimg = StringVar(value='png')
	Radiobutton(main, text='jpeg', value='jpeg', variable=secimg).place(relx=0.7, rely=0.57)
	Radiobutton(main, text='png', value='png', variable=secimg).place(relx=0.8, rely=0.57)

	Label(main, text="Enter message").place(relx=0.6, rely=0.6, height=21, width=104)
	entrysecmes = Entry(main)
	entrysecmes.place(relx=0.7, rely=0.6, relheight=0.05, relwidth=0.200)

	Label(main, text="File Name").place(relx=0.6, rely=0.70, height=21, width=104)
	entrysave = Entry(main)
	entrysave.place(relx=0.7, rely=0.70, relheight=0.05, relwidth=0.200)

	def enc():
		inimage = state['file']
		message = entrysecmes.get()
		name = entrysave.get().strip()
		if not inimage:
			messagebox.showwarning("popup", "Please select an image first")
			return
		if not message:
			messagebox.showwarning("popup", "Please enter a message")
			return
		if not name:
			messagebox.showwarning("popup", "Please enter a file name")
			return
		if secimg.get() == "jpeg" and not is_jpeg(inimage):
			messagebox.showwarning("popup", "jpeg mode needs a .jpg/.jpeg image. Use png mode for other images.")
			return

		ext = '.jpg' if secimg.get() == "jpeg" else '.png'
		# save next to the original image
		outfile = os.path.normpath(os.path.join(os.path.dirname(inimage), name + ext))

		if not messagebox.askyesno("popup", "do you want to encode"):
			messagebox.showwarning("popup", "unsuccessful")
			return
		try:
			if secimg.get() == "jpeg":
				aaa.hide(inimage, outfile, message)
			else:
				lsb.hide(inimage, message=message, auto_convert_rgb=True).save(outfile)
		except Exception as e:
			messagebox.showerror("popup", "Encoding failed:\n" + str(e))
			return
		messagebox.showinfo("popup", "successfully encoded to\n" + outfile)

	Button(main, text="ENCODE", command=enc).place(relx=0.7, rely=0.8, height=31, width=94)
	Button(main, text="Back", command=show_main).place(relx=0.7, rely=0.85, height=31, width=94)


def decode():
	clear_screen()
	set_background("bg2.jpg")
	state = {'file': None}

	LabelTitle = Label(main, text="DECODE", bg="blue", fg="white", width=20)
	LabelTitle['font'] = fontl
	LabelTitle.place(relx=0.6, rely=0.1)

	secimg = StringVar(value='png')
	Radiobutton(main, text='jpeg', value='jpeg', variable=secimg).place(relx=0.7, rely=0.57)
	Radiobutton(main, text='png', value='png', variable=secimg).place(relx=0.8, rely=0.57)

	result = Label(main, text="", wraplength=380, justify=LEFT)
	result.place(relx=0.6, rely=0.65, width=400)

	def deimg():
		if not state['file']:
			messagebox.showwarning("popup", "Please select an image first")
			return
		try:
			if secimg.get() == "png":
				messag = lsb.reveal(state['file'])
			else:
				messag = aaa.reveal(state['file'])
				if isinstance(messag, bytes):
					messag = messag.decode('utf-8', errors='replace')
		except Exception:
			messag = None
		if not messag:
			messagebox.showwarning("popup", "No hidden message found.\nCheck the selected image type.")
			result['text'] = ""
			return
		result['text'] = "Hidden message: " + messag

	Button(main, text="Openfile", command=lambda: open_image(state)).place(relx=0.7, rely=0.2, height=31, width=94)
	Button(main, text="DECODE", command=deimg).place(relx=0.7, rely=0.8, height=31, width=94)
	Button(main, text="Back", command=show_main).place(relx=0.7, rely=0.85, height=31, width=94)


def show_main():
	clear_screen()
	set_background("bg1.jpg")

	encbutton = Button(main, text='Encode', fg="white", bg="black", width=20, command=encode)
	encbutton['font'] = fontl
	encbutton.place(relx=0.6, rely=0.3)

	decbutton = Button(main, text='Decode', fg="white", bg="black", width=20, command=decode)
	decbutton['font'] = fontl
	decbutton.place(relx=0.6, rely=0.5)

	closebutton = Button(main, text='EXIT', fg="white", bg="red", width=20, command=main.destroy)
	closebutton['font'] = fontl
	closebutton.place(relx=0.6, rely=0.7)


show_main()
main.mainloop()
