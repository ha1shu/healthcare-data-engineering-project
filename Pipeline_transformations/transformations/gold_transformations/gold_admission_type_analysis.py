from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
    name="gold_admission_type_analysis"
)
def admission_type_analysis():

    df = spark.read.table("silver_patients_records")

    return (
        df.groupBy("admission_type")
          .agg(
              count("*").alias("total_admissions"),
              round(avg("billing_amount"),2).alias("average_bill")
          )
    )