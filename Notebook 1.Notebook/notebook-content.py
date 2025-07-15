# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8ef75fc9-38ee-4540-affd-be4111bb8fc7",
# META       "default_lakehouse_name": "pro_lh",
# META       "default_lakehouse_workspace_id": "1ab59e4e-fbe5-4a0c-af43-6101f6a68169",
# META       "known_lakehouses": [
# META         {
# META           "id": "8ef75fc9-38ee-4540-affd-be4111bb8fc7"
# META         },
# META         {
# META           "id": "3b2d71c8-46dc-417a-9e15-d135b2382b8b"
# META         },
# META         {
# META           "id": "dc9b54ff-79c2-4832-bdc9-2517c2a84531"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "df783f4e-70dc-435c-9343-bc9bd6b2d3d0",
# META       "workspaceId": "bfdbb2de-2821-4bed-9c9e-31d0875ac841"
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT * FROM pro_lh.dbo.dimension_city LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
