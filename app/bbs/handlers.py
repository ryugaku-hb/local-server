from flask import redirect, render_template, request, url_for

from .models import PostModel

# 初始化帖子模型
post_model = PostModel()


def index_page() -> str:
    """主页处理函数，获取所有帖子并传递给模板"""
    posts = post_model.get_all_posts()

    # 渲染模板返回页面
    return render_template("bbs/index.html", posts=posts)


def new_post_handler():
    """新帖发布页面处理函数"""
    # 获取表单数据
    title = request.form.get("title")
    content = request.form.get("content")
    ip = request.remote_addr
    author = request.form.get("author")

    # 创建新帖子
    post_model.create_post(title, content, ip, author)

    # 重定向到主页
    # return redirect(url_for("bbs.index"))

    # 获取所有帖子
    posts = post_model.get_all_posts()

    # 渲染部分 HTML 返回给客户端
    return render_template("bbs/_post_list.html", posts=posts)


def delete_post_handler(post_index):
    post_model.delete_post(post_index)
    return redirect(url_for("bbs.index"))
