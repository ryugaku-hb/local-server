document.addEventListener("DOMContentLoaded", function () {
  var flashMessage = document.getElementById("flash-message");
  if (flashMessage) {
    // 设置延迟时间后，平滑隐藏 flash 消息
    setTimeout(function () {
      // 添加 fade 类来触发消失动画
      flashMessage.classList.add("fade");
      // 另一种处理方式：如果使用 bootstrap 的默认关闭按钮，这样可以在动画后删除元素
      setTimeout(function () {
        flashMessage.remove(); // 动画结束后，移除元素
      }, 1000); // 与动画的持续时间保持一致
    }, 3000); // 3秒后开始隐藏，可以根据需求调整
  }
});
