import os, time
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import send_from_directory, abort, Response
from typing import Tuple, Union
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS


def allowed_file(filename: str) -> bool:
    """检查文件类型是否符合允许的格式"""
    # 检查文件名是否包含点："." in filename
    # 提取文件扩展名并转换为小写：filename.rsplit(".", 1)[1].lower()
    # 检查扩展名是否在允许的文件类型列表中：filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def is_file_exists(filename: str) -> bool:
    """检查文件是否已经存在"""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return os.path.exists(file_path)


def save_file(file: FileStorage) -> Tuple[Union[None, str], Union[str, None]]:
    """保存上传的文件"""
    if file:  # 如果文件对象存在（即用户上传了文件）
        filename = secure_filename(file.filename)  # 处理文件名
        file_path = os.path.join(UPLOAD_FOLDER, filename)  # 构造文件保存路径

        if is_file_exists(filename):
            return None, "exists"  # 文件已存在，返回 None 和错误类型 "exists"

        file.save(file_path)  # 将文件保存到指定路径
        return filename, None  # 文件保存成功，返回文件名和 None

    return None, "no_file"  # 没有上传文件，返回 None 和错误类型 "no_file"


def get_files() -> list[str]:
    """返回上传的文件列表，过滤掉隐藏文件"""
    return [f for f in os.listdir(UPLOAD_FOLDER) if not f.startswith(".")]


def download_file(filename: str) -> Response:
    """提供文件下载"""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        abort(404, description=f"File '{filename}' not found")  # 返回 404 错误
    return send_from_directory(UPLOAD_FOLDER, filename)  # 从指定目录中发送文件


def get_file_size(filename: str) -> str:
    """获取文件大小"""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return "File not found"

    size = os.path.getsize(file_path)
    if size < 1024:
        return f"{size} bytes"
    elif size < 1048576:  # 1024 * 1024
        return f"{size / 1024:.2f} KB"
    elif size < 1073741824:  # 1024 * 1024 * 1024
        return f"{size / 1048576:.2f} MB"
    else:
        return f"{size / 1073741824:.2f} GB"


def delete_file(filename: str) -> bool:
    """删除文件"""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)  # 删除文件
            return True  # 删除成功，返回 True
        return False  # 文件不存在，返回 False
    except Exception as e:
        return False  # 遇到异常，返回 False

