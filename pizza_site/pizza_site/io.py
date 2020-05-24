import pandas as pd


def get_download_url(shared_url):
    """
    Reformat shared URL as a TSV download URL for easier Pandas import.
    """
    base_url = shared_url.split("/")[:-1]
    base_url.append(f"export?format=tsv")
    download_url = "/".join(base_url)
    return download_url


def read_gsheet(shared_url):
    download_url = get_download_url(shared_url)
    df = pd.read_csv(download_url, index_col=0, sep="\t", header=0)
    df["Price"] = df["Price"].replace("[\$,]", "", regex=True).astype(float)
    return df
