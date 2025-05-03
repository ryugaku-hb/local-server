from flask import Blueprint
from .views import home_page, upload_handler, download_handler, delete_handler

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def home():
    """主页"""
    return home_page()


@bp.route("/upload", methods=["POST"])
def upload():
    """上传文件处理路由"""
    return upload_handler()


@bp.route("/download/<filename>", methods=["GET"])
def download(filename: str):
    """下载文件处理路由"""
    return download_handler(filename)


@bp.route("/delete/<filename>", methods=["POST"])
def delete(filename: str):
    """删除文件处理路由"""
    return delete_handler(filename)
