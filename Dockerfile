#use base image offical from python
FROM python:3.9

#set directory for the application
WORKDIR /app

#system package installation and remove package list to save disk space
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

#copy the requirements file
COPY requirements.txt ./

#install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

#copy the application code
COPY . .

#expose the required port
EXPOSE 8000

#start the flask application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "4"]

