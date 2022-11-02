from mrjob.job import MRJob, MRStep
import psycopg2


class AggregateProduct(MRJob):
    # def reducer_init(self):
    #     # make postgres availabel to mapper
    #     self.conn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port="1234")

    def mapper(self, _, line):
        item = line.strip().split(',')
        month = item[1][-7:]
        yield month, int(item[4])

    def combiner(self, key, values):
        year = key[-4:]
        yield year, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

    # def store(self, key, values):
    #     self.cur = self.conn.cursor()
    #     self.cur.execute('insert into total_order_yearly (year, total_order) values(%s,%s)', (key, values))

    # def steps(self):
    #     return [
    #         MRStep(mapper=self.mapper,
    #                combiner=self.combiner,
    #                reducer=self.reducer),
    #         MRStep(reducer_init=self.reducer_init,
    #                reducer=self.store,
    #                reducer_final=self.reducer_final)
    #     ]

    # def reducer_final(self):
    #     self.conn.commit()
    #     self.conn.close()


if __name__ == '__main__':
    AggregateProduct.run()