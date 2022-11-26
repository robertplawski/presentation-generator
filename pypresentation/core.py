from typing import Optional, List
from pathlib import Path
from itertools import chain
import wikipediaapi
import pptx

# Big thanks, I couldn't figure it out myself
# https://stackoverflow.com/a/12472564

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

class Generator:
    def __init__(self, topics: List[str], lang: str = "pl", author:str = "Author", title:str = "Title", path: Path=Path("output.pptx")):
        self.lang = lang
        self.path = path
        self.title = title
        self.author = author
        self.contents = []
        
        self.wikipedia = wikipediaapi.Wikipedia(language=lang,extract_format=wikipediaapi.ExtractFormat.WIKI) # Create wikipedia class
        self.pages = self.parse_raw_topics(topics) # Parse topics
        self.presentation = pptx.Presentation() # Create presentation class

        self.generate_content(self.pages, self.presentation) # Generate content
        self.save_content() # Save content

    def parse_raw_topics(self, topics):
        result = []
        for topic in topics: 
            if "#" in topic: 
                topic = topic.split("#")
                page = self.wikipedia.page(topic[0])
                section = page.section_by_title(topic[1])
                if page.exists():
                    result.append(section)
                    if section == None:
                        raise Exception("Couldn't find a section")
                    self.contents.append(topic[1])
                else:
                    raise Exception("Couldn't find a page")
            else:
                page = self.wikipedia.page(topic)
                if page.exists():
                    titles = self.recursively_find_sections(page.sections)
                    titles = flatten(titles)
                    for title in titles:
                        result.append(page.section_by_title(title))
                        self.contents.append(title)
                else:
                    raise Exception("Couldn't find a page")

        return result
    def recursively_find_sections(self, sections):
        result=[]
        for s in sections:
            result.append(s.title)
            rec = self.recursively_find_sections(s.sections)
            if rec != []:
                result.append(rec)
        return result

    def generate_content(self, pages, prs):
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        slide.placeholders[0].text = self.title
        slide.placeholders[1].text = self.author
    
        contentslide= prs.slides.add_slide(prs.slide_layouts[1])
        contentslide.placeholders[0].text = "Spis treści"
        contentslide.placeholders[1].text = "\n".join(self.contents)

        for page in pages:
            slide = prs.slides.add_slide(prs.slide_layouts[1])
            slide.shapes.title.text = page.title
            slide.placeholders[1].text = page.text

    def save_content(self):
        self.presentation.save(self.path)
