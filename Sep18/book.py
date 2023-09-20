class Book:
    def __init__(self, title, author, subject, pages, price):
        self.title = title
        self.author = author
        self.subject = subject
        self.pages = pages
        self.price = price
        self.__discount = 0

    def set_discount(self, discount):
        if discount > 0.4:
            raise ValueError("Discount value is too high")
        else:
            self.__discount = discount
            self.price = self.price * (1-self.__discount)

    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}, Subject: {self.subject}, Price: {self.price}"
