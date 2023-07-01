import re

while True:
    # 获取用户输入的文本
    user_input = input("Input:")

    # 检测是否符合新的输入格式
    match = re.match(r'find "(.*?)" in (.*?)\s*$', user_input)

    if match:
        search_text = match.group(1)  # 要查找的文本
        source_file = match.group(2)  # 原文本来源

        try:
            # 从指定文件中读取原文本
            with open(source_file, 'r', encoding='utf-8') as file:
                target_text = file.read()

            # 计算查找内容在目标文本中出现的次数
            count = target_text.count(search_text)

            # 根据次数添加相应的后缀
            if count < 2:
                output = str(count) + "(S)"
            elif count < 5:
                output = str(count) + "(N)"
            else:
                output = str(count) + "(large)"

            # 输出结果
            print(output)

        except FileNotFoundError:
            print(f"file \"{source_file}\" is not found")
    else:
        # 按照原有的格式进行处理
        parts = user_input.split(" - ")

        if len(parts) != 2:
            print("ERROR")
        else:
            target_text = parts[0]  # 要查找的文本
            search_text = parts[1]  # 要在文本中查找次数的内容

            # 计算查找内容在目标文本中出现的次数
            count = target_text.count(search_text)

            # 根据次数添加相应的后缀
            if count < 2:
                output = str(count) + "(S)"
            elif count < 5:
                output = str(count) + "(N)"
            else:
                output = str(count) + "(large)"

            # 输出结果
            print(output)
