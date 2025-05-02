import os
from flask import send_from_directory, abort
from .config import Config


def allowed_file(filename: str) -> bool:
    """检查文件类型是否符合允许的格式"""
    # 检查文件名是否包含点："." in filename
    # 提取文件扩展名并转换为小写：filename.rsplit(".", 1)[1].lower()
    # 检查扩展名是否在允许的文件类型列表中：filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )


def ensure_upload_folder_exists():
    """确保上传文件夹存在，不存在则创建"""
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


def is_file_exists(filename: str) -> bool:
    """检查文件是否已经存在"""
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    return os.path.exists(file_path)


def save_file(file):
    """保存上传的文件"""

    # 处理文件名
    # filename = secure_filename(file.filename)
    filename = file.filename
    # 构造文件保存路径
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)

    if is_file_exists(filename):
        return {"success": False, "error": "exists", "filename": filename}

    # 将文件保存到指定路径
    file.save(file_path)
    return {"success": True, "filename": filename}


def get_files() -> list[str]:
    """返回上传的文件列表，过滤掉隐藏文件"""
    return [f for f in os.listdir(Config.UPLOAD_FOLDER) if not f.startswith(".")]


def download_file(filename: str):
    """提供文件下载"""
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    print()
    print(f"正在下载{file_path}, {Config.UPLOAD_FOLDER}")
    if not os.path.exists(file_path):
        abort(404, description=f"File '{filename}' not found")  # 返回 404 错误
    return send_from_directory(Config.UPLOAD_FOLDER, filename)  # 从指定目录中发送文件


def get_file_size(filename: str) -> str:
    """获取文件大小"""
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
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
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)  # 删除文件
            return True  # 删除成功，返回 True
        return False  # 文件不存在，返回 False
    except Exception as e:
        return False  # 遇到异常，返回 False
