def format_name(f_name, l_name):
    """This is a docstring which can
    explain the function, it also gets populated
    in the documentation"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

print(length)
print(format_name)
