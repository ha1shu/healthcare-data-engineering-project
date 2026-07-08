from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import pipelines as dp



@dp.table(
    name="silver_patients_records",
    comment="Cleaned healthcare patient records"
)
def silver_patients_records():

    df = spark.read.table("healthcare.bronze.patients_records")

    df = df.dropDuplicates()
    df = df.dropna(subset=[
        "name",
        "age",
        "gender",
        "medical_condition",
        "date_of_admission"
    ])

    # Remove trailing spaces
    string_cols = [
        "name",
        "gender",
        "blood_type",
        "medical_condition",
        "doctor",
        "hospital",
        "insurance_provider",
        "admission_type",
        "medication",
        "test_results"
    ]

    for c in string_cols:
        df = df.withColumn(c, trim(col(c)))

    # Standardize text
    df = (
        df
        .withColumn("name", initcap(col("name")))
        .withColumn("gender", initcap(col("gender")))
        .withColumn("doctor", initcap(col("doctor")))
        .withColumn("hospital", initcap(col("hospital")))
        .withColumn("insurance_provider", initcap(col("insurance_provider")))
        .withColumn("medical_condition", initcap(col("medical_condition")))
        .withColumn("admission_type", initcap(col("admission_type")))
        .withColumn("medication", initcap(col("medication")))
        .withColumn("test_results", initcap(col("test_results")))
    )

    # Convert dates
    df = (
        df
        .withColumn("date_of_admission", to_date("date_of_admission", "yyyy-MM-dd"))
        .withColumn("discharge_date", to_date("discharge_date", "yyyy-MM-dd"))
    )

    # Remove invalid age
    df = df.filter((col("age") >= 0) & (col("age") <= 120))

    # Remove negative billing amounts
    df = df.filter(col("billing_amount") >= 0)

    # Add audit columns
    df = (
        df
        .withColumn("created_timestamp", current_timestamp())
        .withColumn("updated_timestamp", current_timestamp())
    )

    return df