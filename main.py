import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog as fd
from tkinterdnd2 import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import StringVar

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

WIDTH = 780
HEIGHT = 520
FILEPATH = ""

image1 = Image


class Photos:
    pass

    def __init__(self, filepath, isSaved, isWaterMarked):

        self.filepath = filepath
        self.isSaved = False
        self.isWaterMarked = False


photo1 = Photos(filepath="none", isSaved=False, isWaterMarked=False)

print(photo1.filepath)

# Drag N Drop Functionality


def get_path(event):
    photo1.isSaved = False

    save_button.state = "disabled"
    photo1.filepath = event.data
    print(photo1.filepath)
    image1 = Image.open(photo1.filepath)
    image1 = image1.resize((580, 480))
    final_img = ImageTk.PhotoImage(image1)

    window.image_label = customtkinter.CTkLabel(
        master=frame_right, image=final_img)
    window.image_label.img = final_img

    window.image_label.grid(column=0, row=1)

    add_watermark_button.state = "normal"

#


window = TkinterDnD.Tk()
window.title("Watermarking Program")
window.config(bg='#1F2022')
window.geometry(f'{WIDTH}x{HEIGHT}')

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

frame_left = customtkinter.CTkFrame(
    master=window, width=180, corner_radius=0,)
frame_left.grid(column=0, row=0, sticky="nswe")

frame_right = customtkinter.CTkFrame(master=window)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


text_variable = StringVar()

frame_right.drop_target_register(DND_FILES)

frame_right.dnd_bind('<<Drop>>', get_path)

# Button Methods


def open_image_button():
    photo1.isSaved = False

    save_button.state = "disabled"
    photo1.filepath = fd.askopenfilename()
    if photo1.filepath:
        print("Turning on add watermark")
        print(photo1.filepath)
        image1 = Image.open(photo1.filepath)
        image1 = image1.resize((580, 480), Image.ANTIALIAS)
        final_img = ImageTk.PhotoImage(image1)

        window.image_label = customtkinter.CTkLabel(master=frame_right)
        window.image_label.configure(image=final_img)
        window.image_label.img = final_img

        window.image_label.grid(column=0, row=1)
        add_watermark_button.state = "normal"


def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)
    if theme_option_optionmenu.get() == "Light":
        print("Light!")
        window.config(bg="#EBEBEC")
    if theme_option_optionmenu.get() == 'Dark':
        window.config(bg="#1F2022")


def save_image():
    final_image = Image.open('images/watermark-temp.jpg')
    filetypes = [('jpg', "*.jpg"), ('png', "*.jpg")]
    filepath = fd.asksaveasfile(
        filetypes=filetypes, defaultextension=filetypes)
    if filepath:
        final_filepath = filepath
        final_image.save(final_filepath)
        photo1.filepath = filepath
        print(photo1.filepath.name)
        image1 = Image.open(photo1.filepath.name)
        image1 = image1.resize((580, 480))
        final_img = ImageTk.PhotoImage(image1)
        window.image_label.configure(image=final_img)
        window.image_label.img = final_img
        window.image_label.grid(column=0, row=1)
        photo1.isSaved = True
        image1.close()
        save_button.state = "disabled"

    else:
        print("Error! No file to save.")


def add_watermark():

    save_button.text_color_disabled = "white"
    save_button.state = "normal"
    dialog = customtkinter.CTkInputDialog(
        text="Type in a watermark:", title="Add Watermark")
    if select_pos_combobox.get() == "Center":
        if photo1.isSaved == True:
            image1 = Image.open(photo1.filepath.name)
            print("Center selected! Drawing watermark now.")
            print("now drawing...")
        else:
            image1 = Image.open(photo1.filepath)
            print("Center selected! Drawing watermark now.")
            print("now drawing...")
        width, height = image1.size
        draw = ImageDraw.Draw(image1)
        text = dialog.get_input()
        font = ImageFont.truetype('arial.ttf', 100)
        textwidth, textheight = draw.textsize(
            text, font)
        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x/2, y/2), text, font=font)
        image1.save('images/watermark-temp.jpg')
        image1 = Image.open('images/watermark-temp.jpg')
        image1 = image1.resize((580, 480))
        final_img = ImageTk.PhotoImage(image1)
        window.image_label.configure(image=final_img)
        window.image_label.img = final_img
        image1.close()
        photo1.isWaterMarked = True

    elif select_pos_combobox.get() == "Top Left":
        if photo1.isSaved == True:
            image1 = Image.open(photo1.filepath.name)
            print("Top Left selected! Drawing watermark now.")
            print("now drawing...")
        else:
            image1 = Image.open(photo1.filepath)
            print("Top Left selected! Drawing watermark now.")
            print("now drawing...")
        width, height = image1.size
        draw = ImageDraw.Draw(image1)
        text = dialog.get_input()
        font = ImageFont.truetype('arial.ttf', 100)
        textwidth, textheight = draw.textsize(
            text, font)
        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((0, 0), text, font=font)
        image1.save('images/watermark-temp.jpg')
        image1 = Image.open('images/watermark-temp.jpg')
        image1 = image1.resize((580, 480))
        final_img = ImageTk.PhotoImage(image1)
        window.image_label.configure(image=final_img)
        window.image_label.img = final_img
        image1.close()
    elif select_pos_combobox.get() == "Bottom Right":
        if photo1.isSaved == True:
            image1 = Image.open(photo1.filepath.name)
            print("Bottom Right selected! Drawing watermark now.")
            print("now drawing...")
        else:
            image1 = Image.open(photo1.filepath)
            print("Bottom Right! selected! Drawing watermark now.")
            print("now drawing...")
        width, height = image1.size
        draw = ImageDraw.Draw(image1)
        text = dialog.get_input()
        font = ImageFont.truetype('arial.ttf', 100)
        textwidth, textheight = draw.textsize(
            text, font)
        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        image1.save('images/watermark-temp.jpg')
        image1 = Image.open('images/watermark-temp.jpg')
        image1 = image1.resize((580, 480))
        final_img = ImageTk.PhotoImage(image1)
        window.image_label.configure(image=final_img)
        window.image_label.img = final_img
        image1.close()

# Buttons


open_button = customtkinter.CTkButton(
    master=frame_left, text="Open Image", command=open_image_button)
open_button.grid(column=0, row=0, padx=10, pady=10)

select_pos_combobox = customtkinter.CTkComboBox(
    master=frame_left, values=["Bottom Right", "Top Left", "Center"])
select_pos_combobox.grid(column=0, row=4, pady=10)
add_watermark_button = customtkinter.CTkButton(
    master=frame_left, text="Add Watermark", command=add_watermark, state="disabled", text_color_disabled="white")
add_watermark_button.grid(column=0, row=1,)
save_button = customtkinter.CTkButton(
    master=frame_left, text="Save Image", command=save_image, state="disabled", text_color_disabled="white")

save_button.grid(column=0, row=2, padx=10, pady=10)
view_image_button = customtkinter.CTkButton(
    master=frame_left, text="View Image", state="disabled", text_color_disabled="white")
view_image_button.grid(column=0, row=3,)
change_appearance_mode_label = customtkinter.CTkLabel(
    master=frame_left, text="Theme")
change_appearance_mode_label.grid(column=0, row=5)
default_theme_option = "Light"
theme_option_optionmenu = customtkinter.CTkOptionMenu(
    master=frame_left, values=["Dark", "Light"], command=change_appearance_mode)
theme_option_optionmenu.grid(column=0, row=9)
theme_option_optionmenu.set_appearance_mode("System")


window.mainloop()
