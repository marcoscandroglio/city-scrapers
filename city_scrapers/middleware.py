
from city_scrapers_core.items import Meeting
from scrapy_wayback_middleware import WaybackMiddleware
import secrets


class CityScrapersWaybackMiddleware(WaybackMiddleware):
    def get_item_urls(self, item):
        MAX_LINKS = 3
        if isinstance(item, Meeting):
            links = []
            if "legistar" in item["source"] and "Calendar.aspx" not in item["source"]:
                links = [item["source"]]
            links.extend(
                secrets.SystemRandom().sample([link.get("href") for link in item.get("links", [])], MAX_LINKS
                )
            )
            return links
        if isinstance(item, dict):
            return secrets.SystemRandom().sample([doc.get("url") for doc in item.get("documents", [])], MAX_LINKS
            )
        return []
