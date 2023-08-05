def print_options_in_dict(dict_to_print):
    """Display the menu options and ask user choice"""
    for item in dict_to_print.items():
        print("{} : {}".format(item[0], item[1]))
    print()


def highlight_input_option(option):
    """Highlights the option user chose and what he is doing currently"""
    print("\n######### Entered option to '{}' #########".format(option.lower()))


