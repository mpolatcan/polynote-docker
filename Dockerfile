ARG JAVA_VERSION=""

FROM openjdk:${JAVA_VERSION}

MAINTAINER Mutlu Polatcan <mutlupolatcan@gmail.com>

ARG POLYNOTE_VERSION=""
ARG POLYNOTE_DOWNLOAD_LINK="https://github.com/polynote/polynote/releases/download/${POLYNOTE_VERSION}/polynote-dist.tar.gz"

ENV POLYNOTE_HOME "/polynote"
ENV PATH=${POLYNOTE_HOME}:$PATH
ENV LISTEN_HOST="0.0.0.0" \
    LISTEN_PORT="8192" \
    STORAGE_DIR="notebooks" \
    STORAGE_CACHE="tmp" \
    BEHAVIOR_DEPENDENCY_ISOLATION="false" \
    BEHAVIOR_KERNEL_ISOLATION="always" \
    UI_BASE_URI="/"

ADD config_template.yml config_loader.py entrypoint.sh ./

RUN apt-get update && \
    apt-get -y install python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install setuptools pyyaml jep jedi virtualenv matplotlib && \
    mkdir -p ${POLYNOTE_HOME} && \
    wget ${POLYNOTE_DOWNLOAD_LINK} && \
    tar -xvzf polynote-dist.tar.gz --strip-components 1 -C ${POLYNOTE_HOME} && \
    rm -r ${POLYNOTE_HOME}/notebooks/examples && \
    rm polynote-dist.tar.gz && \
    chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]