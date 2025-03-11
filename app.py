import os
from flask import Flask
from views import upload_page, download_page, delete_page
from config import PORT


# 创建一个 Flask 应用实例，__name__ 表示当前模块名称
app = Flask(__name__)
# 设置 flash 消息需要的密钥
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")


# 根路由 (/)
@app.route("/", methods=["GET", "POST"])
def home():
    """处理根路由的请求"""
    return upload_page()


# 下载路由
@app.route("/download/<filename>", methods=["GET"])
def download(filename: str):
    """处理下载路由的请求"""
    return download_page(filename)


# 文件删除路由
@app.route("/delete/<filename>", methods=["POST"])
def delete(filename: str):
    """处理文件删除路由的请求"""
    return delete_page(filename)


# 判断该脚本是否是直接运行的（而非作为模块导入）
if __name__ == "__main__":
    # 启动 Flask 服务器，设置调试模式，监听所有接口，使用指定的端口
    app.run(debug=True, host="0.0.0.0", port=PORT)
