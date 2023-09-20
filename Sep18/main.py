from book import Book

book1 = Book(title="Introduction to OOP", author="Amadou Ndiaye",
             subject="OOP", pages=300, price=25000)

book2 = Book(title="Make your first website", author="Ndeye Fatou Diop",
             subject="Web development", pages=150, price=15000)

book3 = Book(title="Introduction to Machine Learning",
             author="Sidy Gueye", subject="AI", pages=500, price=40000)

print("Prices before Black Friday")
print(f"- {book1.price}")
print(f"- {book2.price}")
print(f"- {book3.price}")

book1.set_discount(0.2)
book2.set_discount(0.3)
book3.set_discount(0.7)

print("Prices on Black Friday")
print(f"- {book1.price}")
print(f"- {book2.price}")
print(f"- {book3.price}")
