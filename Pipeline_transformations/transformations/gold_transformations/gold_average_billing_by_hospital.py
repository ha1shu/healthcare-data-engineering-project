from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
    name="gold_average_billing_by_hospital"
)
def average_billing_by_hospital():

    df = spark.read.table("silver_patients_records")

    return (
        df.groupBy("hospital")
          .agg(
              round(avg("billing_amount"),2).alias("average_billing"),
              round(sum("billing_amount"),2).alias("total_revenue")
          )
    )