1. create docker postgres
2. create docker hadoop
3. ingest data to postgres
4. copy data to hdfs
5. mapreduce

python job
1. ingest detail data to postgresql
2. do same transformation as mrjob

mrjob
1. filter product then stored into postgres and hdfs
2. aggregate quantity transaction based on date
3. aggregate quantity transaction based on date and product