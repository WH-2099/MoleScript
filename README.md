# 摩尔庄园 BlueStacks 脚本
![bs-logo-new](/img/bs-logo-new.png)
<img src="img/mole_icon.png" width="150" align="right"/>

手游上线，情怀再起，但面对游戏中枯燥无味的每日任务和资源采集，你是否觉得肝疼呢？

本项目通过生成 BlueStacks 模拟器的宏脚本，帮助玩家护肝。

> 最新进度
> 1. `自动地图资源采集`: 浆果丛林采集路线规划、操作打点中（一张图需要超过50遍的重复测试才能使脚本稳定）
> 2. `自动钓鱼`：时间线分析中
> 3. `自动炒菜`：逻辑整理中




## 为什么要选择本项目
- 本项目最终生成的仅是**宏脚本**，游戏操作仅是基于时间线的模拟点击，不会**读写任何游戏相关数据**，根据相关的法律法规及曾有的司法实践，**不属于外挂**。
- **宏脚本**自身只是操作记录的数据文件，不是可执行文件，**不会内含木马病毒**。
- 本项目使用 **Python 包装了底层操作逻辑**，掌握 Python 的玩家完全可以在此基础上**快速开发自定义的脚本**。


## 为什么不选择本项目
- 本项目**不会提供任何侵入性或破坏游戏环境的功能**（例如 “秒做菜”、“秒钓鱼”、“自动刷屏”等）
- 基于不破坏游戏平衡性的出发点，加之稳定性和兼容性考虑，**宏脚本的耗时相比手动操作更长**



## 出发点
时光流转，曾经的红鼻子小摩尔已成了亮额头大学生。

斗转星移，肝手游肝得精疲力尽。

垂死梦中惊坐起，咱肝不动了！

代码程序入梦来，咱有主意了！

深坐颦蛾眉感时花溅泪，破坏计算机信息系统罪！

出师未捷心先死，咱还年轻不想死！

常使英雄泪满襟，码宏脚本别犯禁！



## 声明
1. **本项目生成的宏脚本独立运行，不读取任何游戏数据，更不修改任何游戏数据，仅以模拟点击的方式完成游戏操作，不具有侵入性。**
2. **本项目协助的操作仅涉及基础的日常资源收集，绝不涉及任何影响游戏环境（平衡性）的内容。**
3. *本项目确实会影响玩家的氪金需求，进而可能触及相关商业公司的利益。小摩尔长大了，可支配的资本增长了，但肩上的压力也比以前大多了 ~~（说白了就是穷）~~，给点活路吧！/(ㄒoㄒ)/*


---
## 联系
### 欢迎关注 [Telegram 频道](https://t.me/mole61)
---


## 功能
- [x] 每日签到
  - [x] 商城每日礼包
  - [x] 超拉礼包
  - [x] SMC工资
- [x] 每日许愿
- [x] 每日占卜
- [x] 每日向导任务
- [x] 每日 NPC 好感度对话
- [x] 自动发言
- [ ] 自动钓鱼
- [x] 自动烹饪（经营菜）
- [ ] 自动炒菜（私房菜）
- [x] 自动伐木林采集
- [ ] 自动地图资源采集（浆果 + 草丛 + 草堆）
  - [x] 摩尔拉雅（白浆果）
  - [x] 前哨站（黑浆果 + 草丛）
  - [ ] 浆果丛林（红浆果 + 橙浆果 + 草丛）
  - [ ] 城堡区 [爱心街区 + 摩尔城堡 + 淘淘乐街]（橙浆果 + 草丛）
  - [ ] 牧场区 [阳光牧场 + 阳光沙滩 + 开心农场]（橙浆果 + 草丛 + 草堆）



## 特性
- 扩展性
  > 采用 Python 代理生成相应的 BlueStacks 宏脚本，可在已有动作基础上轻松扩展新功能
- 复用性
  > 触点坐标与流程控制分离，触点变化时，只需及时更新触点数据即可
- 定制性
  > 各功能独立工作，可依据要求自行定制
- 非侵入性
  > 不触及任何游戏运行过程中的相关数据
- 模拟性
  > 所有操作均基于模拟点击动作，且带有坐标随机漂移（模拟器操作本身自带有较大的时间漂移）
- 独立性
  > 不主动获取任何游戏数据（包括且不限于画面、内存、网络相关的数据）
- 高效性
  > 由于没有主动性检测，执行更高效，对软硬件性能要求很低



## 使用方式
`请注意，以下内容正在根据开发进度逐步完善中`
1. 下载安装 [BlueStacks 5](https://www.bluestacks.com/tw/index.html)
   > [如何下载并安装 BlueStacks 5 ？](https://support.bluestacks.com/hc/zh-tw/articles/360061525271-%E5%A6%82%E4%BD%95%E4%B8%8B%E8%BC%89%E4%B8%A6%E5%AE%89%E8%A3%9DBlueStacks-5)
2. 下载摩尔庄园手游安装包（请注意自己的渠道服情况）
   > 摩尔庄园手游官网：https://mole.leiting.com/home
   >
   > 较为常用的应用商店下载地址（对应渠道服）：
   > - Bilibili：http://www.biligame.com/gamelist.html
   > - 华为：http://app.hicloud.com
   > - 小米：http://app.mi.com
   > - OPPO（可可）：http://store.oppomobile.com
   > - 魅族：http://app.meizu.com
   > - 联想（乐商店）：http://www.lenovomm.com
   > - 酷派：http://www.coolmart.net.cn/
   > - 乐视：http://mobile.leplay.cn/
   > - VIVO：https://dev.vivo.com.cn/doc/products/pc/index.html#firstPag
3. 在 BlueStacks 中安装摩尔庄园手游
4. 手动设置 BlueStacks
   - 画面解析度：1280 x 720
5. 手动设置摩尔庄园
   - 刘海屏：关
6. 下载项目 [json](/json) 文件夹中对应的 json 文件
7. 导入 json 文件为宏脚本
   > [如何从电脑将脚本导入 BlueStacks ？](https://support.bluestacks.com/hc/zh-tw/articles/360056012412-BlueStacks-5%E4%B8%8A%E7%9A%84%E8%85%B3%E6%9C%AC%E7%AE%A1%E7%90%86%E5%99%A8#%E2%80%9C4%E2%80%9D)
8. 更换角色服装为 **向导服**
9. 更换角色载具为 **驴牌滑板车**
10. 运行宏脚本
    > [如何执行/播放现有的脚本？](https://support.bluestacks.com/hc/zh-tw/articles/360056012412-BlueStacks-5%E4%B8%8A%E7%9A%84%E8%85%B3%E6%9C%AC%E7%AE%A1%E7%90%86%E5%99%A8#%E2%80%9C2%E2%80%9D)