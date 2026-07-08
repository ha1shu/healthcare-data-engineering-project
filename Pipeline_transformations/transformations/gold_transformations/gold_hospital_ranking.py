from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.window import Window

@dp.table(
    name="gold_hospital_ranking"
)
def hospital_ranking():

    df = spark.read.table("silver_patients_records")

    result = (
        df.groupBy("hospital")
          .agg(
              count("*").alias("total_patients"),
              round(sum("billing_amount"),2).alias("total_revenue")
          )
    )

    window = Window.orderBy(desc("total_revenue"))

    return result.withColumn(
        "rank",
        dense_rank().over(window)
    )