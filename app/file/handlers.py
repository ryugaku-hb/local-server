from flask import Response, flash, redirect, render_template, request, url_for
from werkzeug.wrappers import Response as BaseResponse

from .file_operations import delete_file, download_file, save_file
from .utils import allowed_file, ensure_upload_folder_exists, get_file_size, get_files


def index_page() -> str:

    # 调用 ensure_upload_folder_exists 来确保上传文件夹存在
    ensure_upload_folder_exists()
    # 获取文件列表
    files = get_files()
    # 渲染模板返回页面
    return render_template("file/index.html", files=files, get_file_size=get_file_size)


def upload_handler() -> BaseResponse:
    # --- request.files 说明 ---
    """
    Flask 中 request.files 是处理文件上传的核心:
    - 它是一个类字典 (dict-like) 结构，包含所有通过 <input type="file"> 上传的文件。
    - 每个 key 对应表单里 <input type="file" name="xxx"> 的 name 值。
    - 每个 value 是一个 Werkzeug 的 FileStorage 对象，包含文件名、文件内容等信息。

    示例 HTML 表单:
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="上传">
    </form>

    示例用法:
    file = request.files["file"]
    file.filename      # 用户上传的文件名
    file.save(path)    # 保存文件到指定路径
    file.read()        # 读取文件内容 (字节流水)
    file.content_type  # MIME 类型 (如 image/png)
    """

    # 检查是否包含文件 part
    if "file" not in request.files:
        flash(message="⚠️ 没有找到上传文件的表单字段。", category="warning")
        return redirect(request.url)

    # 从请求中获取上传的文件
    file = request.files["file"]

    # 如果用户没有选择文件，file.filename 可能是空字符串
    if file.filename == "":
        flash(message="⚠️ 没有选择任何文件，请重新选择。", category="warning")
        return redirect(request.url)

    # 检查文件类型是否合法
    if file and allowed_file(file.filename):
        # 保存文件
        result = save_file(file)

        if not result.success:
            if result.error == "exists":
                flash(message=f"⚠️ 文件 {result.filename} 已存在！", category="warning")
        else:
            flash(message=f"✅ 文件 {result.filename} 上传成功!", category="success")

        return redirect(url_for("file.index"))
    else:
        flash(message="文件类型无效。请上传有效的文件。", category="warning")
        return redirect(url_for("file.index"))


def download_handler(filename: str) -> Response:
    """处理文件下载逻辑"""

    return download_file(filename)


def delete_handler(filename: str) -> BaseResponse:
    """处理文件删除逻辑"""

    result = delete_file(filename)

    if result.success:
        flash(message=f"✅ 文件 {result.filename} 已成功删除！", category="success")
    else:
        flash(
            message=f"❌ 文件 {result.filename} 删除失败！错误信息：{result.error}",
            category="danger",
        )

    return redirect(url_for("file.index"))
