# 第 29 周 · 作品 P3：LangGraph 工作流

- **日期**：2027-05-17～2027-05-23
- **阶段**：2 · Agent 与多 Agent
- **知识层级**：L4
- **投入**：约 15 小时（Agent 约 12 小时，评测与观测约 3 小时）

## 本周目标

README 里的图和实际节点一致，相关与资料不足两条路径都有测试。

## 完成标准

- 用 Mermaid 或等价文本画出节点和边，放进 P3 说明。
- 演示问题有期望路径：检索后直接生成，或改写一次后结束。
- 测试覆盖这两条路径。
- 一页说明写出每个节点是否消耗 token。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【Agent】整理 P3 入口脚本，参数包含问题和 thread id。输出最终答案、来源和停止原因。 |
| 周二 | 2.5h | 【Agent】补齐两条路径的测试，使用假检索和假生成。 |
| 周三 | 2.5h | 【Agent】写 Mermaid 图，节点名与代码一致。自己对着图讲一遍，把卡壳的边改到图或代码里。 |
| 周四 | 2.5h | 【Agent】选两道演示题跑通，把轨迹摘要写进 `notes/p3-demo.md`。 |
| 周五 | 2h | 【Agent】在 README 增加作品 P3：如何运行、图的位置、两条路径各代表什么。 |
| 周末 | 3h | 【评测】从追踪或日志里摘一次运行的节点顺序。标出哪个节点调用了模型、哪个只是规则。算出这一次的大概 token，写入笔记。 |

## Checklist

- [ ] 入口脚本可运行
- [ ] 两条路径有测试
- [ ] 图与代码一致
- [ ] README 含 P3
- [ ] 节点是否耗 token 已标明

## 参考链接

- [用 LangGraph 做检索 Agent](https://docs.langchain.com/oss/python/langgraph/agentic-rag)
- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [持久化](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Mermaid 文档](https://mermaid.js.org/syntax/flowchart.html)
