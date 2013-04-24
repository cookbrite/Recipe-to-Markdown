rescrape
========

Rescrape is a Python tool for scraping online recipes into [Markdown](http://daringfireball.net/projects/markdown/).
Becaue the files are Markdown, they can be opened in any text editor or word processor, easily emailed, and easily modified.
Because Markdown is simple a text file, you'll be able to open your recipes as easily 50 years from now as you can today.

Rescrape provides an abstract scraping class that can be implemented for any website. So far, I implemented scrapers for

    * [AllRecipes.com](http://www.allrecipes.com)
    * [Food.com](http://www.food.com)
    * [The Pioneer Woman](http://www.thepioneerwoman.com)

The abstract class is called RecipeScraper and is in site/AbstractScraper.py.

A site scraper is easily created:

```python
import rescrape
s = rescrape.site.AllRecipesCom("http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx")
```

To print the recipe in Markdown form to standard out, just called:

```python
s.write()
```

You can also use the write function to create a text file:

```python
s.write(to_file = true, "~/Recpies/")
```