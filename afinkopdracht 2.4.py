item1 = input("wat is de prijs van eerste product")
item2 = input("wat is de prijs van tweede product")
item3 = input("wat is de prijs van derde product")
item4 = input("wat is de prijs van vierde product")
item5 = input("wat is de prijs van vijfde product")

subtotal= float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
taxamount = subtotal * 0.07
total = subtotal + taxamount

