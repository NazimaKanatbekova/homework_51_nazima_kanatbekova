class ArticleDb:
    articles = []

    @classmethod
    def add_cat(cls, cat):
        cls.articles.append(cat)

    @classmethod
    def get_cat(cls, name):
        for cat in cls.articles:
            if cat.name == name:
                return cat
        return None

