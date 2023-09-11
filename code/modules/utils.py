# Third-party Libraries
# import xlsxwriter
import pandas as pd
from typing import Union  #,Dict, List


def get_leaves(item: Union[dict, list], key: dict = None) -> list:
    """get_leaves.

    Return all key: values recursively.

    Parameters
    ----------
    item : Union[dict, list]
        The dictionary.
    key : dict, optional
        The key., by default None

    Returns
    -------
    list
        Return key: values recursively.
    """
    try:
        if isinstance(item, dict):
            leaves = {}

            for i in item.keys():
                leaves.update(get_leaves(item[i], i))
            return leaves

        elif isinstance(item, list):
            leaves = {}

            for i in item:
                leaves.update(get_leaves(i, key))
            return leaves

        else:
            return {key: item}

    except Exception as e:
        print(e)


def pandas_df_to_markdown_table(df):
    from IPython.display import Markdown, display
    fmt = ["---" for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
    return df_formatted


def excel_writer(results_path: str, df) -> None:
    """excel_writer.

    Function that writes to an excel file with autofilter and converting dates to datetime in Excel.

    Parameters
    ----------
    results_path : str
        Path to save the file.
    df : pandas.core.frame.DataFrame
        Pandas dataframe.
    """
    # Write methods.
    writer = pd.ExcelWriter(results_path, engine="xlsxwriter", datetime_format="YYY-MM-DD")
    df.to_excel(writer, sheet_name="Sheet1", index=False, freeze_panes=(1, 0))

    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    worksheet.autofilter(0, 0, df.shape[0], df.shape[1] - 1)

    # Format for column headers. No more manually bolding and highlighting cells.

    # Bold all columns.
    bold_format = workbook.add_format({"bold": True})

    # Doing bold twice here because this will overwrite the bold above.
    review_format = workbook.add_format({"bold": True, "bg_color": "#FFC000"})
    investigate_format = workbook.add_format({"bold": True, "bg_color": "#00B0F0"})
    manual_format = workbook.add_format({"bold": True, "bg_color": "#FFFF00"})

    # Bold column names.
    worksheet.write_row("A1:AC1", df.columns, bold_format)

    # Highlight orange.
    worksheet.write_row(
        "C1:D1",
        [
            "",
        ],
        review_format,
    )

    # Highlight light blue.
    worksheet.write_row(
        "E1:F1",
        [
            "",
        ],
        investigate_format,
    )

    # Highlight yellow.
    # Note: I split these up since they are not all connected via ":".
    # Excel overwritten some columns.
    worksheet.write_row(
        "G1:G1",
        [
            "",
        ],
        manual_format,
    )

    worksheet.write_row("AC1", [""], manual_format)

    # NOTE: A close enough solution is converting number to float.
    # for i, j in df.iterrows():
    #     i += 2
    #     # worksheet.write("L{}".format(i), j["Number"], currency_format)
    #     worksheet.write_number("L{}".format(i), j["Number"])

    print("File saved to {}".format(results_path))

    writer.close()


def get_spacy_entity(doc, entity: str) -> list:
    """get_spacy_entity.

    This method will search nlp text for user specified entities.

    Parameters
    ----------
    doc : spacy.tokens.doc.Doc
        Spacy token.
    entity : str
        The entity to search on.

    Returns
    -------
    list
        A list of extracted entities.
    """
    from spacy.lang.en.stop_words import STOP_WORDS
    res = [token.lemma_ for token in doc if token.ent_type_ == entity.upper() and token.lemma_ not in STOP_WORDS]
    return res
