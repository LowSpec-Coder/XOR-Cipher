import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


window = tk.Tk()

window.title("XOR cypher")
window.minsize(300,380)

def calculate():
     A = (int(base.get())**int(alicek.get())) % int(prime.get())
     channel1.configure(text = "\n Alice Sends Over public channel: "+ str(A))
     B = (int(base.get()) ** int(bobk.get())) % int(prime.get())
     channel2.configure(text="\n Bob Sends Over Public channel: " + str(B))
     private_cal.configure(text = "Calculated Shared Secret")
     aliceSharedSecret = (B ** int(alicek.get())) % int(prime.get())
     aliceSS.configure(text = "Alice Shared Key: " + str(aliceSharedSecret))
     bobSharedSecret = (A**int(bobk.get())) % int(prime.get())
     bobSS.configure(text = "Bob Shared Key: " + str(bobSharedSecret))
     #this will encrypt the message
     fo = open("plain.txt","r+")
     fo_ciph = open("cipher.txt", "r+")
     na_of_itr = fo.read()
     no_of_itr = len(na_of_itr)
     msg = na_of_itr
     output_str = ""
     s_key = str(bobSharedSecret) #can also use alice, just the same value
     for i in range(no_of_itr):
        current = msg[i]
        current_key = s_key[i%len(s_key)]
        output_str += chr(ord(current) ^ ord(current_key))

     label_encypt_notif.configure(text= 'Message Encrypted Successfully')
     fo_ciph.write(output_str)
     fo.close()
     fo_ciph.close()







#Labels
public_var = ttk.Label(window, text = "Publicly Shared Variables")
public_var.place(x = 0, y = 0)
shared_prime = ttk.Label(window, text = "shared Prime: ")
shared_prime.place(x = 0, y = 20)
shared_base = ttk.Label(window, text = "shared base: ")
shared_base.place(x = 0, y = 40)
alicekey = ttk.Label(window, text = "Alice key: ")
alicekey.place(x = 0, y = 60)
bobkey = ttk.Label(window, text = "Bob key: ")
bobkey.place(x = 0, y = 80)
label_encypt_notif = ttk.Label(window, text = "")
label_encypt_notif.place(x = 50, y = 250)

channel1 = ttk.Label(window, text = "")
channel1.place(x = 0, y = 130)
channel2 = ttk.Label(window, text = "")
channel2.place(x = 0, y = 160)
private_cal = ttk.Label(window, text = "")
private_cal.place(x = 50, y = 190)
aliceSS = ttk.Label(window, text = "")
aliceSS.place(x = 0, y = 210)
bobSS = ttk.Label(window, text = "")
bobSS.place(x = 0, y = 230)


#Textbox
prime = tk.StringVar()
txtprime = ttk.Entry(window, width = 10, textvariable = prime)
txtprime.place(x = 80, y = 20)
base = tk.StringVar()
txtbase = ttk.Entry(window, width = 10, textvariable = base)
txtbase.place(x = 80, y = 40)
alicek = tk.StringVar()
alicekk = ttk.Entry(window, width = 10, textvariable = alicek)
alicekk.place(x = 80, y = 60)
bobk = tk.StringVar()
bobkk = ttk.Entry(window, width = 10, textvariable = bobk)
bobkk.place(x = 80, y = 80)

#Button
button = ttk.Button(window, text = "calculate", command = calculate)
button.place(x= 0, y = 120)


window.mainloop()