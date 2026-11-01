# 第 37 周 · 用 Compose 按部署方式本地运行

- **日期**：2027-07-12～2027-07-18
- **阶段**：3 · 生产化与求职
- **知识层级**：L5
- **投入**：约 15 小时（作品约 9 小时，求职约 6 小时）

## 本周目标

一条 compose 命令拉起 API，健康检查通过，密钥不写进仓库。

## 完成标准

- Compose 文件定义 API 服务、端口和 healthcheck。
- 容器通过环境变量读取 `OPENAI_API_KEY`、`OPENAI_BASE_URL`、`OPENAI_MODEL`，文件中只有变量名。
- README 写明本地 Conda 或 uv 开发，以及 Compose 运行。
- 一页岗位差距笔记：对照 L0–L5，标出你已经能展示的三件作品。

## 任务拆分（约 15 小时）

| 时段 | 时长 | 任务 |
|------|------|------|
| 周一 | 2.5h | 【作品】整理生产形态的启动命令：工作目录、端口、数据库文件位置。写进部署笔记。 |
| 周二 | 2.5h | 【作品】更新 Compose：健康检查请求 `/health`，失败时能在 `docker compose ps` 里看出来。 |
| 周三 | 2.5h | 【作品】用环境变量文件的示例只保留变量名。确认 `.env` 未被 git 跟踪。 |
| 周四 | 2.5h | 【作品 1.5h】按 README 从零启动 Compose，记录 `/health` 的状态码。【求职 1h】列出目标岗位「Agent 开发工程师」的技能词，对照 L0–L5 打勾。 |
| 周五 | 2h | 【求职】把已能展示的 P1–P4 各用一句话写进 `notes/role-fit.md`，每句包含一个你测过的数字或现象。 |
| 周末 | 3h | 【求职】补全差距笔记：还不能展示的两项（例如评测进 CI、成本数字），对应到后面哪一周。 |

## Checklist

- [ ] Compose 健康检查通过
- [ ] 示例文件只有变量名
- [ ] README 区分开发和运行
- [ ] 岗位对照表已写
- [ ] 差距对应到后续周次

## 参考链接

- [Docker Compose](https://docs.docker.com/compose/)
- [Compose 服务](https://docs.docker.com/reference/compose-file/services/)
- [十二要素：配置](https://12factor.net/config)
- [FastAPI Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [Conda 环境](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
- [uv](https://docs.astral.sh/uv/)
