import os
import bibtexparser
from config import *

bibtex_filename = "./bibtex.bib"

def keep_last_and_only(authors_str):
    """
    This function is dedicated to parse authors, it removes all the "and" but the last and and replace them with ", "
    :param str: string with authors
    :return: string with authors with only one "and"
    """
    authors_str = authors_str.replace('\n', ' ')

    author_lst = authors_str.split(" and ")

    if len(author_lst) <= 8:
        last_author = author_lst[-1]

        without_and = authors_str.replace(" and ", ", ")

        str_ok = without_and.replace(", " + last_author, " and " + last_author)

    else:
        str_ok = ', '.join(author_lst[:8])
        str_ok += ' et al.'
    
    return str_ok.replace('{', '').replace('}', '')


def get_bibtex_line(filename, ID):
    start_line_number = 0
    end_line_number = 0
    
    with open(filename, encoding="utf-8") as myFile:
        for num, line in enumerate(myFile, 1):
            
            # first we look for the beginning line
            if start_line_number == 0:
                if (ID in line) and not ("@String" in line):
                    start_line_number = num
            else:  # after finding the start_line_number we go there
                # the last line contains "}"
                
                # we are at the next entry we stop here, end_line_number have the goof value
                if "@" in line:
                    assert end_line_number > 0
                    break
                
                if "}" in line:
                    end_line_number = num
    assert end_line_number > 0
    return start_line_number, end_line_number

def create_bib_link(ID):
    link = bibtex_filename
    start_bib, end_bib = get_bibtex_line(link, ID)
    link = base_link + link
    
    # bibtex file is one folder upon markdown files
    # link = "../blob/master/" + link
    link += "#L" + str(start_bib) + "-L" + str(end_bib)
    
    # L66-L73
    return link


def get_md_entry(DB, entry, add_comments=True):
    """
    Generate a markdown line for a specific entry
    :param entry: entry dictionary
    :return: markdown string
    """
    md_str = "\n"
    
    md_str += "- "
    
    venue = ""
    year = ""
    
    if "booktitle" in entry.keys():
        venue = entry["booktitle"].replace("Proceedings of ", "")
    if "journal" in entry.keys():
        venue += entry["journal"].replace("{", "").replace("}", "")
    
    venue = venue.replace(" ", "_").replace("-", "_")
    if "year" in entry.keys():
        year = entry['year']
    
    if venue != "" or year != "":
        tag = "![](https://img.shields.io/badge/{}-{}-{})".format(venue, year, color)
        if "url" not in entry.keys():
            print(entry["ID"])
        tag = "[{}]({})".format(tag, entry['url'])
        md_str += "{}".format(tag)
    else:
        md_str += ""
    
    paper_title = entry['title'].replace("{", "")
    paper_title = paper_title.replace("}", "")
    paper_title = paper_title.strip()
    
    if 'url' in entry.keys():
        md_str += " [**" + paper_title + "**](" + entry['url'] + "),"
    else:
        md_str += " **" + paper_title + "**"

    if 'code' in entry.keys():
        code_url = entry['code']
        md_str += f' [[Code]]({code_url})'

    if 'plm' in entry.keys():
        md_str += ' '
        plms = entry['plm'].split(',')
        for plm in plms:
            plm = plm.strip().replace('-', '--')
            md_str += f'![](https://img.shields.io/badge/{plm}-yellow) '

    md_str += "<br>"



    md_str += " by *" + keep_last_and_only(entry['author']) + "*"



    # md_str += " [[bib]](" + create_bib_link(entry['ID']) + ")"
    
    if add_comments:
        # maybe there is a comment to write
        # print(DB.strings)
        md_str += '\n'
        if entry['ID'].lower() in DB.strings:
            # print("Com : " + entry['ID'])
            md_str += '<br>```'
            comment = DB.strings[entry['ID'].lower()]
            comment = comment.replace(r'\n', '<br>')
            md_str += comment
            md_str += '```'
    md_str += '<br><br>'
    # md_str += "</details>"

    # img_link = os.path.join(base_link, "scripts/svg/copy_icon.png")
    # md_str += f'<details><summary></summary>'
    # md_str += f"<pre>```{entry['ID']}```"
    

    return md_str


def get_md(DB, item, key, add_comments, filter_key="", filter_content=None):
    """
    :param DB: list of dictionary with bibtex
    :param item: list of keywords to search in the DB
    :param key: key to use to search in the DB author/ID/year/keyword...
    :return: a md string with all entries corresponding to the item and keyword
    """
    
    all_str = ""
    
    list_entry = {}
    
    number_of_entries = len(DB.entries)
    for i in range(number_of_entries):
        if key in DB.entries[i].keys():
            if filter_key != "":
                if not (filter_key in DB.entries[i].keys() and any(
                        elem in DB.entries[i][filter_key] for elem in filter_content)):
                    continue
            
            if key == "booktitle" or key == "journal":
                if any(DB.entries[i][key].replace("Proceedings of ", "").startswith(elem) for elem in item):
                    str_md = get_md_entry(DB, DB.entries[i], add_comments)
                    list_entry.update({str_md: DB.entries[i]['year']})
            elif key == "author":
                author_list = format_author(DB.entries[i][key])
                
                if any(elem in author_list for elem in item):
                    str_md = get_md_entry(DB, DB.entries[i], add_comments)
                    list_entry.update({str_md: DB.entries[i]['year']})
            elif any(elem in DB.entries[i][key] for elem in item):
                str_md = get_md_entry(DB, DB.entries[i], add_comments)
                list_entry.update({str_md: DB.entries[i]['year']})
    
    sorted_tuple_list = sorted(list_entry.items(), reverse=True, key=lambda x: x[1])
    for elem in sorted_tuple_list:
        all_str += elem[0]
    
    return all_str, len(sorted_tuple_list)


def format_author(author_str: str):
    author_str = author_str.replace(" and\n", " and ")
    author_str = author_str.replace("{-}", " ")
    author_list = author_str.split(" and ")
    formatted_author_list = []
    for author in author_list:
        name = author.split(",")
        name = [str(i).strip() for i in name]
        if len(name) > 1:
            f_name = name[1:]
            f_name.append(name[0])
            formatted_name = " ".join(f_name)
        else:
            formatted_name = name[0]
        
        formatted_author_list.append(formatted_name)
    
    return formatted_author_list


def get_author_list(DB, filter_key, filter_content, filter_num=1):
    entries = DB.entries
    author_dict = {}
    for i, entry in enumerate(entries):
        if filter_key != "":
            if not (filter_key in entry.keys() and any(
                    elem in entry[filter_key] for elem in filter_content)):
                continue
        
        author_list = format_author(entry["author"])
        
        for author in author_list:
            if author in author_dict.keys():
                author_dict[author] = author_dict[author] + 1
            else:
                author_dict[author] = 1
    authors = [k for k, v in sorted(author_dict.items(), key=lambda item: item[1]) if v > filter_num][::-1]
    return authors


def generate_md_file(DB, list_classif, key, plot_title_fct, filename, get_outline, get_hyperlink,
                     dir_path="./", add_comments=True, discrib="",
                     filter_key="", filter_content=None, add_hyperlink=False, hyperlinks=None, mapping_name=None):
    """
    :param dir_path: dictionary path
    :param DB: list of dictionnary with bibtex
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    filename = os.path.join(dir_path, filename)
    
    all_in_one_str = ""
    list_classif_keeped = []
    all_in_one_str_content = ""
    
    count_list = []
    
    if list_classif is None and "author" in key:
        list_classif = get_author_list(DB, filter_key, filter_content)
        list_classif = [[author] for author in list_classif]

    for item in list_classif:
        temp_str = ""
        count = 0
        for k in key:
            str, temp_count = get_md(DB, item, k, add_comments, filter_key, filter_content)
            temp_str += str
            count += temp_count
            if str != "":
                all_in_one_str_content += plot_title_fct(item)
                all_in_one_str_content += str
        if temp_str != "":
            list_classif_keeped.append(item)
            count_list.append(count)
    
    all_in_one_str += get_outline(list_classif_keeped, count_list, filename, discrib, add_hyperlink)
    
    if add_hyperlink:
        all_in_one_str += get_hyperlink(hyperlinks, mapping_name)
    
    all_in_one_str += all_in_one_str_content
    
    f = open(filename, "w", encoding='utf-8')
    f.write(all_in_one_str)
    f.close()
