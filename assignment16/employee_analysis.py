from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EmployeeRDDAnalysis") \
    .getOrCreate()

sc = spark.sparkContext

# Read CSV as RDD
rdd = sc.textFile("employee_data.csv")

header = rdd.first()

data = rdd.filter(lambda x: x != header)

employees = data.map(lambda x: x.split(","))

# -------------------------------------------------
# 1. Sort employees by salary descending
# -------------------------------------------------

sorted_employees = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")

for emp in sorted_employees.collect():
    print(emp)

# -------------------------------------------------
# 2. Department wise total salary
# -------------------------------------------------

dept_salary = employees.map(
    lambda x: (x[2], int(x[3]))
)

dept_totals = dept_salary.reduceByKey(
    lambda a, b: a + b
)

print("\n===== Department Salary Totals =====")

for dept in dept_totals.collect():
    print(dept)

# -------------------------------------------------
# 3. Top 3 Highest Paid Employees
# -------------------------------------------------

top3 = sorted_employees.take(3)

output = []

for emp in top3:
    output.append(",".join(emp))

with open("top_3_employees.txt", "w") as f:
    for row in output:
        f.write(row + "\n")

print("\nTop 3 employees saved to file.")

spark.stop()