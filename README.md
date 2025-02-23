# local-server

简单的本地服务器

## 文件结构

```
local-server/
├── app.py
├── config.py
├── file_operations.py
├── views.py
├── templates/
│   └── index.html
├── .gitignore
├── LICENSE
└── README.md
```

结构说明

| 文件/目录            | 说明                                                          |
| -------------------- | ------------------------------------------------------------- |
| `app.py`             | 保持在项目根目录，作为启动 Flask 应用的主要文件。             |
| `config.py`          | 配置文件，包含上传文件夹、文件大小限制等配置信息。            |
| `file_operations.py` | 处理文件上传、下载等操作的逻辑。                              |
| `views.py`           | 存放视图函数，用来处理上传页面的呈现、文件列表、文件下载等。  |
| `templates/`         | 用于存放 HTML 模板文件，`index.html` 提供文件上传和展示功能。 |
| `.gitignore`         | 用于忽略不需要的文件或目录，如虚拟环境、编译文件等。          |
| `LICENSE`            | 项目的许可证文件。                                            |
| `README.md`          | 项目的说明文件，包含项目的介绍、功能、安装使用方法等。        |

## 运行

1. 安装 Flask

```bash
pip install Flask
# or
pip3 install Flask
```

2. 启动服务器

```bash
python app.py
# or
python3 app.py
```

3. 访问 http://localhost:5001 来上传文件和下载文件。
