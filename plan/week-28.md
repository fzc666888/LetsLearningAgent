# 第 28 周 · 人工确认与线程恢复

- **日期**：2027-05-10～2027-05-16
- **阶段**：2 · Agent 与多 Agent
- **知识层级**：L4
- **投入**：约 15 小时（Agent 约 12 小时，评测与观测约 3 小时）

## 本周目标

拒绝时不写入；同意后写入；进程内用检查点按 thread id 恢复。

## 完成标准

- 新增只在确认后执行的 `save_note` 工具。
- 图在该工具前中断，测试能检查中断原因。
- 使用内存检查点，相同 `thread_id` 可以恢复，不同 id 互不影响。
- 命令行能输入同意或拒绝。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【Agent】阅读中断文档。列出你准备暂停的唯一步骤：保存笔记。 |
| 周二 | 2.5h | 【Agent】在保存工具前设置中断。测试编译后的图会停住，并且文件还没有被创建。 |
| 周三 | 2.5h | 【Agent】接入内存检查点。测试：恢复时传入同意，文件出现；传入拒绝，文件不出现。 |
| 周四 | 2.5h | 【Agent】命令行打印待保存的正文，读取同意或拒绝。thread id 由参数传入。 |
| 周五 | 2h | 【Agent】走通同意和拒绝各一次。把 thread id 和最终状态记入笔记。 |
| 周末 | 3h | 【评测】阅读持久化文档中检查点与线程的部分。写一页：thread id 丢失后你还能不能恢复，以及为什么保存动作必须停在工具之前。 |

## Checklist

- [ ] 保存前会中断
- [ ] 拒绝不会写文件
- [ ] 同意后同一线程可恢复
- [ ] 不同 thread id 隔离
- [ ] 持久化笔记已写

## 参考链接

- [中断](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [持久化](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [函数调用](https://developers.openai.com/api/docs/guides/function-calling)
