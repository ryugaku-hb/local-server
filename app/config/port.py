def get_port_from_input(default_port: int) -> int:
    """提示用户输入端口号，验证输入是否为有效的整数且在 1024~65535 范围内。
    若用户直接回车或输入非法，将返回默认端口。

    Args:
        default_port (int): 默认端口号，当用户不输入或输入无效时使用

    Returns:
        int: 最终使用的端口号
    """

    prompt = f"请输入端口号（1024-65535，回车使用默认 {default_port}）："

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print(f"✅ 使用默认端口：{default_port}。")
            return default_port

        if user_input.isdigit():
            port = int(user_input)

            if 1024 <= port <= 65535:
                print(f"✅ 使用端口：{port}。")
                return port
            else:
                print("❌ 端口号必须在 1024 到 65535 之间。")
        else:
            print("❌ 输入无效，请输入一个数字。")
