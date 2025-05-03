import os
from dataclasses import dataclass
from typing import Optional
from flask import send_from_directory, abort
from flask import Response
from werkzeug.datastructures import FileStorage
from app.config import Config
from .utils import is_file_exists


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
        return DeleteResult(
            success=False, filename=filename, error=f"⚠️ File {filename} Not Found."
        )
    except Exception as e:
        return DeleteResult(success=False, filename=filename, error=str(e))
