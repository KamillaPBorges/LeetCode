import pandas as pd
#primeiro ordena por id do menor para o maior 
#inplace=True é pra substituir, faz a alteracao no proprio df 
#keep first é manter o primeiro 
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
    