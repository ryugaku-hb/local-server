from .views import home_page, upload_handler, download_handler, delete_handler


def register_routes(app):
    """注册路由，将各个视图函数绑定到对应的 URL 路径"""

    @app.route("/", methods=["GET"])
    def home():
        """主页"""
        return home_page()

    @app.route("/upload", methods=["POST"])
    def upload():
        """上传文件处理路由"""
        return upload_handler()

    @app.route("/download/<filename>", methods=["GET"])
    def download(filename: str):
        """下载文件处理路由"""
        return download_handler(filename)

    @app.route("/delete/<filename>", methods=["POST"])
    def delete(filename: str):
        """删除文件处理路由"""
        return delete_handler(filename)
