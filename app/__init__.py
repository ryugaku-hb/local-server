from flask import Flask, redirect, url_for

from .bbs import bbs_bp
from .config import Config
from .file import file_bp


def create_app(config: type[Config]) -> Flask:
    # 创建一个 Flask 应用实例，__name__ 表示当前模块名称
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # 加载配置类中的属性 (包括 SECRET_KEY)
    app.config.from_object(config)

    # 注册 Blueprint
    app.register_blueprint(file_bp)
    app.register_blueprint(bbs_bp)

    # 注册首页跳转
    @app.route("/")
    def home():
        # return redirect(url_for("file.index"))
        return redirect(url_for("bbs.index"))

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for("bbs.index"))

    return app
