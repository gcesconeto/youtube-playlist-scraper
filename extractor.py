# Examples:
# £290,000 Yacht Tour : Beneteau Swift Trawler 35
# €1.4 Million Yacht Tour : Azimut S6
# $5 Million Yacht Tour : Nordhavn 68 NFB


CURRENCY_SIGNS = {"£": "GBP", "€": "EUR", "$": "USD"}


def price_extractor(title):
    space_split = title.split(" ")
    if space_split[0][0] in CURRENCY_SIGNS:
        price = float(space_split[0][1:].replace(",", ""))
        if space_split[1] == "Million":
            price = price * 1000000
        return {"price": price, "currency": CURRENCY_SIGNS[space_split[0][0]]}
    else:
        return {"price": None, "currency": "Not available"}


def concatenate_model(list):
    model = ""
    for word in list:
        model += f" {word}"
    return model.strip()


def model_extractor(title):
    details = title.split(" : ")[1].split(" ")
    if details[0][0] in ["1", "2"]:
        year = details[0][0:4]
        brand = details[1]
        model = concatenate_model(details[2:])
    else:
        year = None
        brand = details[0]
        model = concatenate_model(details[1:])
    return {"year": year, "brand": brand, "model": model}
