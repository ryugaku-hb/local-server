from app import create_app
from app.config import get_runtime_config


# 判断该脚本是否是直接运行的 (而非作为模块导入)
if __name__ == "__main__":

    config, port = get_runtime_config()
    app = create_app(config)

    # 启动 Flask 服务器
    # 设置是否使用调试模式，监听所有接口，使用指定的端口
    app.run(debug=True, host="0.0.0.0", port=port)
