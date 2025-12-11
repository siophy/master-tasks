# hf-waker  
**每天自动唤醒你的 Hugging Face Spaces，永不冷启动！支持多 Space + Telegram 通知**

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/oversizexl/hf-waker/restart_hf_space.yaml?branch=main&label=Wake%20Spaces&logo=github)](https://github.com/oversizexl/hf-waker/actions)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces)
[![Telegram](https://img.shields.io/badge/Notify-Telegram-2CA5E0?logo=telegram)](https://telegram.org)

免费 Space 冷启动慢到崩溃？  
**hf-waker** 每天自动重启 + 保活，让你的项目秒开如飞！

- 支持批量管理多个 Space（一行配置搞定）  
- 每天定时自动重启（默认北京时间 00:00）  
- 手动一键唤醒（支持自定义原因）  
- 成功/失败自动推送 Telegram  
- 单 Space / 多 Space 完全兼容

## 功能一览

| 功能                 | 状态 | 说明                              |
|----------------------|------|-----------------------------------|
| 多 Space 批量管理     | Yes  | 逗号分隔，无限添加                 |
| 每天自动重启         | Yes  | GitHub Actions 定时执行            |
| 手动一键唤醒         | Yes  | 带原因说明                        |
| Telegram 通知        | Yes  | 美观列表 + 时间 + 成功状态         |
| 零维护部署           | Yes  | Fork + 加4个 Secrets 即可永久运行  |

## 3 分钟部署

1. Fork 本仓库 → https://github.com/oversizexl/hf-waker
2. 进入 **Settings → Secrets and variables → Actions**
3. 添加以下 Secrets：

| Name              | 示例值                                          | 必填 |
|-------------------|-------------------------------------------------|------|
| `HF_TOKEN`        | `hf_xxxxxxxxxxxxxxxxxxxxxxxx`                  | Yes  |
| `SPACE_REPO_ID`   | `yourname/demo,yourname2/app,xxx/gradio`        | Yes  |
| `BOT_TOKEN`       | `123456:ABC-DEF1234ghIkl-01234567890`     | No   |
| `CHAT_ID`         | `-1001234567890` 或你的 ID                      | No   |

> HF_TOKEN 获取：https://huggingface.co/settings/tokens （勾选 Write 权限）

4. 完成！默认每天北京时间晚上零点 自动唤醒所有 Space  
   手动触发：Actions → Wake HF Spaces → Run workflow

## Telegram 通知示例

**自动唤醒**  
```
🤖 HF Space 自动保活

⏰ 北京时间 2025-12-11 00:21:39
🛰  Space: username/demo

✅ 保活 成功 🎉
```

**手动唤醒**
```
🖐 HF Space 手动保活

👤 触发人: username
📝 原因: 手动保活
🛰 以下 Space 已保活：
 • username/demo
 • username/demo2

✅ 保活 成功 🎉
```


## 修改唤醒时间（可选）

默认每天 **00:00**（北京时间）  
想改成早上 8 点？编辑 `.github/workflows/restart_hf_space.yaml` 第 6 行：

```yaml
- cron: '0 0 * * *'   # 改成你想要的时间 UTC时间
```



<h2 align="center">如果帮到了你，欢迎点个 🌟 Star 支持一下～</h2>
<h5 align="center">hf-waker —— 让你的 Space 永远醒着</h5>
<div align="center">

[![License](https://img.shields.io/github/license/oversizexl/hf-waker?color=orange)](./LICENSE)  

</div>
