import os  # 导入 os 模块，用于文件和目录操作
from flask import send_from_directory  # 导入 Flask 的 send_from_directory 函数，用于从指定目录返回文件
from config import UPLOAD_FOLDER  # 从 config 模块导入 UPLOAD_FOLDER 配置项，指定文件上传的目录


def save_file(file):
    """
    保存上传的文件

    :param file: 上传的文件对象
    :type file: werkzeug.datastructures.FileStorage
    :return: 上传文件的文件名，如果没有文件则返回 None
    :rtype: str | None
    """
    if file:  # 如果文件对象存在（即用户上传了文件）
        # 如果文件存在，构造保存路径（file_path）并将文件保存到该路径。
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)  # 将文件保存到指定路径
        return file.filename
    return None  # 如果没有上传文件，返回 None


def get_files():
    """
    返回上传的文件列表

    :return: 上传目录中所有文件和目录的列表
    :rtype: list[str]
    """
    return os.listdir(UPLOAD_FOLDER)


def download_file(filename):
    """
    提供文件下载

    :param filename: 要下载的文件的文件名
    :type filename: str
    :return: 返回指定文件的响应，供客户端下载
    :rtype: flask.Response
    """
    # 使用 Flask 的 send_from_directory 函数提供文件下载，指定文件路径和文件名
    return send_from_directory(UPLOAD_FOLDER, filename)


def get_file_size(filename):
    """
    获取文件大小的函数

    该函数根据文件的大小，返回文件的大小单位（字节、KB、MB 或 GB）。

    :param filename: 要获取大小的文件名
    :type filename: str
    :return: 文件大小的字符串表示
    :rtype: str
    :raises Exception: 如果文件路径错误或文件不存在，会抛出异常并返回错误信息
    """
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
    """
    删除文件

    该函数尝试删除上传目录中的指定文件。如果文件不存在，返回 False。
    如果删除操作成功，返回 True；如果发生错误，返回错误信息。

    :param filename: 要删除的文件名
    :type filename: str
    :return: 删除操作是否成功
    :rtype: bool
    :raises Exception: 如果删除过程中发生异常，返回错误信息
    """
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)  # 构造文件路径
        if os.path.exists(file_path):  # 判断文件是否存在
            os.remove(file_path)  # 删除文件
            return True  # 返回 True 表示删除成功
        return False  # 如果文件不存在，返回 False
    except Exception as e:
        return str(e)  # 如果出现错误，返回错误信息
