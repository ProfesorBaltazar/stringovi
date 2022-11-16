#program koji provjerava velika i mala slova u riječi
a = input("Upišite riječ:  ")
if a==a.upper():
    print("Sva slova su velika:  ")
else:
    if a==a.lower():
        print("Sva slova su mala.")
    else:
        print("Ima i velikih i malih slova.")
   