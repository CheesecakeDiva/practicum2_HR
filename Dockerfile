FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV WORK_DIR="/usr/src/app"
RUN mkdir -p ${WORK_DIR}
WORKDIR ${WORK_DIR}

RUN addgroup --system maintenance && \
    adduser --system --ingroup maintenance django_web && \
    chown -R django_web:maintenance ${WORK_DIR}

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . ${WORK_DIR}

RUN mkdir -p ${WORK_DIR}/static/
RUN chmod -R og+w ${WORK_DIR}/static/

USER django_web

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
