ARG JAVA_VERSION=""

FROM openjdk:${JAVA_VERSION}

MAINTAINER Mutlu Polatcan <mutlupolatcan@gmail.com>

ARG SPARK_VERSION=""
ARG SPARK_HADOOP_VERSION=""
ARG SPARK_DOWNLOAD_LINK="http://www-eu.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz"

ENV POLYNOTE_HOME "/polynote"
ENV SPARK_HOME "${POLYNOTE_HOME}/spark"
ENV PATH=$PATH:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${POLYNOTE_HOME} \
	LISTEN_HOST="0.0.0.0" \
	LISTEN_PORT="8192" \
	STORAGE_DIR="notebooks" \
	STORAGE_CACHE="tmp" \
	BEHAVIOR_DEPENDENCY_ISOLATION="false" \
	BEHAVIOR_KERNEL_ISOLATION="always" \
	UI_BASE_URI="/"

ADD config_template.yml /polynote_config_template.yml
ADD config_loader.py /polynote_config_loader.py
ADD entrypoint.sh /polynote_entrypoint.sh

WORKDIR ${POLYNOTE_HOME}

RUN apt-get update && \
    apt-get -y install python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install setuptools pyyaml jep jedi virtualenv matplotlib && \
    mkdir -p ${POLYNOTE_HOME} ${SPARK_HOME} && \
    wget ${SPARK_DOWNLOAD_LINK} && \
    tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz -C ${POLYNOTE_HOME} && \
    rm spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz && \
    mv ${POLYNOTE_HOME}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}/* ${SPARK_HOME} && \
    rm -r ${POLYNOTE_HOME}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION} && \
    chmod +x polynote_entrypoint.sh
