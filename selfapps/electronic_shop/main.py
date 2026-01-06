import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("articles.csv", dtype={"id": str})

class Product:
    def __init__(self, prod_id):
        self.name = df.loc[df["id"] == prod_id, "name"].squeeze()
        self.price = df.loc[df["id"] == prod_id, "price"].squeeze()
        self.stock = df.loc[df["id"] == prod_id, "in stock"].squeeze()

    def availability(self):
        if self.stock != 0:
            return True
        else:
            return False

class Buy:
    def __init__(self, prod_id, prod_object):
        self.prod_id = prod_id
        self.name = prod_object.name
        self.price = prod_object.price
        self.stock = prod_object.stock

    def receipt(self):
        df.loc[df["id"] == self.prod_id, "in stock"] = self.stock - 1
        df.to_csv("articles.csv", index=False)
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(w=50, h=8, text=f"Receipt: {self.prod_id}", ln=1)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(w=50, h=8, text=f"Article: {self.name}", ln=1)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(w=50, h=8, text=f"Price: {self.price}", ln=1)
        pdf.output("receipt.pdf")

print(df)
prod_ID = input("Enter product ID of product you want to buy: ")

product = Product(prod_ID)

if product.availability():
    buy = Buy(prod_ID, product)
    buy.receipt()
    print("Product is bought successfully!")
else:
    print("Product is not available")
