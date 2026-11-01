# 第 36 周 · 阶段收口：整理 P2 至 P4

- **日期**：2027-07-05～2027-07-11
- **阶段**：2 · Agent 与多 Agent
- **知识层级**：L4
- **投入**：约 15 小时（Agent 约 12 小时，评测与观测约 3 小时）

## 本周目标

按文档能分别跑起 P2、P3、P4；阶段复盘写明 L3 与 L4 里仍不稳的部分。

## 完成标准

- 一份说明包含三个作品的命令、输入例子和期望现象。
- 轨迹评测和 P1 召回脚本都能在无密钥模式下跑夹具。
- 复盘列出要带到生产化阶段的两个风险：成本和错误引用。
- 依赖文件与 README 的安装命令一致。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【Agent】核对 P2、P3、P4 的脚本参数，把命令抄进 `notes/agent-portfolio.md` 并实际各跑一次夹具或真实例子。 |
| 周二 | 2.5h | 【Agent】让无密钥的 pytest 覆盖三个作品的主路径。失败就补假模型，而不是把密钥写进 CI。 |
| 周三 | 2.5h | 【Agent】检查依赖安装命令。用 README 里的 Conda 或 uv 命令在笔记中记录你验证过的那一条。 |
| 周四 | 2.5h | 【Agent】删除重复的实验脚本入口，或在说明里标出哪一个是正式入口。保留评测数据文件。 |
| 周五 | 2h | 【Agent】更新根目录 README 的作品列表，链到 P1–P4 的说明。若应用 README 还没有这些小节，就补上。 |
| 周末 | 3h | 【评测】重跑轨迹评测夹具和一页节点日志，写阶段复盘：步数上限、交接上限、批评规则各自挡住过什么。 |

## Checklist

- [ ] 三个作品都有命令
- [ ] 无密钥测试通过
- [ ] 安装命令核对过
- [ ] 正式入口明确
- [ ] 阶段复盘已写

## 参考链接

- [LangGraph 概览](https://docs.langchain.com/oss/python/langgraph/overview)
- [子代理](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
- [ReAct 论文](https://arxiv.org/abs/2210.03629)
- [GitHub Actions 中的密钥](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
