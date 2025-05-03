import os
from app.config import Config


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


def ensure_upload_folder_exists():
    """确保上传文件夹存在，不存在则创建"""
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


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


def get_upload_folder() -> str:
    return os.path.abspath(Config.UPLOAD_FOLDER)


def get_files() -> list[str]:
    """返回上传的文件列表，过滤掉隐藏文件。

    Returns:
        list[str]: 所有非隐藏文件的文件名列表 (不含以点开头的文件)。
    """
    return [f for f in os.listdir(Config.UPLOAD_FOLDER) if not f.startswith(".")]
