# Winston C. Yang
#
# Created 2012-06-02
#
# This code is part of the event Random Hacks of Kindness.
# ------------------------------------------------------------------------------
# Read the input file.
#
# The input file has XML in an unusual format.
#
# Parse the input file using simple string operations.
#
# (It would be better to use an XML module, but I might need some time
# to learn one.)
#
# Convert the XML to JSON.
#
# Write the JSON to an output file.
# ------------------------------------------------------------------------------
input_file_path = "format_xml_for_food_display_table.txt"
input_file = open(input_file_path)
lines = input_file
# ------------------------------------------------------------------------------
dictionary_list = list()

for line in lines:

    line = line.strip()

    # Examples of lines in the input file:
    #
    # <Food_Display_Row>
    # <Food_Code>
    # 12350000</Food_Code>
    # <Display_Name>
    # Sour cream dip</Display_Name>
    # <Portion_Default>
    # 1.00000</Portion_Default>
    if line == "<Food_Display_Row>":

        line = next(lines).strip()

        d = dict()

        while line != "</Food_Display_Row>":

            if line.startswith("<"):

                # Get the tag name.
                #
                # Ignore the "<" and ">" at the ends.
                tag_name = line[1:-1]

                # Get the tag value.
                #
                # Assume that the value ends before a "<".
                line = next(lines).strip()
                i = line.index("<")
                tag_value = line[:i]
                d[tag_name] = tag_value

                #print(tag_name, tag_value)
                line = next(lines).strip()

        dictionary_list.append(d)
# ------------------------------------------------------------------------------
def reformat_value(value):

    # Is the value a number?
    try:
        return float(value)
    except ValueError:
        # The value is not a number. Surround it with double
        # quotes.
        return "\"" + value + "\""
# ------------------------------------------------------------------------------
def rename_key(key):

    if key == "Food_Code":

        key = "id"
    else:
        # Delete underscores.
        key = key.replace("_", "")

        # Make the first character lowercase.
        key = key[0].lower() + key[1:]

    return key
# ------------------------------------------------------------------------------
def format_key_value(key, value):

    return "{space}\"{key}\"=>{value},".format(
        space=4*" ",
        key=key,
        value=value,
        )
# ------------------------------------------------------------------------------
# Open the output file.
output_file_path = "create_json.php"
output_file = open(output_file_path, "w+")
# ------------------------------------------------------------------------------
# Write the dictionaries to the output file.
#
# Use a format like the following:
#(
#    "addedSugars"=>1.57001,
#    "alcohol"=>0.0,
#    "calories"=>133.65,
#    "displayName"=>"Sour cream dip",
# :
# :
#
# Some dictionaries have the same display name. Keep only the first
# one.
display_name_set = set()

for d in dictionary_list:

    display_name = d["Display_Name"]

    # Have we seen the display name before?
    if display_name in display_name_set:

        # Ignore this dictionary.
        continue
    else:

        # Keep track of the display name.
        display_name_set.add(display_name)

    # Print the dictionary.
    print("array(", file=output_file)

    for key in sorted(d):

        value = reformat_value(d[key])
        key = rename_key(key)

        s = format_key_value(key, value)
        print(s, file=output_file)

    print("),", file=output_file)
