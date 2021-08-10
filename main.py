import justpy as jp
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary

from webapp.page import Page
import inspect

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

imports = list(globals().values())
# imports = globals()



for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)

jp.justpy()