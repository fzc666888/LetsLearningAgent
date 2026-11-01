# 第 1 周 · Python 工程脚手架与第一次模型调用

- **日期**：2026-11-02～11-08
- **阶段**：0 · 工程底座
- **知识层级**：L0
- **投入**：约 15 小时（按已定稿日程：周一至周五做工程，周末完成模型调用）

## 本周目标

Python 工程脚手架 + FastAPI 带测试小 API + 一次真实 LLM 调用。

## 完成标准

仓库可启动；pytest 绿；/health + CRUD；LLM 脚本打通。

- 仓库可启动
- pytest 绿
- /health + CRUD
- LLM 脚本打通

## 任务拆分（约 15 小时）

按日安排与下表一致，已定稿条目保持原句。

- 周一 2.5h：Conda/venv 环境与仓库、README、.gitignore、首 commit。Conda 或 uv 均可，本仓库推荐 Conda 亦可。在 README 写明创建环境、安装依赖和启动命令。`.gitignore` 忽略 `.env`、`__pycache__` 和虚拟环境目录。完成本周代码的第一次提交。
- 周二 2.5h：小模块 + 类型 + pytest≥5。写一个纯函数模块（去空白、按长度截断、统计词数），参数和返回值加上类型注解。pytest 至少 5 个用例，覆盖正常输入、空字符串和长度边界。
- 周三 2.5h：FastAPI /health + /items CRUD（内存）。`GET /health` 返回状态；`/items` 支持创建、列表、按 id 读取、更新和删除。数据放在进程内存里。
- 周四 2.5h：TestClient 集成测试 + routers/schemas/services 分层。路由、Pydantic 模型和业务函数分文件。用 TestClient 覆盖 `/health` 和 items 的增删改查，并包含一个 id 不存在时的失败用例。
- 周五 2h：Dockerfile / compose，容器 /health=200。写出 Dockerfile 与 Compose 文件。容器启动后请求 `/health` 得到状态码 200。把构建和启动命令写进 README。
- 周末 3h：scripts/llm_hello.py，密钥环境变量，打印 token 用量。脚本从环境变量 `OPENAI_API_KEY` 读取密钥；使用兼容网关时再读 `OPENAI_BASE_URL` 与 `OPENAI_MODEL`。发送一句短提示，打印回复，以及用量里的 prompt token 与 completion token。密钥只留在环境变量中。

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | Conda/venv 环境与仓库、README、.gitignore、首 commit。Conda 或 uv 均可，本仓库推荐 Conda 亦可。在 README 写明创建环境、安装依赖和启动命令。`.gitignore` 忽略 `.env`、`__pycache__` 和虚拟环境目录。完成本周代码的第一次提交。 |
| 周二 | 2.5h | 小模块 + 类型 + pytest≥5。写一个纯函数模块（去空白、按长度截断、统计词数），参数和返回值加上类型注解。pytest 至少 5 个用例，覆盖正常输入、空字符串和长度边界。 |
| 周三 | 2.5h | FastAPI /health + /items CRUD（内存）。`GET /health` 返回状态；`/items` 支持创建、列表、按 id 读取、更新和删除。数据放在进程内存里。 |
| 周四 | 2.5h | TestClient 集成测试 + routers/schemas/services 分层。路由、Pydantic 模型和业务函数分文件。用 TestClient 覆盖 `/health` 和 items 的增删改查，并包含一个 id 不存在时的失败用例。 |
| 周五 | 2h | Dockerfile / compose，容器 /health=200。写出 Dockerfile 与 Compose 文件。容器启动后请求 `/health` 得到状态码 200。把构建和启动命令写进 README。 |
| 周末 | 3h | scripts/llm_hello.py，密钥环境变量，打印 token 用量。脚本从环境变量 `OPENAI_API_KEY` 读取密钥；使用兼容网关时再读 `OPENAI_BASE_URL` 与 `OPENAI_MODEL`。发送一句短提示，打印回复，以及用量里的 prompt token 与 completion token。密钥只留在环境变量中。 |

## Checklist

- [ ] 环境 README
- [ ] pytest
- [ ] CRUD
- [ ] 分层测试
- [ ] Docker
- [ ] LLM hello

## 参考链接

- [Python 教程](https://docs.python.org/3/tutorial/)
- [venv](https://docs.python.org/3/library/venv.html)
- [Conda 环境](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
- [uv](https://docs.astral.sh/uv/)
- [pytest 入门](https://docs.pytest.org/en/stable/getting-started.html)
- [FastAPI 第一步](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI 测试](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI 大项目结构](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Docker 入门](https://docs.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/)
- [FastAPI 与 Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [OpenAI 快速开始](https://developers.openai.com/api/docs/quickstart)
- [Pro Git 中文](https://git-scm.com/book/zh/v2)
