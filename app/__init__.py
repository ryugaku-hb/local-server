from flask import Flask
from .config import RuntimeConfig
from .routes import register_routes


def create_app(runtime_config: RuntimeConfig):
    # 创建一个 Flask 应用实例，__name__ 表示当前模块名称
    app = Flask(__name__, template_folder="./templates", static_folder="./static")

    # 加载配置类中的属性 (包括 SECRET_KEY)
    app.config.from_object(runtime_config.config)

    register_routes(app)

    return app
