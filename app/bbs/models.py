from datetime import datetime
import json, os


class Post:
    """单个帖子的封装类"""

    def __init__(self, title, content, ip, author):
        self.title = title
        self.content = content
        self.ip = ip
        self.author = author
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "ip": self.ip,
            "author": self.author,
            "timestamp": self.timestamp,
        }

    def __getitem__(self, key):
        return self.to_dict()[key]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["title"],
            content=data["content"],
            ip=data["ip"],
            author=data["author"],
            timestamp=data["timestamp"],
        )


class PostModel:
    """帖子数据模型"""

    def __init__(self, filepath: str = "data/posts.json"):
        self._posts: list[Post] = []
        self._filepath = filepath
        self._ensure_directory()
        self._load_posts()

    def _ensure_directory(self):
        os.makedirs(os.path.dirname(self._filepath), exist_ok=True)

    def _save_posts(self):
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(
                [post.to_dict() for post in self._posts],
                f,
                ensure_ascii=False,
                indent=2,
            )

    def _load_posts(self):
        if os.path.exists(self._filepath):
            with open(self._filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._posts = [Post.from_dict(d) for d in data]

    def create_post(self, title: str, content: str, ip: str, author: str) -> Post:
        post = Post(title, content, ip, author)
        self._posts.append(post)
        self._save_posts()
        return post

    def get_all_posts(self) -> list[Post]:
        # 倒序返回，最新的帖子在前面
        return self._posts[::-1]

    def delete_post(self, post_index: int):
        """根据索引删除帖子 (索引基于倒序)"""
        real_index = len(self._posts) - 1 - post_index
        if 0 <= real_index < len(self._posts):
            self._posts.pop(real_index)
            self._save_posts()
