# ubuntu
FROM theeluwin/ubuntu-konlpy:latest
LABEL maintainer="Jamie Seol <theeluwin@gmail.com>"

# init
RUN mkdir -p /workspace
WORKDIR /workspace

# install packages
RUN pip3 install setuptools networkx nose nose-exclude flake8 coverage

# run
ADD . /workspace/
RUN python setup.py build && \
	python setup.py install
ENTRYPOINT []
CMD ["nosetests", "--config=.noserc"]
