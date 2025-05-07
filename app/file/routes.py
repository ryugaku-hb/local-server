from . import file_bp
from .handlers import (delete_handler, download_handler, index_page,
                       upload_handler)

# 绑定 Blueprint 路由和视图处理函数
# Blueprint 名为 "file"，挂载在 url_prefix="/file"

# 实际访问路径
# /file/
# /file/upload
# /file/download/<filename>
# /file/delete/<filename>

# url_for() 的 endpoint 参数格式为 "file.函数名"
# 使用 url_for("file.函数名")


@file_bp.route("/", methods=["GET"])
def index():
    """主页"""
    return index_page()


@file_bp.route("/upload", methods=["POST"])
def upload():
    """上传文件处理路由"""
    return upload_handler()


@file_bp.route("/download/<filename>", methods=["GET"])
def download(filename: str):
    """下载文件处理路由"""
    return download_handler(filename)


@file_bp.route("/delete/<filename>", methods=["POST"])
def delete(filename: str):
    """删除文件处理路由"""
    return delete_handler(filename)
