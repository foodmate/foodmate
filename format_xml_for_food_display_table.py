# Winston C. Yang
#
# Created 2012-06-02
#
# This code is part of the event Random Hacks of Kindness.
# ------------------------------------------------------------------------------
# Read the input file, which is an XML file.
#
# Format the XML as follows, by adding a newline after ">"'s.
#
# <?xml version="1.0"?>
# <Food_Display_Table>
#
#
# <Food_Display_Row>
#<Food_Code>
#12350000</Food_Code>
#<Display_Name>
#Sour cream dip</Display_Name>
#<Portion_Default>
#1.00000</Portion_Default>
#
# Write the output to an output file.
# ------------------------------------------------------------------------------
# Open the input file.
input_file_path = "Food_Display_Table.xml"
input_file = open(input_file_path)
# ------------------------------------------------------------------------------
# Open the output file.
output_file_path = "format_xml_for_food_display_table.txt"
output_file = open(output_file_path, "w+")
# ------------------------------------------------------------------------------
# Format the XML.
#
# Write the output to the output file.
for line in input_file:

    line = line.replace(">", ">\n")

    print(line, file=output_file)
