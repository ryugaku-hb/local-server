// 当整个文档加载完成后执行
document.addEventListener("DOMContentLoaded", function () {
  // 获取发帖表单元素
  // <form id="post-form" action="..." method="post"> </from>
  const form = document.querySelector("#post-form");

  // 如果页面上没有找到表单，打印错误并中止
  if (!form) {
    console.error("⚠️ post-form not found!");
    return;
  }
  // 给表单添加提交事件的监听器
  form.addEventListener("submit", function (e) {
    // 阻止默认提交行为（防止页面刷新）
    e.preventDefault();
    // 使用 FormData 自动收集表单数据
    const formData = new FormData(form);

    // 发送异步 POST 请求，将表单数据提交到服务器
    fetch(form.action, {
      method: "POST",
      body: formData, // 直接提交 FormData，会自动处理 multipart/form-data
    })
      .then((response) => {
        // 如果响应状态不是 200~299，则抛出错误
        if (!response.ok) throw new Error("提交失败");
        return response.text(); // 解析返回的 HTML 内容
      })
      .then((html) => {
        // 将返回的新帖子列表 HTML 替换到页面中
        document.querySelector("#post-list-container").innerHTML = html;
        // 清空表单内容（重置）
        form.reset();
      })
      .catch((err) => {
        // 如果网络请求出错，打印错误信息
        console.error("网络错误：", err);
      });
  });
});
