import tkinter as tk
import psutil

def get_tcp_connections():
    connections = []
    for conn in psutil.net_connections(kind='tcp'):
        if conn.laddr and conn.raddr:
            connections.append(f"{conn.laddr[0]}:{conn.laddr[1]} -> {conn.raddr[0]}:{conn.raddr[1]} - {conn.status}")
    return connections

def update_connections():
    connection_list.delete(0, tk.END)
    for connection in get_tcp_connections():
        connection_list.insert(tk.END, connection)
    root.after(1000, update_connections)

root = tk.Tk()
root.title("TCP Connection Monitor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="TCP Connections:")
label.pack()

connection_list = tk.Listbox(frame, width=50, height=15)
connection_list.pack()

update_button = tk.Button(frame, text="Update", command=update_connections)
update_button.pack()

quit_button = tk.Button(frame, text="Quit", command=root.destroy)
quit_button.pack()

update_connections()

root.mainloop()
