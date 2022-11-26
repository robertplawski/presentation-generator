from typing import Optional, List
from pathlib import Path
import wikipediaapi

class Generator:
    def __init__(self, topics: List[str], lang: str = "pl", path: Path=Path("output.txt")):
        self.lang = lang
        self.path = path

        self.wikipedia = wikipediaapi.Wikipedia(language=lang)
        print(topics)
        self.pages = self.parse_raw_topics(topics)
        self.output = self.generate_content(self.pages)

        self.save()

    def parse_raw_topics(self, topics):
        result = []
        for topic in topics:
            topic = topic.split("#")
            print(topic)
            page = self.wikipedia.page(topic[0])
            subsection = page.section_by_title(topic[1])
            if page.exists():
                print([i.title for i in page.sections])
                result.append(page)
            else:
                pass # implement exception

        return result

    def generate_content(self, pages):
        result = []
        for page in pages:
            result.append(page.text)
        return result

    def save(self):
        with open(self.path, "w+") as f:
            f.write("")
        with open(self.path, "a+") as f:
            for item in self.output:
                f.write(item)
