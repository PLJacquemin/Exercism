import re


def parse(markdown):
    # splitting everything
    lines = markdown.splitlines()

    # type of patterns
    bold_re = re.compile(r"__(.*?)__")
    italic_re = re.compile(r"_(.*?)_")
    header_re = re.compile(r"(#+) (.*)")
    list_re = re.compile(r"\* (.*)")
    # encapsulation of list
    list_tot = re.compile(r"<li>(.*)</li>")

    lines_re = []

    for line in lines:
        # substract pattern by markdown
        line = bold_re.sub(r"<strong>\1</strong>",line)
        line = italic_re.sub(r"<em>\1</em>",line)
        is_header = header_re.match(line)
        is_list = list_re.match(line)
        # if header
        if is_header:
            line = "<h{0}>{1}</h{0}>".format(len(is_header.group(1)),is_header.group(2))
        # if list
        elif is_list:
            line = list_re.sub(r"<li>\1</li>",line)
        # if not header nor list
        else:
            line ="<p>{0}</p>".format(line)
        lines_re.append(line)

    # writing output
    markdown_re = ''.join(lines_re)
    # encapsulation of list and return result
    return list_tot.sub(r"<ul><li>\1</li></ul>",markdown_re)
