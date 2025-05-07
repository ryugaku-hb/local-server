// 当整个文档加载完成后执行
document.addEventListener("DOMContentLoaded", function () {
  // 获取发帖表单元素
  const form = document.querySelector("#post-form");
  const authorInput = document.querySelector("#author");

  // 如果页面上没有找到表单，打印错误并中止
  if (!form) {
    console.error("⚠️ post-form not found!");
    return;
  }

  restoreAuthor(authorInput);
  bindFormSubmit(form, authorInput);
});

/**
 * 为发帖表单绑定提交事件处理逻辑，包括表单异步提交、作者保存与恢复、帖子列表更新等。
 *
 * @param {HTMLFormElement} formEl - 发帖表单元素，必须存在。
 * @param {HTMLInputElement|null} authorInput - 作者名输入框元素，用于保存和恢复作者信息。可选。
 */
function bindFormSubmit(formEl, authorInput) {
  formEl.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(formEl);

    saveAuthor(authorInput);

    fetch(formEl.action, {
      method: "POST",
      body: formData,
    })
      .then((res) => {
        if (!res.ok) throw new Error("提交失败");
        return res.text();
      })
      .then((html) => {
        updatePostList(html);
        formEl.reset();
        restoreAuthor(authorInput); // 提交后恢复作者名
      })
      .catch((err) => console.error("网络错误：", err));
  });
}

/**
 * 用新的 HTML 内容更新页面上的帖子列表容器（#post-list-container）。
 *
 * @param {string} html - 从服务器返回的 HTML 字符串，用于替换原有帖子列表内容。
 */
function updatePostList(html) {
  const container = document.querySelector("#post-list-container");
  if (container) {
    container.innerHTML = html;
  } else {
    console.warn("⚠️ 无法找到 #post-list-container 容器");
  }
}

/**
 * 从 localStorage 中恢复作者名称，并填充到输入框中。
 *
 * @param {HTMLInputElement|null} inputEl - 目标输入框元素。如果为空或无效，则不执行任何操作。
 */
function restoreAuthor(inputEl) {
  if (!inputEl) return;
  const savedValue = localStorage.getItem("bbs_author");
  if (savedValue) {
    inputEl.value = savedValue;
  }
}

/**
 * 将输入框中的作者名称保存到 localStorage。
 * 如果输入为空则删除原有记录。
 *
 * @param {HTMLInputElement|null} inputEl - 目标输入框元素。如果为空或无效，则不执行任何操作。
 */
function saveAuthor(inputEl) {
  if (!inputEl) return;
  const val = inputEl.value.trim();
  if (val) {
    localStorage.setItem("bbs_author", val);
  } else {
    localStorage.removeItem("bbs_author");
  }
}
