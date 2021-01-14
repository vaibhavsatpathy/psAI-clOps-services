FROM amazonlinux:2
RUN yum update -y && yum upgrade -y 
RUN yum install -y gcc \
    make \
    unzip \
    xz-devel \
    poppler-utils \
    openssl-devel \
    bzip2-devel \
    libffi-devel \
    wget \
    tar 
COPY . /app
WORKDIR /app
ENV PYTHON_VERSION 3.8.6
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
    && tar xzf Python-${PYTHON_VERSION}.tgz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure --enable-optimizations \
    && make altinstall \
    && rm -f /Python-${PYTHON_VERSION}.tgz
RUN pip3.8 install -U pip \
    && pip3.8 install wheel
RUN pip3.8 install -r requirements.txt
ENV work_dir=/app/temp
EXPOSE 8080
RUN chmod 777 docker_entrypoint.sh
ENTRYPOINT [ "/bin/bash" ]
CMD [ "docker_entrypoint.sh" ]