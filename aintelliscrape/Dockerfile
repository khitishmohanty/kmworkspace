FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT [ "python3" ]
CMD ["app.py"]