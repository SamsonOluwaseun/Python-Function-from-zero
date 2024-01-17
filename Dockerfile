FROM public.ecr.aws/lambda/python:3.8 

RUN mkdir -p /app
RUN apt-get update && apt-get install -y openssl libssl-dev
COPY ./main.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]