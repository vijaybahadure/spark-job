# spark/Dockerfile

# Base image
FROM openjdk:11-jre-slim

# Set environment variables
ENV SPARK_VERSION=3.3.0
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark

# Install dependencies
RUN apt-get update && apt-get install -y curl && \
    curl -o /tmp/spark.tgz \
    "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" && \
    tar -xvf /tmp/spark.tgz -C /opt/ && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /opt/spark && \
    rm /tmp/spark.tgz

# Set environment variables
ENV PATH="$SPARK_HOME/bin:$PATH"

# Install PySpark dependencies
RUN apt-get install -y python3-pip && pip3 install pyspark

# Copy application code
COPY app /opt/spark/app

# Set the working directory
WORKDIR /opt/spark/app

# Command to run when starting the container
CMD ["spark-submit", "word_count.py"]
