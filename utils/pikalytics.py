import logging
from utils import sqlite


logger = logging.getLogger(__file__)


class Pikalytics():

    def __init__(self, index=1, url='https://google.com', **kwarg):
        _all_status = ['招式', '隊友', '物品', '特性', '努力值']
        self._mapping = {
            1: 't_move', 2: None,
            3: 't_item', 4: 't_ability', 5: 't_nature'}
        self.table = self._mapping[index]
        self._template = {
            'name': _all_status[index-1], # Cause index start from 1.
            'abilities': [],
            'url': url
        }
        logger.debug(f'搜尋 Pikalytic 各中文技能...')

    def poke_mapping(self, items):
        with sqlite.connect() as con:
            for it in items:
                if self.table is not None:
                    item_query = sqlite.exec_one(
                        con,
                        f"SELECT * FROM '{self.table}' WHERE name_en == '{it[0]}'")
                    it[0] = item_query['name_zh']
                if self._template['name'] == '招式':
                    it[1] = item_query['category']
            logger.info(self._template['name'] +
                        ' query result: ' + str(items))
            self._template['abilities'] = items

    @property
    def template(self):
        return self._template
