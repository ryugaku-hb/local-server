document.addEventListener("DOMContentLoaded", () => {
  const messages = document.querySelectorAll(".flash-message");

  messages.forEach((msg) => {
    setTimeout(() => {
      msg.classList.add("fade-out");
      msg.addEventListener(
        "transitionend",
        () => {
          msg.remove();
        },
        { once: true }
      ); // 防止触发多次
    },2000); // 自动消失时间
  });
});
