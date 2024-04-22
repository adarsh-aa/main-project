import tkinter as tk
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
import subprocess

class CameraViewerApp:
    def __init__(self, master):
        self.master = master
        master.title("Camera Surveillance Viewing System")
        master.geometry("800x600")  # Set window size

        # Set background color
        master.configure(bg="#f0f0f0")

        # Create logout button
        self.logout_button = tk.Button(master, text="Logout", command=self.logout, bg="#ff3333", fg="white")
        self.logout_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        # Create left frame for navigation
        self.left_frame = tk.Frame(master, borderwidth=2, relief=tk.SUNKEN, bg="#d9d9d9")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Hyperlink labels for navigation
        self.home_label = tk.Label(self.left_frame, text="Home", fg="blue", cursor="hand2", bg="#d9d9d9")
        self.home_label.pack(pady=10, padx=30)
        self.home_label.bind("<Button-1>", self.go_home)
        
        self.camera_label = tk.Label(self.left_frame, text="Cameras", fg="blue", cursor="hand2", bg="#d9d9d9")
        self.camera_label.pack(pady=10, padx=30)
        self.camera_label.bind("<Button-1>", self.go_cameras)

        # Main frame for camera sessions
        self.main_frame = tk.Frame(master, borderwidth=2, relief=tk.SUNKEN, bg="#ffffff")
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a list to store camera sessions
        self.camera_sessions = [
            {"name": "Camera 1", "video_path": "C:\\Users\\user\\python files\\front\\afriq1.MP4"},
            
            # Add more cameras with their respective video paths
        ]

        # Display camera sessions
        self.display_camera_sessions()

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.destroy()

    def go_home(self, event):
        # Placeholder function for navigating to home
        print("Going to home")

    def go_cameras(self, event):
        # Placeholder function for navigating to cameras
        print("Going to cameras")
        subprocess.Popen(['python', 'C:\\Users\\user\\python files\\front\\inci1.py'])

    def display_camera_sessions(self):
        # Clear any previous camera sessions displayed
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Display each camera session
        for camera_index, camera in enumerate(self.camera_sessions, start=1):
            camera_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief=tk.RIDGE)
            camera_frame.pack(fill=tk.X, padx=5, pady=5)

            camera_name_label = tk.Label(camera_frame, text=camera["name"], bg="#ffffff", fg="black")
            camera_name_label.pack(side=tk.LEFT, padx=10, pady=5)

            # Create a video player for each camera session
            video_player = tk.Label(camera_frame, bg="black")
            video_player.pack(side=tk.RIGHT, padx=10, pady=5)

            # Open video file for the camera
            video_path = camera.get("video_path")  # Provide the path to your video file
            if video_path:
                cap = cv2.VideoCapture(video_path)
                if cap.isOpened():
                    # Function to update video player label with frames
                    def update_video():
                        ret, frame = cap.read()
                        if ret:
                            # Resize the frame to desired dimensions (e.g., 320x240)
                            frame = cv2.resize(frame, (320, 240))
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                            video_player.config(image=photo)
                            video_player.image = photo
                            video_player.after(10, update_video)  # Update video player after 10ms
                        else:
                            cap.release()  # Release video capture when playback ends

                    # Start updating video player
                    update_video()
                else:
                    print(f"Unable to open video file: {video_path}")
            else:
                print("No video path provided for camera")

        # After displaying all cameras, update the GUI
        self.main_frame.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraViewerApp(root)
    root.mainloop()
