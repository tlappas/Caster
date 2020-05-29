import dragonfly

def double_text_punc_dict():
    return {
        # Swap the logic for default quotes
        # "quotes":                            "\"\"",
        # "thin quotes":                         "''",
        "thick quotes":                      "\"\"",
        "quotes":                              "''",
        "tickris":                             "``",
        "prekris":                             "()",
        "brax":                                "[]",
        "curly":                               "{}",
        "angle":                               "<>",
    }

def _inv_dtpb():
    return {v: k for k, v in double_text_punc_dict().items()}

def text_punc_dict():
    # Insurers comma is recognized consistently with DNS/Natlink and
    # if/else statement workaround engines that do not expect punctuation symbol as a command
    if (dragonfly.get_current_engine().name == 'natlink'):
        comma = "(comma | ,)"
    else:
        comma = "comma"

    _id = _inv_dtpb()
    return {
        "ace":                                                " ",
        "clamor":                                             "!",
        "chocky":                                            "\"",
        "hash tag":                                           "#",
        "Dolly":                                              "$",
        "modulo":                                             "%",
        "ampersand":                                          "&",
        "apostrophe | single quote | chicky":                 "'",
        "left " + _id["()"]:                                  "(",
        "right " + _id["()"]:                                 ")",
        # Additional Parens keywords
        "lefty":                                              "(",
        "righty":                                             ")",
        "starling":                                           "*",
        "plus":                                               "+",
        comma:                                                ",",
        "minus":                                              "-",
        # Adding another hyphen word. Need to check for some reason dash is
        #   already responding is a '-'. Not sure if that's a built-in
        #   Dragon feature.
        "dash":                                               "-",
        "period | dot":                                       ".",
        "slash":                                              "/",
        "deckle":                                             ":",
        "semper":                                             ";",
        # Less than / greater than
        "less":                                               "<",
        "great":                                              ">",
        # "[is] less than | left " + _id["<>"]:               "<",
        "left " + _id["<>"]:                                  "<",
        "[is] less [than] [or] equal [to]":                  "<=",
        "equals sign":                                        "=",
        "[is] equal to":                                     "==",
        # "[is] greater than | right " + _id["<>"]:           ">",
        "right " + _id["<>"]:                                 ">",
        "[is] greater [than] [or] equal [to]":               ">=",
        "questo":                                             "?",
        "(atty | at symbol)":                                 "@",
        "left " + _id["[]"]:                                  "[",
        "backslash":                                         "\\",
        "right " + _id["[]"]:                                 "]",
        "carrot":                                             "^",
        # Easier underscrore"
        "under":                                              "_",
        "underscore":                                         "_",
        "ticky | ((left | right) " + _id["``"] + " )":        "`",
        "left " + _id["{}"]:                                  "{",
        "pipe (sim | symbol)":                                "|",
        "right " + _id["{}"]:                                 "}",
        # Individual curls
        "right curl":                                         "{",
        "left curl":                                          "}",
        "tilde":                                              "~",
        # Multi-symbol
        "dunder | dunderscore":                              "__",
        "equals":                                           " = ",
        "less than":                                        " < ",
        "greater than":                                     " > ",
        "equality":                                        " == ",
        "hash":                                              "# "
    }
