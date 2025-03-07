from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from chatbot_live.config.ConfigStore import *
from chatbot_live.udfs.UDFs import *

def explode_matches(spark: SparkSession, PineconeLookup_1: DataFrame) -> DataFrame:
    flt_col = PineconeLookup_1.withColumn("pinecone_matches", explode_outer("pinecone_matches")).columns
    selectCols = [col("pinecone_matches") if "pinecone_matches" in flt_col else col("pinecone_matches"),                   col("input") if "input" in flt_col else col("text").alias("input"),                   col("channel") if "channel" in flt_col else col("channel"),                   col("ts") if "ts" in flt_col else col("ts"),                   col("created_at") if "created_at" in flt_col else col("created_at")]

    return PineconeLookup_1.withColumn("pinecone_matches", explode_outer("pinecone_matches")).select(*selectCols)
