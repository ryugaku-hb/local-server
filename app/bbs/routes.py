from . import bbs_bp
from .handlers import delete_post_handler, index_page, new_post_handler


@bbs_bp.route("/", methods=["GET"])
def index():
    """主页"""
    return index_page()


@bbs_bp.route("/new", methods=["POST"])
def new_post():
    return new_post_handler()


@bbs_bp.route("/delete/<int:post_index>", methods=["POST"])
def delete_post(post_index):
    return delete_post_handler(post_index)
