import openai
import os
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# response_list = openai.Model.list()
# print(response_list)

# messages = []
# 定义文件路径
filename = "history/default.json"

history_global = []
# 如果文件存在，读取文件内容并将其反序列化为Python对象
if os.path.exists(filename):
    with open(filename, "r") as f:
        history_global = json.load(f)
# 如果文件不存在，将messages初始化为空数组
else:
    history_global = [{"role": "system", "content": "You are a helpful assistant."}]


def talk():
    global history_global
    print("当前会话历史:")
    print_history(history_global)

    while True:
        question = input("我: ")

        if question.strip() == "":
            continue

        if question.lower() == "help":
            print("指令帮助:")
            print(" help : 帮助")
            print(" clear : 清空当前history")
            print(" quit : 退出程序, 并将当前history保存到 history/default.json")
            print(
                " save : 将当前history保存到指定文件, 如 `save history/test.json`,如果没有指定具体文件，则保存到 history/default.json")
            print(" save now: 将当前history保存到时间戳文件: history/<时间戳>.json")
            print(
                " load : 导入指定文件作为当前history, 如 `load history/test.json`,如果没有指定具体文件，则导入 history/default.json")
            print(
                " show : 查看指定会话历史文件, 如 `show history/test.json`,如果没有指定具体文件，则查看 history/default.json")
            print(" show cur: 查看当前会话历史")
            continue

        if question.lower() == "clear":
            history_global = [{"role": "system", "content": "You are a helpful assistant."}]
            print_history(history_global)
            continue

        if question.lower() == "quit":
            # 将数据转换为JSON格式
            json_data = json.dumps(history_global)
            # 将JSON数据写入文件
            with open(filename, "w") as history_file:
                history_file.write(json_data)
            break

        if question.lower() == "save":
            # 将数据转换为JSON格式
            json_data = json.dumps(history_global)
            # 将JSON数据写入文件
            with open(filename, "w") as history_file:
                history_file.write(json_data)
            continue

        if question.lower() == "save now":
            save_file_path = "history/history_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
            # 将数据转换为JSON格式
            json_data = json.dumps(history_global)
            # 将JSON数据写入文件
            with open(save_file_path, "w") as history_file:
                history_file.write(json_data)
            continue

        if question.lower().startswith("save"):
            save_file_path = question[5:]
            if len(save_file_path) == 0:
                print("请指定保存路径")
                continue
            # 将数据转换为JSON格式
            json_data = json.dumps(history_global)
            # 将JSON数据写入文件
            print(save_file_path)
            with open(save_file_path, "w") as history_file:
                history_file.write(json_data)
            continue

        if question.lower() == "load":
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    history_global = json.load(f)
            # 如果文件不存在，将messages初始化为空数组
            else:
                history_global = [{"role": "system", "content": "You are a helpful assistant."}]
            print_history(history_global)
            continue

        if question.lower().startswith("load"):
            load_file_path = question[5:]
            if len(load_file_path) == 0:
                print("请指定导入文件路径")
                continue
            if os.path.exists(load_file_path):
                with open(load_file_path, "r") as f:
                    history_global = json.load(f)
            # 如果文件不存在，将messages初始化为空数组
            else:
                print("指定导入文件不存在: " + load_file_path)
            print_history(history_global)
            continue

        if question.lower() == "show":
            print_history(history_global)
            continue

        if question.lower().startswith("show"):
            show_file_path = question[5:]
            if len(show_file_path) == 0:
                print("请指定查看文件路径")
                continue
            if os.path.exists(show_file_path):
                with open(show_file_path, "r") as f:
                    history_read = json.load(f)
                    print_history(history_read)
            # 如果文件不存在，将messages初始化为空数组
            else:
                print("指定查看文件不存在: " + show_file_path)
            continue

        messages = history_global[-6:]
        messages.append({"role": "user", "content": question})
        history_global.append({"role": "user", "content": question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        print()
        # print(response)
        response_id = response["id"]
        print("response_id: " + response_id)
        response_prompt_tokens = response["usage"]["prompt_tokens"]
        print(f"response_prompt_tokens: {response_prompt_tokens}")
        response_completion_tokens = response["usage"]["completion_tokens"]
        print(f"response_completion_tokens: {response_completion_tokens}")
        response_total_tokens = response["usage"]["total_tokens"]
        print(f"response_total_tokens: {response_total_tokens}")
        answer = response["choices"][0]["message"]["content"]
        print("openAI API:" + answer)
        history_global.append({"role": "assistant", "content": answer})
        print()


def print_history(h):
    for ele in h:
        print(f"[{ele['role']}]:{ele['content']}")
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # num = 100
    # print(f"数字:{num}")
    talk()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
