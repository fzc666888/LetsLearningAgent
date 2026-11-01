# 第 42 周 · 不依赖密钥的评测进 CI

- **日期**：2027-08-16～2027-08-22
- **阶段**：3 · 生产化与求职
- **知识层级**：L5
- **投入**：约 15 小时（作品约 9 小时，求职约 6 小时）

## 本周目标

召回或轨迹夹具低于阈值时 CI 失败；真实模型评测仍在本机手动跑。

## 完成标准

- CI 运行现有 pytest，外加一个夹具评测命令。
- 工作流文件不包含密钥值，也不引用不存在的秘密来冒充已配置。
- 阈值写在评测配置里，并有一次你故意改坏夹具后看到失败、再改回的记录。
- 面试笔记能解释为什么线上评测和离线夹具要分开。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【作品】选定进入 CI 的命令：夹具上的 recall 或轨迹比较。确认该命令不读取 `OPENAI_API_KEY`。 |
| 周二 | 2.5h | 【作品】把命令加进 GitHub Actions。本地用同样的命令跑通。 |
| 周三 | 2.5h | 【作品】把阈值设成当前夹具刚好通过的值。写进配置并在笔记记录。 |
| 周四 | 2.5h | 【作品 1.5h】临时改坏一条夹具预期，确认命令失败，然后恢复。【求职 1h】写出 CI 失败时你第一眼该看的文件。 |
| 周五 | 2h | 【求职】准备五分钟说明：夹具保证什么、真实评测还要看什么、密钥为什么留在本机环境变量。 |
| 周末 | 3h | 【求职】把这段说明写成逐字稿，计时。标出你可能会被追问的两个词：阈值和假模型。 |

## Checklist

- [ ] CI 命令不需要密钥
- [ ] 工作流里没有密钥值
- [ ] 阈值有记录
- [ ] 改坏夹具时命令会失败
- [ ] 五分钟稿已计时

## 参考链接

- [GitHub Actions 测试 Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Actions 中的密钥](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [工作流语法](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [pytest 入门](https://docs.pytest.org/en/stable/getting-started.html)
