import os
from typing import Type
from dataclasses import dataclass
from .utils import get_debug_mode, get_port


# 限定模块对外暴露的公有接口
# 当使用 `from config import *` 时，仅导入以下名称
__all__ = ["Config", "RuntimeState", "get_runtime_config"]


# ===== 默认配置 (可通过环境变量覆盖) =====


# 配置上传目录 (默认: uploads)
UPLOAD_FOLDER = os.getenv("FLASK_UPLOAD_FOLDER", "uploads")  # 上传目录 uploads
# 配置最大上传文件大小
MAX_CONTENT_LENGTH = int(
    os.getenv("FLASK_MAX_CONTENT_LENGTH", 100 * 1024 * 1024)
)  # 100 MB
# 允许上传的文件扩展名 (白名单)
ALLOWED_EXTENSIONS = {
    "txt",
    "pdf",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "ppt",
    "pptx",
    "png",
    "jpg",
    "jpeg",
    "gif",
    "mp4",
    "mov",
    "avi",
}
# 会话密钥 (用于 session 和 flash 的加密)
# 优先使用环境变量，否则自动生成随机密钥
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", os.urandom(24))  # 从环境变量读取更安全的密钥

# 默认启动端口
PORT = int(os.getenv("FLASK_PORT", 5001))


# ===== 配置类定义 =====


class Config:
    """基础配置 (开发/生产通用)"""

    UPLOAD_FOLDER = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = MAX_CONTENT_LENGTH  # 请求体大小限制 (字节)
    ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
    SECRET_KEY = SECRET_KEY  # 会话签名密钥
    PORT = PORT


class DevelopmentConfig(Config):
    """开发环境配置"""

    DEBUG = True  # 调试模式
    ENV = "development"  # 运行环境  (开发/生产)


class ProductionConfig(Config):
    """生产环境配置"""

    DEBUG = False
    ENV = "production"


@dataclass
class RuntimeConfig:
    config: Type[Config]  # 配置类 (如 DevelopmentConfig 或 ProductionConfig)
    debug: bool  # 是否启用调试模式
    port: int  # 启动 Flask 应用的端口号

    def is_dev(self) -> bool:
        return self.config.EMV == "development"

    def is_prod(self) -> bool:
        return self.config.EMV == "production"

    def __repr__(self):
        return (
            f"<RuntimeState env={self.config.EMV} debug={self.debug} port={self.port}>"
        )


# ===== 运行时配置获取与环境变量设置相关函数 =====


def _set_env_variables(config: Type[Config], port: int, debug: bool):
    """设置环境变量供子进程读取"""
    os.environ["FLASK_PORT"] = str(port)
    os.environ["FLASK_DEBUG"] = str(debug)
    os.environ["FLASK_ENV"] = config.ENV


def _get_env_variables() -> RuntimeConfig:
    """从环境变量中获取配置"""
    port = int(os.getenv("FLASK_PORT", str(Config.PORT)))
    debug = os.getenv("FLASK_DEBUG", str(DevelopmentConfig.DEBUG)) == "True"
    selected_config = DevelopmentConfig if debug else ProductionConfig

    return RuntimeConfig(selected_config, debug, port)


def get_runtime_config() -> RuntimeConfig:
    """获取运行时的配置，包括配置类、调试模式和端口号。

    Returns:
        RuntimeConfig: 封装的配置对象。
    """

    # --- WERKZEUG_RUN_MAIN 说明 ---
    """
    WERKZEUG_RUN_MAIN 是 Werkzeug 开发服务器在调试模式下使用的一个环境变量,
    主要用于区分主进程和自动重启的子进程。

    作用机制:
    当 Flask 应用以 debug=True 启动时, Werkzeug 会启用自动重启功能 (热更新)
    此时会启动两个进程:
    - 主进程: 执行原始命令 (如 python app.py), 此时 WERKZEUG_RUN_MAIN 未设置或为 None
    - 子进程: Werkzeug 自动重启应用时创建, 此时会设置 WERKZEUG_RUN_MAIN = 'true'

    典型使用场景:
    if __name__ == "__main__":
        if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
            # 这段代码只在主进程执行一次
        app.run(debug=True)

    通过判断 os.environ["WERKZEUG_RUN_MAIN"] 是否为 "true",
    可以避免主进程和子进程重复执行某些逻辑，例如 input()
    """

    if os.getenv("WERKZEUG_RUN_MAIN") != "true":  # 只在主进程中执行一次
        # 主进程: 提示用户输入端口号和是否启用调试模式，并存入环境变量
        port = get_port(default_port=Config.PORT)
        debug = get_debug_mode(default_debug=DevelopmentConfig.DEBUG)

        # 根据 debug 决定用哪个配置类
        selected_config = DevelopmentConfig if debug else ProductionConfig

        # 写入环境变量供子进程读取
        _set_env_variables(selected_config, port, debug)

        return RuntimeConfig(selected_config, debug, port)
    else:
        # 子进程: 从主进程传来的环境变量中读取端口号和调试标志
        return _get_env_variables()


class RuntimeState:
    """表示当前运行时的配置信息"""

    def __init__(self, config: Type[Config], debug: bool, port: int):
        self.config = config
        self.debug = debug
        self.port = port

    def is_dev(self) -> bool:
        return self.config.env == "development"

    def is_prod(self) -> bool:
        return self.env == "production"

    def __repr__(self):
        return f"<RuntimeState env={self.env} debug={self.debug} port={self.port}>"
