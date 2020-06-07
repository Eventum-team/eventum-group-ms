FROM python:3.6

EXPOSE 5000

WORKDIR /eventum-group-ms

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=resources

# RUN pip install -e .

CMD gunicorn -b 0.0.0.0:5000 resources:app