import tkinter as tk
import psutil

def get_running_processes():
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(f"PID: {process.info['pid']} - Name: {process.info['name']} - CPU %: {process.info['cpu_percent']} - Memory %: {process.info['memory_percent']}")
    return processes

def update_processes():
    process_list.delete(0, tk.END)
    for process in get_running_processes():
        process_list.insert(tk.END, process)
    root.after(1000, update_processes)

root = tk.Tk()
root.title("Process Monitor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Running Processes:")
label.pack()

process_list = tk.Listbox(frame, width=70, height=15)
process_list.pack()

update_button = tk.Button(frame, text="Update", command=update_processes)
update_button.pack()

quit_button = tk.Button(frame, text="Quit", command=root.destroy)
quit_button.pack()

update_processes()

root.mainloop()
