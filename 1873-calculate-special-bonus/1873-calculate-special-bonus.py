import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0

    condicao = (
        (employees["employee_id"] % 2 == 1) &
        (~employees["name"].str.startswith("M"))
    )

    employees.loc[condicao, "bonus"] = employees.loc[condicao, "salary"]

    resultado = employees[["employee_id", "bonus"]]

    resultado = resultado.sort_values(by="employee_id")

    return resultado
