ARG BASE_URL

FROM ${BASE_URL}/library/pytorch:2.1.0-py3.10-cuda11.8.0 AS builder
 
WORKDIR /workspace
RUN python -m venv --system-site-packages /workspace/venv
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt


FROM ${BASE_URL}/library/pytorch:2.1.0-py3.10-cuda11.8.0 as v1

COPY --from=builder /workspace/ /workspace

WORKDIR /workspace

COPY sdxl-base  /workspace

COPY src/ /workspace/src

ENV PYTHONPATH /workspace/src

CMD ["/workspace/venv/bin/python", "-u", "/workspace/src/main.py"]
