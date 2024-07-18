FROM nvidia/cuda:11.3.0-base-ubuntu20.04 AS base_gpu

ENV DEBIAN_FRONTEND=noninteractive

# PYTHON STACK
ENV PYTHON_VERSION=3.8
ENV PYTHON_MINOR_VERSION=6

ADD package_requirements.txt package_requirements.txt
# Added python sources cleanup after installation for smaller image
RUN apt-get -qq update -y && \
    xargs -a package_requirements.txt apt-get -qq install -y && \
	apt-get -qq clean && \
	rm -rf /var/lib/apt/lists/* && \
    curl --silent https://www.python.org/ftp/python/${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}.tgz | tar -xzf - -C /opt && \
    cd /opt/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION} && \
    ./configure --enable-optimizations && \
    make altinstall && \
	curl --silent https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python${PYTHON_VERSION} get-pip.py && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python${PYTHON_VERSION} 1 && \
    rm -rf ~/.cache && \
    rm -rf /opt/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}

WORKDIR /opt/project/
ADD ../requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf ~/.cache
ADD ../my_project /opt/project

#####

FROM ubuntu:20.04 AS base_no_gpu

ENV DEBIAN_FRONTEND=noninteractive

# PYTHON STACK
ENV PYTHON_VERSION=3.8
ENV PYTHON_MINOR_VERSION=6

ADD ../package_requirements.txt package_requirements.txt
# Added python sources cleanup after installation for smaller image
RUN apt-get -qq update -y && \
    xargs -a package_requirements.txt apt-get -qq install -y && \
	apt-get -qq clean && \
	rm -rf /var/lib/apt/lists/* && \
    curl --silent https://www.python.org/ftp/python/${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}.tgz | tar -xzf - -C /opt && \
    cd /opt/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION} && \
    ./configure --enable-optimizations && \
    make altinstall && \
	curl --silent https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python${PYTHON_VERSION} get-pip.py && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python${PYTHON_VERSION} 1 && \
    rm -rf ~/.cache && \
    rm -rf /opt/Python-${PYTHON_VERSION}.${PYTHON_MINOR_VERSION}

WORKDIR /opt/project/
ADD ../requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf ~/.cache
ADD ../my_project /opt/project

ENTRYPOINT ["/usr/bin/env"]

##### examples
FROM base_no_gpu AS data_collection
CMD ["python", "cli.py", "data-collection"]

FROM base_no_gpu AS tensorboard_metrics
RUN mkdir -p /opt/tensorboard
CMD ["python", "cli.py", "monitoring", "--min-nb-feedback", "50", "--logdir", "/opt/tensorboard"]

FROM base_no_gpu AS unit_tests
CMD ["python", "-m", "pytest", "-vv", "--junitxml=reports/result.xml", "tests/"]

FROM base_gpu AS integration_tests_gpu
CMD ["python", "-m", "pytest", "-vv", "--junitxml=reports/result.xml", "tests/"]
