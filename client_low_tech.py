"""Script for Tkinter GUI chat client."""
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pygame
import time


def receive():
    bipfile = '/home/hcourtei/OtherPythonFiles/Tchat/clochette.wav'
    pygame.mixer.init()
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            v = vol.get()
            pygame.mixer.music.set_volume(float(v)/10) # Met le volume à 0.5 (moitié)
            pygame.mixer.music.load(bipfile)
            pygame.mixer.music.play()
            time.sleep(1)

        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


print("Entering listic net")
entry_field.bind("<Return>", send)
entry_field.pack(fill=tkinter.X)
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
top.resizable(True, True)
top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = 'localhost'  # input('Enter host: ')
PORT = 1503 # input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()

