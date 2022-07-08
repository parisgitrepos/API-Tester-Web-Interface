FROM python:3
WORKDIR /docker_files
COPY requirements.txt requirements.txt
RUN pip3 -r install requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]