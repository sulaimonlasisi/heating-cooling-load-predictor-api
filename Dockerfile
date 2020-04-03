FROM python:3.8-slim AS python
WORKDIR /app
COPY app.py linear_reg.joblib requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
