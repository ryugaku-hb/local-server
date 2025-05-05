# 技术知识点整理

本项目使用了前后端相关技术，以下为按模块整理的知识点，便于查阅和复习。

- [4. JavaScript - DOM 操作](#4-javascript---dom-操作)
  - [4.1. 获取与修改 DOM 元素](#41-获取与修改-dom-元素)
  - [4.2. 创建与插入元素](#42-创建与插入元素)
- [5. JavaScript - DOM 事件监听](#5-javascript---dom-事件监听)
  - [5.1. 常见事件类型](#51-常见事件类型)
  - [5.2. DOMContentLoaded - 文档加载完成后执行初始化代码](#52-domcontentloaded---文档加载完成后执行初始化代码)
  - [5.3. submit - 表单提交事件](#53-submit---表单提交事件)
- [6. JavaScript - 异步交互与数据处理](#6-javascript---异步交互与数据处理)
  - [6.1. fetch API 使用](#61-fetch-api-使用)
  - [6.2. FormData](#62-formdata)
  - [6.3. Promise](#63-promise)
    - [6.3.1. 链式调用（Promise chaining）](#631-链式调用promise-chaining)


### 3.3. DOM 操作

#### 3.3.1. 元素查找

- `document.getElementById(id)` - 通过 id 获取单个元素
- `getElementsByClassName(class)`
- `getElementsByTagName(tag)`

🔶 语法

```js
// 获取指定 class 的所有元素（HTMLCollection）
var elements = document.getElementsByClassName(names);
var elements = element.getElementsByClassName(names);

// 获取指定标签的所有元素（HTMLCollection）
var elements = document.getElementsByTagName(name);
var elements = element.getElementsByTagName(tagName);
```

- `querySelector(selector)`
- `querySelectorAll(selector)`

🔶 语法

```js
// 返回匹配 CSS 选择器的第一个元素
var element = document.querySelector(selectors);
var element = baseElement.querySelector(selectors);

// 返回匹配 CSS 选择器的所有元素（NodeList）
var elementList = document.querySelectorAll(selectors);
var elementList = baseElement.querySelectorAll(selectors);
```

```js
// 查找文档中第一个类名为 "myclass" 的元素
var el = document.querySelector(".myclass");

// 查找文档里第一个没有 type 属性
// 或有值为 “text/css 的 type 属性的 <style> 元素
let el = document.body.querySelector(
  "style[type='text/css'], style:not([type])"
);
```

```js
// 查找文档中所有 <p> 元素的 NodeList
var matches = document.querySelectorAll("p");
// 查找文档中所有 <div> 元素的列表，其中 class 包含 "note" 或 "alert"
var matches = document.querySelectorAll("div.note, div.alert");

// 查找文档中的 body 元素的所有 <p> 后代元素
var matches = document.body.querySelectorAll("p");
```

🔹 访问匹配项

```js
var highlightedItems = userList.querySelectorAll(".highlighted");

highlightedItems.forEach(function (userItem) {
  deleteUser(userItem);
});
```

#### 3.3.2. 文档节点

- `document` - 表示整个 HTML 文档对象

🔹 文档结构访问

- `document.body` - 获取 `<body>` 元素
- `document.head` - 获取 `<head>` 元素
- `document.title` - 获取／设置文档标题
- `document.documentElement` - 根元素 `<html>`
- `document.URL` - 当前文档的完整 URL
- `document.domain`
- `document.referrer`

🔹 元素创建

- `document.createElement(tagName)` - 创建一个新的 HTML 元素
- `document.createTextNode(text)` - 创建一个文本节点

#### 3.3.3. 节点与元素操作

🔹 内容读写

- `element.innerHTML` - 获取／设置元素内的 HTML 内容
- `element.textContent` - 获取／设置元素内的纯文本内容

🔹 节点关系

- `element.parentNode` - 父节点
- `element.children` - 子元素集合（不含文本）
- `element.childNodes` - 所有子节点（含文本／空格）

* `element.firstChild` - 第一个子节点
* `element.lastChild` - 最后一个子节点
* `element.nextSibling` - 下一个兄弟节点
* `element.previousSibling` - 上一个兄弟节点

- nodeType
- nodeName

🔹 属性操作

- `element.setAttribute(name, value)` - 设置属性
- `element.getAttribute(name)` - 获取属性值
- `element.removeAttribute(name)` - 移除属性

- hasAttribute() - 判断属性是否存在

* dataset - 获取所有 `data-*` 属性对象

🔹 类名操作

- `element.classList.add()` - 添加类型
- `element.classList.remove()` - 移除类名
- `element.classList.toggle()` - 切换类名
- contains()

🔹 插入与移除

- `element.appendChild(child)` - 将子元素添加到元素尾部
- `element.prepend(child)` - 将子元素添加到元素开头
- `element.insertBefore(new, reference)` - 将新节点插入到参考节点前

* `element.insertAdjacentHTML(position, html)` - 将 HTML 字符串插入指定位置（如 `"beforeend"`）

- `element.removeChild(child)` 移除子节点
- `element.remove()` - 删除当前节点

#### 3.3.4. 浏览器窗口与样式

- `window` - 全局窗口对象（默认作用域）

🔹 滚动与尺寸

- window.scrollTo(x, y) - 滚动到页面指定位置
- window.scrollBy(dx, dy)
- window.innerWidth - 视口大小
- window.innerHeight

🔹 样式处理

- getComputedStyle(element) - 获取某元素的最终计算样式
- element.style.property - 内联样式设置（如 `element.style.color = 'red'`）

🔹 弹窗

- alert() - 弹窗提示
- confirm()
- prompt()

🔹 定时

- setTimeout(fn, ms) - 延时执行函数
- clearTimeout(id)
- setInterval(fn, ms) - 每隔一段时间重复执行函数
- clearInterval(id)

#### 3.3.5. 事件机制

- `element.addEventListener(type, handler)` - 添加事件监听器
- `element.removeEventListener(type, handler)` - 移除事件监听器

* `element.onclick = function` - 设置点击事件（不推荐混用）

🔹 常见事件类型
• click, mouseover, input, submit, change, keydown, load, DOMContentLoaded

🔹 事件对象属性

- event.target - 触发事件的元素
- event.currentTarget - 监听器绑定的元素
- event.preventDefault() - 阻止默认行为
- event.stopPropagation() - 阻止事件冒泡

## 4. JavaScript - DOM 操作

### 4.1. 获取与修改 DOM 元素

```js
const el = document.querySelector("#my-id"); // 获取 ID 元素
el.textContent = "新文本内容"; // 修改文本内容
el.innerHTML = "<strong>加粗内容</strong>"; // 修改 HTML 内容
el.classList.add("active"); // 添加类
el.classList.remove("hidden"); // 移除类
el.classList.toggle("open"); // 切换类状态
```

| 方法                 | 说明                                              |
| -------------------- | ------------------------------------------------- |
| `querySelector()`    | 返回匹配的第一个元素（支持 CSS 选择器）           |
| `classList.add()`    | 添加 class                                        |
| `classList.remove()` | 移除 class                                        |
| `classList.toggle()` | 切换 class 是否存在                               |
| `setAttribute()`     | 设置属性（如 `el.setAttribute('name', 'value')`） |
| `remove()`           | 从 DOM 中移除元素                                 |

| 属性          | 说明                    |
| ------------- | ----------------------- |
| `textContent` | 设置／获取元素纯文本    |
| `innerHTML`   | 设置／获取元素内部 HTML |

### 4.2. 创建与插入元素

```js
const div = document.createElement("div");
div.textContent = "我是新元素";
document.body.appendChild(div); // 插入到 body 最后
```

| 方法                     | 说明                                  |
| ------------------------ | ------------------------------------- |
| `createElement(tag)`     | 创建新元素（如 `div` `li` `span` 等） |
| `appendChild(node)`      | 添加为子元素（放在最后）              |
| `prepend(node)`          | 添加为第一个子元素（放在最前）        |
| `insertBefore(new, ref)` | 插入到指定元素前                      |

## 5. JavaScript - DOM 事件监听

### 5.1. 常见事件类型

| 事件类型       | 说明                                 |
| -------------- | ------------------------------------ |
| `click`        | 点击                                 |
| `input`        | 输入内容变更时触发（实时）           |
| `change`       | 输入后失焦（如 `select` `checkbox`） |
| `focus` `blur` | 获取／失去焦点                       |
| `keydown`      | 键盘按下                             |
| `submit`       | 表单提交                             |
| `mouseover`    | 鼠标悬停                             |

```js
inputEl.addEventListener("input", (e) => {
  console.log("当前值：", e.target.value);
});
```

### 5.2. DOMContentLoaded - 文档加载完成后执行初始化代码

当 HTML 文档被完全加载和解析完成之后触发（不需要等待样式表、图片等外部资源加载完成）。

```js
// .addEventListener() 给 DOM 元素添加事件监听器
document.addEventListener("DOMContentLoaded", function () {
  // 页面初始化逻辑，如获取 DOM 元素、绑定事件等
});
```

| 特点     | 说明                                                     |
| -------- | -------------------------------------------------------- |
| 触发时机 | 当 HTML 文档完全加载和解析完成（不包括图片、样式等资源） |
| 常见用途 | 初始化事件监听器、获取 DOM 元素                          |
| 事件对比 | `window.onload` 会等待所有资源加载（包括图片）           |

### 5.3. submit - 表单提交事件

用户点击 `<button type="submit">` 或按回车提交表单时触发。

```js
// .addEventListener() 给 DOM 元素添加事件监听器
form.addEventListener("submit", function (e) {
  // 浏览器会向表单的 action 地址发起请求，并刷新页面。
  // e.preventDefault() 阻止默认事件行为（如表单提交刷新）
  e.preventDefault();
  // 自定义表单处理逻辑
});
```

| 特点         | 说明                                             |
| ------------ | ------------------------------------------------ |
| 触发时机     | 表单被提交时（用户点击提交按钮或按回车）         |
| 默认行为     | 向 `form.action` 发送请求并刷新页面              |
| 阻止默认提交 | 使用 `e.preventDefault()` 避免刷新，实现异步处理 |

```js
// submit 触发时机是用户提交表单（如点击 <button type="submit">）
form.addEventListener("submit", function (e) {
  e.preventDefault(); // 阻止浏览器默认刷新页面行为

  const formData = new FormData(form); // 收集表单数据

  // fetch(form.action): 向指定地址发送异步 POST 请求
  // form.action: 获取表单的提交地址
  // Content-Type: 提交 FormData 时不需要手动设置，
  // 浏览器自动使用 multipart/form-data 并附带边界信息
  fetch(form.action, {
    method: "POST",
    body: formData,
  })
    .then((res) => {
      if (!res.ok) throw new Error("提交失败");
      return res.text(); // 假设返回的是 HTML 片段
    })
    .then((html) => {
      document.querySelector("#post-list-container").innerHTML = html;
      // form.reset(): 提交完成后清空输入内容
      form.reset(); // 清空表单
    })
    .catch((err) => {
      console.error("网络错误：", err);
    });
});
```

## 6. JavaScript - 异步交互与数据处理

### 6.1. fetch API 使用

`fetch()` 是现代 JavaScript 中用于 **发送 HTTP 请求** 的 API，是 `XMLHttpRequest` 的替代品。

🔹 基础语法

```js
fetch("https://api.example.com/data")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

🔹 常见请求示例

```js
// 发送 GET 请求
fetch("http://example.com/movies.json")
  .then((response) => response.json())
  .then((data) => console.log(data));∏

// 发送 POST 请求（JSON 格式）
fetch("/api/login", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ username: "alice", password: "1234" }),
});
```

### 6.2. FormData

`FormData` 接口可用于构造键值对形式的表单数据，常用于上传文件或复杂表单提交。

🔹 创建 `FormData` 对象

```js
// 1. 从表单自动创建
const form = document.querySelector("form");
const formData = new FormData(form);

// 2. 手动添加字段
const formData = new FormData();
formData.append("username", "Alice");
formData.append("file", fileInput.files[0]);
```

🔹 搭配 `fetch()` 发送请求

```js
fetch("/upload", {
  method: "POST",
  body: formData,
});
```

⚠️ 注意事项

- 不需要手动设置 `Content-Type`，浏览器会自动添加 `multipart/form-data` 并设置边界（boundary）。
- 若使用 `<input type="file">` 上传文件，需确保表单含有 `enctype="multipart/form-data"`。
- 后端必须支持并解析 `multipart/form-data` 编码格式，否则无法正确接收文件和表单字段。

### 6.3. Promise

📌 创建一个 `Promise`

```js
// 创建一个新的 Promise 实例
const myPromise = new Promise((resolve, reject) => {
  const success = true; // 模拟操作是否成功

  if (success) {
    // 操作成功时，调用 resolve()，将结果传出
    resolve("操作成功！");
  } else {
    // 操作失败时，调用 reject()，传出错误信息
    reject("出错了！");
  }
});
```

📌 使用 `.then()` 和 `.catch()` 处理

```js
myPromise
  .then((result) => {
    // 如果 Promise 状态为 fulfilled（已成功），执行这里的回调函数
    console.log("成功：", result); // 输出：成功：操作成功！
  })
  .catch((error) => {
    // 如果 Promise 状态为 rejected（已失败），执行这里的回调函数
    console.error("失败：", error); // 如果失败会输出：失败：出错了！
  });
```

#### 6.3.1. 链式调用（Promise chaining）

```js
// 创建一个立即 resolve 的 Promise，初始值为 1
new Promise((resolve) => {
  resolve(1); // 第一步：传出数字 1
})
  .then((num) => {
    console.log("第一步：", num); // 输出：第一步：1
    return num + 1; // 返回的新值将传入下一个 then
  })
  .then((num) => {
    console.log("第二步：", num); // 输出：第二步：2
    return num * 2; // 继续传递给下一个 then
  })
  .then((num) => {
    console.log("第三步：", num); // 输出：第三步：4
    // 这里没有返回值也可以，链式调用到此为止
  });
```

每一个 `.then()` 返回的值，都会传给下一个 `.then()`，形成链式调用；如果中间任何一个 `.then()` 抛出错误，就会跳到 `.catch()`（如果有）。

📌 `fetch` + `Promise` 示例（带 `FormData`）

```js
// 获取页面中第一个 form 元素
const form = document.querySelector("form");

// 使用 FormData 自动收集表单中的所有字段（包括文件）
const formData = new FormData(form);

// 使用 fetch 发起异步请求，向服务器提交表单数据
fetch("/submit", {
  method: "POST", // 使用 POST 方法
  body: formData, // 直接传入 FormData，浏览器会自动设置 multipart/form-data 类型
})
  .then((res) => {
    // 检查响应状态码是否是成功（200-299）
    if (!res.ok) throw new Error("请求失败");

    // 返回解析后的 JSON 数据（也可以是 res.text(), res.blob() 等）
    return res.json();
  })
  .then((data) => {
    // 处理后端返回的数据
    console.log("响应数据：", data);
  })
  .catch((err) => {
    // 网络错误或上面手动抛出的错误
    console.error("错误：", err);
  });
```
