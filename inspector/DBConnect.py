import pymysql
import json

with open('inspector/conf.json') as file:
    config = json.load(file)


class DBConnect:
    def __init__(self, sample_id):
        self.conn = pymysql.connect(host=config['host'], port=config['port'], user=config['user'], password=config['password'],
                                    database=config['database'], charset=config['charset'])
        self.sample_id = sample_id

    def get_sample_type(self):
        try:
            with self.conn.cursor() as curs:
                sql_form = "select source_type from tbl_yfilemetadata where id ={}"
                sql = sql_form.format(self.sample_id)
                curs.execute(sql)
                sample_type = curs.fetchone()
                return sample_type[0]
        finally:
            pass

    def get_annotations_data(self):
        try:
            with self.conn.cursor() as curs:
                sql_form = "SELECT * FROM tbl_annotations_data where sample_id={} order by offset_start,offset_end desc,aType,aSeq"
                sql = sql_form.format(self.sample_id)
                curs.execute(sql)
                annotations_data = curs.fetchall()
                return annotations_data
        finally:
            self.conn.close()
