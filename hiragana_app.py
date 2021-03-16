from tkinter import *
from PIL import ImageTk, Image
from random import randint, random


root = Tk()
root.title('Hiragana App!')
root.iconbitmap(r'C:\Users\Nicolas\Pictures/icon.ico')
root.geometry("500x500")



def random_hiragana(hiragana_answer, hiragana_key, hiragana_path):
    # Creating a list
    #global vowels_list
    #vowels_list = ['a', 'i', 'u', 'e','o']
    hiragana_list2 = {"vowels_list" : ['a','i','e','o','u'],
                      "ka_list" : ['ka','ki','ku','ke','ko']}

    hiragana_list = hiragana_list2[hiragana_key]


    if hiragana_answer in hiragana_list:
        hiragana_list.remove(hiragana_answer)

    global rando_hiragana
    global respuesta
    rando_hiragana = randint(0, len(hiragana_list) - 1)
    hiragana = hiragana_path + hiragana_list[rando_hiragana] + ".png"
    respuesta = hiragana_list[rando_hiragana]

    global hiragana_image
    hiragana_image = ImageTk.PhotoImage(Image.open(hiragana))
    show_hiragana.config(image=hiragana_image, bg="white")


#never shows at the begining the u for random
def hiragana_ans(nico_list, nico_path):
    hiragana_answer = hiragana_input.get().lower()
    hiragana_label.config(text=hiragana_input.get().lower())

    #determine if everything is correct

    if hiragana_answer == respuesta:

        response = "Correct! " + respuesta.title()
    else:
        response = "Incorrect! " + respuesta.title()

    hiragana_label.config(text=response)

    hiragana_input.delete(0,'end')

    random_hiragana(hiragana_answer,nico_list, nico_path)

def hiragana(initial_hira, hira_list, hira_path):
    hiding()
    global show_hiragana
    global hiragana_label
    hiragana_frame.pack(fill=BOTH, expand=1)
    show_hiragana = Label(hiragana_frame)
    show_hiragana.pack(pady=15)
    random_hiragana(initial_hira, hira_list, hira_path)

    # Creating an entry box
    global hiragana_input
    hiragana_input = Entry(hiragana_frame, font=("Helvetica", 18), bd="2")
    hiragana_input.pack(pady=10)


    # Answer button
    hiragana_answerbt = Button(hiragana_frame, text="Submit Answer", command=lambda: hiragana_ans(hira_list, hira_path))
    hiragana_answerbt.pack(pady=5)

    # Creating labels

    hiragana_label = Label(hiragana_frame, text="", font=("Helvetica", 18), bg="white")
    hiragana_label.pack(pady=15)

#Hiding all frames
def hiding():
    for widget in hiragana_frame.winfo_children():
        widget.destroy()


    hiragana_frame.pack_forget()
    ka_frame.pack_forget()

#Create the menu
my_menu = Menu(root)
root.config(menu = my_menu)

#menu items

hiragana_menu = Menu(my_menu)
my_menu.add_cascade(label = "All Symbols", menu = hiragana_menu)
vowPath = r"C:/gui/hiragana_v/"
kaPath = r"C:/gui/hiragana_ka/"
hiragana_menu.add_command(label="Vowels", command = lambda: hiragana('u', "vowels_list",vowPath))
hiragana_menu.add_command(label="Ka Syllabary", command = lambda: hiragana('ku', "ka_list",kaPath))

hiragana_menu.add_separator()
hiragana_menu.add_command(label="Exit", command=root.quit)

#Creating frames

hiragana_frame = Frame(root, width = 500, height = 500, bg="white")
ka_frame = Frame(root, width = 500, height = 500, bg = "white")




root.mainloop()