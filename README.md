# LetsLearningAgent

本仓库记录 Agent 开发工程师一年学习计划（2026-11 至 2027-10，每周约 15 小时）。

## 学习计划

- 一年总任务：[LEARNING.md](LEARNING.md)
- 周计划索引：[plan/README.md](plan/README.md)
- 每周文件：`plan/week-01.md` 至 `plan/week-48.md`

先读 [LEARNING.md](LEARNING.md)，确认阶段、知识地图和作品集，再从 [plan/README.md](plan/README.md) 进入当周。

## 第 1 周代码

周二的文本函数和周三的 FastAPI 在 `code/week01/`。本地开发使用 Conda 环境 `LearningAgent`（Python 3.12）。`requirements.txt` 列出 pip 依赖；`environment.yml` 使用同一组版本范围，并固定 Python 3.12。Docker 按这份环境文件创建同名环境。

### Conda 本地开发

已有环境时：

```bash
conda activate LearningAgent
cd code/week01
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

新建环境时，在 `code/week01` 执行：

```bash
conda env create -f environment.yml
conda activate LearningAgent
```

启动后访问 `http://127.0.0.1:8000/health`，交互文档在 `http://127.0.0.1:8000/docs`。条目数据只存在于进程内存中，重启后清空。

### Docker

镜像基于 Miniconda。容器内 uvicorn 监听 `0.0.0.0:8000`，Compose 把该端口映射到宿主机 `8000`。构建上下文排除 `.env`，密钥留在本机环境变量中。

```bash
cd code/week01
docker compose build
docker compose up -d
curl -sS -D - http://127.0.0.1:8000/health
docker compose down
```

验收：`/health` 状态码为 200，响应体为 `{"status":"ok"}`。`docker compose down` 停止并移除这次启动的容器。启动前让宿主机 8000 端口空闲。
