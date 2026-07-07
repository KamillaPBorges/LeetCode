import pandas as pd
#vamos usar .str.capitalize() que deixa a primeira letra maiuscula
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id")