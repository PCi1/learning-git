product = ["roquefort", "stilton", "brie", "gouda", "edam", "parmezan", "mozzarella", "czechosłowacki ser zo owczego mleka"]
price = [12.50, 11.24, 9.30 , 8.55 , 11, 16.50, 14, 122.32]
for i in range(len(product)):
    a='{:0.2f}'.format(price[i])
    b='{:36.36}'.format(product[i])
    report = f"produkt: {b}cena:{a}zł"
    print(report)