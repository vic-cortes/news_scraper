# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsscraperPipeline:
    def process_item(self, item, spider):
        return item


class BookScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip all blank spaces
        field_names = adapter.field_names()

        for field_name in field_names:
            value = adapter.get(field_name)

            if field_name in ["description"]:
                continue

            if isinstance(value, dict):
                continue

            adapter[field_name] = value.strip()

        # Category lowercase
        lowercase_key = ["category"]

        for key in lowercase_key:
            value = adapter.get(key)

            if not value:
                continue
            adapter[key] = value.lower()

        price_key = ["price"]

        for key in price_key:
            value = adapter.get(key)
            value = value.replace("£", "")
            adapter[key] = float(value)

        return item
