from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from web_ingest.config.ConfigStore import *
from web_ingest.udfs.UDFs import *

def index_urls(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("xml")\
        .option("rowTag", "url")\
        .schema(
          StructType([
            StructField("changefreq", StringType(), True), StructField("loc", StringType(), True), StructField("priority", DoubleType(), True)
        ])
        )\
        .load("dbfs:/dais_gen_ai/web/bronze/sitemap/")
