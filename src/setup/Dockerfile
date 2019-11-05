ARG JAVA_VERSION=""
ARG SPARK_VERSION=""

FROM mpolatcan/polynote:base-spark-${SPARK_VERSION}-java${JAVA_VERSION}

MAINTAINER Mutlu Polatcan <mutlupolatcan@gmail.com>

ARG POLYNOTE_VERSION=""
ARG POLYNOTE_DOWNLOAD_LINK="https://github.com/polynote/polynote/releases/download/${POLYNOTE_VERSION}/polynote-dist.tar.gz"

RUN wget ${POLYNOTE_DOWNLOAD_LINK} && \
    tar -xvzf polynote-dist.tar.gz --strip-components 1 -C ${POLYNOTE_HOME} && \
    rm -r ${POLYNOTE_HOME}/notebooks/examples && \
    rm polynote-dist.tar.gz

ENTRYPOINT ["./polynote_entrypoint.sh"]
