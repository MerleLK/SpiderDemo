import mysql.connector as connector
from SpiderDemo import settings

"""
DROP TABLE IF EXISTS `dd_name`;
CREATE TABLE `dd_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `xs_name` varchar(255) DEFAULT NULL,
  `xs_author` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `name_id` varchar(255) DEFAULT NULL,
  `novel_url` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
"""
conn = connector.connect(user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD, host=settings.MYSQL_HOST,
                         database=settings.MYSQL_DB)
cur = conn.cursor()


class Sql:
    @classmethod
    def insert_data(cls, xs_name, xs_author, category, name_id, novel_url):
        sql = "INSERT INTO dd_name (xs_name, xs_author, category, name_id, novel_url) VALUES (%s,%s,%s,%s,%s)"

        value = (xs_name, xs_author, category, name_id, novel_url)
        cur.execute(sql, value)
        conn.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
