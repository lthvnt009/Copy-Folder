import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import winreg

# Khởi tạo đường dẫn
source_folder = ""
destination_folder = ""

# Thông tin để lưu vào Registry
REG_PATH = r"Software\YourAppName\Settings"
KEY_NAME = "LastSourcePath"

def load_last_path_from_registry():
    """Tải đường dẫn cuối cùng từ Windows Registry"""
    global source_folder
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        path, _ = winreg.QueryValueEx(reg_key, KEY_NAME)
        winreg.CloseKey(reg_key)
        
        if os.path.isdir(path):
            source_folder = path
            source_path_label.configure(text=source_folder)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Không thể tải đường dẫn từ Registry: {e}")

def save_path_to_registry(path):
    """Lưu đường dẫn vào Windows Registry"""
    try:
        reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        winreg.SetValueEx(reg_key, KEY_NAME, 0, winreg.REG_SZ, path)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"Không thể lưu đường dẫn vào Registry: {e}")

def select_source_folder():
    """Hàm chọn thư mục nguồn"""
    global source_folder
    new_path = filedialog.askdirectory(title="Chọn thư mục nguồn")
    if new_path:
        source_folder = new_path
        source_path_label.configure(text=source_folder)
        save_path_to_registry(source_folder)

def select_destination_folder():
    """Hàm chọn thư mục đích"""
    global destination_folder
    destination_folder = filedialog.askdirectory(title="Chọn nơi lưu")
    if destination_folder:
        destination_path_label.configure(text=destination_folder)

def copy_folder_structure():
    """Hàm sao chép cấu trúc thư mục"""
    global source_folder, destination_folder

    if not source_folder or not destination_folder:
        messagebox.showwarning("Lỗi", "Vui lòng chọn cả thư mục nguồn và nơi lưu!")
        return

    try:
        for dirpath, dirnames, filenames in os.walk(source_folder):
            relative_path = os.path.relpath(dirpath, source_folder)
            destination_path = os.path.join(destination_folder, relative_path)
            
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
                print(f"Đã tạo thư mục: {destination_path}")

        messagebox.showinfo("Hoàn thành", "Đã hoàn thành")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra trong quá trình sao chép: {e}")

# Thiết lập chế độ giao diện
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Sao chép cấu trúc thư mục")
root.geometry("400x280")
root.resizable(False, False)

# Thêm icon cho chương trình
try:
    # Mở file ảnh và thay đổi kích thước cho phù hợp
    icon_image = Image.open("folder.ico")
    # Tạo PhotoImage từ ảnh đã mở
    icon_photo = ImageTk.PhotoImage(icon_image)
    # Đặt icon cho cửa sổ chính
    root.iconphoto(False, icon_photo)
except Exception as e:
    print(f"Không thể tải icon: {e}")
    pass

# Frame chính để chứa các thành phần và loại bỏ màu nền
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Nút chọn thư mục nguồn và nhãn đường dẫn
source_button = ctk.CTkButton(main_frame, text="Chọn thư mục nguồn", command=select_source_folder,
                              fg_color="#FFC107", text_color="black", hover_color="#FFA000",
                              corner_radius=10, font=("Segoe UI", 12, "bold"), height=40)
source_button.pack(fill=tk.X, pady=(5, 2))
source_path_label = ctk.CTkLabel(main_frame, text="", wraplength=350, font=("Segoe UI", 11), text_color="#5e5e5e")
source_path_label.pack(fill=tk.X, pady=(0, 10))

# Nút chọn nơi lưu và nhãn đường dẫn
destination_button = ctk.CTkButton(main_frame, text="Chọn nơi lưu", command=select_destination_folder,
                                  fg_color="#FFC107", text_color="black", hover_color="#FFA000",
                                  corner_radius=10, font=("Segoe UI", 12, "bold"), height=40)
destination_button.pack(fill=tk.X, pady=(10, 2))
destination_path_label = ctk.CTkLabel(main_frame, text="", wraplength=350, font=("Segoe UI", 11), text_color="#5e5e5e")
destination_path_label.pack(fill=tk.X, pady=(0, 10))

# Nút sao chép
copy_button = ctk.CTkButton(main_frame, text="Sao chép!", command=copy_folder_structure,
                            fg_color="#FFC107", text_color="black", hover_color="#FFA000",
                            corner_radius=10, font=("Segoe UI", 12, "bold"), height=40)
copy_button.pack(fill=tk.X, pady=(15, 5))

# Tải đường dẫn đã lưu khi khởi chạy chương trình
load_last_path_from_registry()

# Chạy vòng lặp chính
root.mainloop()