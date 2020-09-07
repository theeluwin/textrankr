# ubuntu
FROM theeluwin/ubuntu-konlpy:latest
LABEL maintainer="Jamie Seol <theeluwin@gmail.com>"

# init
RUN mkdir -p /workspace
WORKDIR /workspace

# install packages
RUN pip install -U pip
RUN pip install setuptools networkx nose nose-exclude flake8 coverage coveralls requests

# install this package
ADD . /workspace/
RUN python setup.py build && \
	python setup.py install

# run test
ENTRYPOINT []
CMD ["nosetests", "--config=.noserc"]
