import os

# 从环境变量中读取配置（如果没有，使用默认值）
# 配置上传目录
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")  # 上传目录 uploads
# 配置最大上传文件大小
MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 100 * 1024 * 1024))  # 100 MB
# 允许上传的文件类型
ALLOWED_EXTENSIONS = {
    "txt",
    "pdf",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "ppt",
    "pptx",
    "png",
    "jpg",
    "jpeg",
    "gif",
    "mp4",
    "mov",
    "avi",
}

# 配置端口
PORT = int(os.getenv("PORT", 5002))

# 创建上传目录（如果不存在）
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
