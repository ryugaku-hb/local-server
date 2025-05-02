# local-server

简单的本地服务器

## 1. 极速上手

```bash
# 仅首次使用
python3 -m venv venv          # 创建虚拟环境
source venv/bin/activate      # 激活虚拟环境（Linux/Mac）
python3 -m pip install Flask  # 在虚拟环境中安装 Flask

# 再次使用
source venv/bin/activate      # 激活已存在的虚拟环境

# 启动服务器
python3 app.py
```

## 2. 文件结构

```python
local-server/
├── app.py  # 应用启动入口
│
├── app/
│   ├── __init__.py
│   ├── config.py  # 配置管理，包含上传文件夹、文件大小限制等配置信息
│   ├── routes.py  # 路由注册
│   ├── views.py   # 页面逻辑
│   ├── file_operations.py  # 文件操作，处理文件上传、下载等操作的逻辑
│   ├── utils.py   # 工具函数
│   ├── static/
│   └── templates/
│
├── uploads/
│
├── venv/      # Python 虚拟环境，用于安装 Flask 和其他依赖的包
├── LICENSE    # 项目的许可证文件
├── README.md  # 项目的说明文件，包含项目的介绍、功能、安装使用方法等
└── ...
```
