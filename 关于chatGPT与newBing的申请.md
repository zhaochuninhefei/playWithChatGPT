关于chatGPT与newBing的申请
=====

# chatGPT
在国内想使用chatGPT比较麻烦，因为openAI做了两个限制:
- 注册openAI账户时要发送激活码到手机，但是它不允许使用中国地区的手机号。
- 访问openAI时，它会检查你的IP，并禁止中国地区IP的访问，包括香港。


因此你需要:

1. `science go online`，这个需要自己发挥聪明才智。
2. 去弄个境外手机短信服务，用来在注册的时候接收激活码。(比如在`https://sms-activate.org/`上购买手机号服务)

第一点靠大家自己八仙过海各显神通，第二点的话，网上已经有大量的教程，这里就不赘述了。

> 然后，等你注册好开始使用chatGPT以后，你会发现它动不动就说你在过去一个小时提了太多问题，但其实你才刚打开chatGPT，一个问题都还没问。。。
> 
> 所以真要把chatGPT当作工作助手的话，大概要购买plus服务，一个月20刀。。。用不起用不起。。。

## 关于openai的API
注册好openAI的帐号以后，你还可以用openAI的API，你需要:

1. 登录openai站点以后去`https://platform.openai.com/account/api-keys`生成自己的`API keys`。
2. 用python3(3.6以上)写代码，具体参考官方文档`https://platform.openai.com/docs/guides/chat`，模型可以选择`gpt-3.5-turbo`。这里其实可以直接问chatGPT具体怎么做。。。或者问new bing也行。。。
> 关于第2步，现在访问openai的API也需要`science go online`了。。。

具体的API使用示例可以参考:

<a href="./play-openai" target="_blank">play-openai</a>

另外，某些工具或插件也需要你输入自己的APIKey，和步骤2一样去生成一下即可。

> openai官方发邮件说这个api很便宜: `It’s priced at $0.002 per 1K tokens, which is 10x cheaper than the existing GPT-3.5 models.`。。。然后我看了下自己的openAI账户，原来注册的时候送了18刀，到`2023/4/1`过期，所以现在还能免费用一阵子。。。


# newBing
new bing目前不需要`science go online`，不需要境外手机服务，你需要做的是:
> 2023/3/13以后，new bing 也需要`science go online`才能访问了。。。而且必须是开客户端的那种。。。

1. 注册一个微软账户(`https://account.microsoft.com/`)，国内的邮箱就可以，比如我就用qq邮箱注册的。注册好了以后在edge和bing站点上登录你的微软账户。
   > 微软的所有站点访问起来都太慢，即使注册成功，登录也很慢。。。你需要耐心。。。lots of patience。。。
2. 由于咱们访问`bing.com`时会自动跳转到`cn.bing.com`，所以需要为本地edge浏览器安装一个用来修改http头属性`X-Forwarded-For`的插件，比如ModHeader，这个网上也有很多教程，这里也不多说了。或者直接使用dev版本的edge，这个方式我没试过，据说可以。
   > 开启`science go online`后就不会自动跳转到`cn.bing.com`了，也就不用插件了。
3. 访问`bing.com/new`，按照提示申请加入newBing的候补队列，微软的东西做的不太友好，我当时找不到申请入口，然后一顿瞎操作，也不知道怎么搞地就加入候补队列了。。。加入成功的话，你的微软帐号注册邮箱会收到一封邮件：`You're on the waitlist for the new Bing!`，然后就且等着吧。。。
   > 微软号称做了这两个事情可以更快地通过候补正式使用newBing: 一个是本地edge浏览器的home页面设置为bing并登录你的微软账户，另一个是手机上下载bing浏览器并登录你的微软账户。
4. 大概几天以后，如果你收到了通知邮件:`You're in! Welcome to the new Bing!`，那么恭喜你，通过了候补，可以使用newBing了。。。我当时21号进入候补队列，25号收到的`you are in`通知邮件。。。
5. 此时你重新打开edge(ModHeader要一直开着)，然后访问`bing.com`，只要不跳到`cn.bing.com`，你就可以在上方菜单里找到聊天，点击它，就可以开始浪了。
   > 开启`science go online`后自然也不用一直开插件。


new bing 可以使用的话，你就能看到这个"聊天"按钮

![](images/newbing.jpg)

点击后来到聊天页面:

![](images/2023-03-01-16-52-06.png)

当然，它经常挂掉，每次会话只能提几个问题，没有有趣的灵魂，脾气也不太好。。。emmm。。。就这样吧。。。

> 2023/3/13 追记: 今天下午开始，我不能访问new bing了，浏览器报错说跳转次数太多。查了一下，我在访问`bing.com`时总会被跳转回`cn.bing.com`。。。感觉是bing后台升级了加了啥限制。。。据说目前需要全局`science go online`并把微软帐号设置为米国地区才可以访问new bing。。。我没有全局`science go online`，确实没办法。。。不管清多少次cookie，浏览器开不开`science go online`都不行，总会跳回`cn.bing.com`。。。
