# os：用于处理文件和目录的操作，如文件路径的拼接（os.path.join）和列出目录中的文件（os.listdir）。
import os  # 导入 os 模块，用于文件和目录操作
# Flask 中的一个函数，用于从指定目录返回文件，可以实现文件下载的功能。
from flask import send_from_directory  # 导入 Flask 的 send_from_directory 函数，用于从指定目录返回文件
# UPLOAD_FOLDER：从配置文件（config.py）导入上传文件保存的目录路径。
from config import UPLOAD_FOLDER  # 从 config 模块导入 UPLOAD_FOLDER 配置项，指定文件上传的目录


def save_file(file):
    """保存上传的文件"""
    if file:  # 如果文件对象存在（即用户上传了文件）
        # 如果文件存在，构造保存路径（file_path）并将文件保存到该路径。
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # 构造文件保存路径，将上传文件的文件名与上传目录结合
        # 返回文件名（file.filename），可以在文件列表中展示或用于其他用途。
        file.save(file_path)  # 将文件保存到指定路径
        return file.filename  # 返回文件名，供后续操作使用（例如文件列表中展示）
    return None  # 如果没有上传文件，返回 None


def get_files():
    """返回上传的文件列表"""
    # 使用 os.listdir 获取上传目录下的所有文件和目录列表
    return os.listdir(UPLOAD_FOLDER)


def download_file(filename):
    """提供文件下载"""
    # 使用 Flask 的 send_from_directory 函数提供文件下载，指定文件路径和文件名
    return send_from_directory(UPLOAD_FOLDER, filename)


def get_file_size(filename):
    """获取文件大小的函数"""
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)  # 根据你的文件存储路径调整
        size = os.path.getsize(file_path)
        if size < 1024:
            return f"{size} bytes"
        elif size < 1048576:
            return f"{size / 1024:.2f} KB"
        elif size < 1073741824:
            return f"{size / 1048576:.2f} MB"
        else:
            return f"{size / 1073741824:.2f} GB"
    except Exception as e:
        return str(e)  # 如果文件不存在或路径错误，返回错误信息


def delete_file(filename):
    """删除文件"""
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)  # 构造文件路径
        if os.path.exists(file_path):  # 判断文件是否存在
            os.remove(file_path)  # 删除文件
            return True  # 返回 True 表示删除成功
        return False  # 如果文件不存在，返回 False
    except Exception as e:
        return str(e)  # 如果出现错误，返回错误信息
