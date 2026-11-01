# 第 8 周 · 阶段收口：可运行的小服务

- **日期**：2026-12-21～2026-12-27
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（工程约 10 小时，LLM 概念约 5 小时）

## 本周目标

别人按 README 能在 Conda 或 uv 下跑起服务和测试；模型入口与工程入口都有说明。

## 完成标准

- README 含环境、测试、本地启动、Compose 启动和模型脚本。
- `pytest` 与 `ruff check` 在干净环境通过。
- 有一个使用 mock 模型客户端的接口测试，CI 不需要密钥。
- 复盘笔记列出 L0 已掌握项和仍不稳的两项。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【工程】整理目录：配置、路由、模型、服务、测试、脚本各就各位。删掉无用的临时代码，保留已有测试。 |
| 周二 | 2.5h | 【工程】增加 `scripts/dev.sh` 或等价说明，包含安装、测试、启动。命令在 README 里可复制。 |
| 周三 | 2.5h | 【工程】增加一个薄的生成接口，业务层依赖可替换的客户端。测试注入假客户端，断言状态码和响应字段。 |
| 周四 | 2.5h | 【工程】在新环境按 README 从头执行一遍（Conda 或 uv 任选你的日常工具，另一种在文档里保持可执行）。修文档和真实命令不一致的地方。 |
| 周五 | 2h | 【LLM】把前几周关于消息角色、token、采样和流式的笔记收成一页概念卡，每条不超过四行。 |
| 周末 | 3h | 【LLM】写阶段复盘：服务能做什么、测试如何保证、真实调用如何配置环境变量。列出进入 RAG 阶段前要守住的两条工程习惯。 |

## Checklist

- [ ] README 可按步骤执行
- [ ] pytest 与 ruff 通过
- [ ] 生成接口有 mock 测试
- [ ] 概念卡已整理
- [ ] 阶段复盘已写

## 参考链接

- [FastAPI 大项目结构](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [pytest 入门](https://docs.pytest.org/en/stable/getting-started.html)
- [Ruff](https://docs.astral.sh/ruff/)
- [uv](https://docs.astral.sh/uv/)
- [Conda 环境](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
- [OpenAI Python 库](https://github.com/openai/openai-python)
