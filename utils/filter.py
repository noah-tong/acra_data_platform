from config.cargo_hubs import CARGO_HUBS


def filter_cargo_hubs(df):

    return df[
        df["iata"].isin(CARGO_HUBS)
    ].copy()