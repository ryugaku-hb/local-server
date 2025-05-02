# 1. 模板说明

- [1. 模板说明](#1-模板说明)
  - [1.1. index.html](#11-indexhtml)
    - [1.1.1. 代码分析](#111-代码分析)
    - [1.1.2. 🏷️ 分隔符](#112-️-分隔符)
    - [1.1.3. 🏷️ include 标签：嵌入模板片段](#113-️-include-标签嵌入模板片段)
    - [1.1.4. 🏷️ 模板继承](#114-️-模板继承)
      - [1.1.4.1. extends 标签：模板继承](#1141-extends-标签模板继承)
      - [1.1.4.2. block 标签：定义可覆盖区域](#1142-block-标签定义可覆盖区域)
      - [1.1.4.3. 基础模板](#1143-基础模板)
      - [1.1.4.4. 子模板](#1144-子模板)
      - [1.1.4.5. `super()` 用法](#1145-super-用法)
      - [1.1.4.6. 嵌套扩展](#1146-嵌套扩展)
      - [1.1.4.7. 命名区块结束标签](#1147-命名区块结束标签)
  - [1.2. base.html](#12-basehtml)
    - [1.2.1. 代码分析](#121-代码分析)
  - [1.3. partials/\_flash\_messages.html](#13-partials_flash_messageshtml)
    - [1.3.1. 代码分析](#131-代码分析)
    - [1.3.2. with 标签：定义局部变量](#132-with-标签定义局部变量)
    - [1.3.3. if 标签：条件判断](#133-if-标签条件判断)
    - [1.3.4. for 标签：遍历可迭代对象](#134-for-标签遍历可迭代对象)
  - [1.2.4. partials/\_upload\_form.html](#124-partials_upload_formhtml)
    - [1.2.5. 代码分析](#125-代码分析)
  - [1.4. partials/\_file\_list.html](#14-partials_file_listhtml)
    - [1.4.1. 代码分析](#141-代码分析)

## 1.1. index.html

```Jinja
{% extends "base.html" %}
{% block title %}本地文件服务器 Local File Server{% endblock %}
{% block content %}
  {% include "./partials/_flash_messages.html" %}
  <h1 class="display-4 text-center mb-4">上传和下载文件</h1>
  {% include "./partials/_upload_form.html" %}
  {% include "./partials/_file_list.html" %}
{% endblock %}
```

### 1.1.1. 代码分析

```jinja
{% extends "base.html" %}
<!-- 当前模板 继承 自 base.html，也就是说，
渲染时会以 base.html 为骨架，并替换或补充其中的 block 区域。 -->
<!-- ✅ {% ... %} 是 Jinja 模板语法 中的「语句语法」，用来表示控制语句或结构指令。 -->

<!-- 设置页面的标题 -->
<!-- 此处设置的是网页的标题栏内容，指示该网页是一个本地文件服务器页面。 -->
{% block title %}本地文件服务器 Local File Server{% endblock %}
<!-- 替换 title 区块 -->
<!-- 这个 block title 会替换 base.html 中的: -->
<title>{% block title %}本地文件服务器{% endblock %}</title>
<!-- 渲染后变成: -->
<title>本地文件服务器 Local File Server</title>

{% block content %}
<!-- 开始重写 base.html 中的 content 块，填充当前页面的具体内容 -->
<!-- 替换 content 区块 -->
{% block content %}
  ...
{% endblock %}
<!-- 会替换掉 base.html 中的: -->
<div class="container my-5">
  {% block content %}{% endblock %}
</div>

  <!-- 用来显示提示消息 (如操作成功或失败) -->
  <!-- 通常这个文件用于显示一闪而过的提示信息，如「上传成功」或「删除失败」等。 -->
  {% include "./partials/_flash_messages.html" %}
  <!-- 表示将 ./partials/_flash_messages.html 这个文件的内容原封不动插入到这里 -->

  <!-- 主标题 -->
  <!-- 用的是 Bootstrap 的样式类。 -->
  <!-- 渲染出来就是个大标题，居中，底部带点间距，内容是：「上传和下载文件」。 -->
  <h1 class="display-4 text-center mb-4">上传和下载文件</h1>

  <!-- 上传表单 -->
  <!-- 这一行会插入一个用于上传文件的 HTML 表单，
  通常包含 <form>、<input type="file"> 和提交按钮等内容。 -->
  {% include "./partials/_upload_form.html" %}

  <!-- 文件列表 -->
  <!-- 这一行会插入显示当前已上传文件列表的 HTML 代码，
  比如一个 <ul> 或 <table>，展示文件名、大小、下载链接等。 -->
  {% include "./partials/_file_list.html" %}

{% endblock %}
<!-- 结束 content 块 -->
```

### 1.1.2. 🏷️ 分隔符

```jinja
<!-- Jinja 支持几种分隔符。
默认的 Jinja 分隔符配置如下: -->

{% ... %}
<!-- 用于语句 (Statements) -->
{{ ... }}
<!-- 用于表达式 (Expressions)，打印到模板输出 -->
{# ... #}
<!-- 用于注释，这些注释不会被包含在模板输出中 -->

<!-- Jinja 使用 {% ... %}、{{ ... }} 和 {# ... #} 来分别定义语句、表达式和注释。 -->
```

### 1.1.3. 🏷️ include 标签：嵌入模板片段

```jinja
<!-- 用于引入其他模板文件的内容，并将其渲染结果嵌入当前模板中。 -->
<!-- 常用于复用页面结构片段，例如：导航栏、页眉、页脚、表单、消息提示等。 -->

{% include 'header.html' %}
<!-- header.html 的内容将在此处渲染输出 -->

<main>
  <h1>页面主体内容</h1>
</main>

{% include 'footer.html' %}
<!-- footer.html 的内容将在此处渲染输出 -->
```

### 1.1.4. 🏷️ 模板继承

#### 1.1.4.1. extends 标签：模板继承

```jinja
<!-- 用于继承另一个模板 (通常是基础模板)，实现代码复用和统一布局。 -->
{% extends "base.html" %}
<!-- 这表示当前模板继承了 base.html，并可以在其中覆盖其定义的 block 内容。 -->
```

#### 1.1.4.2. block 标签：定义可覆盖区域

```jinja
<!-- 定义一个可以被子模板重写的内容块。这在模板继承时很重要。 -->

<!-- 父模板中的写法 (如 base.html) -->
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}默认标题{% endblock %}</title>
  </head>
  <body>
    <header>统一头部</header>
    <main>
      {% block content %}默认内容{% endblock %}
    </main>
    <footer>统一页脚</footer>
  </body>
</html>

<!-- 子模板中的写法 -->
{% extends "base.html" %}

{% block title %}本地文件服务器 Local File Server{% endblock %}

{% block content %}
  <h1>欢迎来到本地服务器</h1>
  <p>请上传您的文件。</p>
{% endblock %}

<!-- 这会替换掉 base.html 中的 title 和 content 块内容。 -->

<!-- 一个模板中只能有一个 {% extends %};
但可以有多个 {% block %};
block 必须出现在父模板和子模板中名称一致才能生效;
如果子模板未覆盖某个 block，父模板中的默认内容会被保留。 -->
```

#### 1.1.4.3. 基础模板

```jinja
<!-- 这是一个基础模板 base.html，
它定义了一个简单的 HTML 骨架文档，适用于一个简单的两栏页面。
子模板的任务是填充空的区块 (block) -->

<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>

<!-- 在这个例子中，{% block %} 标签定义了四个区块，子模板可以填充这些区块。
block 标签仅仅是告诉模板引擎，子模板可能会覆盖这些占位符。 -->

<!-- block 标签可以位于其他区块 (如 if) 内，
但无论 if 区块是否被渲染，block 标签都会被执行。 -->
```

#### 1.1.4.4. 子模板

```jinja
<!-- {% extends %} 标签是关键。
它告诉模板引擎这个模板「扩展“另一个模板。 -->

{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color:#336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}

<!-- 当模板引擎解析这个模板时，它首先会查找父模板。
extends 标签应该是模板中的第一个标签，放在它前面的内容会被直接打印出来，可能会引起混淆。 -->

<!-- 因为子模板没有定义 footer 区块，所以父模板中的值会被使用。 -->
```

#### 1.1.4.5. `super()` 用法

```jinja
<!-- 可以通过调用 super() 来渲染父模板的区块内容。
这会返回父模板区块的结果: -->

{% block sidebar %}
    <h3>Table Of Contents</h3>
    ...
    {{ super() }}
{% endblock %}
```

#### 1.1.4.6. 嵌套扩展

```jinja
<!-- 当有多个 {% extends %} 层级时，
可以链式使用 `super()` 来跳过继承树中的某一层。 -->

# parent.tmpl
body: {% block body %}Hi from parent.{% endblock %}

# child.tmpl
{% extends "parent.tmpl" %}
{% block body %}Hi from child. {{ super() }}{% endblock %}

# grandchild1.tmpl
{% extends "child.tmpl" %}
{% block body %}Hi from grandchild1.{% endblock %}

# grandchild2.tmpl
{% extends "child.tmpl" %}
{% block body %}Hi from grandchild2. {{ super.super() }}{% endblock %}
```

```jinja
<!-- 渲染 child.tmpl 会输出:
body: Hi from child. Hi from parent. -->

<!-- 渲染 grandchild1.tmpl 会输出:
body: Hi from grandchild1. -->

<!-- 渲染 grandchild2.tmpl 会输出:
body: Hi from grandchild2. Hi from parent. -->
```

#### 1.1.4.7. 命名区块结束标签

```jinja
<!-- Jinja 允许你在结束标签后写出区块的名称，以提高可读性: -->

{% block sidebar %}
    {% block inner_sidebar %}
        ...
    {% endblock inner_sidebar %}
{% endblock sidebar %}
<!-- 但是，endblock 后的名称必须与区块名称匹配。 -->
```

## 1.2. base.html

```jinja
<!DOCTYPE html>
<html lang="zh">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="本地文件服务器，提供简单的文件上传和下载功能" />
    <meta name="keywords" content="本地文件服务器, 文件上传, 文件下载, Python, 网络服务器" />
    <title>
      {% block title %}本地文件服务器{% endblock %}
    </title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" />
    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/styles.css') }}" />
  </head>
  <body>
    <div class="container my-5">
      {% block content %}{% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/flash_messages.js') }}"></script>
  </body>
</html>
```

### 1.2.1. 代码分析

```jinja
<!DOCTYPE html>
<html lang="zh">

  <head>
    <!-- 设置字符编码为 UTF-8，以支持多语言字符 -->
    <meta charset="UTF-8" />
    <!-- 设置视口，确保页面在不同设备上自适应布局 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- 提供页面的简短描述，有助于 SEO -->
    <meta name="description" content="本地文件服务器，提供简单的文件上传和下载功能" />
    <!-- 提供相关的关键词，有助于 SEO（尽管现代搜索引擎不太依赖此标签） -->
    <meta name="keywords" content="本地文件服务器, 文件上传, 文件下载, Python, 网络服务器" />

    <title>
      {% block title %}本地文件服务器{% endblock %}
    </title>
    <!-- 页面标题块，子模板可以覆盖 -->
    <!-- 使用 Flask 的模板块，提供一个可替换的标题，默认为“本地文件服务器” -->

    <!-- 引入 Bootstrap CSS，提供响应式布局和基础样式  -->
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" />

    <!-- 引入外部的 CSS 样式文件，用于自定义样式 -->
    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/styles.css') }}" />
    <!-- url_for(): flask.url_for() 函数。 -->

  </head>

  <body>
    <!-- 创建响应式容器，添加上下边距 -->
    <div class="container my-5">

      {% block content %}{% endblock %}
      <!-- 页面内容部分占位符，允许子模板自定义内容 -->

    </div>

    <!-- 引入 Bootstrap JS，支持 Bootstrap 组件的交互行为 -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

    <!-- 引入新的 JavaScript 文件 -->
    <script src="{{ url_for('static', filename='js/flash_messages.js') }}"></script>
    <!-- url_for(): flask.url_for() 函数。 -->

  </body>
</html>
```

## 1.3. partials\/\_flash_messages.html

```jinja
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <div id="flash-message"
         class="alert alert-info alert-dismissible fade show"
         role="alert">
      <ul class="mb-0">
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
      </ul>
      <button type="button"
              class="btn-close"
              data-bs-dismiss="alert"
              aria-label="Close"></button>
    </div>
  {% endif %}
{% endwith %}
```

### 1.3.1. 代码分析

```jinja
<!-- 获取当前请求中所有闪现 (flash) 消息 -->
{% with messages = get_flashed_messages() %}
<!-- 使用 get_flashed_messages() 函数获取当前请求中的所有闪现消息 -->
<!-- ✅ with 标签用于定义一个新的局部变量，作用范围仅限于 with 标签内部。
这意味着 messages 变量会在 with 块内创建，并且可以在 with 块内使用。 -->
<!-- 这里通过 get_flashed_messages() 函数获得闪存消息，
将其赋值给 messages 变量，之后的模板代码就可以使用这个变量了。 -->

  <!-- 如果存在闪现消息，则显示消息框 -->
  {% if messages %}
  <!-- ✅ if 标签用于判断 messages 是否有值。
  在这里，它用于检查是否有待显示的闪存消息。 -->
  <!-- 如果 messages 列表中有内容 (即存在闪存消息)，
  则 if 块内部的 HTML 会被渲染并显示在页面上；
  如果没有消息，则什么也不显示。 -->

    <!-- 使用 Bootstrap 的警告框样式，`alert-info` 表示信息类型的消息 -->
    <div id="flash-message"
         class="alert alert-info alert-dismissible fade show"
         role="alert">

      <!-- 创建一个无序列表来显示所有消息 -->
      <ul class="mb-0">
        <!-- 遍历所有闪现消息，并以列表项显示 -->
        {% for message in messages %}
        <!-- 通过 { % for message in messages % } 循环遍历所有的闪现消息，并在页面上显示为列表项 -->
        <!-- ✅ for 标签用于循环遍历 messages 中的每一条消息，
        并将它们显示在 HTML 列表中。 -->
        <!-- 对于 messages 列表中的每一条消息，
        都会创建一个 <li> 元素，显示消息内容。
        这里假设 messages 是一个字符串列表 (例如：['Message 1', 'Message 2'])，
        每个字符串会被渲染成一个 li 标签。 -->
          <li>{{ message }}</li>
        {% endfor %}
      </ul>

      <button type="button"
              class="btn-close"
              data-bs-dismiss="alert"
              aria-label="Close"></button>
    </div>
    <!-- 使用 Bootstrap 提供的关闭按钮，点击后会关闭该消息框 -->

  {% endif %}
{% endwith %}
```

### 1.3.2. with 标签：定义局部变量

```jinja
<!-- with 标签用于在模板中定义局部变量，
可以让你在一个特定的范围内使用这些变量，而不影响外部作用域。 -->
<!-- 它通常用于在模板中处理复杂的表达式并将其保存为变量，提升模板的可读性。 -->

{% with messages = get_flashed_messages() %}
  {% if messages %}
    <div class="alert alert-info">
      <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
      </ul>
    </div>
  {% endif %}
{% endwith %}
<!-- with 标签用来在模板内部创建一个局部变量 messages，
并将 get_flashed_messages() 函数的返回值赋给它。 -->
<!-- 这样就可以在 with 标签内部使用 messages，它的作用范围仅限于 with 标签内。 -->
```

### 1.3.3. if 标签：条件判断

```jinja
<!-- if 标签用于在模板中执行条件判断。
根据条件的结果，模板可以渲染不同的内容或执行不同的逻辑。
if 标签非常常用于动态渲染内容。 -->

{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
{% else %}
  <p>Please log in to continue.</p>
{% endif %}
<!-- if 标签判断 user.is_authenticated 的值。
如果为 True，则渲染 "Welcome" 消息；否则，渲染 "Please log in" 提示。 -->
```

### 1.3.4. for 标签：遍历可迭代对象

```jinja
<!-- for 标签用于遍历一个可迭代的对象 (如列表、字典等)，并对每一项执行某些操作。
它通常用于生成基于数据集合的动态列表或表格。 -->

<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% else %}
    <li>No items found.</li>
  {% endfor %}
</ul>
<!-- for 标签遍历 items 列表中的每个元素，并生成一个 <li> 元素来显示每个项。 -->
<!-- 如果列表为空，则 else 部分会执行，显示 "No items found"。 -->
```

## 1.2.4. partials\/\_upload_form.html

```jinja
<h2 class="mt-5">上传文件</h2>
<form method="post" action="/upload" enctype="multipart/form-data" class="list-group mt-4">
  <div class="input-group mb-3">
    <input type="file" name="file" class="form-control" id="fileInput" required />
    <button type="submit" class="btn btn-outline-secondary">上传</button>
  </div>
</form>
```

### 1.2.5. 代码分析

```jinja
<!-- 页面标题，显示「上传文件」，并为其添加了上边距 -->
<h2 class="mt-5">上传文件</h2>

<!-- 创建表单
- method="post": 表单使用 POST 方法提交数据，这是最常用的文件上传方法。
- action="/upload": 表单数据会提交到 /upload 路径，
通常在后端路由中有相应的处理程序来接收和处理这个请求。
- enctype="multipart/form-data": 该属性指定表单的数据编码类型。
对于文件上传，必须使用 multipart/form-data，否则文件将无法正确上传。 -->
<form method="post" action="/upload" enctype="multipart/form-data" class="list-group mt-4">

  <!-- `class="list-group"` 用于应用 Bootstrap 的样式，`mt-4` 添加上边距 -->
  <div class="input-group mb-3">

    <!-- 文件输入框
    - type="file": 该输入框允许用户选择文件。
    - name="file": 文件输入框的名称属性，用于在表单提交时，后端根据这个名称来获取文件。
    - id="fileInput": 为该元素设置一个唯一的标识符，
    通常在 JS 中用来引用它，或者与其他元素进行关联。
    - required: 此属性确保用户在提交表单之前必须选择一个文件，否则表单不能提交。 -->
    <input type="file" name="file" class="form-control" id="fileInput" required />

    <!-- 提交按钮，点击后提交表单以上传文件
    type="submit": 定义按钮的类型为提交按钮，点击时提交表单。
    「上传」是按钮的文本，表示该按钮的功能。 -->
    <button type="submit" class="btn btn-outline-secondary">上传</button>

  </div>
</form>
```

## 1.4. partials\/\_file_list.html

```jinja
<h2 class="mt-5">可供下载的文件</h2>
<ul class="list-group mt-4 shadow-sm">
    {% for filename in files %}
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div class="d-flex w-75 justify-content-between align-items-center">
                <a href="{{ url_for('download', filename=filename) }}"
                   class="text-truncate file-name">{{ filename }}</a>
                <div class="file-info text-muted ms-3">
                    <span class="file-size">{{ get_file_size(filename) }}</span>
                </div>
            </div>
            <form method="post" action="{{ url_for('delete', filename=filename) }}">
                <button type="submit"
                        onclick="return confirm('确定要删除此文件吗？')"
                        class="btn btn-danger btn-sm">删除</button>
            </form>
        </li>
    {% endfor %}
</ul>
```

```jinja
<table class="table table-hover table-bordered shadow-sm mt-4">
    <thead class="table-light">
        <tr>
            <th>文件名</th>
            <th>大小</th>
            <th>操作</th>
        </tr>
    </thead>
    <tbody>
        {% for filename in files %}
            <tr>
                <td class="text-truncate">
                    <a href="{{ url_for('download', filename=filename) }}">
                        <i class="bi bi-file-earmark"></i> {{ filename }}
                    </a>
                </td>
                <td class="text-muted">{{ get_file_size(filename) }}</td>
                <td>
                    <form method="post" action="{{ url_for('delete', filename=filename) }}">
                        <button type="submit"
                                onclick="return confirm('确定要删除此文件吗？')"
                                class="btn btn-danger btn-sm">
                            <i class="bi bi-trash"></i> 删除
                        </button>
                    </form>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```

```jinja
<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3 mt-4">
    {% for filename in files %}
        <div class="col">
            <div class="card shadow-sm">
                <div class="card-body d-flex justify-content-between align-items-center">
                    <a href="{{ url_for('download', filename=filename) }}"
                       class="text-truncate">
                        <i class="bi bi-file-earmark-text"></i> {{ filename }}
                    </a>
                    <span class="text-muted">{{ get_file_size(filename) }}</span>
                </div>
                <div class="card-footer text-end">
                    <form method="post" action="{{ url_for('delete', filename=filename) }}">
                        <button type="submit"
                                onclick="return confirm('确定要删除此文件吗？')"
                                class="btn btn-danger btn-sm">
                            <i class="bi bi-trash"></i> 删除
                        </button>
                    </form>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
```

### 1.4.1. 代码分析

无序列表方式显示文件

```jinja
<!-- 页面标题，显示“可供下载的文件”，并添加了上边距 -->
<h2 class="mt-5">可供下载的文件</h2>

<!-- 创建一个无序列表，使用 Bootstrap 的 list-group 样式，`mt-4` 添加上边距 -->
<ul class="list-group mt-4 shadow-sm">

    <!-- 遍历文件列表 `files`，为每个文件生成一个列表项 -->
    {% for filename in files %}

        <!-- 每个文件的列表项，使用 Bootstrap 的样式，使项之间的布局是水平的，并且居中对齐 -->
        <li class="list-group-item d-flex justify-content-between align-items-center">

            <!-- 使用 flexbox 排版文件名称和文件信息 -->
            <div class="d-flex w-75 justify-content-between align-items-center">

                <!-- 文件名的链接，点击后会触发下载操作 -->
                <a href="{{ url_for('download', filename=filename) }}"
                   class="text-truncate file-name">{{ filename }}</a>
                <!-- `url_for` 用于生成下载链接 -->

                <!-- 显示文件信息，`ms-3` 添加左边距  -->
                <div class="file-info text-muted ms-3">
                    <!-- 显示文件大小 -->
                    <span class="file-size">{{ get_file_size(filename) }}</span>
                    <!-- `get_file_size` 是一个 Python 函数，用于获取文件的大小 -->
                </div>
            </div>

            <!-- 创建删除文件的表单，`url_for` 用于生成删除文件的 URL -->
            <form method="post" action="{{ url_for('delete', filename=filename) }}">
                <!-- 删除按钮，点击后会弹出确认对话框，确认后提交表单删除文件 -->
                <button type="submit"
                        onclick="return confirm('确定要删除此文件吗？')"
                        class="btn btn-danger btn-sm">删除</button>
                <!-- type="submit": 表单提交按钮
                onclick="return confirm('确定要删除此文件吗？')":
                点击按钮时会弹出确认框，确认后才提交表单 -->
            </form>

        </li>
    {% endfor %}
</ul>

<!-- 文件信息显示:
每个 <li> 中包括文件的下载链接 (通过 url_for('download', filename=filename) 动态生成)，
文件名通过 {{ filename }} 展示，并且使用了 text-truncate 类来确保文件名过长时不会超出边界。 -->

<!-- 文件大小: 
使用了 get_file_size(filename) 函数来动态获取每个文件的大小，
并展示在每个文件项旁边，text-muted 类使其显得较为简洁。 -->

<!-- 删除按钮:
每个文件旁边有一个删除按钮，点击后会提交删除请求。
通过 onclick="return confirm('确定要删除此文件吗？')" 弹出确认对话框，
避免用户误操作。 -->
```

表格方式显示文件

```jinja
<table class="table table-hover table-bordered shadow-sm mt-4">
    <thead class="table-light">
        <tr>
            <th>文件名</th>
            <th>大小</th>
            <th>操作</th>
        </tr>
    </thead>
    <tbody>
        {% for filename in files %}
            <tr>
                <td class="text-truncate">
                    <a href="{{ url_for('download', filename=filename) }}">
                        <i class="bi bi-file-earmark"></i> {{ filename }}
                    </a>
                </td>
                <td class="text-muted">{{ get_file_size(filename) }}</td>
                <td>
                    <form method="post" action="{{ url_for('delete', filename=filename) }}">
                        <button type="submit"
                                onclick="return confirm('确定要删除此文件吗？')"
                                class="btn btn-danger btn-sm">
                            <i class="bi bi-trash"></i> 删除
                        </button>
                    </form>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>

<!-- 使用 <table> 标签来展示文件信息，
表格的结构包括 <thead> (表头) 和 <tbody> (表格主体)。每一行代表一个文件。 -->
<!-- 表头包含三个列，分别是「文件名」、「大小」和「操作」。
通过 Bootstrap 的 table-light 类给表头加上浅色背景。 -->

<!-- 文件名: 使用 <a> 标签将文件名放在一个超链接中，
点击时会调用 url_for('download', filename=filename) 来下载文件。 -->
<!-- 文件大小: 通过 get_file_size(filename) 获取并显示文件大小，
text-muted 类使其更加简洁。 -->
```

卡片布局方式显示文件

```jinja
<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3 mt-4">
    {% for filename in files %}
        <div class="col">
            <div class="card shadow-sm">
                <div class="card-body d-flex justify-content-between align-items-center">
                    <a href="{{ url_for('download', filename=filename) }}"
                       class="text-truncate">
                        <i class="bi bi-file-earmark-text"></i> {{ filename }}
                    </a>
                    <span class="text-muted">{{ get_file_size(filename) }}</span>
                </div>
                <div class="card-footer text-end">
                    <form method="post" action="{{ url_for('delete', filename=filename) }}">
                        <button type="submit"
                                onclick="return confirm('确定要删除此文件吗？')"
                                class="btn btn-danger btn-sm">
                            <i class="bi bi-trash"></i> 删除
                        </button>
                    </form>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
```
