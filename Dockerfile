FROM alpine:3

RUN apk --no-cache add --update \
  bash \
  curl \
  graphviz \
  python3 \
  py3-pip \
  msttcorefonts-installer \
  fontconfig && \
  update-ms-fonts && \
  fc-cache -f

RUN curl -fsSL https://clis.cloud.ibm.com/install/linux > /tmp/bxinstall.sh && \
  sh /tmp/bxinstall.sh && \
  rm /tmp/bxinstall.sh

ADD . /app
RUN cd /app && pip3 install -r requirements.txt

ENV PATH="/app:${PATH}"

VOLUME [ "/home" ]
WORKDIR "/home"