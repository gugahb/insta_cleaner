FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    && apt-get clean

# Cria e define diretório de trabalho
WORKDIR /app
COPY app/ /app

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps
RUN apt-get install -y xvfb

CMD ["xvfb-run", "--auto-servernum", "python", "main.py"]
