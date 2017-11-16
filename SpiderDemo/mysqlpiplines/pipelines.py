from .sql import Sql
from SpiderDemo.items import SpiderdemoItem


class SpiderDemoPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, SpiderdemoItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print("exists name_id!")
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                novel_url = item['novel_url']
                Sql.insert_data(xs_name, xs_author, category, name_id, novel_url)
                print('beginning save the novel name.......')
