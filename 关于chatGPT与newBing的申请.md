关于chatGPT与newBing的申请
=====

# chatGPT
在国内想使用chatGPT比较麻烦，因为openAI做了两个限制:
- 注册openAI账户时要发送激活码到手机，但是它不允许使用中国地区的手机号。
- 访问openAI时，它会检查你的IP是否是中国地区，包括香港，都是会被禁止访问的。


因此你需要:

1. 科学上网，这个需要自己发挥聪明才智。
2. 去弄个境外手机短信服务，用来在注册的时候接收激活码。(比如在`https://sms-activate.org/`上购买手机号服务)

第一点靠大家自己八仙过海想办法，第二点的话，网上已经有大量的教程，这里就不赘述了。

> 然后，等你注册好开始使用chatGPT以后，你会发现动不动就告诉你过去一个小时提了太多问题，但其实你才刚打开chatGPT。。。所以真要把chatGPT当作工作助手的话，大概要购买plus服务？这个我就不清楚了。

# newBing
new bing目前不需要科学上网，不需要境外手机服务，你需要做的是:

1. 注册一个微软账户(`https://account.microsoft.com/`)，国内的邮箱就可以，比如我就用qq邮箱注册的。
2. 由于咱们访问bing.com时会自动跳转到`cn.bing.com`，所以需要为本地edge浏览器安装一个用来修改http头属性`X-Forwarded-For`的插件，比如ModHeader，这个网上也有很多教程，这里也不多说了。或者直接使用dev版本的edge，这个方式我没试过，据说可以。
3. 访问`bing.com/new`，按照提示申请加入newBing的候补队列，微软的东西做的不太友好，我当时一顿瞎操作，也不知道怎么就加入候补队列了。。。加入成功的话，你的微软帐号注册邮箱会受到一封邮件：`You're on the waitlist for the new Bing!`，然后就且等着吧。。。
4. 大概一周以后，你可能会收到通知你已经可以使用newBing了的邮件:`You're in! Welcome to the new Bing!`
5. 此时你重新打开edge(ModHeader要一直开着)，然后访问`bing.com`，只要不跳到`cn.bing.com`，你就可以在上方菜单里找到聊天，点击它，就可以开始浪了。

new bing 可以使用的话，你就能看到这个"聊天"按钮

![](images/newbing.jpg)

点击后来到聊天页面:

![](images/2023-03-01-16-52-06.png)

当然，它经常挂掉，每次会话只能提5个问题，没有有趣的灵魂，脾气也不太好。。。emmmm。。。就这样吧。。。
