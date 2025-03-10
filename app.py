from flask import Flask
from views import upload_page, download_page, delete_page
from config import PORT
from flask import Response as FlaskResponse
from werkzeug.wrappers import Response as WerkzeugResponse

# 创建一个 Flask 应用实例，__name__ 表示当前模块名称
app = Flask(__name__)
# 设置 flash 消息需要的密钥
app.secret_key = "default_secret_key"
# app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')


# 根路由 (/)
@app.route("/", methods=["GET", "POST"])
def home() -> WerkzeugResponse | str:  # home 函数处理根路由的请求
    return upload_page()  # 返回上传页面视图函数的内容


# 下载路由 (/download/<filename>)
# @app.route('/download/<filename>') 定义了一个带有动态参数 filename 的路由，
# 当请求访问类似 /download/somefile.txt 时，filename 参数会被传递到 download() 函数。
# download() 函数调用 download_page(filename)，返回处理该文件下载的页面。
@app.route("/download/<filename>")  # 定义一个动态路由，<filename> 表示文件名
def download(filename: str) -> FlaskResponse:  # download 函数处理文件下载请求
    return download_page(filename)  # 返回下载页面视图函数，传递文件名作为参数


# 文件删除路由
@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename: str) -> WerkzeugResponse:
    return delete_page(filename)  # 调用删除文件的视图函数


# 判断该脚本是否是直接运行的（而非作为模块导入）
if __name__ == "__main__":
    # app.run() 启动 Flask 服务器
    # debug = True 启用调试模式，方便开发时查看错误信息并自动重载
    # host='0.0.0.0' 使应用监听所有网络接口（即允许外部访问）
    # port=PORT 设置 app 运行在指定端口，该端口号从 config 获取
    app.run(debug=True, host="0.0.0.0", port=PORT)
