# Examples:
# £290,000 Yacht Tour : Beneteau Swift Trawler 35
# €1.4 Million Yacht Tour : Azimut S6
# $5 Million Yacht Tour : Nordhavn 68 NFB


CURRENCY_SIGNS = {"£": "GBP", "€": "EUR", "$": "USD"}


def price_extractor(title):
    try:
        space_split = title.split(" ")
        mult_factor = 1
        if space_split[0][0] in CURRENCY_SIGNS:
            if space_split[1] == "Million" or space_split[0][-1] == "M":
                mult_factor = 1000000
            price = (
                float(space_split[0][1:].replace(",", "").replace("M", ""))
                * mult_factor
            )
            return {"price": price, "currency": CURRENCY_SIGNS[space_split[0][0]]}
        else:
            return {"price": None, "currency": "Not available"}
    except:
        print("Exception extracting price")
        return {"price": None, "currency": None}


def concatenate_model(list):
    try:
        model = ""
        for word in list:
            model += f" {word}"
        return model.strip()
    except:
        print("Exception defining model name")
        return "Model error"


def model_extractor(title):
    try:
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
    except:
        print("Exception extracting model info")
        return {"year": None, "brand": None, "model": None}
