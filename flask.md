# Flask

Flask 是一个用 Python 编写的轻量级 Web 框架。它通过简单的接口帮助你构建 Web 应用程序。

> [官方文档](https://flask.palletsprojects.com/en/stable/)

- [1. 安装 - Installation](#1-安装---installation)
  - [1.1. 依赖项 - Dependencies](#11-依赖项---dependencies)
  - [1.2. 虚拟环境 - Virtual environments](#12-虚拟环境---virtual-environments)
    - [1.2.1. 创建虚拟环境 - Create an environment](#121-创建虚拟环境---create-an-environment)
    - [1.2.2. 激活虚拟环境 - Activate the environment](#122-激活虚拟环境---activate-the-environment)
    - [1.2.3. 安装 Flask - Install Flask](#123-安装-flask---install-flask)
- [2. 快速入门 Quickstart](#2-快速入门-quickstart)
  - [2.1. 一个最小的应用 - A Minimal Application](#21-一个最小的应用---a-minimal-application)
    - [2.1.1. 应用发现行为 - Application Discovery Behavior](#211-应用发现行为---application-discovery-behavior)
    - [2.1.2. 外部可见的服务器 - Externally Visible Server](#212-外部可见的服务器---externally-visible-server)
  - [2.2. 调试模式 - Debug Mode](#22-调试模式---debug-mode)
  - [2.3. HTML 转义 - HTML Escaping](#23-html-转义---html-escaping)
  - [2.4. 路由 - Routing](#24-路由---routing)
  - [2.5. 变量规则 - Variable Rules](#25-变量规则---variable-rules)
  - [2.6. 唯一的 URL／重定向行为 - Unique URLs / Redirection Behavior](#26-唯一的-url重定向行为---unique-urls--redirection-behavior)
  - [2.7. URL 构建](#27-url-构建)
  - [2.8. HTTP 方法 - HTTP Methods](#28-http-方法---http-methods)
    - [2.8.1. 分离不同 HTTP 方法的视图](#281-分离不同-http-方法的视图)
  - [2.9. 静态文件 - Static Files](#29-静态文件---static-files)
  - [2.10. 渲染模板 - Rendering Templates](#210-渲染模板---rendering-templates)
  - [2.11. 访问请求数据 - Accessing Request Data](#211-访问请求数据---accessing-request-data)
    - [2.11.1. 上下文本地变量 - Context Locals](#2111-上下文本地变量---context-locals)
    - [2.11.2. 请求对象 - The Request Object](#2112-请求对象---the-request-object)
    - [2.11.3. 文件上传 - File Uploads](#2113-文件上传---file-uploads)
    - [2.11.4. Cookies](#2114-cookies)
  - [2.12. 重定向和错误处理 - Redirects and Errors](#212-重定向和错误处理---redirects-and-errors)
    - [2.12.1. 重定向](#2121-重定向)
    - [2.12.2. 错误处理](#2122-错误处理)
    - [2.12.3. 自定义错误页面](#2123-自定义错误页面)
  - [2.13. 关于响应 - About Responses](#213-关于响应---about-responses)
  - [2.14. 使用 JSON 的 API - APIs with JSON](#214-使用-json-的-api---apis-with-json)
- [API](#api)
  - [send\_file 函数](#send_file-函数)
  - [send\_from\_directory 函数](#send_from_directory-函数)

## 1. 安装 - Installation

### 1.1. 依赖项 - Dependencies

以下依赖项会在安装 Flask 时自动安装。

- Werkzeug 实现了 WSGI，这是应用程序与服务器之间的标准 Python 接口。
- Jinja 是一个模板语言，用于渲染应用程序提供的页面。
- MarkupSafe 随 Jinja 一起提供，它在渲染模板时对不可信的输入进行转义，以防止注入攻击。
- ItsDangerous 安全地签署数据，以确保其完整性。这用于保护 Flask 的会话 cookie。
- Click 是一个命令行应用框架，提供 flask 命令并允许添加自定义管理命令。
- Blinker 提供对信号的支持。

### 1.2. 虚拟环境 - Virtual environments

使用虚拟环境来管理项目的依赖项，适用于开发和生产环境。

虚拟环境解决了什么问题？随着 Python 项目增多，你可能需要使用不同版本的 Python 库，甚至是不同版本的 Python 本身。一个项目中库的更新可能会破坏另一个项目的兼容性。

虚拟环境是独立的 Python 库组，每个项目都有一个。为一个项目安装的包不会影响其他项目或操作系统的包。

Python 自带 `venv` 模块，用于创建虚拟环境。

#### 1.2.1. 创建虚拟环境 - Create an environment

创建一个项目文件夹，并在其中创建 `.venv` 文件夹：

```bash
# macOS/Linux
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv

# Windows
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

#### 1.2.2. 激活虚拟环境 - Activate the environment

在开始项目之前，激活对应的虚拟环境：

```bash
# macOS/Linux
$ . .venv/bin/activate

# Windows
> .venv\Scripts\activate
```

#### 1.2.3. 安装 Flask - Install Flask

在已激活的虚拟环境中，使用以下命令安装 Flask：

```bash
$ pip install Flask
```

Flask 现在已安装在你的虚拟环境中。

## 2. 快速入门 Quickstart

Flask 是一个用 Python 编写的轻量级 Web 框架。它通过简单的接口帮助你构建 Web 应用程序。

> <https://flask.palletsprojects.com/en/stable/quickstart/>

### 2.1. 一个最小的应用 - A Minimal Application

一个最小的 Flask 应用看起来是这样的：

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

代码分析：

1. 导入 Flask 类：首先，我们导入了 Flask 类，它的实例将作为我们的 WSGI 应用。
2. 创建 Flask 实例：我们创建了一个 Flask 实例，`__name__` 是模块的名称，Flask 需要它来知道在哪里寻找资源，如模板和静态文件。
3. 定义路由：使用 `@app.route()` 装饰器来告诉 Flask，当访问该 URL 时应该调用哪个函数。
4. 返回消息：函数返回我们希望在浏览器中显示的内容。默认情况下，Flask 会把返回内容当作 HTML 渲染。

保存代码为 `hello.py` 或其他类似的名字。请确保不要将文件命名为 `flask.py`，否则会与 Flask 本身发生冲突。

运行应用程序时，可以使用 `flask` 命令或 `python -m flask`。你需要使用 `--app` 选项来指定 Flask 应用所在的位置。

```bash
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

#### 2.1.1. 应用发现行为 - Application Discovery Behavior

如果文件命名为 `app.py` 或 `wsgi.py`，则不需要使用 `--app` 选项。更多细节请查看 Flask 的 [命令行接口（Command Line Interface）](https://flask.palletsprojects.com/en/stable/cli/) 部分。

这个简单的内置服务器适合测试，但在生产环境中不建议使用，详细的部署方式请参考 Flask 的 [生产环境部署（Deploying to Production）](https://flask.palletsprojects.com/en/stable/deploying/) 文档。

访问 `http://127.0.0.1:5000/`，应该能看到你返回的 "Hello, World!" 消息。

#### 2.1.2. 外部可见的服务器 - Externally Visible Server

如果你运行服务器，会发现它仅能从本地访问，而不能从网络中的其他计算机访问。出于安全考虑，默认情况下 Flask 会限制调试模式下的访问。

如果关闭调试器或信任网络中的用户，可以通过添加 `--host=0.0.0.0` 来让服务器对外公开：

```bash
$ flask run --host=0.0.0.0
```

### 2.2. 调试模式 - Debug Mode

Flask 提供了调试模式，启用后，代码更改时会自动重载服务器，并且在请求发生错误时，浏览器中会显示交互式调试器。

启用调试模式：

```bash
$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

警告：调试器允许从浏览器执行任意 Python 代码，因此存在较大安全风险。不要在生产环境中启用开发服务器或调试器。

### 2.3. HTML 转义 - HTML Escaping

当返回 HTML 时，任何由用户提供的值都需要进行转义，以防止注入攻击。Flask 默认通过 Jinja 模板引擎来自动处理这个问题。

可以使用 `escape()` 函数手动转义 HTML，如下所示：

```python
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

如果用户提交了包含 JavaScript 的名字，如 `<script>alert("bad")</script>`，转义后，浏览器会把它渲染为文本，而不是执行脚本。

在路由中的 `<name>` 捕获来自 URL 的值，并将其传递给视图函数。

### 2.4. 路由 - Routing

现代的 web 应用程序使用有意义的 URL 来帮助用户记住并直接访问页面。Flask 使用 `@app.route()` 装饰器将函数与 URL 绑定。

例如：

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

你可以将 URL 中的一部分做成动态的，并为它设置多个规则。

### 2.5. 变量规则 - Variable Rules

可以在 URL 中添加变量部分，通过 `<variable_name>` 标记。然后，函数会将 `<variable_name>` 作为关键字参数传递。还可以使用转换器指定参数的类型，如 `<int:variable_name>`。

例如：

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

转换器类型：

- `string`：接受没有斜杠的任何文本（默认）
- `int`：接受正整数
- `float`：接受正浮动值
- `path`：像 `string`，但也可以接受斜杠
- `uuid`：接受 UUID 字符串

### 2.6. 唯一的 URL／重定向行为 - Unique URLs / Redirection Behavior

以下两个规则在使用结尾斜杠（trailing slash）上有所不同：

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

`projects` 端点的规范 URL 以结尾斜杠（/projects/）结尾。这类似于文件系统中的文件夹。如果你访问没有结尾斜杠的 URL（例如 `/projects`），Flask 会将你重定向到带有结尾斜杠的规范 URL（`/projects/`）。

`about` 端点的规范 URL 不带结尾斜杠。这类似于文件的路径名。访问带有结尾斜杠的 URL（例如 `/about/`）会返回 404 "Not Found" 错误。这有助于确保这些资源的 URL 唯一，从而避免搜索引擎重复索引相同的页面。

结尾斜杠的作用：

对于 `projects` 端点，带有斜杠的 URL 被视为一个目录。访问没有斜杠的 URL 时，Flask 会自动进行重定向，以确保最终访问的是带斜杠的 URL。

对于 `about` 端点，不带斜杠的 URL 被视为文件路径。如果访问带有斜杠的 URL，则会触发 404 错误，因为这不符合文件路径的标准格式。

### 2.7. URL 构建

使用 `url_for()` 函数来构建指向特定函数的 URL。它的第一个参数是函数名，之后是任意数量的关键字参数，每个关键字参数对应 URL 规则中的变量部分。未知的变量部分会作为查询参数附加到 URL 中。

例如：

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

输出结果：

```bash
/
/login
/login?next=/
/user/John%20Doe
```

### 2.8. HTTP 方法 - HTTP Methods

Flask 默认只响应 GET 请求，你可以使用 `route()` 装饰器的 `methods` 参数来处理不同的 HTTP 方法。

例如：

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

在上面的例子中，`login()` 函数处理了 `/login` 路由的 GET 和 POST 请求。这可以很有用，因为两种请求可能会共享一些公共数据。

#### 2.8.1. 分离不同 HTTP 方法的视图

你也可以将不同的 HTTP 方法分别处理，通过不同的函数来组织视图。Flask 提供了快捷方式来装饰这些路由，比如 `get()`、`post()` 等，用于处理常见的 HTTP 方法。

```python
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

在这个示例中，`login_get() `函数处理 GET 请求，而 `login_post()` 函数处理 POST 请求。

### 2.9. 静态文件 - Static Files

动态 Web 应用程序通常也需要静态文件。通常情况下，CSS 和 JavaScript 文件就属于静态文件。理想情况下，你的 Web 服务器应该被配置来为你提供这些文件，但在开发过程中，Flask 也可以为你处理这些文件。只需要在你的项目中创建一个名为 `static` 的文件夹，Flask 会将其视为静态文件夹，并可以通过 `/static` 路径来访问这些文件。

示例：

要为静态文件生成 URL，使用特殊的 `'static'` 端点名称：

```python
url_for('static', filename='style.css')
```

这会生成指向 `static/style.css` 文件的 URL。

解释：

- 静态文件：这些是不会改变的文件，比如样式表（CSS）、JavaScript 文件、图片等。在 Web 应用中，这些文件通常是前端用户界面的一部分。
- Flask 处理静态文件：在开发模式下，Flask 会自动为你提供静态文件。当你创建一个名为 `static` 的文件夹时，Flask 会将其中的文件作为静态文件来处理，路径为 `/static`。
- `url_for('static', filename='style.css')`：Flask 提供了 `url_for()` 函数来动态生成静态文件的 URL。在这个例子中，`filename` 参数指定了文件的名称，生成的 URL 会指向 `static/style.css` 文件。

### 2.10. 渲染模板 - Rendering Templates

Flask 使用 Jinja2 模板引擎来生成 HTML。

要渲染模板，你可以使用 `render_template()` 方法。你只需要提供模板的名称和你想要传递给模板引擎的变量，作为关键字参数。

例如：

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
```

Flask 会在 `templates` 文件夹中查找模板。如果你的应用程序是一个模块，模板文件夹位于模块旁边；如果是一个包，模板文件夹实际上位于包内：

模块的情况：

```bash
/application.py
/templates
    /hello.html
```

包的情况：

```bash
/application
    /__init__.py
    /templates
        /hello.html
```

对于模板，你可以使用 Jinja2 模板的全部功能。

示例模板：

```html
<!DOCTYPE html>
<title>Hello from Flask</title>
{% if person %}
<h1>Hello {{ person }}!</h1>
{% else %}
<h1>Hello, World!</h1>
{% endif %}
```

在模板中，你还可以访问 `config`、`request`、`session` 和 `g` 对象，以及 `url_for()` 和 `get_flashed_messages()` 函数。

Flask 支持模板继承，允许你在多个页面中复用相同的 HTML 结构（如头部、导航、页脚等），减少代码重复。

Flask 自动转义模板中的 HTML 内容，确保安全。如果你知道某个变量包含的 HTML 是安全的，可以通过 `Markup` 类或 `|safe` 过滤器标记它。

### 2.11. 访问请求数据 - Accessing Request Data

Flask 使用全局的 `request` 对象来提供客户端请求的数据。虽然这个对象是“全局”的，但它通过 上下文局部变量（Context Locals） 来保证线程安全。每个请求都有自己的上下文，并且 Flask 会为每个线程绑定一个独立的请求对象。

#### 2.11.1. 上下文本地变量 - Context Locals

Flask 中的某些对象是全局对象，但与通常的全局对象不同。它们实际上是指向特定上下文（context）中本地对象的代理。简单来说，Flask 使用这种方式来保证不同请求之间的数据隔离。

上下文局部变量：这个概念意味着尽管 Flask 使用全局对象（如 request），它们实际上是每个线程（或上下文）特定的代理。这使得多个请求能够并发处理而不互相干扰。

请求上下文绑定：Flask 在处理请求时会智能地绑定当前请求的应用和 WSGI 环境到当前的线程或上下文中。这样可以确保一个应用的请求不会影响到另一个应用。

#### 2.11.2. 请求对象 - The Request Object

`request` 对象已经在 API 部分有详细文档，我们在这里不做详细介绍。这里是一些常见操作的概述。

首先需要从 Flask 模块中导入 `request`：

```python
from flask import request
```

当前的请求方法可以通过 `method` 属性获取。要访问表单数据（通过 POST 或 PUT 请求传输的数据），可以使用 `form` 属性。下面是一个完整的示例：

示例：

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

如果表单中没有某个键，`request.form` 会抛出一个特殊的 `KeyError`。你可以像处理标准 `KeyError` 一样捕获它，如果不捕获它，Flask 会显示 HTTP 400 错误页面。因此，对于许多情况，你不需要处理这个问题。

要访问 URL 中提交的参数（如 `?key=value`），你可以使用 `args` 属性：

```python
searchword = request.args.get('key', '')
```

我们建议使用 `get` 方法或捕获 `KeyError` 来访问 URL 参数，因为用户可能会更改 URL，直接给他们一个 400 错误页面并不友好。

#### 2.11.3. 文件上传 - File Uploads

Flask 使得文件上传处理变得很容易。只需要确保在 HTML 表单中设置 `enctype="multipart/form-data"` 属性，否则浏览器根本不会传输文件。

上传的文件存储在内存中或文件系统的临时位置。你可以通过查看 `request` 对象的 `files` 属性来访问这些文件。每个上传的文件都存储在该字典中。它的行为类似于标准的 Python 文件对象，但它也有一个 `save()` 方法，允许你将文件存储到服务器的文件系统中。

示例：

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

如果你想知道文件在客户端上传之前是如何命名的，可以通过 `filename` 属性获取文件名。然而，请注意，这个值可以被伪造，因此千万不要轻信这个值。如果你想使用客户端的文件名来存储文件，应该通过 Werkzeug 提供的 `secure_filename()` 函数来处理文件名：

示例：

```python
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...
```

#### 2.11.4. Cookies

要访问 cookies，可以使用 `cookies` 属性。要设置 cookies，可以使用响应对象的 `set_cookie` 方法。request 对象的 `cookies` 属性是一个字典，包含客户端传递的所有 cookies。如果你想使用会话，不要直接使用 cookies，而是使用 Flask 的会话机制，它会在 cookies 上添加一些额外的安全性。

读取 cookies：

```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

存储 cookies：

```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

请注意，cookies 是通过响应对象来设置的。由于你通常只会从视图函数返回字符串，Flask 会自动将其转换为响应对象。如果你想显式地创建响应对象，可以使用 `make_response()` 函数，并进行修改。

有时你可能会在响应对象还不存在时就想设置一个 cookie。你可以通过使用 [Deferred Request Callbacks](https://flask.palletsprojects.com/en/stable/patterns/deferredcallbacks/) 模式来实现这一点。

### 2.12. 重定向和错误处理 - Redirects and Errors

Flask 提供了两个常用功能来处理重定向和错误：

#### 2.12.1. 重定向

使用 `redirect()` 函数可以将用户重定向到其他端点。可以配合 `url_for()` 来生成目标端点的 URL。例如：

```python
from flask import redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))
```

#### 2.12.2. 错误处理

使用 `abort()` 函数可以提前终止请求并返回一个错误代码。例如：

```python
from flask import abort

@app.route('/login')
def login():
    abort(401)  # 返回 401 错误，即未授权
    this_is_never_executed()  # 这一行永远不会执行
```

#### 2.12.3. 自定义错误页面

默认情况下，Flask 为每个错误代码（如 404 或 500）显示黑白的错误页面。如果你希望自定义错误页面，可以使用 `errorhandler()` 装饰器来捕获特定的错误代码并返回自定义的 HTML 页面。例如：

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

这里的 404 代码表示页面未找到。`render_template()` 渲染一个自定义的 HTML 错误页面，然后 Flask 会返回一个带有 404 状态码的响应。

总结：

- `redirect()`：用于将用户重定向到另一个页面。
- `abort()`：用于终止请求并返回指定的 HTTP 错误代码。
- `errorhandler()`：用于自定义错误页面，通过装饰器捕获特定的错误代码并返回自定义响应。

### 2.13. 关于响应 - About Responses

Flask 中的视图函数返回值会自动转换为响应对象。

根据返回值的类型，Flask 会采取不同的处理方式：

1. 字符串返回值：如果视图函数返回的是一个字符串，Flask 会将其转换为一个响应对象，字符串作为响应体，状态码为 200（OK），MIME 类型为 `text/html`。
2. 字典或列表返回值：如果返回的是字典或列表，Flask 会调用 `jsonify()` 将其转换为 JSON 响应。
3. 迭代器或生成器：如果返回的是一个字符串或字节的迭代器／生成器，则 Flask 会将其视为一个流式响应（streaming response）。
4. 元组返回值：如果返回的是一个元组，元组中的元素可以提供额外的信息。元组应该是以下格式之一：
   - `(response, status)`：返回响应和状态码。
   - `(response, headers)`：返回响应和头信息。
   - `(response, status, headers)`：返回响应、状态码和头信息。
   - 其中，状态码值将覆盖默认的状态码，而头信息可以是一个列表或字典形式的额外头字段。
5. 其他情况：如果返回值不符合上述情况，Flask 会认为该返回值是一个有效的 WSGI 应用程序，并将其转换为响应对象。

获取响应对象：如果你希望在视图中获取生成的响应对象，可以使用 `make_response()` 函数。

例如，下面是一个错误处理函数，默认返回一个带 404 状态的错误页面：

```python
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

如果你想修改响应对象，可以使用 `make_response()` 包裹返回值：

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

### 2.14. 使用 JSON 的 API - APIs with JSON

在编写 API 时，JSON 是常见的响应格式。当视图返回字典或列表时，Flask 会自动将其转换为 JSON 格式的响应。

例如，下面是一个返回 JSON 的简单 API：

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

如果你返回一个字典或列表，Flask 会自动调用 `jsonify()`，并将字典或列表序列化为 JSON 格式。需要注意的是，字典或列表中的数据必须是可序列化为 JSON 的类型。

对于复杂的数据类型（如数据库模型），你可能需要使用序列化库，将其转换为有效的 JSON 格式。Flask 社区有许多序列化库和 API 扩展，可以帮助处理更复杂的应用。

## API

### send_file 函数

```python
"""
flask.send_file(path_or_file, mimetype=None, as_attachment=False, 
    download_name=None, conditional=True, etag=True, 
    last_modified=None, max_age=None)

用来将文件内容发送给客户端。
它适用于将静态文件或其他文件内容返回给客户端，比如文件下载等。

参数说明：
  path_or_file：
   文件的路径或者是一个文件样式的对象。
   如果传入的是路径，路径应该是相对于当前工作目录的；
   如果是文件样式对象，则应以二进制模式打开，通常用于内存中创建的文件，如使用 io.BytesIO。
  mimetype：要发送的文件的 MIME 类型。
   如果未提供，Flask 会尝试从文件名推测 MIME 类型。
  as_attachment：是否提示浏览器下载文件，而不是直接显示。
   默认为 False，即直接显示文件。
   如果设置为 True，则浏览器会提示用户下载该文件。
  download_name：浏览器下载文件时默认使用的文件名。
   如果没有提供，默认使用传入的文件名。
  conditional：启用基于请求头的条件和范围响应。
   默认为 True，如果文件路径和 environ 可用，它允许部分内容传输。
  etag：是否为文件计算 ETag（实体标签），用于条件请求。
   如果传入 True，则会基于文件路径计算 ETag；也可以传入一个自定义的 ETag 字符串。
  last_modified：文件的最后修改时间。
   如果未提供，Flask 会尝试从文件路径中获取这个时间。
  max_age：设置客户端缓存文件的最大时长，单位为秒。
   如果设置了，会添加 Cache-Control: public 头，
   否则默认为 no-cache，以便进行条件缓存。

返回值：
  Response：返回一个包含文件内容的 HTTP 响应，可以供客户端下载或显示。
"""
from flask import send_file

@app.route('/download')
def download():
    path = 'path/to/file.pdf'
    return send_file(path, as_attachment=True, download_name='file.pdf')
```

### send_from_directory 函数

```python
"""
flask.send_from_directory(directory, path, **kwargs)

用来从指定的目录中发送文件，类似于 send_file()。
这个方法常用于处理文件下载，比如提供静态文件或用户上传的文件。

参数说明：
  directory：
   文件所在的目录，路径必须是相对于当前应用根路径的。
   此值不得由客户端提供，否则会存在安全隐患。
  path：要发送的文件路径，相对于 directory。
  kwargs：其他传递给 send_file() 的参数。

返回值：
  Response：返回一个包含文件内容的 HTTP 响应，供客户端下载。
"""
@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )

# 在这个例子中，当用户请求 /uploads/<name> 时，
# Flask 会从 UPLOAD_FOLDER 配置的目录中找到对应的文件并返回给用户。
# as_attachment=True 参数会使文件作为附件下载。
```
