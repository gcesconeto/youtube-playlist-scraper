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
            if space_split[1] in ["Million", "million"] or space_split[0][-1] == "M":
                mult_factor = 1000000
            elif space_split[0][-1] == "K":
                mult_factor = 1000
            price = (
                float(space_split[0][1:].replace(",", "").replace("M", "").replace("K", ""))
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


def model_extractor(title, pub_date):
    try:
        post_colon = title.split(" : ")
        if len(post_colon) < 2:
            post_colon = title.split("Yacht Tour ")
        details = post_colon[1].split(" ")
        if details[0][0] in ["1", "2"]:
            year = details[0][0:4]
            brand = details[1]
            model = concatenate_model(details[2:])
        else:
            year = pub_date[0:4]
            brand = details[0]
            model = concatenate_model(details[1:])
        return {"year": year, "brand": brand, "model": model}
    except:
        print("Exception extracting model info")
        return {"year": None, "brand": None, "model": None}
