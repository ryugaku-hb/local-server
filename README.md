# local-server

简单的本地服务器

## 1. 极速上手

```bash
# 首次使用
python3 -m venv venv  # 创建虚拟环境
source venv/bin/activate  # 激活虚拟环境（Linux/Mac）
python3 -m pip install Flask  # 在虚拟环境中安装 Flask

# 再次使用
source venv/bin/activate  # 激活已存在的虚拟环境

# 启动服务器
python3 app.py
```

## 2. 文件结构

```bash
local-server/
│   # 保持在项目根目录，作为启动 Flask 应用的主要文件。
├── app.py
│   # 配置文件，包含上传文件夹、文件大小限制等配置信息。
├── config.py
│   # 处理文件上传、下载等操作的逻辑。
├── file_operations.py
│   # 存放视图函数，用来处理上传页面的呈现、文件列表、文件下载等。
├── views.py
│   # 用于存放 HTML 模板文件
├── templates/
│   │   # index.html 提供文件上传和展示功能。
│   └── index.html
├── static/
│   └── css/
│       └── styles.css
│
│   # 用于忽略不需要的文件或目录，如虚拟环境、编译文件等。
├── .gitignore
│   # 项目的许可证文件。
├── LICENSE
│   # 项目的说明文件，包含项目的介绍、功能、安装使用方法等。
└── README.md
```

## 3. 运行

### 3.1. 安装 Flask

```bash
pip install Flask
# or
pip3 install Flask

# or
# 在某些系统限制的情况下
python3 -m venv .venv         # 创建虚拟环境
source .venv/bin/activate     # 激活虚拟环境
python3 -m pip install Flask  # 在虚拟环境中安装 Flask

# .venv 作为虚拟环境目录不方便，可以选择其他更直观的目录名
python3 -m venv env  # 例如 venv、env 或者其他你习惯的名字
source env/bin/activate
python3 -m pip install Flask
```

---

<p><details><summary>【✦ ✧ ✩ ❌ <b>Error</b> ⚠️ ✩ ✧ ✦】</summary><p>

#### 3.1.1. 安装报错

使用 Homebrew 安装 Flask 时发生了以下错误。

```bash
% pip3 install Flask
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.

    If you wish to install a Python library that isn't in Homebrew,
    use a virtual environment:

    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install xyz

    If you wish to install a Python application that isn't in Homebrew,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. You can install pipx with

    brew install pipx

    You may restore the old behavior of pip by passing
    the '--break-system-packages' flag to pip, or by adding
    'break-system-packages = true' to your pip.conf file. The latter
    will permanently disable this error.

    If you disable this error, we STRONGLY recommend that you additionally
    pass the '--user' flag to pip, or set 'user = true' in your pip.conf
    file. Failure to do this can result in a broken Homebrew installation.

    Read more about this behavior here: <https://peps.python.org/pep-0668/>

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

上述报错内容的中文翻译如下：

```bash
# 错误：externally-managed-environment

# × 这个环境是外部管理的。
# ╰─> 要安装 Python 包到系统中，请尝试使用 brew install，其中 xyz 是你要安装的包名。

# 如果你想安装一个不在 Homebrew 中的 Python 库，请使用虚拟环境：

    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install xyz

# 如果你想安装一个不在 Homebrew 中的 Python 应用程序，
# 最简单的方法是使用 pipx install xyz，它会为你管理虚拟环境。
# 你可以通过以下命令安装 pipx：

    brew install pipx

# 你也可以通过传递 --break-system-packages 参数来恢复 pip 的旧行为，
# 或者将 break-system-packages = true 添加到你的 pip.conf 文件中。
# 后者将永久禁用这个错误。

# 如果你禁用了这个错误，强烈建议你同时使用 --user 参数，
# 或者在 pip.conf 文件中设置 user = true。否则可能会导致 Homebrew 安装损坏。

# 阅读更多关于这个行为的信息：https://peps.python.org/pep-0668/

# 注意：如果你认为这是一个错误，请联系你的 Python 安装或操作系统发行版提供商。
# 你可以通过传递 --break-system-packages 来覆盖此错误，
# 风险是可能会破坏你的 Python 安装或操作系统。

# 提示：查看 PEP 668 以了解详细规范。
```


#### 3.1.2. 创建虚拟环境

如果你的系统环境有一些限制，或者你不希望影响全局 Python 安装，可以考虑创建一个虚拟环境。

进入项目目录，在你的项目目录中进行如下操作：

```bash
# 创建虚拟环境
python3 -m venv .venv
# 激活虚拟环境
source .venv/bin/activate
# 在虚拟环境中安装 Flask
python3 -m pip install Flask
```

命令说明：

```bash
# 创建虚拟环境
python3 -m venv .venv
# python3：
#  这是 Python 3 的命令。
#  因为一些系统可能同时安装了 Python 2 和 Python 3，
#  所以需要使用 python3 来指定使用 Python 3。
# -m：
#  这是 Python 的一个命令行选项，它允许你运行 Python 模块（即 .py 文件）。
#  在这里，-m venv 表示运行 Python 的 venv 模块来创建一个虚拟环境。
# venv：
#  是 Python 内置的模块，用于创建虚拟环境。
#  虚拟环境是一个隔离的环境，包含独立的 Python 解释器和包，可以避免项目间的包版本冲突。
# .venv：
#  这是你要创建的虚拟环境的名称。
#  你可以根据需要更改这个名字，例如改为 myenv 等。

# 生成的目录结构：
# .venv/
# │
# ├── bin/                   # 包含虚拟环境的可执行文件，包括 Python 解释器和脚本
# │   ├── activate           # 用于激活虚拟环境的脚本（Linux/macOS）
# │   ├── python             # Python 解释器的链接
# │   ├── pip                # 包管理工具的链接
# │   └── ...                # 其他脚本和可执行文件
# │
# ├── include/               # 包含 C 语言头文件，主要用于编译 C 扩展
# │
# ├── lib/                   # 存放 Python 标准库和你安装的第三方库
# │   └── pythonX.Y/         # 其中 X.Y 是你使用的 Python 版本号（例如 python3.8）
# │       └── site-packages/ # 存放安装的第三方包
# │
# ├── lib64/                 # 在某些系统中，这个目录包含与 `lib` 相同的内容
# │
# └── pyvenv.cfg             # 配置文件，保存虚拟环境的配置信息（例如 Python 版本）

# bin/ 目录：
#  包含虚拟环境的可执行文件和脚本，例如：
#  • activate：激活虚拟环境的脚本。
#  对于 macOS 和 Linux 系统使用 source .venv/bin/activate 来激活环境。
#  • python：指向虚拟环境中的 Python 解释器，
#  确保你在虚拟环境中运行的程序使用的是虚拟环境中的 Python。
#  • pip：包管理工具 pip，用于安装和管理包。
# lib/ 目录：
#  包含 Python 的标准库和在虚拟环境中安装的第三方包。
#  这个目录中的 site-packages/ 目录会存放你安装的所有 Python 库。
# include/ 目录：
#  如果你安装的某些库需要编译 C 扩展，它会用到这个目录。
#  通常对于 Python 开发来说不常用。
# pyvenv.cfg 文件：
#  配置文件，存储虚拟环境的元信息，
#  如使用的 Python 版本、虚拟环境的路径等。

# 激活虚拟环境
source .venv/bin/activate
# source：
#  这是一个 Linux/macOS 的命令，用于执行一个脚本。
#  这个命令会在当前的 shell 环境中激活虚拟环境。
# .venv/bin/activate：
#  这是虚拟环境中的 activate 脚本。
#  它位于 .venv 目录下的 bin 子目录中，运行它可以激活虚拟环境。
#  在 Windows 系统中，路径会是 .venv\Scripts\activate。

# 当你运行这条命令时，系统会激活虚拟环境，使得后续的 Python 命令都在该虚拟环境中执行。
# 此时，你的 shell 提示符通常会显示虚拟环境的名字，
# 比如 (.venv)，表示当前处于虚拟环境中。
# 激活虚拟环境后，你安装的包将只作用于该环境，而不会影响全局的 Python 环境。

# 在虚拟环境中安装 Flask
python3 -m pip install Flask
# python3：
#  表示使用 Python 3 版本来运行命令。
# -m：
#  运行指定模块，这里是运行 pip 模块。
# pip：
#  是 Python 包管理工具，用于安装和管理 Python 包。
# install：
#  是 pip 的一个命令，用来安装指定的包。
# Flask：
#  是你要安装的包名称。
#  Flask 是一个流行的 Python Web 框架，用于构建 web 应用。

# 这条命令的作用是使用 pip 包管理工具，在当前虚拟环境中安装 Flask 框架。
# 安装过程会下载 Flask 及其相关依赖包并将它们安装到虚拟环境中。
```

完整输出如下：

```bash
# 1. 创建虚拟环境
% python3 -m venv .venv
# 使用 python3 -m venv .venv 创建了一个名为 .venv 的虚拟环境。
# 2. 激活虚拟环境
% source .venv/bin/activate
# 激活了这个虚拟环境。
# 激活后，所有的 Python 命令都将在这个环境中运行，而不会影响全局的 Python 环境。
# 3. 安装 Flask
% python3 -m pip install Flask
# 使用 pip 安装 Flask 及其依赖包。安装过程会下载以下软件包：
# • Flask（核心框架）
# • Werkzeug（Flask 的 WSGI 工具）
# • Jinja2（模板引擎）
# • itsdangerous（用于安全性处理）
# • click（命令行工具）
# • blinker（事件处理）
# • MarkupSafe（用于保护 HTML 标签）
# 安装过程显示了这些依赖项的下载进度。
Collecting Flask
  Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting Werkzeug>=3.1 (from Flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from Flask)
  Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from Flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from Flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask)
  Downloading MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (4.0 kB)
Downloading flask-3.1.0-py3-none-any.whl (102 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
# 4. 安装成功
Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0
# 显示 Flask 和所有相关依赖包安装成功，具体安装的版本如下：
# • Flask 3.1.0
# • Jinja2 3.1.5
# • MarkupSafe 3.0.2
# • Werkzeug 3.1.3
# • blinker 1.9.0
# • click 8.1.8
# • itsdangerous 2.2.0

# 5. 提示 pip 有新版本
[notice] A new release of pip is available: 25.0 -> 25.0.1
[notice] To update, run: pip install --upgrade pip
# 提示 pip 有新版本（25.0.1），并建议你更新到最新版本。
```

</p></details></p>

---

### 3.2. 启动服务器

```bash
python app.py
# or
python3 app.py
```

### 3.3. 访问服务器

```bash
% python app.py
 * Serving Flask app 'app'
# 这行显示 Flask 正在启动并运行 app.py 文件中的应用程序。
# 这里的 'app' 是 Flask 应用对象的名称。
 * Debug mode: on
# 表示 Flask 正在以 调试模式 启动，这意味着任何代码的修改都会触发应用的自动重启，
# 并且你可以查看详细的错误信息。这个模式通常用于开发过程中。
WARNING: This is a development server. Do not use it in a production deployment.
# 警告信息，说明这个开发服务器仅用于开发和调试，不能用于生产环境。
# 在生产环境中，应该使用更强大的服务器，如 Gunicorn 或 uWSGI。
 * Running on all addresses (0.0.0.0)
# 表示 Flask 应用正在监听所有可用的网络接口（IP 地址），
# 这意味着应用不仅可以通过 localhost 访问，还可以通过局域网中的其他设备访问。
 * Running on http://127.0.0.1:5001
# Flask 应用正在本地服务器上运行，IP 地址是 127.0.0.1，端口号是 5001。
# 你可以通过浏览器访问 http://127.0.0.1:5001 查看应用。
 * Running on http://192.168.31.147:5001
# Flask 应用也可以通过局域网 IP 地址 192.168.31.147 访问，
# 这意味着在同一局域网内的其他设备也能访问该应用，前提是该设备可以访问该 IP 地址。
Press CTRL+C to quit
# 提示你可以按 CTRL+C 来停止 Flask 服务器的运行。
 * Restarting with stat
# 由于调试模式开启，当 Flask 检测到文件变化时，它会自动重启服务器。
# 这里 stat 表示 Flask 检查文件状态的方式。
 * Debugger is active!
# 表示 Flask 的调试器已启动。
# 如果有代码错误，调试器可以提供详细的堆栈跟踪，帮助你定位问题。
 * Debugger PIN: 779-321-427
# 这是调试器的 PIN（个人识别码），
# 如果你在调试过程中遇到问题，需要通过浏览器输入该 PIN 来访问调试界面。
```
