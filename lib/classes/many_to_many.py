class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        return self.title
    
    
        
class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        return self.name

    def articles(self):
        # if isinstance(articles, Article):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # if isinstance(article, Article):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
        


    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @name.setter
    def name (self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    


    def articles(self):
        # if isinstance(article, Article):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # if isinstance(author, Author):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass