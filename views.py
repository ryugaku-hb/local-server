from flask import render_template, request, redirect, url_for, flash
from flask import Response as FlaskResponse
from werkzeug.wrappers import Response as WerkzeugResponse
from file_operations import (
    allowed_file,
    save_file,
    get_files,
    download_file,
    get_file_size,
    delete_file,
)


def upload_page() -> WerkzeugResponse | str:
    """处理文件上传请求并展示文件列表页面"""
    # 如果是 POST 请求，表示用户提交了上传文件
    if request.method == "POST":
        # 从请求中获取上传的文件
        # 在 files 中，每个 key 对应 <input type="file" name=""> 里的 name 属性
        # 每个 value 是一个 Werkzeug 的 FileStorage 对象
        file = request.files["file"]

        if file and allowed_file(file.filename):
            filename, error_type = save_file(file)  # 保存文件

            if error_type == "exists":  # 文件已存在
                flash(f"文件 {file.filename} 已存在！")  # 提示文件已存在
            elif error_type == "no_file":  # 没有上传文件
                flash("没有选择文件，请选择一个文件上传。")  # 提示用户没有选择文件
            else:
                flash(f"文件 {filename} 上传成功!")  # 文件上传成功提示

            return redirect(url_for("home"))
        else:
            flash("文件类型无效。请上传有效的文件。")
            return redirect(url_for("home"))

    # 如果是 GET 请求，则显示上传页面和文件列表
    files = get_files()
    # 渲染 index.html 模板，并传递文件列表等
    return render_template("index.html", files=files, get_file_size=get_file_size)


def download_page(filename: str) -> FlaskResponse:
    """提供文件下载的网页接口"""
    return download_file(filename)


def delete_page(filename: str) -> WerkzeugResponse:
    """删除指定文件的网页接口"""
    if delete_file(filename):
        flash(f"文件 {filename} 已成功删除！")
    else:
        flash(f"文件 {filename} 删除失败。")
    return redirect(url_for("home"))
