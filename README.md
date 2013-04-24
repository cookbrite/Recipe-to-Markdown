rescrape
========

Rescrape is a Python tool for scraping online recipes into [Markdown](http://daringfireball.net/projects/markdown/).
Becaue the files are Markdown, they can be opened in any text editor or word processor, easily emailed, and easily modified.
Because Markdown is simple a text file, you'll be able to open your recipes as easily 50 years from now as you can today.

Rescrape provides an abstract scraping class that can be implemented for any website. So far, I implemented scrapers for

* [AllRecipes.com](http://www.allrecipes.com)
* [Food.com](http://www.food.com)
* [The Pioneer Woman](http://www.thepioneerwoman.com)

Please write other scrapers and issue pull requests!

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
s.write(to_file = true, "~/Recipes/")
```

> Grilled Salmon I Recipe
>
> http://allrecipes.com/Recipe/Grilled-Salmon-I/Detail.aspx
>
> * Servings: 6
> * Prep Time:  15 mins
> * Cook Time:  16 mins
> * Total Time:  2 hrs 31 mins
>
> Ingredients:
>
> * 1 1/2 pounds salmon fillets
> * lemon pepper to taste
> * garlic powder to taste
> * salt to taste
> * 1/3 cup soy sauce
> * 1/3 cup brown sugar
> * 1/3 cup water
> * 1/4 cup vegetable oil
>
> Directions:
>
> 1. Season salmon fillets with lemon pepper, garlic powder, and salt.
> 2. In a small bowl, stir together soy sauce, brown sugar, water, and vegetable oil until sugar is dissolved. Place fish in a large resealable > plastic bag with the soy sauce mixture, seal, and turn to coat. Refrigerate for at least 2 hours.
> 3. Preheat grill for medium heat.
> 4. Lightly oil grill grate. Place salmon on the preheated grill, and discard marinade. Cook salmon for 6 to 8 minutes per side, or until the fish flakes easily with a fork.