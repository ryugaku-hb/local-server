from flask import Blueprint

file_bp = Blueprint("file", __name__, url_prefix="/file", template_folder="templates")


from . import routes  # 导入路由
