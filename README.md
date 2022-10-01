# EyeAligningBot
## 最新消息
...
## 简介
我的世界（Minecraft）速通辅助工具，自动完成末影之眼像素级对准。EyeAligningBot（下简称Bot）通过实时截取游戏图像定位末影之眼，并不断调整鼠标十字准星使二者对齐，帮助速通玩家精准定位要塞，完成双传。

A useful tool for Minecraft speedrun.

**适用情况：**
速通中，玩家收集了足够的烈焰棒和末影珍珠，搭建地狱门传送到主世界，接下来需要精确测量要塞的位置。


**默认的设置仅适用于1080p屏幕，其他情况请参考“个性化设置”！！！**

## 快速使用
Bot的用法很简单，打开Bot，接下来只需调整“视频”和“鼠标设置”并按步骤点击Bot界面的选项框和按钮：
1. 基础的对眼操作：投掷末影之眼，等末影之眼稳定在空中，暂停游戏并调整视频设置为：FOV 30（适用于1080p显示屏，其他屏幕参考下面的”个性化设置“），调整鼠标设置为：灵敏度 最低，原始输入 关。
2. 选择窗口：选择Minecraft游戏窗口名，点击右侧“确定”。    ->    Bot状态显示：“窗口句柄：xxx”
3. 检测末影之眼：Bot通过存储的末影之眼模板，在游戏窗口内搜索末影之眼的位置。  ->    Bot状态显示：“检测结果如上”
4. 对准：Bot通过调整鼠标十字准星，自动对准末影之眼瞳孔，并达到像素级精度。    ->    Bot状态显示：“已对准”
5. （下接Ninjabrain-Bot的使用）

视频教程参考我的b站视频（顺便给个三连哦~）。
我的b站账号：https://space.bilibili.com/244384103/
## 个性化设置
在默认设置的基础上，为了能兼容不同玩家的设备并适应玩家颜色偏好，添加了个性化设置的功能。
个性化设置主要涉及两方面：不同分辨率屏幕的模板（在./imgs中）、Bot界面主题修改（setting.json）。前者实现了不同设备的兼容，后者允许玩家自定义Bot界面的颜色风格。
解压Bot的压缩包，关注两个文件（夹），./imgs 和 setting.json。
1. ./imgs，该文件夹下存放了各种分辨率的图片，请依据自己的显示屏分辨率选择（默认1080x1920），修改setting.json的内容。
2. settings.json，该文件是Bot的配置文件。文件内容以及参数说明如下，请依据自己的需求进行修改。
```
// 按照显示屏分辨率设置，目前支持3种分辨率，"1080": 1080x1920，"2k": 1440x2560，"4k": 2160x3840
// 如果不在上述3种分辨率中，请选择最相近的分辨率，如果bot无法正常使用，请在b站私信
// 如有其他常见的分辨率，可在b站私信增加
"resolution": "2k",

// 下面的参数是用于筛选窗口名的。简单来说，只要把游戏窗口的部分文字填到下面的 :"xxx"  中即可。
// (有代码基础的玩家可以这样理解，预先设置一个字符串，去检索全部窗口名的列表，如果窗口名包含这个字符串，就保留该窗口名)
"minecraft_windows_filter": "Minecraft" ,

// 设置Bot主题！可选的主题附在下面，可以设置自己喜欢的颜色。
"bot_theme": "litera"
```
```
// 可选的颜色主题：
// theme: "cosmo", "flatly", "litera", "minty", "yeti", "pulse", "united",
//              "morph",  "journal",  "darkly",  "superhero", "solar", "cyborg",
//              "vapor", "simplex",  "cerculean",
```

## 常见问题
