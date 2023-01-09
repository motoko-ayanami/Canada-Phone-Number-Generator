import csv

def generate_phone_numbers(phone_number):
    # If the phone number is complete (i.e. it has no 'x's), return it as a list
    if "x" not in phone_number:
        # Check if the NPA is "514" and the NXX is one of the excluded numbers
        if phone_number[:3] == "514" and phone_number[3:6] in [
            "211",
            "311",
            "411",
            "511",
            "555",
            "611",
            "711",
            "811",
            "911",
            "950",
            "263",
            "438",
            "450",
            "460",
            "514",
            "537",
            "579",
            "958",
            "959",
            "468",
            "584",
            "753",
        ]:
            return []
        elif phone_number[:3] == "438" and phone_number[3:6] in [
            "211",
            "311",
            "411",
            "511",
            "555",
            "611",
            "711",
            "811",
            "911",
            "950",
            "976",
            "263",
            "438",
            "450",
            "460",
            "514",
            "537",
            "579",
            "958",
            "959",
            "218",
            "219",
            "231",
            "232",
            "234",
            "235",
            "236",
            "253",
            "305",
            "306",
            "307",
            "309",
            "312",
            "314",
            "332",
            "367",
            "423",
            "425",
            "426",
            "427",
            "429",
            "443",
            "445",
            "446",
            "449",
            "451",
            "453",
            "454",
            "470",
            "510",
            "512",
            "513",
            "515",
            "516",
            "517",
            "529",
            "531",
            "532",
            "534",
            "535",
            "536",
            "539",
            "542",
            "543",
            "545",
            "546",
            "547",
            "556",
            "557",
            "559",
            "575",
            "576",
            "578",
            "581",
            "582",
            "583",
            "584",
            "585",
            "586",
            "587",
            "589",
            "612",
            "613",
            "614",
            "615",
            "616",
            "617",
            "620",
            "621",
            "623",
            "624",
            "625",
            "626",
            "627",
            "628",
            "629",
            "631",
            "632",
            "633",
            "634",
            "635",
            "636",
            "637",
            "639",
            "640",
            "641",
            "642",
            "643",
            "645",
            "646",
            "647",
            "649",
            "651",
            "652",
            "653",
            "654",
            "655",
            "656",
            "657",
            "658",
        ]:
            return []
        else:
            return [phone_number]
    # Otherwise, generate all possible numbers for the first 'x' and recursively generate
    # possible combinations of numbers for the rest of the phone number
    phone_numbers = []
    # Check if the fourth digit is an 'x'
    if phone_number[3] == "x":
        # Generate all possible numbers except for 0 and 1
        for number in range(2, 10):
            phone_numbers += generate_phone_numbers(
                phone_number.replace("x", str(number), 1)
            )
    else:
        # Generate all possible numbers
        for number in range(10):
            phone_numbers += generate_phone_numbers(
                phone_number.replace("x", str(number), 1)
            )
    return phone_numbers


# Prompt the user for a partial phone number
phone_number = input(
    "Enter a partial phone number with unknown digits represented by 'x': "
)

# Generate all possible phone numbers
phone_numbers = generate_phone_numbers(phone_number)

# Write the list of phone numbers to a CSV file
with open("phone_numbers.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([[phone_number] for phone_number in phone_numbers])

print(f"Wrote {len(phone_numbers)} phone numbers to 'phone_numbers.csv'.")
