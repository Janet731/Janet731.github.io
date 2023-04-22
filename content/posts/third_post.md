---
title: "12306抢票攻略"
date: 2023-04-22T13:44:37+08:00
draft: false
tags: ["lifehack"]
categories: ["好没用的技能"]
featuredImagePreview: "/featureImages/12306.png"
---
# 12306抢票脚本使用攻略

参考视频：

{{< bilibili BV1mK4y1V7cd 1 >}}

[源项目github地址](https://github.com/gzldc/12306)

本文将介绍一种12306抢票脚本，可以在五一、国庆等需要蹲点抢票的情况下使用，可以有效避免手速不够快导致抢不到火车票的情况！

## 配环境

该项目支持的版本为python3.6-3.7，因此需要使用anaconda安装python3.6-3.7的虚拟环境。如果使用苹果m芯片，新建虚拟机时需要在终端先输入：
```
conda config --env --set subdir osx-64
```
再使用下面两句新建虚拟环境和进入虚拟环境
```
conda create -n for12306 python=3.7
conda activate for12306
```
最后将该项目clone过来，根据项目内的requirements.txt下载依赖项
```
cd /path/to/12306
pip install -r requirements.txt
```

## 配置抢票内容

这里只需要修改`TickerConfig.py`这一个文件。

**首先需要按照注释⾥⾯修改购票信息**

**！！修改这三个值，才能让脚本正确地在12306上登陆**

{{< image src="/12306-1.png" caption="一定要改tk值！" >}}

*⚠️：tk值过十几分钟就会过期，所以最好在抢票前十分钟内获取tk值然后填入*

### 获取tk值脚本

视频中介绍了一种用chrome浏览器的检查来获得tk值的方法，但这种方法较为复杂，需要耗费较长时间。因此我们可以使用油猴脚本来帮我们完成这一步：

{{< image src="/12306-2.png" caption="使用脚本获得tk值" >}}

在[这个网站](https://greasyfork.org/zh-CN/scripts/419934-%E8%8E%B7%E5%8F%9612306cookie%E5%80%BC)获得油猴脚本～

## 开始抢票！

最后需要先执行这句加入cdn：
```
python run.py c
```
然后执行这句开始抢票:
```
python run.py r
```

## 结果展示

{{< image src="/12306-3.png" caption="脚本订票成功页面" >}}

{{< image src="/12306-4.png" caption="这里是用脚本抢到了五一黄金周的卧铺！" >}}

**祝愿大家都能抢到心仪的火车票～**