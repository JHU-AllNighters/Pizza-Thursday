import json

from src import read_gsheet, parse_dataframe


def main(shared_url):
    """
    Parse a dataframe of prices.
    """
    pizza_df = read_gsheet(shared_url)
    cost_dict = parse_dataframe(pizza_df, "People", "Price")
    return json.dumps(cost_dict, indent=4)
