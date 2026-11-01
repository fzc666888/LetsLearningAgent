# 第 35 周 · 节点耗时、token 预算与失败分类

- **日期**：2027-06-28～2027-07-04
- **阶段**：2 · Agent 与多 Agent
- **知识层级**：L4
- **投入**：约 15 小时（Agent 约 12 小时，评测与观测约 3 小时）

## 本周目标

超过预算时图会停止并写明原因；失败能归到四类之一。

## 完成标准

- 每个节点日志含名称、`latency_ms` 和 token 数。
- 预算用 token 上限表示，测试可把上限设得很小并断言停止。
- 失败分类覆盖：工具错误、空检索、循环或交接上限、结构化输出无效。
- 一次演示运行的分类和总 token 写入笔记。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【Agent】加节点计时包装。测试断言包装后的日志含名称和毫秒。 |
| 周二 | 2.5h | 【Agent】累计 prompt 与 completion token。没有真实用量时允许节点声明 0，并在日志里标明是估算还是接口返回。 |
| 周三 | 2.5h | 【Agent】设置预算。达到预算后写入停止原因 `budget`，不再调用下一个模型节点。用测试锁定。 |
| 周四 | 2.5h | 【Agent】实现分类函数，把已有停止原因映射到四类。每类至少一条单测。 |
| 周五 | 2h | 【Agent】跑 P3 或 P4 各一道，保存节点日志和分类结果。 |
| 周末 | 3h | 【评测】对照 OpenTelemetry 的 span 字段，写一页：你的节点日志还缺 trace id 或 parent 中的哪一个。给出下一阶段要补的两个字段。 |

## Checklist

- [ ] 节点日志含时延
- [ ] token 预算会停止
- [ ] 四类失败都有测试
- [ ] 一次演示已归类
- [ ] 与 span 的差距已写下

## 参考链接

- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/getting-started/)
- [LangSmith](https://docs.smith.langchain.com/)
- [持久化](https://docs.langchain.com/oss/python/langgraph/persistence)
- [十二要素：日志](https://12factor.net/logs)
