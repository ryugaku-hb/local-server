# os：用于处理文件和目录的操作，如文件路径的拼接（os.path.join）和列出目录中的文件（os.listdir）。
import os  # 导入 os 模块，用于文件和目录操作
# Flask 中的一个函数，用于从指定目录返回文件，可以实现文件下载的功能。
from flask import send_from_directory  # 导入 Flask 的 send_from_directory 函数，用于从指定目录返回文件
# UPLOAD_FOLDER：从配置文件（config.py）导入上传文件保存的目录路径。
from config import UPLOAD_FOLDER  # 从 config 模块导入 UPLOAD_FOLDER 配置项，指定文件上传的目录


# 用于保存上传的文件。
# 步骤：
# 1. 检查是否存在文件对象（if file）。
# 2. 如果文件存在，构造保存路径（file_path）并将文件保存到该路径。
# 3. 返回文件名（file.filename），可以在文件列表中展示或用于其他用途。
# 4. 如果没有上传文件，则返回 None。
def save_file(file):
    """保存上传的文件"""
    if file:  # 如果文件对象存在（即用户上传了文件）
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # 构造文件保存路径，将上传文件的文件名与上传目录结合
        file.save(file_path)  # 将文件保存到指定路径
        return file.filename  # 返回文件名，供后续操作使用（例如文件列表中展示）
    return None  # 如果没有上传文件，返回 None


# 获取指定目录下的所有文件和文件夹。
# 使用 os.listdir(UPLOAD_FOLDER) 列出上传目录中的所有文件。
# 返回的是文件和文件夹名称的列表。
def get_files():
    """返回上传的文件列表"""
    return os.listdir(UPLOAD_FOLDER)  # 使用 os.listdir 获取上传目录下的所有文件和目录列表


# 用于提供文件下载功能。
# 使用 send_from_directory 函数从上传目录中返回指定文件，并将其发送给客户端。
# 这个函数会生成合适的 HTTP 响应，使得浏览器可以触发文件下载。
def download_file(filename):
    """提供文件下载"""
    return send_from_directory(UPLOAD_FOLDER, filename)  # 使用 Flask 的 send_from_directory 函数提供文件下载，指定文件路径和文件名
