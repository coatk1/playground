# Standard Libraries
import string

# Third-party Libraries
import pandas as pd


def customer_excel_writer(results_path: str, df: pd.DataFrame, autofilter: bool = True, format: bool = False, column_str: str = "", column_list: list = [], column_color: str = "") -> None:
    """customer_excel_writer.

    Function that writes to an excel file with custom additions:
    - autofilter
    - coloring headers

    Parameters
    ----------
    results_path : str
        Path to save the file.
    df : pd.DataFrame
        Pandas dataframe.
    autofilter : bool, optional
        Boolean for adding autofilter to excel sheet column headers, by default True
    format : bool, optional
        Boolean for adding formatting to excel sheet column headers (i.e. bold headers, highlighted headers, etc.), by default False
    column_str : str, optional
        String representing the column headers in excel (i.e. A1:C1), by default ""
    column_list : list, optional
        List of column names, by default []
    column_color : str, optional
        Hex color to highlight the column headers (i.e. #FFFF00), by default ""

    Returns
    -------
    None

    Examples
    --------
    >>> save.customer_excel_writer("save_normal_excel.xlsx", df)
    >>> save.customer_excel_writer("save_no_filter_excel.xlsx", df, autofilter=False)
    >>> save.customer_excel_writer("save_format_default_excel.xlsx", df, format=True, column_list=list(df.columns))
    >>> save.customer_excel_writer("save_format_custom_excel.xlsx", df, format=True, column_list=list(df.columns)[0:3], column_str="A1:C1", column_color="#00B0F0")
    """
    sheet_num = "Sheet1"

    # Write methods.
    writer = pd.ExcelWriter(path=results_path, engine="xlsxwriter", datetime_format="YYYY-MM-DD")
    df.to_excel(excel_writer=writer, sheet_name=sheet_num, index=False, freeze_panes=(1, 0))

    workbook = writer.book
    worksheet = writer.sheets[sheet_num]

    if autofilter:
        worksheet.autofilter(0, 0, df.shape[0], df.shape[1] - 1)

    if format:

        # Bold column names.
        # worksheet.write_row("A1:C1", df.columns, workbook.add_format({"bold": True}))

        if len(column_color) == 0:
            column_color = "#FFFF00"  # Yellow

        if len(column_str) == 0:

            # Create a list of alphabet letters (for excel columns) for the length of the dataframe.
            excel_column_list = [list(string.ascii_uppercase)[i] + "1" for i in range(len(list(df.columns)))]

            column_str = excel_column_list[0] + ":" + excel_column_list[-1]  # All columns in dataframe

        # Highlight.
        worksheet.write_row(
            column_str,
            column_list,
            workbook.add_format({"bold": True, "bg_color": column_color}),
        )

        print(f"File saved to {results_path}")

        writer.close()
