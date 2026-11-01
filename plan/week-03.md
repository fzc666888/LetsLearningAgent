# 第 3 周 · SQLite 持久化与消息结构

- **日期**：2026-11-16～2026-11-22
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

items 落在 SQLite 中，测试使用临时库；同时用类型描述一段对话消息列表。

## 完成标准

- 创建、读取、更新、删除都经过数据库，重启进程后数据仍在。
- 测试用 `tmp_path` 独立数据库，用例之间互不污染。
- 有一个带类型的消息模型，能表示 system、user、assistant 三种角色。
- 笔记说明上下文窗口是输入加输出的总预算，并举一个超长截断的例子。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】引入 SQLModel 或 SQLAlchemy，把 Item 表建在 SQLite 文件上。应用启动时创建表。保留 `/health`。 |
| 周二 | 2.5h | 【工程】把上周的内存 CRUD 换成数据库实现。服务层仍不直接写在路由函数里。 |
| 周三 | 2.5h | 【工程】测试夹具为每个用例生成临时数据库文件。覆盖创建后能读到、更新后字段变化、删除后 404、空列表。 |
| 周四 | 2.5h | 【工程】给列表加上稳定排序（按 id 或创建时间）。补一个「重复创建同一名称」的行为说明，并在测试里固定下来。 |
| 周五 | 2h | 【LLM】定义 `ChatMessage`（角色、内容）和 `Conversation`（有序列表）。写纯函数：追加消息、取最后 n 条。为它们写至少 4 个 pytest。 |
| 周末 | 3h | 【LLM】阅读上下文窗口。用 tiktoken 或官方用量字段，给一段自己写的三轮对话估算 token。在笔记里记下模型名来自 `OPENAI_MODEL`，以及估算值和真实用量的差异。 |

## Checklist

- [ ] CRUD 使用 SQLite
- [ ] 临时库测试互相隔离
- [ ] 分层仍然保持
- [ ] 消息模型有类型和测试
- [ ] 笔记含 token 估算

## 参考链接

- [SQLModel 建表](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/)
- [SQLAlchemy 快速开始](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [FastAPI SQL 数据库](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [SQLite 语言](https://www.sqlite.org/lang.html)
- [pytest tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [typing](https://docs.python.org/3/library/typing.html)
- [tiktoken](https://github.com/openai/tiktoken)
