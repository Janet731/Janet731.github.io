---
title: "用油猴脚本免费看vip视频和干别的🤔"
date: 2023-01-18T23:47:09+08:00
draft: false
tags: ["lifehack"]
categories: ["好没用的技能"]
featuredImagePreview: "/featureImages/tampermonkeylogo.png"
---
不想再给视频网站、百度网盘充会员了😠！可以用TamperMonkey成为白嫖滴神🤩

## 免费看vip视频
在[greasy fork](https://greasyfork.org/zh-CN)网站上有详细的步骤👇

首先需要根据浏览器类型配置相应的脚本运行插件，我在chrome浏览器上下载并安装了Tampermonkey。
{{< admonition info "Tampermonkey官网简介" false >}}
Tampermonkey用于在网站上运行所谓的用户脚本（有时也称为Greasemonkey脚本）。

用户脚本是小型计算机程序，可以更改页面的布局，添加或删除新功能和内容或自动执行操作。
{{< /admonition >}}
在[该网站](https://greasyfork.org/zh-CN/scripts)找到相关脚本并下载。我目前在用[第一条](https://greasyfork.org/zh-CN/scripts/370634-%E6%87%92%E4%BA%BA%E4%B8%93%E7%94%A8-%E5%85%A8%E7%BD%91vip%E8%A7%86%E9%A2%91%E5%85%8D%E8%B4%B9%E7%A0%B4%E8%A7%A3%E5%8E%BB%E5%B9%BF%E5%91%8A-%E5%85%A8%E7%BD%91%E9%9F%B3%E4%B9%90%E7%9B%B4%E6%8E%A5%E4%B8%8B%E8%BD%BD-%E7%9F%A5%E4%B9%8E%E5%A2%9E%E5%BC%BA-%E7%9F%AD%E8%A7%86%E9%A2%91%E6%97%A0%E6%B0%B4%E5%8D%B0%E4%B8%8B%E8%BD%BD-%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98%E7%9B%B4%E6%8E%A5%E4%B8%8B%E8%BD%BD%E7%AD%89%E5%A4%9A%E5%8A%9F%E8%83%BD%E5%B7%A5%E5%85%B7%E7%AE%B1-%E5%8A%9F%E8%83%BD%E5%8F%AF%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%85%B3-%E9%95%BF%E6%9C%9F%E6%9B%B4%E6%96%B0-%E6%94%BE%E5%BF%83%E4%BD%BF%E7%94%A8-v6)，点进去在油猴页面安装就可以用了🤩！使用效果如下图：
   
{{< image src="/tamperMonkey.png" caption="用油猴脚本免费看爱奇艺vip视频" >}}

然后我发现在这个宝藏网站上还有好多实用的脚本，于是我又下载了两个探索了一下⬇️
   
{{< image src="/tamperMonkey2.png" caption="我的油猴脚本们" >}}

---

## 文本复制

亲测这个[文本选中复制](https://greasyfork.org/zh-CN/scripts/405130-%E6%96%87%E6%9C%AC%E9%80%89%E4%B8%AD%E5%A4%8D%E5%88%B6)脚本有效，直接安装脚本就可以使用了。

终于可以直接ctrl+c，ctrl+v知网了😍

{{< image src="/tamperMonkey3.png" caption="不限字数，直接复制粘贴" >}}

---

## 百度网盘加速下载

这个百度网盘加速下载比较难搞，还需要额外安装一个Aria2软件:

{{< admonition info "Aria2简介" false >}}

Aria2是一款自由、跨平台命令行界面的下载管理器，该软件根据GPLv2许可证进行分发。支持的下载协议有：HTTP、HTTPS、FTP、Bittorrent和Metalink。

{{< /admonition >}}

mac上安装aria2可以通过在终端下输入`brew install aria2`，或者在[这里](https://github.com/aria2/aria2/releases/tag/release-1.35.0)下载对应的安装包。接着在终端输入`aria2c`就可以使用。

但是这样安装的aria2只能在终端使用，非常不方便。因此可以在[这里](https://github.com/NickYang29/aria2gui)下载一个对应的gui软件，这样能更清楚地看到正在下载的内容。

下载该软件后，mac会提醒“这是不明开发者开发的内容，无法打开”。这时需要进入“系统设置-隐私与安全-安全”处选择强行打开该软件。

将这些都安装好了后，就可以在百度网盘网页端快速下载文件了🤩

{{< image src="/tamperMonkey4.png" caption="点击红色的“简易下载助手”，选择“发送至aria2”，就开始下载了" >}}

{{< image src="/tamperMonkey5.png" caption="可以看到正在下载的内容和下载速度" >}}

*提醒：这个插件在第二次下载时就要求扫码关注微信公众号了。。*