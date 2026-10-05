from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .master("local[*]") \
    .getOrCreate()

dados = [
    ("Notebook", "Eletrônicos", 3600,00),
    ("Smartphone", "Eletrônicos", 3000,00),
    ("Tablet", "Eletrônicos", 300,00),
    ("Notebook", "Eletrônicos", 100,00),
    ("Smartphone", "Eletrônicos", 250,00),
    ("Mesa de Escritório", "Móveis", 500,00),
    ("Cadeira de Escritório", "Móveis", 350,00)
]

motor = spark.createDataFrame(dados, ["Produto", "Categoria", "Preço"])

filtrado = motor.filter(motor["Preço"] > 500)
resultado = filtrado.groupBy("Categoria").count()

resultado.show()

spark.stop()