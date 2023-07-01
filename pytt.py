import re

while True:
    user_input = input("Input:")

    match = re.match(r'find "(.*?)" in (.*?)\s*$', user_input)

    if match:
        search_text = match.group(1)  
        source_file = match.group(2)  

        try:
            with open(source_file, 'r', encoding='utf-8') as file:
                target_text = file.read()

            count = target_text.count(search_text)

            if count < 2:
                output = str(count) + "(S)"
            elif count < 5:
                output = str(count) + "(N)"
            else:
                output = str(count) + "(large)"

            print(output)

        except FileNotFoundError:
            print(f"file \"{source_file}\" is not found")
    else:
        parts = user_input.split(" - ")

        if len(parts) != 2:
            print("ERROR")
        else:
            target_text = parts[0]  
            search_text = parts[1]  

            count = target_text.count(search_text)

            if count < 2:
                output = str(count) + "(S)"
            elif count < 5:
                output = str(count) + "(N)"
            else:
                output = str(count) + "(large)"

            print("output:",output)
