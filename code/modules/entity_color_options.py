# Source(s):
# - https://github.com/allenai/scispacy/issues/141#issuecomment-518274586
# - https://github.com/explosion/spaCy/blob/master/spacy/displacy/render.py

# Standard Libraries
import random

# TEXT_ENTITIES = []

# REGEX_ENTITIES = []

DEFAULT_LABEL_COLORS = {
    "CARDINAL": "#e4e7d2",
    "DATE": "#bfe1d9",
    "EVENT": "#ffeb80",
    "FAC": "#9cc9cc",
    "GPE": "#feca74",
    "LANGUAGE": "#ff8197",
    "LAW": "#ff8197",
    "LOC": "#ff9561",
    "MONEY": "#e4e7d2",
    "NORP": "#c887fb",
    "ORDINAL": "#e4e7d2",
    "ORG": "#7aecec",
    "PERCENT": "#e4e7d2",
    "PERSON": "#aa9cfc",
    "PRODUCT": "#bfeeb7",
    "QUANTITY": "#e4e7d2",
    "TIME": "#bfe1d9",
    "WORK_OF_ART": "#f0d0ff",
}


def get_entities(model) -> dict:
    """get_entities.

    Method that gets the entities/ labels from spaCy.

    Parameters
    ----------
    model : spacy model
        spacy model.

    Returns
    -------
    dict
        A dictionary of lists of the available entities in the model.
    """
    nlp = model.load()

    # Entity Rulers
    text_entities_list = list(nlp.__dict__["_meta"]["labels"]["entity_ruler"])

    # Regex
    regex_list = []

    # Additional labels
    additional_labels = [
        "UNKNOWN",
    ]

    # Regex
    combined_regex_list = regex_list + additional_labels

    all_ents = {
        "TEXT_ENTITIES": text_entities_list,
        "REGEX_ENTITIES": combined_regex_list,
    }

    return all_ents


def color_generator(number_of_entities: int) -> list:
    """color_generator.

    Takes the number of custom entities and generates random colors for each.

    Author(s): https://github.com/phosseini

    Parameters
    ----------
    number_of_entities : int
        The total number of custom entities.

    Returns
    -------
    list
        A list of random generated hex colors.
    """
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_entities)]

    return color


def get_entity_options(all_ents=None) -> dict:
    """get_entity_options.

    Generating color options for visualizing the named entities.

    Author(s): https://github.com/phosseini

    Parameters
    ----------
    all_ents : dict
        A dictionary of lists of the available entities in the model.

    Returns
    -------
    dict
        A dictionary of the entities list names and generated colors.

    Examples
    --------
    >>> import spacy
    >>> from entity_color_options import get_entities, get_entity_options
    >>> all_ents = get_entities(SPACY_MODEL)
    >>> nlp = SPACY_MODEL.load()
    >>> doc = nlp("Some text here.")
    >>> spacy.displacy.render(doc, style="ent", jupyter=True, options=get_entity_options(all_ents))
    """
    # Colors dictionary
    colors = DEFAULT_LABEL_COLORS

    # Condition to check for custom entity labels.

    # This condition looks for current entities in the imported/ passed in model.
    if all_ents:
        # Combine new entity lists. This is done to preserve the original spaCy colors.
        custom_entity_list = all_ents["TEXT_ENTITIES"] + all_ents["REGEX_ENTITIES"]  # Add new entity list here

    # if TEXT_ENTITIES and REGEX_ENTITIES:

    #     # Combine new entity lists. This is done to preserve the original spaCy colors.
    #     custom_entity_list = TEXT_ENTITIES + REGEX_ENTITIES  # Add new entity list here

    else:
        custom_entity_list = []

    # Generate random colors for the length of the new entities.
    color = color_generator(len(custom_entity_list))

    # Add each color to the "colors" dictionary.
    for i in range(len(custom_entity_list)):
        colors[custom_entity_list[i]] = color[i]

    # Combine all entity lists.
    # entity_list = SPACY_ENTITIES + custom_entity_list
    entity_list = list(DEFAULT_LABEL_COLORS.keys()) + custom_entity_list

    # entity_list = list(DEFAULT_LABEL_COLORS.keys())

    options = {"ents": entity_list, "colors": colors}

    return options
