import json
import os
from datetime import datetime


class Post:
    """封装单个帖子的类，包含标题、内容、作者、IP 和时间戳。"""

    def __init__(self, title, content, ip, author):
        """初始化一个新的 Post 实例。

        Args:
            title (str): 帖子标题。
            content (str): 帖子内容。
            ip (str): 发布者 IP 地址。
            author (str): 作者名称。
        """
        self.title = title
        self.content = content
        self.ip = ip
        self.author = author
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """将帖子转换为字典格式。

        Returns:
            dict: 包含帖子的标题、内容、IP、作者和时间戳的字典。
        """
        return {
            "title": self.title,
            "content": self.content,
            "ip": self.ip,
            "author": self.author,
            "timestamp": self.timestamp,
        }

    def __getitem__(self, key):
        """允许通过键访问帖子字段，如 dict 一样。

        Args:
            key (str): 字段名，例如 "title"。

        Returns:
            Any: 对应字段的值。
        """
        return self.to_dict()[key]

    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建 Post 实例。

        Args:
            data (dict): 包含帖子信息的字典。

        Returns:
            Post: 创建好的 Post 实例。
        """
        return cls(
            title=data["title"],
            content=data["content"],
            ip=data["ip"],
            author=data["author"],
        )


class PostModel:
    """管理帖子数据的模型类，支持创建、获取、删除帖子并保存到本地文件。"""

    def __init__(self, filepath: str = "data/posts.json"):
        """初始化 PostModel，自动加载已有帖子数据。

        Args:
            filepath (str, optional): 帖子数据保存路径，默认为 'data/posts.json'。
        """
        self._posts: list[Post] = []
        self._filepath = filepath
        self._ensure_directory()
        self._load_posts()

    def _ensure_directory(self):
        """确保帖子保存目录存在，若不存在则创建。
        """
        os.makedirs(os.path.dirname(self._filepath), exist_ok=True)

    def _save_posts(self):
        """将当前帖子列表保存到 JSON 文件中。
        """
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(
                [post.to_dict() for post in self._posts],
                f,
                ensure_ascii=False,
                indent=2,
            )

    def _load_posts(self):
        """从 JSON 文件加载帖子数据。
        """
        if os.path.exists(self._filepath):
            with open(self._filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._posts = [Post.from_dict(d) for d in data]

    def create_post(self, title: str, content: str, ip: str, author: str) -> Post:
        """创建一个新帖子并保存到文件。

        Args:
            title (str): 帖子标题。
            content (str):  帖子内容。
            ip (str): 发布者 IP。
            author (str): 作者名。

        Returns:
            Post: 新创建的帖子实例。
        """
        post = Post(title, content, ip, author)
        self._posts.append(post)
        self._save_posts()
        return post

    def get_all_posts(self) -> list[Post]:
        """获取所有帖子。

        Returns:
            list[Post]: 所有帖子组成的列表（按时间顺序）。
        """
        # 倒序返回，最新的帖子在前面
        return self._posts[::-1]
        # return self._posts

    def delete_post(self, post_index: int):
        """根据索引删除帖子（索引是倒序的，最新的为索引 0）。

        Args:
            post_index (int): 倒序索引位置的帖子编号。
        """
        real_index = len(self._posts) - 1 - post_index
        if 0 <= real_index < len(self._posts):
            self._posts.pop(real_index)
            self._save_posts()
