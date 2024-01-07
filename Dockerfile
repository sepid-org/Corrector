# pull official base image
FROM python:3.9

# set work directory
WORKDIR /app

RUN pip install --upgrade pip

# copy requirements
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN adduser sepid

RUN mkdir -p /app/logging && chown -R sepid /app/logging \
	&& mkdir -p /app/media && chown -R sepid /app/media

RUN chown -R sepid /usr/src/app/

USER sepid

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]