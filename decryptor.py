#John Paul R. Asis BSCS-3A
#XOR Cypher

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


window = tk.Tk()

window.title("XOR Decryptor")
window.minsize(250,200)


def browseFiles(): 
   
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
    

    myfile = open(filename,'r')
    encrypt_text = myfile.read()
    myfile.close()
    fw = open("plain2.txt", "r+")
    no_of_itr = len(encrypt_text)
    na_of_itr = encrypt_text
    output_str = ""
    s_key = key.get()
    for i in range(no_of_itr):
        current = na_of_itr[i]
        current_key = s_key[i%len(s_key)]
        output_str += chr(ord(current) ^ ord(current_key))

    label_decrypt_notif.configure(text= 'Decrypted Successfully')
    fw.write(output_str)
    fw.close()




#Labels
lblkey = ttk.Label(window, text = "Enter Key: ")
lblkey.place(x = 0, y = 20)
label_decrypt_notif = ttk.Label(window, text="")
label_decrypt_notif.place(x = 50, y = 70)

#TextBox
key = tk.StringVar()
txtkey = ttk.Entry(window, width = 20, textvariable = key)
txtkey.place(x = 60, y = 20)

#Buttons
btndecrypt = ttk.Button(window, text = "Browse files and Decrypt", command = browseFiles)
btndecrypt.place(x = 0, y = 50)
window.mainloop()