#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2021 WH-2099

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json
import math
from collections import UserList
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from random import randint, uniform
from typing import Iterable, Optional
from time import sleep

# 按钮位置，左上为 0.0 ，右下为 100.0
button_positions = {
    "屏幕空白": (50.0, 5.0),
    "头像": (4.0, 7.0),
    "头像_便捷": (12.0, 94.0),
    "头像_精简": (20.0, 94.0),
    "头像_设置": (6.0, 49.0),
    "头像_设置_X": (92.5, 3.5),
    "头像_设置_X_确定": (58.5, 60.0),
    "头像_设置_基础设置": (95.0, 15.0),
    "头像_设置_基础设置_画面质量_流畅": (27.5, 57.0),
    "头像_设置_基础设置_渲染品质_低": (33.0, 66.0),
    "头像_设置_基础设置_刘海屏_关": (33.0, 75.5),
    "头像_设置_基础设置__帧数_低": (25.0, 39.0),
    "头像_设置_基础设置__最大视野范围_高": (42.0, 47.5),
    "头像_设置_基础设置__同屏人数_0": (29.1, 56.9),
    "头像_设置_视角设置": (95.0, 26.0),
    "头像_设置_视角设置_2.5D视角": (30.0, 47.0),
    "头像_设置_视角设置_3D视角": (65.0, 47.0),
    "头像_设置_社交设置": (95.0, 38.0),
    "商城": (24.0, 7.0),
    "商城_X": (92.0, 4.0),
    "商城_礼包": (7.0, 49.0),
    "商城_礼包_每日": (24.0, 16.0),
    "商城_礼包_每日_免费": (27.0, 52.5),
    "超级拉姆": (29.0, 7.0),
    "超级拉姆_X": (92.0, 4.0),
    "超级拉姆_每日奖励": (20.0, 88.0),
    "超级拉姆_每日奖励_领取": (11.5, 60.0),
    "订单": (71.0, 7.0),
    "时报": (76.0, 7.0),
    "SMC": (81.0, 7.0),
    "SMC_X": (92.0, 4.0),
    "SMC_每日工资": (90.0, 92.5),
    "SMC_每日工资_马上领取": (50.0, 64.0),
    "SMC_农夫": (21.0, 53.0),
    "SMC_向导": (50.0, 53.0),
    "SMC_厨师": (79.0, 53.0),
    "脚印": (86.0, 7.0),
    "任务": (91.0, 7.0),
    "任务_X": (92.0, 4.0),
    "任务_向导派遣": (94.0, 67.0),
    "任务_向导派遣_接取任务": (74.5, 81.5),
    "任务_向导派遣_前往领奖": (74.5, 81.5),
    "任务_向导派遣_确认": (74.5, 81.5),
    "任务_向导派遣_领奖": (74.5, 81.5),
    "任务_向导派遣_任务_0": (76.0, 17.0),  # 自上向下，从 0 递增
    "任务_向导派遣_任务_1": (76.0, 31.0),  # 自上向下，从 0 递增
    "任务_向导派遣_任务_2": (76.0, 45.0),  # 自上向下，从 0 递增
    "地图": (96.0, 7.0),
    "地图_X": (97.0, 5.5),
    "地图_浆果丛林": (12.5, 58.0),
    "地图_摩尔拉雅": (24.0, 23.0),
    "地图_阳光牧场": (32.5, 59.5),
    "地图_阳光沙滩": (29.5, 79.0),
    "地图_前哨站": (43.5, 24.5),
    "地图_爱心街区": (45.5, 46.0),
    "地图_摩尔城堡": (56.5, 44.0),
    "地图_开心农场": (56.0, 75.5),
    "地图_淘淘乐街": (69.5, 46.5),
    "地图_随便逛逛": (76.0, 71.5),
    "地图_家园": (7.5, 79.5),
    "地图_小镇": (13.5, 79.5),
    "地图_餐厅": (19.5, 79.5),
    "地图_角色功能切换": (8.5, 93.0),
    "地图_角色_洛克": (19.0, 93.0),
    "地图_角色_尼克": (25.0, 93.0),
    "地图_角色_杰西": (31.0, 93.0),
    "地图_角色_丝尔特": (40.0, 93.0),
    "地图_角色_埃里克斯": (46.0, 93.0),
    "地图_角色_彩虹": (52.0, 93.0),
    "地图_角色_花婶": (58.0, 93.0),
    "地图_角色_克劳": (66.5, 93.0),
    "地图_角色_弗礼德": (72.5, 93.0),
    "地图_角色_琦琦": (78.0, 93.0),
    "地图_角色_艾尔": (83.5, 93.0),
    "地图_角色_艾米": (89.5, 93.0),
    "地图_角色_大力": (95.0, 93.0),
    "地图_角色__汤米": (43.0, 93.0),
    "地图_角色__梅森": (52.5, 93.0),
    "地图_角色__尤尤": (62.5, 93.0),
    "地图_角色__茜茜": (72.0, 93.0),
    "地图_角色__贝琪": (77.5, 93.0),
    "地图_角色__瑞琪": (87.5, 93.0),
    "地图_角色__菩提": (97.0, 93.0),
    "地图_功能_城堡许愿池": (19.0, 93.0),
    "地图_功能_泡泡龙": (29.0, 93.0),
    "地图_功能_扭蛋机": (34.5, 93.0),
    "地图_功能_抓娃娃机": (44.0, 93.0),
    "地图_功能_连连看": (50.0, 93.0),
    "地图_功能_消消乐": (55.5, 93.0),
    "地图_功能_茜茜占卜": (65.0, 93.0),
    "地图_功能_随便逛逛": (75.0, 93.0),
    "主线": (4.5, 21.0),
    "支线": (10.5, 21.0),
    "日常": (16.5, 21.0),
    "活动": (81.0, 15.5),
    "扭蛋机": (86.0, 15.5),
    "新手目标": (91.0, 15.5),
    "店铺": (96.0, 15.5),
    "摇杆_中": (17.0, 75.5),
    "摇杆_上": (17.0, 65.0),
    "摇杆_下": (17.0, 86.5),
    "摇杆_左": (11.0, 75.5),
    "摇杆_右": (23.0, 75.5),
    "骑乘": (3.5, 59.0),
    "小镇": (30.0, 84.0),
    "好友": (30.0, 94.0),
    "表情": (37.0, 82.5),
    "动作": (44.5, 82.5),
    "动作_挥手": (16.5, 80.5),
    "动作_跳舞": (23.0, 80.5),
    "动作_摇摆": (29.5, 80.5),
    "动作_坐下": (16.5, 93.5),
    "动作_鼓掌": (23.0, 93.5),
    "动作_大笑": (29.5, 93.5),
    "动作__服装动作": (16.5, 93.5),
    "投掷": (52.0, 82.5),
    "互动_主": (85.0, 75.0),
    "互动_副": (76.5, 65.0),
    "互动_钓鱼": (86.0, 69.0),
    "钓鱼_鱼饵": (96.5, 70.0),
    "钓鱼_鱼饵_X": (84.5, 84.5),
    "钓鱼_鱼饵_0": (19.5, 93.0),  # 自左向右，从 0 递增
    "钓鱼_鱼饵_1": (24.5, 93.0),  # 自左向右，从 0 递增
    "钓鱼_鱼饵_2": (29.5, 93.0),  # 自左向右，从 0 递增
    "背包": (81.0, 94.0),
    "家园": (86.0, 94.0),
    "家园_伐木林_镐": (32.0, 92.0),
    "家园_伐木林_斧": (38.0, 92.0),
    "家园_伐木林_镰": (44.0, 92.0),
    "拉姆": (91.0, 94.0),
    "装扮": (96.0, 94.0),
    "餐厅_提示_取消": (41.0, 60.0),
    "餐厅_提示_确认": (59.0, 60.0),
    "餐厅_菜谱": (96.0, 63.0),
    "餐厅_菜谱_前往": (25.5, 86.5),
    "餐厅_菜谱_快速烹饪": (25.5, 86.5),
    "餐厅_管理": (96.0, 72.5),
    "餐厅_管理_开始营业": (48.5, 78.0),
    "餐厅_管理_领取": (48.0, 77.5),
    "餐厅_布置": (96.0, 83.0),
    "发言": (46.0, 90.0),
    "许愿_继续": (70.0, 75.0),
    "许愿_选项_0": (82.5, 58.0),  # 自下向上，从 0 递增
    "许愿_选项_1": (82.5, 45.5),  # 自下向上，从 0 递增
    "许愿_选项_2": (82.2, 33.0),  # 自下向上，从 0 递增
    "对话_继续": (70.0, 88.0),
    "对话_选项_0": (86.0, 57.0),  # 自下向上，从 0 递增，0 特殊处理
    "对话_选项_1": (86.0, 49.5),  # 自下向上，从 0 递增
    "对话_选项_2": (86.0, 39.5),  # 自下向上，从 0 递增
    "对话_选项_3": (86.0, 29.5),  # 自下向上，从 0 递增
    "对话_选项_4": (86.0, 19.5),  # 自下向上，从 0 递增
    "对话_选项_5": (86.0, 9.5),  # 自下向上，从 0 递增
    "发言_输入": (20.0, 95.5),
    "发言_发送": (43.5, 95.0),
    "发言_X": (48.5, 49.5),
    "发言_综合": (5.0, 13.5),
    "发言_跨服": (5.0, 22.5),
    "发言_本服": (5.0, 32.0),
    "发言_附近": (5.0, 41.5),
    "发言_小镇": (5.0, 51.0),
    "发言_私聊": (5.0, 60.0),
    "发言_系统": (5.0, 70.0),
}

# 华东位置，左上为 0.0 ，右下为 100.0
slide_positions = {
    "头像_设置_基础设置": (50.0, 50.0),
    "任务_向导派遣": (50.0, 50.0),
    "餐厅_菜单": (68.0, 68.0),
    "对话_选项": (86.0, 9.5),
    "动作": (22.5, 87.5),
}


def change_speed(input: float) -> float:
    """将线性输入 [0.0, 1.0] 变速，非线性输出 [0.0, 1.0]"""
    return math.cos((input + 1) * math.pi) / 2.0 + 0.5


@dataclass
class Wait(object):
    """等待动作"""

    last_time: int  # 持续时间，单位为 ms

    def generate(self) -> list:
        global timestamp_now
        timestamp_now += self.last_time
        return []


class MouseButton(Enum):
    """鼠标按钮枚举"""

    LEFT = 0
    RIGHT = 1
    MIDDLE = 2
    L = LEFT
    R = RIGHT
    M = MIDDLE


@dataclass
class Click(object):
    """点击动作"""

    x: float  # X 坐标，单位为百分比
    y: float  # Y 坐标，单位为百分比
    delay_time: int = 300  # 延迟时间，单位为 ms
    last_time: int = 30  # 持续时间，单位为 ms
    random_delta: float = 0.0  # 随机位移，单位为百分比
    click_times: int = 1  # 点击次数
    mouse_button: MouseButton = MouseButton.LEFT  # 鼠标按键

    def generate(self) -> list[dict]:
        global timestamp_now
        l = []

        if self.mouse_button is MouseButton.LEFT:
            button_name = "Mouse"
        elif self.mouse_button is MouseButton.RIGHT:
            button_name = "MouseRButton"
        elif self.mouse_button is MouseButton.MIDDLE:
            button_name = "MouseMButton"

        if self.random_delta != 0.0:
            x = self.x + uniform(-self.random_delta, self.random_delta)
            y = self.y + uniform(-self.random_delta, self.random_delta)
        else:
            x = self.x
            y = self.y

        for i in range(self.click_times):
            timestamp_now += self.delay_time
            mouse_down = {
                "Delta": 0,
                "EventType": button_name + "Down",
                "Timestamp": timestamp_now,
                "X": x,
                "Y": y,
            }
            l.append(mouse_down)

            timestamp_now += self.last_time

            mouse_up = {
                "Delta": 0,
                "EventType": button_name + "Up",
                "Timestamp": timestamp_now,
                "X": x,
                "Y": y,
            }
            l.append(mouse_up)

        return l


class ClickButton(Click):
    """点击按钮"""

    def __init__(self, name: str, **kwargs) -> None:
        global button_positions
        kwargs.setdefault("delay_time", 1500)
        kwargs.setdefault("random_delta", 1.0)
        super().__init__(*button_positions[name], **kwargs)


@dataclass
class Drag(object):
    """拖动动作"""

    x0: float  # 起始点 X 坐标，单位为百分比
    y0: float  # 起始点 Y 坐标，单位为百分比
    x1: float  # 终止点 X 坐标，单位为百分比
    y1: float  # 终止点 Y 坐标，单位为百分比
    delay_time: int = 300  # 延迟时间，单位为 ms
    move_time: int = 1000  # 运动时间，单位为 ms
    interval_time: int = 50  # 间隔时间，单位为 ms
    keep_time: int = 30  # 维持时间，单位为 ms
    random_delta: float = 0.0  # 随机位移，单位为百分比
    mouse_button: MouseButton = MouseButton.LEFT  # 鼠标按键

    def generate(self) -> list[dict]:
        global timestamp_now
        l = []

        if self.mouse_button is MouseButton.LEFT:
            button_name = "Mouse"
        elif self.mouse_button is MouseButton.RIGHT:
            button_name = "MouseRButton"
        elif self.mouse_button is MouseButton.MIDDLE:
            button_name = "MouseMButton"

        if self.random_delta != 0.0:
            delta = uniform(-self.random_delta, self.random_delta)
            x0 = self.x0 + delta
            y0 = self.y0 + delta
            x1 = self.x1 + delta
            y1 = self.y1 + delta
        else:
            x0 = self.x0
            y0 = self.y0
            x1 = self.x1
            y1 = self.y1

        timestamp_now += self.delay_time

        mouse_down = {
            "Delta": 0,
            "EventType": button_name + "Down",
            "Timestamp": timestamp_now,
            "X": x0,
            "Y": y0,
        }
        l.append(mouse_down)

        dx = x1 - x0
        dy = y1 - y0
        total_steps = math.ceil(self.move_time / self.interval_time)
        for i in range(total_steps):
            progress = (i + 1) / total_steps
            progress = change_speed(progress)
            timestamp_now += self.interval_time

            mouse_move = {
                "Delta": 0,
                "EventType": "MouseMove",
                "Timestamp": timestamp_now,
                "X": x0 + dx * progress,
                "Y": y0 + dy * progress,
            }
            l.append(mouse_move)

        timestamp_now += self.keep_time

        mouse_up = {
            "Delta": 0,
            "EventType": button_name + "Up",
            "Timestamp": timestamp_now,
            "X": x1,
            "Y": y1,
        }
        l.append(mouse_up)

        return l


class MoveUp(Drag):
    """向上移动"""

    def __init__(self, keep_time: int, **kwargs) -> None:
        kwargs.setdefault("delay_time", 500)
        kwargs.setdefault("move_time", 500)
        kwargs.setdefault("random_delta", 1.0)
        super().__init__(
            *button_positions["摇杆_中"],
            *button_positions["摇杆_上"],
            keep_time=keep_time,
            **kwargs,
        )


class MoveDown(Drag):
    """向下移动"""

    def __init__(self, keep_time: int, **kwargs) -> None:
        kwargs.setdefault("delay_time", 500)
        kwargs.setdefault("move_time", 500)
        kwargs.setdefault("random_delta", 1.0)
        super().__init__(
            *button_positions["摇杆_中"],
            *button_positions["摇杆_下"],
            keep_time=keep_time,
            **kwargs,
        )


class MoveLeft(Drag):
    """向左移动"""

    def __init__(self, keep_time: int, **kwargs) -> None:
        kwargs.setdefault("delay_time", 500)
        kwargs.setdefault("move_time", 500)
        kwargs.setdefault("random_delta", 1.0)
        super().__init__(
            *button_positions["摇杆_中"],
            *button_positions["摇杆_左"],
            keep_time=keep_time,
            **kwargs,
        )


class MoveRight(Drag):
    """向右移动"""

    def __init__(self, keep_time: int, **kwargs) -> None:
        kwargs.setdefault("move_time", 500)
        kwargs.setdefault("random_delta", 1.0)
        super().__init__(
            *button_positions["摇杆_中"],
            *button_positions["摇杆_右"],
            keep_time=keep_time,
            **kwargs,
        )


@dataclass
class Slide(object):
    """滑动动作"""

    delta: int
    x: float  # X 坐标，单位为百分比
    y: float  # Y 坐标，单位为百分比
    delay_time: int = 500  # 延迟时间，单位为 ms
    last_time: int = 3000  # 持续时间，单位为 ms
    random_delta: float = 0.0  # 随机位移，单位为百分比
    slide_times: int = 1  # 滑动次数

    def generate(self) -> list[dict]:
        global timestamp_now
        l = []

        if self.random_delta != 0.0:
            x = self.x + uniform(-self.random_delta, self.random_delta)
            y = self.y + uniform(-self.random_delta, self.random_delta)
        else:
            x = self.x
            y = self.y

        for i in range(self.slide_times):
            timestamp_now += self.delay_time
            mouse_wheel = {
                "Delta": self.delta,
                "EventType": "MouseWheel",
                "Timestamp": timestamp_now,
                "X": x,
                "Y": y,
            }
            l.append(mouse_wheel)
            timestamp_now += self.last_time

        return l


class SlideDown(Slide):
    """向下滑动"""

    def __init__(self, name: str, **kwargs) -> None:
        kwargs["random_delta"] = 0.5
        super().__init__(-120, *slide_positions[name], **kwargs)


class SlideUp(Slide):
    """向上滑动"""

    def __init__(self, name: str, **kwargs) -> None:
        kwargs["random_delta"] = 0.5
        super().__init__(120, *slide_positions[name], **kwargs)


@dataclass
class Input(object):
    string: str
    backspace: int = 0  # 退格次数
    enter: int = 0  # 回车次数
    delay_time: int = 1000  # 延迟时间，单位为 ms
    last_time: int = 1000  # 持续时间，单位为 ms

    def generate(self) -> list[dict]:
        global timestamp_now
        l = []

        timestamp_now += self.delay_time
        input_message = {
            "EventType": "IME",
            "Msg": f"start_{self.string}_end del={self.backspace} enter={self.enter}",
            "Timestamp": timestamp_now,
        }
        l.append(input_message)
        timestamp_now += self.last_time

        return l


class ActionChain(UserList):
    """动作链"""

    def generate(self) -> list[dict]:
        l = []
        for action in self.data:
            l += action.generate()
        return l

    def __add__(self, other: "ActionChain") -> "ActionChain":
        result = ActionChain()
        result.data.extend(self.data)
        result.data.extend(other.data)
        return result

    def __mul__(self, other: int) -> "ActionChain":
        result = ActionChain()
        result.data = self.data * other
        return result


class Pick(ActionChain):
    """采集"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ClickButton("互动_主"),
            Wait(3000),
        ]


class GetOff(ActionChain):
    """下车
    坐下动作会强制取消骑乘状态"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ClickButton("动作"),
            ClickButton("动作_坐下"),
        ]


class ClickArea(ActionChain):
    """区域点击"""

    def __init__(
        self, x0: float, y0: float, x1: float, y1: float, delta: float = 10.0
    ) -> None:
        super().__init__()
        for i in range((x1 - x0) // delta):
            x = x0 + (i + 1) * delta
            for j in range((y1 - y0) // delta):
                y = y0 + (j + 1) * delta
                self.data.append(Click(x, y, delay_time=300 + randint(0, 500)))
        self.data.append(Wait(3000))  # 等待响应


class Speak(ActionChain):
    """发言"""

    def __init__(self, word: str, channel: str = "附近") -> None:
        self.data += [
            ClickButton("发言_输入"),
            ClickButton("发言_" + channel),
            Input(word),
            ClickButton("发言_发送"),
            ClickButton("发言_X"),
        ]


class ChangeMap(ActionChain):
    """更换地图"""

    def __init__(self, name: str, last_time: int = 120000) -> None:
        super().__init__()
        self.data += [
            ClickButton("地图"),
            ClickButton("地图_" + name),
            Wait(last_time),
        ]


class Navigate2NPC(ActionChain):
    """NPC 导航"""

    def __init__(self, name: str, last_time: int = 120000) -> None:
        super().__init__()
        _y = button_positions["地图_角色功能切换"][1]
        self.data += [
            ClickButton("地图"),
            Drag(20.0, _y, 80.0, _y),
        ]

        # 需要翻页
        if name in (
            "汤米",
            "梅森",
            "尤尤",
            "茜茜",
            "贝琪",
            "瑞琪",
            "菩提",
        ):
            self.data.append(Drag(80.0, _y, 20.0, _y))
            name = "_" + name

        self.data += [
            ClickButton("地图_角色_" + name),
            Wait(last_time),
            ClickButton("对话_继续"),
        ]
        if name != "克劳":
            # 通过重进对话来刷新选项并重置位置
            # 克劳处空间狭小，可能卡住
            self.data += [
                ClickButton("对话_选项_0"),
                Wait(3000),
                ClickButton("互动_主"),
                ClickButton("对话_继续"),
            ]


class Navigate2Feature(ActionChain):
    """功能导航"""

    def __init__(self, name: str, last_time: int = 120000) -> None:
        super().__init__()
        self.data += [
            ClickButton("地图"),
            ClickButton("地图_角色功能切换"),
            ClickButton("地图_功能_" + name),
            Wait(last_time),
        ]


class InitSettings(ActionChain):
    """初始化设置"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ClickButton("头像"),
            ClickButton("头像_精简"),
            ClickButton("头像_便捷"),
            ClickButton("头像_设置"),
            ClickButton("头像_设置_基础设置"),
            ClickButton("头像_设置_基础设置_画面质量_流畅"),
            ClickButton("头像_设置_基础设置_渲染品质_低"),
            ClickButton("头像_设置_基础设置_刘海屏_关"),
            SlideDown("头像_设置_基础设置", slide_times=3),
            ClickButton("头像_设置_基础设置__帧数_低"),
            ClickButton("头像_设置_基础设置__最大视野范围_高"),
            ClickButton("头像_设置_基础设置__同屏人数_0", random_delta=0.0),
            ClickButton("头像_设置_视角设置"),
            ClickButton("头像_设置_视角设置_2.5D视角"),
            ClickButton("头像_设置_X"),
            ClickButton("头像_设置_X_确定"),
            Wait(5000),
            ClickButton("屏幕空白"),
        ]


class CheckIn(ActionChain):
    """签到"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ClickButton("商城"),
            ClickButton("商城_礼包"),
            ClickButton("商城_礼包_每日"),
            ClickButton("商城_礼包_每日_免费"),
            ClickButton("屏幕空白"),
            ClickButton("商城_X"),
            Wait(1000),
            ClickButton("超级拉姆"),
            ClickButton("超级拉姆_每日奖励"),
            ClickButton("超级拉姆_每日奖励_领取"),
            ClickButton("屏幕空白"),
            ClickButton("超级拉姆_X"),
            Wait(1000),
            ClickButton("SMC"),
            ClickButton("SMC_每日工资"),
            ClickButton("SMC_每日工资_马上领取"),
            ClickButton("屏幕空白"),
            ClickButton("SMC_X"),
            Wait(1000),
        ]


class Divine(ActionChain):
    """占卜"""

    def __init__(self) -> None:
        super().__init__()
        self.data = [
            Navigate2Feature("茜茜占卜"),
            ClickButton("对话_选项_0"),
            Wait(3000),
            ClickButton("互动_主"),
            ClickButton("对话_继续"),
            ClickButton("对话_选项_3"),
            Wait(1500),
            Drag(
                uniform(40.0, 50.0),
                uniform(60.0, 70.0),
                uniform(50.0, 60.0),
                uniform(70.0, 80.0),
                random_delta=1.0,
            ),
            Wait(3000),
            ClickButton("屏幕空白"),
            Wait(5000),
            Click(84.5, 63.0, random_delta=0.5),
            Wait(1000),
        ]


class MakeWish(ActionChain):
    """许愿"""

    def __init__(self) -> None:
        super().__init__()
        self.data = [
            ChangeMap("爱心街区"),
            Navigate2Feature("城堡许愿池", 3000),
            ClickButton("互动_主"),
            Wait(3000),
            ClickButton("许愿_继续"),
            ClickButton("许愿_选项_0"),
            ClickButton("屏幕空白"),
            Wait(1000),
            ClickButton("互动_主"),
            Wait(10000),
            ClickButton("许愿_继续"),
            ClickButton(f"许愿_选项_{randint(0, 2)}"),
            ClickButton("许愿_继续"),
            ClickButton("许愿_继续"),
            Wait(1000),
        ]


class GuiderMission(ActionChain):
    """向导任务
    穿向导服
    默认选头三个任务：摩尔城堡，摩尔拉雅雪山，浆果丛林"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ChangeMap("摩尔城堡"),
            ClickButton("任务"),
            ClickButton("任务_向导派遣"),
            ClickButton("任务_向导派遣_接取任务"),
            Wait(10000),
            ClickButton("对话_选项_3"),
            Wait(1000),
            ClickButton("任务_向导派遣_任务_0"),
            ClickButton("任务_向导派遣_任务_1"),
            ClickButton("任务_向导派遣_任务_2"),
            ClickButton("任务_向导派遣_确认"),
            ClickButton("屏幕空白"),
            Wait(1000),
        ]

        self.do()  # 接取任务后就在摩尔城堡，无须换图
        self.do("摩尔拉雅")
        self.do("浆果丛林")

        self.data += [
            ChangeMap("摩尔城堡"),
            ClickButton("任务"),
            ClickButton("任务_向导派遣"),
            ClickButton("任务_向导派遣_前往领奖"),
            Wait(10000),
            ClickButton("对话_选项_3"),
            ClickButton("任务_向导派遣_领奖"),
            ClickButton("屏幕空白"),
            Wait(1000),
        ]

    def do(self, where: Optional[str] = None) -> None:
        if where:
            self.data.append(ChangeMap(where))

        self.data += [
            ClickButton("动作"),
            SlideDown("动作"),
            ClickButton("动作__服装动作"),
            Wait(21000),
        ]


class GatherForest(ActionChain):
    """伐木林资源采集
    不保证全部采集，但刷满 SMC 经验足以"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            MoveDown(3000),
            MoveLeft(500),
        ]
        for i in range(5):
            self.do(5 - i)
            self.data.append(MoveRight(i * 2000))
            self.do(5 - i)
            self.data.append(MoveUp(i * 2000))
            self.do(5 - i)
            self.data.append(MoveLeft(i * 1000))
            self.do(5 - i)
            self.data.append(MoveDown(i * 1000))

    def do(self, n: int) -> None:
        for i in range(n):
            self.data += [
                ClickButton("家园_伐木林_镐"),
                ClickButton("互动_主", delay_time=2000, click_times=3),
                ClickButton("家园_伐木林_斧"),
                ClickButton("互动_主", delay_time=2000, click_times=5),
                ClickButton("家园_伐木林_镰"),
                ClickButton("互动_主", delay_time=2000, click_times=7),
            ]


class GatherMoerlaya(ActionChain):
    """摩尔拉雅资源采集
    5 个白浆果
    夜间 5轮"""

    def __init__(self, n: int = 5) -> None:
        super().__init__()
        self.data.append(ChangeMap("摩尔拉雅"))
        for i in range(5):
            self.do()

    def do(self) -> None:
        self.data += [
            ChangeMap("摩尔拉雅", 25000),
            ClickButton("骑乘"),
            MoveUp(500),
            MoveRight(1400),
            Pick(),
            ClickButton("骑乘"),
            MoveLeft(2200),
            MoveDown(4200),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(3100),
            MoveDown(4500),
            MoveRight(500),
            Pick(),
            Navigate2NPC("茜茜", 20000),
            ClickButton("对话_选项_0"),
            MoveRight(100),
            MoveDown(1200),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(4300),
            MoveUp(500),
            MoveRight(300),
            Pick(),
        ]


class GatherQianShaoZhan(ActionChain):
    """前哨站资源采集
    13 个黑浆果
    1 个草丛（剩余两个草丛距离远，浆果刷新快，暂时不采集）
    夜间 5 轮"""

    def __init__(self, n: int = 5) -> None:
        super().__init__()
        self.data.append(ChangeMap("前哨站"))
        self.prepare()
        for i in range(n):
            self.do()

    def prepare(self) -> None:
        self.data += [
            Navigate2NPC("瑞琪", 30000),
            ClickButton("对话_选项_0"),
            ClickButton("骑乘"),
            MoveDown(1300),
            MoveRight(3500),
            MoveUp(1000),
        ]

    def do(self) -> None:
        """13 个黑浆果"""
        self.data += [
            Pick(),
            ClickButton("骑乘"),
            MoveRight(4100),
            MoveDown(3850),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(4950),
            MoveUp(200),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(350),
            MoveUp(3800),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(250),
            Pick(),
            ClickButton("骑乘"),
            MoveDown(400),
            MoveRight(650),
            Pick(),
            ClickButton("骑乘"),
            MoveDown(3300),
            Pick(),
            ClickButton("骑乘"),
            MoveDown(500),
            MoveRight(450),
            Pick(),
            ClickButton("骑乘"),
            MoveDown(1350),
            MoveLeft(50),
            Pick(),
            ClickButton("骑乘"),
            MoveDown(5200),
            MoveLeft(11050),
            Pick(),
            ClickButton("骑乘"),
            MoveLeft(3100),
            MoveUp(1500),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(100),
            MoveUp(2000),
            Pick(),
            ClickButton("骑乘"),
            MoveUp(1300),
            MoveRight(900),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(500),
            MoveUp(4500),
        ]


class GatherJiangGuoCongLin(ActionChain):
    """TODO: 浆果丛林资源采集
    6 个红浆果
    ？ 个橙浆果
    5 个草丛"""

    def __init__(self, n: int = 5) -> None:
        super().__init__()
        # self.data.append(ChangeMap("浆果丛林"))
        self.prepare()
        for i in range(n):
            self.do()
            break

    def prepare(self):
        self.data.append(MoveDown(2300))

    def do(self) -> None:
        self.data += [
            Pick(),
            ClickButton("骑乘"),
            MoveLeft(1600),
            MoveUp(1800),
            MoveRight(500),
            Pick(),
            ClickButton("骑乘"),
            MoveLeft(1400),
            MoveUp(1300),
            Pick(),
            ClickButton("骑乘"),
            MoveUp(1500),
            MoveRight(2000),
            Pick(),
            ClickButton("骑乘"),
            MoveRight(1500),
            MoveUp(1500),
            MoveRight(2000),
            Pick(),
            ClickButton("骑乘"),
            MoveUp(2000),
            MoveRight(1500),
            Pick(),
            ClickButton("骑乘"),
        ]
        return
        [
            Pick(),
            ClickButton("骑乘"),
            MoveUp(),
            MoveDown(),
            MoveLeft(),
            MoveRight(),
        ]


class Talk2NPC(ActionChain):
    """NPC 对话好感度"""

    def __init__(self) -> None:
        super().__init__()
        self.NPCs = {
            "杰西": 10000,
            "洛克": 10000,
            "尼克": 5000,
            "埃里克斯": 10000,
            "丝尔特": 5000,
            "花婶": 10000,
            "琦琦": 25000,
            "艾米": 10000,
            "汤米": 15000,
            "克劳": 90000,
            "弗礼德": 90000,
            "茜茜": 120000,
            "贝琪": 30000,
            "艾尔": 150000,
            "尤尤": 150000,
            "菩提": 35000,
            "梅森": 40000,
            "彩虹": 90000,
            "瑞琪": 90000,
        }
        self.data.append(ChangeMap("摩尔城堡"))
        for name, time in self.NPCs.items():
            self.data.append(Navigate2NPC(name, time))
            self.do(name)

        self.data.append(Wait(1000))

    def next(self) -> None:
        self.data += [
            ClickButton("对话_选项_0"),
            ClickButton("对话_选项_1"),
            ClickButton("对话_继续"),
        ]

    def do(self, name: str) -> None:
        choice = {
            "杰西": 2,
            "琦琦": 2,
        }
        n = choice.get(name, 1)
        self.data += [
            SlideDown("对话_选项"),  #  应对 NPC 对话选项多于 6 个的情况
            ClickButton("对话_选项_" + str(n)),
        ]
        for i in range(3):
            self.next()
        self.data.append(Wait(1000))


class Cook(ActionChain):
    """烹饪
    扩建过一次的厨房
    4 个炉子都是空的
    上菜窗口无空缺
    上菜窗口无对应菜品（浆果捞）"""

    def __init__(self, cook_times: int = 10) -> None:
        super().__init__()
        self.prepare(wait=8000)
        for i in range(cook_times):
            self.do()

    def prepare(self, wait: int) -> None:
        self.data += [
            ClickButton("餐厅_菜谱"),
            ClickButton("餐厅_菜谱_前往"),
            Wait(wait),
        ]

    def do(self) -> None:
        for i in range(4):
            self.order()
            self.move_left()

        self.prepare(wait=0)
        self.data.append(Wait(50000))

        for i in range(4):
            self.get()
            self.move_left()
        self.prepare(3000)

    def get(self) -> None:
        self.data += [
            ClickButton("互动_主"),
            ClickButton("餐厅_提示_取消"),  # 相当于点击屏幕空白，防错位
            Wait(500),
        ]

    def order(self) -> None:
        self.data += [
            ClickButton("互动_主"),
            ClickButton("餐厅_提示_取消"),  # 相当于点击屏幕空白，防错位
            SlideDown("餐厅_菜单"),
            Click(52.0, 77.5, random_delta=0.5),
            # 第二列坐标
            # Click(63.0, 77.5, random_delta=0.5),
            ClickButton("餐厅_菜谱_快速烹饪"),
            Wait(500),
        ]

    def move_left(self) -> None:
        self.data.append(MoveLeft(5))


class GoFishing(ActionChain):
    """TODO: 钓鱼"""

    def __init__(self) -> None:
        super().__init__()
        self.data += [
            ClickButton("钓鱼_鱼饵"),
            ClickButton("钓鱼_鱼饵_0"),
        ]
        for i in range(100):
            self.do()

    def do(self):
        self.data += [
            ClickButton("互动_主"),
            Wait(1000),
            ClickButton("互动_主", delay_time=0),
            Wait(1000),
            ClickButton("互动_主", delay_time=0),
            ClickButton("屏幕空白"),
        ]


def export(actions: Iterable, name: str, **kwargs) -> None:
    """导出 BlueStacks 可用的 json 文件"""
    global timestamp_now
    timestamp_now = 0
    events = []
    for action in actions:
        events.extend(action.generate())
    data = {
        "Acceleration": 1,
        "CreationTime": datetime.now().strftime("%Y%m%dT%H%M%S"),
        "DoNotShowWindowOnFinish": False,
        "Events": events,
        "LoopDuration": 0,  # TillTIme 模式下有效，循环时长，单位为 s
        "LoopInterval": 0,  # 循环间隔，单位为 s
        "LoopIterations": 1,  # TillLoopNumber 模式下有效，循环次数
        "LoopType": "TillLoopNumber",  # "TillLoopNumber" "TillTime" "UntilStopped"
        "MacroSchemaVersion": 2,
        "RestartPlayer": False,
        "RestartPlayerAfterMinutes": 60,
    }
    data |= kwargs
    with open(f"./json/{name}.json", "wt", encoding="utf-8") as f:
        json.dump(data, f)
    print(f"{name}: {timedelta(milliseconds=timestamp_now)}")


def debug(actions: Iterable) -> None:
    """对应时间输出事件"""

    from pprint import pp
    from sys import exit

    export(actions, f"DEBUG_{datetime.now().strftime('%H-%M-%S')}")
    sleep(5)
    global timestamp_now
    timestamp_now = 0
    events = []
    for action in actions:
        events.extend(action.generate())

    timestamp = 0
    for event in events:
        sleep((event["Timestamp"] - timestamp) / 1000.0)
        timestamp = event["Timestamp"]
        print(f"{'#'*30} {timedelta(milliseconds=timestamp)}")
        pp(event)

    exit()


if __name__ == "__main__":
    # debug(GatherJiangGuoCongLin())

    export(InitSettings(), "初始化设置")
    export(CheckIn(), "日常签到")
    export(Divine(), "日常占卜")
    export(MakeWish(), "日常许愿")
    export(GuiderMission(), "日常向导任务")
    export(GatherMoerlaya(), "摩尔拉雅采集")
    export(GatherQianShaoZhan(), "前哨站采集")
    # export(GatherJiangGuoCongLin(), "浆果丛林采集")
    export(Talk2NPC(), "日常 NPC 好感度对话")
    export([ClickButton("互动_主", delay_time=300)], "辅助互动", LoopType="UntilStopped")
    export(GatherForest(), "辅助伐木林采集")
    export(Cook(), "烹饪")
    export(
        InitSettings()
        + CheckIn()
        + Divine()
        + MakeWish()
        + GuiderMission()
        + Talk2NPC(),
        "日常整合",
    )
