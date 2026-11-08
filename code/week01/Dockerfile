FROM continuumio/miniconda3:26.7.1-1

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CONDA_PLUGINS_AUTO_ACCEPT_TOS=yes \
    PATH="/opt/conda/envs/LearningAgent/bin:${PATH}"

WORKDIR /app

COPY environment.yml /tmp/environment.yml
RUN conda config --set channel_priority strict \
    && conda config --remove channels defaults \
    && conda config --add channels conda-forge \
    && conda env create -f /tmp/environment.yml \
    && conda clean -afy \
    && rm -f /tmp/environment.yml \
    && useradd --create-home --uid 1000 app \
    && chown -R app:app /app

COPY --chown=app:app app ./app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
