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
python3 run.py
```

## 2. 文件结构

```python
local-server/
├── run.py  # 应用启动入口
│
├── app/
│   ├── __init__.py  # 初始化 Flask 应用，注册蓝图 (blueprint)
│   │ 
│   ├── file/                   # 文件模块
│   │   ├── __init__.py         # 注册 file blueprint
│   │   ├── routes.py           # 路由注册
│   │   ├── handlers.py         # 上传、下载、删除处理逻辑
│   │   ├── file_operations.py  # 文件操作函数
│   │   ├── utils.py            # 工具函数
│   │   ├── static/
│   │   └── templates/          # 文件模块独立模板
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config.py  # 配置文件
│   │   └── port.py    # 获取端口输入的逻辑
│   │
│   ├── config.py   # 配置管理
│   ├── static/
│   └── templates/  # 公共模板目录
│
├── uploads/
│
├── venv/      # Python 虚拟环境，用于安装 Flask 和其他依赖的包
├── LICENSE    # 项目的许可证文件
├── README.md  # 项目的说明文件，包含项目的介绍、功能、安装使用方法等
└── ...
```
