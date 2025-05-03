import os
from dataclasses import dataclass
from typing import Optional
from flask import send_from_directory, abort
from flask import Response
from werkzeug.datastructures import FileStorage
from .config import Config


def allowed_file(filename: str) -> bool:
    """检查文件类型是否符合允许的格式。

    步骤说明:
    1. 检查文件名是否包含点: "." in filename
    2. 提取文件扩展名，并转换为小写: filename.rsplit(".", 1)[1].lower()
    3. 检查扩展名是否在允许的文件类型列表中: filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    Args:
        filename (str): 上传的文件名，例如 "example.jpg"。

    Returns:
        bool: 如果扩展名合法，返回 True；否则返回 False。
    """
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )


def ensure_upload_folder_exists():
    """确保上传文件夹存在，不存在则创建"""
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


def is_file_exists(filename: str) -> bool:
    """检查上传目录中是否已存在指定文件。

    步骤说明:
    1. 将文件名与上传目录拼接成完整路径
    2. 使用 os.path.exists 判断该路径下是否存在文件

    Args:
        filename (str): 要检查的文件名，例如 "data.pdf"。

    Returns:
        bool: 若文件已存在，返回 True；否则返回 False。
    """
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    return os.path.exists(file_path)


# 定义保存结果的数据结构
@dataclass
class SaveResult:
    """表示文件保存操作的结果。

    Attributes:
        success (bool): 是否成功保存文件。
        filename (str): 被尝试保存的文件名。
        error (Optional[str]): 保存失败时的错误信息；成功时为 None。
    """

    success: bool
    filename: str
    error: Optional[str] = None


def save_file(file: FileStorage) -> SaveResult:
    """保存上传的文件。

    - 如果文件已存在，则不保存，并返回错误信息。
    - 如果文件不存在，则保存并返回成功信息。

    Args:
        file (FileStorage): Flask 接收到的上传文件对象，通常来自 request.files["file"]。

    Returns:
        SaveResult: 保存结果对象。
    """

    filename = file.filename
    # 构造文件保存路径
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)

    if is_file_exists(filename):
        return SaveResult(success=False, error="exists", filename=filename)

    # 将文件保存到指定路径
    file.save(file_path)
    return SaveResult(success=True, filename=filename)


def get_files() -> list[str]:
    """返回上传的文件列表，过滤掉隐藏文件。

    Returns:
        list[str]: 所有非隐藏文件的文件名列表 (不含以点开头的文件)。
    """
    return [f for f in os.listdir(Config.UPLOAD_FOLDER) if not f.startswith(".")]


def download_file(filename: str) -> Response:
    """提供文件下载。

    Args:
        filename (str): 要下载的文件名。

    Returns:
        Response: Flask 的响应对象，包含待下载的文件内容。
    """
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    print(f"正在下载 {file_path}，上传目录为: {Config.UPLOAD_FOLDER}。")

    if not os.path.exists(file_path):
        # 返回 404 错误页面
        abort(404, description=f"⚠️ File '{filename}' Not Found.")

    # send_from_directory: 安全地从指定目录中发送文件
    return send_from_directory(os.path.abspath(Config.UPLOAD_FOLDER), filename)


def get_file_size(filename: str) -> str:
    """获取指定文件的大小，并以可读格式返回 (如 KB、MB)。

    Args:
        filename (str): 要查询的文件名。

    Returns:
        str: 文件大小的字符串表示；如果文件不存在，则返回 "File not found"。
    """
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


@dataclass
class DeleteResult:
    """表示文件删除操作的结果。

    Attributes:
        success (bool): 是否成功删除文件。
        filename (str): 被尝试删除的文件名。
        error (Optional[str]): 删除失败时的错误信息，成功时为 None。
    """

    success: bool
    filename: str
    error: Optional[str] = None


def delete_file(filename: str) -> DeleteResult:
    """删除上传目录中的指定文件。

    Args:
        filename (str): 要删除的文件名。

    Returns:
        DeleteResult: 删除操作的结果，包含成功与否、错误信息和文件名。
    """

    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return DeleteResult(success=True, filename=filename)
        return DeleteResult(success=False, filename=filename, error=f"⚠️ File {filename} Not Found.")
    except Exception as e:
        return DeleteResult(success=False, filename=filename, error=str(e))
