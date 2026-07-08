from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
    name="gold_patient_count_by_hospital"
)
def gold_patient_count_by_hospital():

    df = spark.read.table("silver_patients_records")

    return (
        df.groupBy("hospital")
          .agg(count("*").alias("total_patients"))
          .orderBy(desc("total_patients"))
    )