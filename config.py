import os

# 配置上传目录
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 配置最大上传文件大小
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB
