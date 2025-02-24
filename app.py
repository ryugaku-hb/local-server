from flask import Flask  # 导入 Flask 类，用于创建 Flask 应用
from views import upload_page, download_page, delete_page  # 从 views 模块中导入上传页面和下载页面等的视图函数

# 创建一个 Flask 应用实例，__name__ 表示当前模块名称
app = Flask(__name__)


# 根路由 (/)
# 使用 @app.route() 装饰器定义了根路由 /，支持 GET 和 POST 请求
@app.route('/', methods=['GET', 'POST'])  # 定义根路由，支持 GET 和 POST 请求
def home():  # home 函数处理根路由的请求
    return upload_page()  # 返回上传页面视图函数的内容


# 下载路由 (/download/<filename>)
# @app.route('/download/<filename>') 定义了一个带有动态参数 filename 的路由，
# 当请求访问类似 /download/somefile.txt 时，filename 参数会被传递到 download() 函数。
# download() 函数调用 download_page(filename)，返回处理该文件下载的页面。
@app.route('/download/<filename>')  # 定义一个动态路由，<filename> 表示文件名
def download(filename):  # download 函数处理文件下载请求
    return download_page(filename)  # 返回下载页面视图函数，传递文件名作为参数


# 文件删除路由
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    return delete_page(filename)  # 调用删除文件的视图函数


# 判断该脚本是否是直接运行的（而非作为模块导入）
# 如果是，启动 Flask 开发服务器。
if __name__ == '__main__':
    # app.run() 启动 Flask 服务器
    # debug = True：启用调试模式，方便开发时查看错误信息并自动重载。
    # host='0.0.0.0'：使应用监听所有网络接口（即允许外部访问）。
    # port=5001：设置应用运行在 5001 端口。
    app.run(debug=True, host='0.0.0.0', port=5002)  # 启动 Flask 开发服务器，设置调试模式，监听所有 IP 地址，端口为 5001
