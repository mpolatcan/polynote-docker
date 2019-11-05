ARG JAVA_VERSION=""

FROM openjdk:${JAVA_VERSION}

MAINTAINER Mutlu Polatcan <mutlupolatcan@gmail.com>

ENV POLYNOTE_HOME "/polynote"
ENV PATH=${POLYNOTE_HOME}:$PATH \
	LISTEN_HOST="0.0.0.0" \
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
    chmod +x entrypoint.sh
