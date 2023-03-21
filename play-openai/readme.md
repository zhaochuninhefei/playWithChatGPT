play-openai
========

尝试使用openai的API, `gpt-3.5-turbo`模型。


# 记录

## 1.创建play-openai工程
使用pycharm创建本地`play-openai`工程，选择创建本地环境目录`venv`，并使用本地python，版本`3.8.10`。

## 2.安装openai
在打开的pycharm工程中，选择`File -> Settings -> Project:play-openai -> Python interprefer`。

在打开的界面列表中，选择左上方的`+`按钮，然后在弹出框里搜索`openai`，选择并安装`openai`，注意版本信息，目前是`v0.27.2`。

安装成功后，在`Python interprefer`界面就会看到`openai`及其相关依赖库。

## 3.安装dotenv
在打开的pycharm工程中，选择`File -> Settings -> Project:play-openai -> Python interprefer`。

在打开的界面列表中，选择左上方的`+`按钮，然后在弹出框里搜索`python-dotenv`，选择并安装`python-dotenv`，目前版本是`1.0.0`。

## 4.创建环境文件与预埋openAI API Key
在根目录下创建`.env`文件，填入OPENAI_API_KEY:
```
OPENAI_API_KEY=<你的openAI API Key>
```

## 5.测试API
首先，你需要`import openai`，然后定义一个测试方法:
```
def testGpt():
    print("testGpt...")

    question = "Who is the second best player in NBA history?"
    print("question: " + question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who is the best player in NBA history?"},
            {"role": "assistant", "content": "Michael Jordan"},
            {"role": "user", "content": question}
        ]
    )

    print(response)

    print("")
    print("answer:" + response["choices"][0]["message"]["content"])
```
注意，通过`openai.ChatCompletion.create`创建一个openAI的API请求，目前使用的模型是`gpt-3.5-turbo`，必要的参数只有两个:
- model 填入模型名称，如这里的`gpt-3.5-turbo`
- messages 填入prompt。 role是`system`时，content用来写一些提示；role是user时，表示这是一个提问; role是assistant时，表示这是一个回答，通过成对的user与assistant问答，给openAI模型进一步的提示，这就是语境内学习的例子。而最后一个没有回答的提问，就是让模型回答的问题。

返回的response结构如下:
```
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "回答...",
        "role": "assistant"
      }
    }
  ],
  "created": xxxx,
  "id": "xxxx",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 52,
    "prompt_tokens": 49,
    "total_tokens": 101
  }
}
```
我们通过`response["choices"][0]["message"]["content"]`获得回答。

接下来，就可以像`main.py`中的`askAndAnwser`那样，编写一个自己的问答程序了。

## 6.问答示例
```
我: 你好啊，我应该怎么称呼你?
openAI API:你可以称呼我为AI助手。有什么可以帮助你的？
我: AI助手你好。能帮我写一首古体诗吗？主题是赞美祖国。
openAI API:当然可以。以下是我为您创作的古体诗：

红旗飘扬扬，山河美无疆。
中华大地上，万物生光芒。

莘莘学子勤，走向未来路。
英雄儿女志，铸就伟大楼。

长城虽有悔，胜利在前方。
民族大团结，祖国更兴旺。

让我们心潮澎湃，敬爱伟大祖国。
不忘初心肝，努力向前跑。
我: emmm，有进步，但还是很挫啊哈哈。我这么说你不介意吧？
openAI API:当然不介意！作为助手，我的主要目标是帮助您解决问题和提供必要的支持。如果您有任何疑问或需要进一步的帮助，请随时告诉我。
我: 能给我介绍一下java的版本发布历史，以及目前的发布策略吗？
openAI API:好的，以下是Java的版本发布历史和目前的发布策略：

1. Java版本发布历史：

- JDK 1.x: Java最初的版本，包括Java 1.0和1.1，于1995年和1996年发布；
- JDK 1.2: 也被称为Java 2，于1998年发布；
- JDK 1.3: 也被称为Java 2版本1.3，于2000年发布；
- JDK 1.4: 也被称为Java 2版本1.4，于2002年发布；
- JDK 5.0: 也被称为Java 5，于2004年发布，引入了语言特性如泛型、枚举、自动装箱等；
- Java SE 6: 也被称为Java 6，于2006年发布；
- Java SE 7: 于2011年发布，引入了语言特性如字符串在switch语句中的支持等；
- Java SE 8: 于2014年发布，引入了Lambda表达式、Stream API及日期/时间API等；
- Java SE 9: 于2017年发布，引入了模块系统及JShell等特性；
- Java SE 10: 于2018年发布，引入了var本地变量类型推断和应用类数据共享等特性；
- Java SE 11: 于2018年发布，是第一个长期支持版本（LTS），引入了本地变量语法和HTTP客户端API等特性；
- Java SE 12: 于2019年3月发布，引入Switch Expressions、JVM Error Reporting等功能；
- Java SE 13: 于2019年9月发布，引入Text Blocks、Dynamic CDS Archive等功能；
- Java SE 14: 于2020年3月发布，引入Switch Expressions增强、Records等功能；
- Java SE 15: 于2020年9月发布，引入Sealed Classes、Hidden Classes等功能。

2. Java的发布策略：

自Java SE 9开始，Java采用了一种新的发布策略，称为Java版本发布许可（Java Version Release Licenses）。该策略将Java发布分为两类：

- 长期支持版本（LTS）：每三年发布一个LTS版本，LTS版本在发布后会持续支持8年；
- 短期支持版本（Non-LTS）：非LTS版本每六个月发布一个，这些版本只会获得六个月的免费支持。

Java SE 11是第一个LTS版本，Java SE 17将会是下一个LTS版本。使用Java LST版本可以获得更长时间的支持和更新，而短期版本则适合那些需要及时获得新特性的用户。

```

> gpt-3.5写古诗很烂，另外它的训练数据有点老，所以不知道Java已经出到19了，马上20就出来了，也不知道现在Java的LTS发布周期变成两年了。。。

## 7.talkWithSession
talkWithSession是一个支持会话session的对话程序，通过每次将上次对话内容加入messages，让模型获取对话上下文信息。

但这样有一个小问题，就是增加了每次调用API时的prompt的token数量，目前我在openai的API文档中没有发现使用接口`v1/chat/completions`时可以不重复统计prompt中历史消息的方法。

不过gpt-3.5的API那么便宜，也不用太在意会话中token的重复统计了。
