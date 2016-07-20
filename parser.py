def parse_unquoted(unparsed_string):
    first_space = unparsed_string.find(' ')
    if first_space == -1:
        return (unparsed_string, "")
    else:
        return (unparsed_string[0:first_space], unparsed_string[first_space:])


def parse_quoted(unparsed_string):
    ending_quote = unparsed_string.index("'")
    return (unparsed_string[0:ending_quote], unparsed_string[ending_quote+1:])


def parse_args(args):
    parsed_args = []
    unparsed = args
    while len(unparsed) > 0:
        if unparsed[0] == " ":
            unparsed = unparsed[1:]
        elif unparsed[0] == "'":
            (next_arg, unparsed) = parse_quoted(unparsed[1:])
            parsed_args.append(next_arg)
        else:
            (next_arg, unparsed) = parse_unquoted(unparsed)
            parsed_args.append(next_arg)
    return parsed_args
