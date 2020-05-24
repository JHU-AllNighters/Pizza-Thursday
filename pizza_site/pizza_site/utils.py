import json

from .io import read_gsheet
from .parse import parse_dataframe


def main(shared_url):
    """
    Parse a dataframe of prices.
    """
    pizza_df = read_gsheet(shared_url)
    cost_dict = parse_dataframe(pizza_df, "People", "Price")
    return json.dumps(cost_dict, indent=4)
