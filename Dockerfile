FROM python
COPY . /test
WORKDIR /test
RUN pip install nltk
CMD python python_script.py