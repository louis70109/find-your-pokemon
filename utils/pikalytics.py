import logging
from utils import sqlite
from typing import List, Dict, Union, Any

logger = logging.getLogger(__file__)


class Pikalytics:
    _ALL_STATUS: List[str] = ['招式', '隊友', '物品', '特性', '努力值']
    _MAPPING: Dict[int, Union[str, None]] = {
        1: 't_move',
        2: None,
        3: 't_item',
        4: 't_ability',
        5: 't_nature'
    }

    def __init__(self, index: int = 1, url: str = 'https://google.com', **kwargs: Dict[str, str]) -> None:
        self.table: Union[str, None] = self._MAPPING.get(index)
        self._template: Dict[str, Union[str, List[Dict[str, str]]]] = {
            'name': self._ALL_STATUS[index-1],
            'abilities': [],
            'url': url
        }
        logger.debug('搜尋 Pikalytic 各中文技能...')

    def poke_mapping(self, items: List[List[str]]) -> None:
        with sqlite.connect() as con:
            for it in items:
                if self.table is not None:
                    item_query: Dict[str, str] = sqlite.exec_one(
                        con,
                        f"SELECT * FROM '{self.table}' WHERE name_en == '{it[0]}'"
                    )
                    it[0] = item_query['name_zh']
                if self._template['name'] == '招式':
                    it[1] = item_query['category']
            logger.info(f"{self._template['name']} query result: {items}")
            self._template['abilities'] = items

    @property
    def template(self) -> Dict[str, Any]:
        return self._template