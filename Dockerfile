FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

COPY ./app/ui.py ./ui.py
COPY ./conn_attack.csv ./conn_attack.csv

RUN pip3 install streamlit
RUN pip3 install pandas
RUN pip3 install -U scikit-learn

CMD ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker build -t python .
# docker run -p 8501:8501 python
