import pandas as pd


def main():
    xlsx = pd.ExcelFile('data/input.xlsx')
    mainData = pd.read_excel(xlsx, 'Data')

    columns = list(mainData)

    excludeBillingIndex = mainData.columns.get_loc("Exclude Billing")
    cridIndex = mainData.columns.get_loc("CRID")

    df = pd.DataFrame({
        columns[excludeBillingIndex]: mainData[columns[excludeBillingIndex]],
        columns[cridIndex]: mainData[columns[cridIndex]],
    })

    for (index_label, row_series) in df.iterrows():
        if pd.isnull(row_series.values[0]) or row_series.values[0] != 'OK':
            # do some work
            row_series.values[0] = "DONE"

    df.to_excel('data/output.xlsx', sheet_name='crid', index=False)


if __name__ == "__main__":
    main()
