FROM python:3.11-slim

RUN pip install --upgrade pip
RUN pip install pandas numpy
RUN pip install matplotlib seaborn
RUN pip install scikit-learn scipy requests

WORKDIR /app/pipeline/

COPY *.py *.sh *.csv /app/pipeline/

RUN chmod +x /app/pipeline/summary.sh

CMD ["/bin/bash"]