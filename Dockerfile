FROM python:3-alpine3.15

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 5153

# Run the application.
CMD ["python", "app.py"]
