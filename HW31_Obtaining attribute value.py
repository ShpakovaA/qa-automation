# using string methods

href_attr_values = []

a_tag_begginning = '<a'

with open('wiki_page.txt') as f:
    for line in f:
        if a_tag_begginning in line:

            while line.count("<a") >= 1:
                start_a_tag_index = line.index(a_tag_begginning)
                start_href_attr_index = line.index('href="', start_a_tag_index)
                end_href_attr_index = line.index('"', start_href_attr_index + len('href="'))
                href_value = line[start_href_attr_index+len('href="'):end_href_attr_index]
                href_attr_values.append(href_value)
                line = line[end_href_attr_index:]

                if line.count("<a") > 1:
                    start_a_tag_index = line.index(a_tag_begginning)

print(href_attr_values)




# using regular expressions

with open('wiki_page.txt') as f:
    data = f.read()
    import re
    href_attr_values_using_re = re.findall(r'<a .*?href=\"(.+?)\"', data)
    print(href_attr_values_using_re)

# ['111/wiki/HTML111', '222/wiki/Form_(HTML)222', '333NEW333', '444/wiki/Image_map#Server-side444', '555/w/index.php?title=Query_string&amp;action=edit&amp;section=2555', '666/wiki/Form_(HTML)666']
