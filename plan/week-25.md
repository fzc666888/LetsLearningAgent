# 第 25 周 · LangGraph 的状态、节点与边

- **日期**：2027-04-19～2027-04-25
- **阶段**：2 · Agent 与多 Agent
- **知识层级**：L4
- **投入**：约 15 小时（Agent 约 12 小时，评测与观测约 3 小时）

## 本周目标

图能从起点走到终点；节点函数可以在测试里替换。

## 完成标准

- 安装 LangGraph，版本记在依赖文件中。
- 状态里至少有消息列表和一个字符串字段。
- 两个节点按固定边执行，测试断言字段被第二个节点改写。
- 笔记用自己的话定义状态、节点和边。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【Agent】按官方安装说明加入 LangGraph。写一个最小图：单节点返回固定消息，测试 `invoke` 的结果。 |
| 周二 | 2.5h | 【Agent】定义本项目的状态：消息、查询、草稿。节点一写入规范化查询，节点二写入草稿。 |
| 周三 | 2.5h | 【Agent】用固定边连接起点、两个节点和终点。画出邻接关系，放进笔记。 |
| 周四 | 2.5h | 【Agent】测试里把第二个节点换成假函数，断言图的其余部分仍被调用。 |
| 周五 | 2h | 【Agent】给节点二接上你已有的模型客户端，但测试仍走假函数。真实调用一次，保存草稿。 |
| 周末 | 3h | 【评测】阅读 LangGraph 概览和 Graph API 中关于状态与边的部分。写一页：这张图目前哪一步是确定的，哪一步交给了模型。 |

## Checklist

- [ ] 依赖中有 LangGraph
- [ ] 两节点图可运行
- [ ] 假节点测试通过
- [ ] 邻接关系已画下
- [ ] 笔记区分确定步骤和模型步骤

## 参考链接

- [LangGraph 概览](https://docs.langchain.com/oss/python/langgraph/overview)
- [安装 LangGraph](https://docs.langchain.com/oss/python/langgraph/install)
- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [LangGraph 快速开始](https://docs.langchain.com/oss/python/langgraph/quickstart)
