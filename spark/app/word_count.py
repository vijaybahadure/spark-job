# spark/app/word_count.py

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Load data
text_file = spark.read.text("/data/sample.txt")

# Split words and count occurrences
word_counts = text_file.rdd.flatMap(lambda line: line.value.split()) \
                           .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda a, b: a + b)

# Collect the results
results = word_counts.collect()

# Print the word counts
for word, count in results:
    print(f"{word}: {count}")

# Stop Spark Session
spark.stop()
