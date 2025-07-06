# Use Python 3.10 slim as the base image
FROM  crpi-8vadjonh2nyqyvih.cn-shanghai.personal.cr.aliyuncs.com/cityark/python:3.12-slim

# 配置国内 pip 源
RUN mkdir -p ~/.pip \
    && echo '[global]' >> ~/.pip/pip.conf \
    && echo 'index-url = https://mirrors.aliyun.com/pypi/simple/' >> ~/.pip/pip.conf

# 安装 poetry
RUN pip install poetry==1.8.0

# 复制 poetry 配置文件
COPY pyproject.toml poetry.lock* ./

# 安装依赖（不创建虚拟环境，且不安装项目本身）
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# 复制项目全部代码
COPY . .

WORKDIR /app

# Expose port 8000
EXPOSE 8000

# # Command to run the application
# CMD ["chroma", "run", "--host", "0.0.0.0", "--path", "/chroma/data"]
CMD ["python", "src/hello_world/main.py"]