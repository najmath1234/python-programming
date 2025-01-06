class Publisher:
    def __init__ (self,name):
        self.name=name
class Book(Publisher):
    def __init__ (self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def show_details(self):
        print("Publisher",self.name)
        print("title",self.title)
        print("author",self.author)
class python(Book):
    def __init__ (self,name,title,author,price,no_of_pages):
        super().__init__ (name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def show_details(self):
        print("Publisher",self.name)
        print("title",self.title)
        print("author",self.author)
        print("price",self.price)
        print("no_of_pages",self.no_of_pages)
book=python("dc books","python","najma",1200,190)
book.show_details()
        
    
        
