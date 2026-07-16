# cookie-tool

一个简单的Cookie获取辅助工具。程序会打开平台登录页，待用户手动完成登录后，将当前会话的Cookie导出到本地 `cookie.txt` 文件。

> 本项目仅用于个人学习、测试和合法授权场景。请勿获取、传播或使用他人的Cookie。

## 功能特点

- 交互式选择平台，无需手动复制浏览器请求头
- 由用户在真实浏览器中手动登录
- 将Cookie统一保存为可直接使用的字符串格式
- 使用浏览器无痕模式，每次获取后自动关闭浏览器
- 小红书支持切换不同账号后连续获取
- 小红书Cookie会将 `abRequestId` 字段调整到最前面

## 支持平台

| 序号 | 平台 | 支持状态 |
| --- | --- | --- |
| 1 | 抖音 | ✅ |
| 2 | 快手 | ✅ |
| 3 | 小红书 | ✅ |
| 4 | 小红书蒲公英 | ✅ |
| 5 | 知乎 | ✅ |
| 6 | 哔哩哔哩 | ✅ |
| 7 | 百度 | ✅ |
| 8 | 微博 PC 端 | ✅ |
| 9 | 微博移动端 | ✅ |

## 环境要求

- Python3
- Chrome或其他可被DrissionPage识别的Chromium浏览器
- [DrissionPage](https://github.com/g1879/DrissionPage)

## 安装

1. 克隆项目并进入目录：

   ```bash
   git clone <你的仓库地址>
   cd ck_v1.6
   ```

2. 安装依赖：

   ```bash
   python -m pip install DrissionPage
   ```

## 使用演示

[点击查看 Cookie 小工具使用演示](https://www.zhihu.com/zvideo/1831601214263021568)

## 使用方法

1. 运行程序：

   ```bash
   python "cookie小工具v1.6.py"
   ```

2. 根据提示输入平台对应的数字。
3. 程序打开浏览器后，在网页中完成登录。
4. 确认已经登录成功，再回到终端按 `Enter` 键。
5. Cookie会保存到程序当前运行目录的 `cookie.txt` 中。

在等待登录的提示中输入 `Q` 或 `q`，可结束程序。

### 小红书多账号获取

选择小红书后，程序会询问是否继续获取下一个Cookie。如需继续，输入 `y` 后使用另一个账号登录。

> 同一账号重复登录不代表获取了多个独立账号的Cookie。

## 输出说明

Cookie会以下列格式写入 `cookie.txt`：

```text
name1=value1;name2=value2;name3=value3;
```

每次启动程序时，已存在的 `cookie.txt` 会被删除并重新生成。请提前备份仍需使用的内容。

## 安全提示

- Cookie通常具有与账号密码相近的登录权限，请勿发送给他人。
- 请勿将真实的 `cookie.txt` 提交到GitHub或其他公开仓库。
- 如Cookie疑似泄露，请立即在对应平台退出会话、修改密码或重置登录状态。
- 无痕模式不等于Cookie完全不落地；本工具会明确将结果保存到本地文件。

## 常见问题

### 浏览器没有正常打开

请先确认 Chrome/Chromium 已正确安装，然后升级 DrissionPage：

```bash
python -m pip install -U DrissionPage
```

### 获取到的Cookie无法使用

Cookie可能因账号退出、超时、风险控制或平台规则变更而失效。请确认网页已经完成登录，再在终端中按 `Enter` 键导出。

### 为什么原来的 cookie.txt 不见了

这是当前版本的预期行为：程序启动后会清理上一次的输出，避免新旧 Cookie 混在一起。

## 贡献

欢迎提交Issue反馈问题，或通过Pull Request提交改进。请勿在Issue、截图、日志或测试数据中附带真实Cookie。

## 作者

[马哥python说](https://github.com/mashukui)

---

如果这个项目对你有帮助，欢迎点一个Star⭐️。
