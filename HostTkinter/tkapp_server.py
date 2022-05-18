from tkinter import messagebox, ttk, Text, filedialog
import tkinter as tk
import os 
import time
import datetime
import socket
import argparse

M_SIZE = 1024
class Application(tk.Frame):
    def __init__(self, host, port, master):
        super().__init__(master)

        self.master.geometry("1280x768")
        self.master.title("Tkinter with Video Streaming and Capture")
        self.locaddr = (host, port) 
        self.create_socket()
        self.create_widgets()

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)

    def create_widgets(self):
        frame = ttk.Frame(self.master, padding=10)
        frame.grid()
        refer_button = ttk.Button(frame, text=u'出力ボタン', command=self.server) 
        refer_button.grid(row=3, column=1) 
        self.log = Text(self.master, state='disabled',borderwidth=5, width=70, height=30, wrap='none', padx=10,pady=10) 
        ys = ttk.Scrollbar(self.master, orient = 'vertical', command = self.log.yview) 
        
        self.log['yscrollcommand'] = ys.set 
        self.log.grid(row=4, column=0) 
        ys.grid(column = 1, row = 4, sticky = 'ns')
    
    def writeToLog(self,msg): 
        self.log['state'] = 'normal' 
        self.log.insert('end', str(msg)+'\n') 
        self.log.update()
        self.log['state'] = 'disabled'

    def server(self):
        while True:
            try:
                print('Waiting message')
                message, cli_addr = self.sock.recvfrom(M_SIZE)
                message = message.decode(encoding='utf-8')
                self.writeToLog(message)
                print(f'Received message is [{message}]')
                time.sleep(1)
                print('Send response to Client')
                self.sock.sendto('Success to receive message'.encode(encoding='utf-8'), cli_addr)
                
            except KeyboardInterrupt:
                self.sock.close()
                break

    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--port", default=8890, help="port for UDP")
    parser.add_argument("--host", default="192.168.10.107", help="Main PC host")
    args = parser.parse_args()

    root = tk.Tk()
    app = Application(args.host, args.port, root)#Inherit
    app.mainloop()

