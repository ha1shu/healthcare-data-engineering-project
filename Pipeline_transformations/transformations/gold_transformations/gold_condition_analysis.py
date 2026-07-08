from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
    name="gold_condition_analysis"
)
def condition_analysis():

    df = spark.read.table("silver_patients_records")

    return (
        df.groupBy("medical_condition")
          .agg(
              count("*").alias("patient_count"),
              round(avg("billing_amount"),2).alias("average_bill")
          )
          .orderBy(desc("patient_count"))
    )