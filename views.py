# render_template: 用于渲染 HTML 模板，返回一个完整的页面。
# request: 用于获取请求数据，包括文件、表单数据等。
# redirect: 用于重定向到指定的路由。
# url_for: 用于动态生成 URL，通常与 redirect 配合使用。
from flask import render_template, request, redirect, url_for
# 从 file_operations 模块中导入文件操作相关的函数
from file_operations import save_file, get_files, download_file, get_file_size, \
    delete_file


# 该函数用于处理文件上传和展示文件列表的逻辑。
def upload_page():
    """处理文件上传并展示文件列表"""
    if request.method == 'POST':  # 如果是 POST 请求，表示用户提交了上传文件
        # 获取文件并保存
        file = request.files['file']  # 从请求中获取上传的文件，'file' 是表单中文件字段的名称
        save_file(file)  # 调用 save_file 函数将文件保存到服务器
        return redirect(url_for('home'))  # 上传完成后，重定向到首页，即刷新文件列表页面

    # 如果是 GET 请求，则显示上传页面和文件列表
    files = get_files()  # 获取当前所有文件列表
    return render_template('index.html', files=files, get_file_size=get_file_size)  # 渲染 index.html 模板，并传递文件列表


# 该函数用于处理文件下载。当用户点击下载链接时，调用 download_file 函数并传入文件名，返回文件下载的响应。
def download_page(filename):
    """文件下载"""
    return download_file(filename)  # 调用 download_file 函数返回文件下载的响应


def delete_page(filename):
    """删除文件"""
    # 调用 delete_file 函数删除文件
    success = delete_file(filename)
    if success:
        return redirect(url_for('home'))  # 删除成功后重定向到首页
    else:
        return f"Failed to delete file: {filename}", 400  # 如果删除失败，返回错误信息
