import os
from .port import get_port_from_input


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
    'py',
    'md'
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


# ===== 获取运行时配置 =====


def get_runtime_config():
    """获取运行时的配置，包括配置类和端口号。"""

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
        port = get_port_from_input(default_port=Config.PORT)

        # 写入环境变量供子进程读取
        os.environ["FLASK_PORT"] = str(port)

        return (
            Config,
            port,
        )
    else:
        # 子进程: 从主进程传来的环境变量中读取端口号和调试标志
        port = int(os.getenv("FLASK_PORT", str(Config.PORT)))

        return (
            Config,
            port,
        )
