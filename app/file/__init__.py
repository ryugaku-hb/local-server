from flask import Blueprint

# 创建一个名为 file 的 Blueprint，绑定前缀 /file，使用本模块下的 templates/ 目录作为模板文件夹。
# 用于注册文件模块的路由和视图逻辑，并指定该模块所用的模板目录。
file_bp = Blueprint(
    "file",
    __name__,
    url_prefix="/file",
    template_folder="templates",
    static_folder="static",
)

# --- Blueprint 说明 ---

# 实例: file_bp
# 定义的 Blueprint 实例，后续用它来注册路由。
# 例如: @file_bp.route("/upload")

# 参数: "file"
# 创建一个名为 "file" 的 Blueprint，"file" 是 Blueprint 的名称，也是 url_for() 和 endpoint 的前缀。
# 例如: url_for("file.index") 就是访问这个模块的 index 视图。
# 如果是 "bbs" 模块，就写 Blueprint("bbs", ...)，然后访问: url_for("bbs.index")。

# 参数: __name__
# 当前模块的名字。
# Flask 用它来定位模板和静态文件目录的相对路径。

# 参数: url_prefix="/file"
# 这个模块所有的路由都会以 /file 开头。
# Blueprint 路由: @file_bp.route("/"), 实际访问路径: /file/。
# Blueprint 路由: @file_bp.route("/upload"), 实际访问路径: /file/upload。
# 避免多个模块路由冲突 (每个模块有独立命名空间)。

# 参数: template_folder="templates"
# 告诉 Flask: 这个 Blueprint 使用相对路径 "templates" 作为模板目录。
# 路径是相对于定义这个 Blueprint 的 Python 文件。

# 参数: static_folder="static"


from . import routes  # 导入路由
