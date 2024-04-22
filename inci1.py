import tkinter as tk
from tkinter import ttk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera Details")
        self.root.configure(bg="#f0f0f0")

        # Creating the header label
        header_label = tk.Label(root, text="Camera", font=('Helvetica', 18, 'bold'), bg="#f0f0f0")
        header_label.pack(pady=10)

        # Creating the table to display camera details
        self.camera_tree = ttk.Treeview(root, columns=('IP Address', 'Stream Session'), show="headings", selectmode='browse')
        self.camera_tree.heading('IP Address', text='IP Address')
        self.camera_tree.heading('Stream Session', text='Stream Session')
        self.camera_tree.pack(padx=20, pady=(0, 10), ipadx=10, ipady=10)

        # Creating section to enter IP address and stream session
        entry_frame = tk.Frame(root, bg="#f0f0f0")
        entry_frame.pack(pady=(10, 5))

        ip_label = tk.Label(entry_frame, text="Enter IP Address:", bg="#f0f0f0", font=('Helvetica', 10))
        ip_label.grid(row=0, column=0, padx=(20, 5), pady=5, sticky="w")
        self.ip_entry = tk.Entry(entry_frame)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        stream_label = tk.Label(entry_frame, text="Enter Stream Session:", bg="#f0f0f0", font=('Helvetica', 10))
        stream_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="w")
        self.stream_entry = tk.Entry(entry_frame)
        self.stream_entry.grid(row=1, column=1, padx=5, pady=5)

        # Creating Add or Edit button
        self.add_edit_button = tk.Button(root, text="Add / Edit", command=self.add_or_edit_camera, bg="#4CAF50", fg="white", font=('Helvetica', 10, 'bold'), relief='raised')
        self.add_edit_button.pack(pady=(5, 10))

        # Creating the table at the bottom
        bottom_frame = tk.Frame(root, bg="#f0f0f0")
        bottom_frame.pack(pady=10)

        bottom_table_label = tk.Label(bottom_frame, text="Camera Details Table", font=('Helvetica', 12, 'bold'), bg="#f0f0f0")
        bottom_table_label.pack()

        # Creating the table to display camera details at the bottom
        self.bottom_table = ttk.Treeview(bottom_frame, columns=('Serial No.', 'Location', 'Snapshot', 'Recording'), show="headings", selectmode='browse')
        self.bottom_table.heading('Serial No.', text='Serial No.')
        self.bottom_table.heading('Location', text='Location')
        self.bottom_table.heading('Snapshot', text='Snapshot')
        self.bottom_table.heading('Recording', text='Recording')
        self.bottom_table.pack(padx=20, pady=10, ipadx=10, ipady=10)

    def add_or_edit_camera(self):
        ip_address = self.ip_entry.get()
        stream_session = self.stream_entry.get()

        # Retrieve selected item from the tree
        selected_item = self.camera_tree.selection()
        if selected_item:
            self.camera_tree.item(selected_item, values=(ip_address, stream_session))
        else:
            self.camera_tree.insert('', 'end', values=(ip_address, stream_session))

        # Clearing the entry fields after adding/editing
        self.ip_entry.delete(0, 'end')
        self.stream_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
