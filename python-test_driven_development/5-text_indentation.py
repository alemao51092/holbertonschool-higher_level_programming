#!/usr/bin/python3
"""shebang"""


def text_indentation(text):
    """print text"""
    SpaceCheck = False
    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in {".", "?", ":"}:
            print(text[i] + "\n")
            SpaceCheck = True
        if SpaceCheck:
            if i < len(text) - 1 and text[i + 1] == " ":
                continue
            SpaceCheck = False
        else:
            print(text[i], end="")
