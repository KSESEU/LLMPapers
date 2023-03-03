import json

from utils import generate_md_file
import bibtexparser
from config import *

file_name = 'bibtex.bib'
with open(file_name, encoding='utf-8') as bibtex_file:
    bibtex_str = bibtex_file.read()
bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))


def check_repetition(DB=bib_db):
    bib_dict = {}
    for entry in DB.entries:
        title = entry["title"]
        title = str(title).strip()
        title = title.replace("{", "").replace("}", "")
        if title in bib_dict.keys():
            bib_dict[title] = bib_dict[title] + 1
        else:
            bib_dict[title] = 1
    repet_bib = [i for i in bib_dict.keys() if bib_dict[i] > 1]

    if len(repet_bib) != 0:
        print("Attention! Repetition detected in the bibtex file! Please check the following entries:")
        print("---------------------------")
    for i, title in enumerate(repet_bib):
        print(i + 1, title)


def plot_titles(titles):
    title = titles[0]
    if title == 'FCST':
        title += ' 计算机科学与探索'
    if title in sub_titles:
        return '\n' + "#### " + title + '\n'
    return '\n' + "### " + title + '\n'


def get_outline(list_classif, count_list, filename, dicrib, add_hyperlink=False):
    # todo: could be removed
    str_outline = "# " + 'Resources on ChatGPT and Large Language Models' + "\n"

    str_outline += 'Collection of  papers and related works for Large Language Models ' \
                   '(ChatGPT, GPT-3, Codex etc.).\n'

    str_outline += "## " + 'Contributors' + "\n"
    str_outline += 'This repository is contributed by the following contributors.\n'
    str_outline += '- **Organizers**: [Guilin Qi (漆桂林)](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm), [Xiaofang Qi (戚晓芳)](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm)\n'
    str_outline += '- **Paper Collectors**: Zafar Ali, ' \
                   '[Sheng Bi (毕胜)](https://github.com/bisheng), ' \
                   '[Yongrui Chen (陈永锐)](https://github.com/Bahuia), ' \
                   'Zizhuo Chen (陈孜卓), ' \
                   '[Xinbang Dai (戴鑫邦)](https://github.com/OBriennnnn), ' \
                   'Huan Gao (高桓), ' \
                   '[Nan Hu (胡楠)](https://github.com/HuuuNan), ' \
                   'Shilong Hu (胡世龙), ' \
                   '[Jingqi Kang (康婧淇)](https://github.com/JingqiKang), ' \
                   '[Jiaqi Li (李嘉琦)](https://github.com/aoluming), ' \
                   'Dehai Min (闵德海), ' \
                   'Yiming Tan (谭亦鸣), ' \
                   '[Tongtong Wu (吴桐桐)](http://wutong8023.site/), ' \
                   '[Songlin Zhai (翟松林)](https://github.com/SonglinZhai), ' \
                   '[Yuxin Zhang (张裕欣)](https://github.com/Zzyx1996)\n'
    str_outline += '- **Maintainers**: [Runzhe Wang (王润哲)](https://github.com/sid0527), ' \
                   '[Shenyu Zhang (张沈昱)](https://github.com/ZSY-SZ) \n\n'
    str_outline += 'The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git). ' \
                   'If you\'d like to commit to this repo, please modify [bibtex.bib](https://github.com/KSESEU/LLMPapers/blob/main/bibtex.bib) ' \
                   'or [related_works.json](https://github.com/KSESEU/LLMPapers/blob/main/related_works.json) and re-generate ' \
                   '[README.md](https://github.com/KSESEU/LLMPapers/blob/main/README.md) using `python scripts/run.py`.\n\n'

    str_outline += dicrib + "\n\n"

    str_outline += '## Papers\n\n'

    str_outline += "### Outline \n"

    if add_hyperlink:
        hyperlink = f"![](https://img.shields.io/badge/Hyperlink-{color})"
        link = base_link + filename + '#hyperlink'
        str_outline += "- [" + hyperlink + "](" + link + ')\n'

    count_dct = {}
    for i, item in enumerate(list_classif):
        count_dct[item[0]] = count_list[i]

    for item in list_classif:
        if item[0] in sub_titles.keys():
            count_dct[sub_titles[item[0]]] += count_dct[item[0]]

    for i, item in enumerate(list_classif):
        flag = True if item[0] in sub_titles.keys() else False
        paper_number = "![](https://img.shields.io/badge/{}-{}-{})".format(
            item[0].replace(" ", "_").replace("-", "--"), str(count_dct[item[0]]), color)
        link = base_link + "" + filename + "#" + item[0].replace(" ", "-").lower()
        paper_number = "[{}]({})".format(paper_number, link)

        if flag:
            str_outline += "  - " + paper_number + '\n'
        else:
            str_outline += "- " + paper_number + '\n'

    return str_outline


def get_hyperlink(hyperlinks, mapping_name):
    str_hyperlink = "### Hyperlinks \n"

    hyperlinks = sorted(hyperlinks)

    # Note: please check the branch name carefully!
    str_hyperlink += f"- [[Overview]]({base_link}README.md) -- [Homepage]({base_link}README.md)\n"
    for i, item in enumerate(hyperlinks):
        str_hyperlink += "- "
        str_hyperlink += f" -- [{mapping_name[item]}]({base_link}taxonomy/{item})\n"

    return str_hyperlink


def plot_content(index, keys, dir_path, disc, list_type, plot_titles=plot_titles, sub_dirs=None, mapping_name=None):
    for dir_ in [sub_dirs[0][index], "./"]:
        generate_md_file(DB=bib_db, list_classif=list_type, key=keys, plot_title_fct=plot_titles,
                         filename="README.md", add_comments=True, dir_path=dir_,
                         mapping_name=mapping_name,
                         discrib=disc, add_hyperlink=True, hyperlinks=dir_path, get_outline=get_outline,
                         get_hyperlink=get_hyperlink)
        if index != 0:
            break


# check repetition
check_repetition()
'''
dir_path = ["./", "contribution", "time", "application", "supervision", "approach", "setting",
            "research_question", "backbone_model", "dataset", "metrics", "author",'techniques',"venue"]
            
'''
dir_path = ["./", "time", "author", 'techniques', "venue"]

mapping_name = {
    "./": "Summary",
    "venue": "Published Venue",
    "time": "Published Time",
    "application": "Application",
    "contribution": "Contribution",
    "supervision": " Learning Paradigm",
    "approach": "Approach",
    "setting": "Setting",
    "research_question": "Research Questions",
    "backbone_model": "Backbone Model",
    "dataset": "Dataset",
    "metrics": "Metrics",
    "author": "Author",
    "techniques": 'Techniques'
}
dir_path_IE4all = ["taxonomy/" + dp for dp in dir_path]

sub_dirs = [dir_path_IE4all]

# 0 Home
list_type = [[bm] for bm in fined_taxonomy["Techniques"]]
# list_type.sort()
index = 0
disc = ""
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 2 time
list_type = [[str(year)] for year in range(1980, 2030)][::-1]
index = 1
disc = "This page categorizes the literature by the **Last Post**"
plot_content(index=index, keys=["year"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)
"""
# 1 Contribution
list_type = [[typ] for typ in fined_taxonomy["Contribution"]]
index = 1
disc = "This page categorizes the literature by the Contribution"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 3 application
list_type = [[app] for app in fined_taxonomy["Application"]]
index = 3
disc = "This page categorizes the literature by the **Continual Learning Application**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 4 supervision
list_type = [[sp] for sp in fined_taxonomy["Supervision"]]
index = 4
disc = "This page categorizes the literature by the **Learning Paradigm**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 5 approach
list_type = []
for key in fined_taxonomy["Approach"]:
    if key in fined_taxonomy.keys():
        list_type += [[k] for k in fined_taxonomy[key]]
    else:
        list_type.append([key])`
index = 5
disc = "This page categorizes the literature by the **Continual Learning Approach**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 6 setting
list_type = [[setting] for setting in fined_taxonomy["Setting"]]
index = 6
disc = "This page categorizes the literature by the **Continual Learning Setting**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 8 research question
list_type = [[rq] for rq in fined_taxonomy["RQs"]]
list_type.sort()
index = 7
disc = "This page categorizes the literature by the **Research Questions**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 9 backbone model
list_type = [[bm] for bm in fined_taxonomy["Backbone"]]
index = 8
disc = "This page categorizes the literature by the **Backbone Model**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 10 dataset
list_type = [[bm] for bm in fined_taxonomy["Dataset"]]
list_type.sort()
index = 9
disc = "This page categorizes the literature by the **Dataset**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 11 Metric
list_type = [[bm] for bm in fined_taxonomy["Metrics"]]
list_type.sort()
index = 10
disc = "This page categorizes the literature by the **Metrics**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)
"""
# 12 Author
index = 2
disc = "This page categorizes the literature by the **Author**"
plot_content(index=index, keys=["author"], dir_path=dir_path, disc=disc, list_type=None, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 13 Techniques
list_type = [[bm] for bm in fined_taxonomy["Techniques"]]
# list_type.sort()
index = 3
disc = "This page categorizes the literature by the **Techniques**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 14 Venue
list_type = [[venue] for venue in fined_taxonomy["Conference"]]
list_type += fined_taxonomy["Journal"]
list_type.append(fined_taxonomy["Preprint"])
list_type.sort()
index = 4
disc = "This page categorizes the literature by the **Published Venue**"
plot_content(index=index, keys=["booktitle", "journal"], dir_path=dir_path, disc=disc, list_type=list_type,
             sub_dirs=sub_dirs, mapping_name=mapping_name)

class_name_mapper = {
    'git': 'Git Repos',
    'article': 'Articles',
    'blog': 'Blogs',
    'demo': 'Demos',
    'report': 'Reports',
    'lecture': 'Lectures'
}

with open('README.md', 'a+', encoding='utf-8') as f:
    related_works_str = '\n\n## Related Works\n\n'

    related_works = json.load(open('related_works.json', 'r', encoding='utf-8'))
    tmp_dct = {}
    for work in related_works:
        if work['class'] not in tmp_dct.keys():
            tmp_dct[work['class']] = []
        tmp_dct[work['class']].append(work)

    for cl in tmp_dct.keys():
        related_works_str += f'### {class_name_mapper[cl]}\n\n'
        for work in tmp_dct[cl]:
            title = work['title']
            url = work['url']

            work_str = f'- [**{title.strip()}**]({url}),'
            if 'author' in work.keys():
                author = work['author']
                work_str += f'<br>by {author}'
            if 'desc' in work.keys():
                desc = work['desc']
                work_str += f'<br> ```{desc.strip()}```'
            work_str += '\n\n'
            related_works_str += work_str

    f.write(related_works_str)

with open('README.md', 'a+', encoding='utf-8') as f:
    related_works_str = '\n\n## Related Works\n\n'

    related_works = json.load(open('related_works.json', 'r', encoding='utf-8'))
    tmp_dct = {}
    for work in related_works:
        if work['class'] not in tmp_dct.keys():
            tmp_dct[work['class']] = []
        tmp_dct[work['class']].append(work)

    for cl in tmp_dct.keys():
        related_works_str += f'### {class_name_mapper[cl]}\n\n'
        for work in tmp_dct[cl]:
            title = work['title']
            url = work['url']

            work_str = f'- [**{title.strip()}**]({url}),'
            if 'author' in work.keys():
                author = work['author']
                work_str += f'<br>by {author}'
            if 'desc' in work.keys():
                desc = work['desc']
                work_str += f'<br> ```{desc.strip()}```'
            work_str += '\n\n'
            related_works_str += work_str

    f.write(related_works_str)

with open('README.md', 'a+', encoding='utf-8') as f:
    advertise_str = '\n\n## <img src="https://avatars.githubusercontent.com/u/77821103?s=400&u=17b0ffcd148c697c9f604d8ed4241ffa8fb62257&v=4" alt="img" style="zoom:25%; vertical-align: middle" /> Researcher Recruitment 科研人员招聘\n'

    advertise_str += '*Knowledge Science and Engineering Lab* is recruiting researchers! You are welcome to apply for the following positions:\n'
    advertise_str += '- **Research Assistant**: Bachelor degree or above, proficient in Python/Java, familiar with machine learning espicially deep learning models.\n'
    advertise_str += '- **Postdoctoral Fellow**: Doctoral research in Artificial Intelligence, published at least 3 high-quality papers. \n'
    advertise_str += '- **Lecturer, Associate Professor and Professor** \n\n'
    advertise_str += 'If you are interested in our research and meet the above requirements, feel free to contact Prof. [Guilin Qi](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm).\n\n'

    advertise_str += '*知识科学与工程实验室*正在招聘科研人员！欢迎申请以下岗位：\n'
    advertise_str += '- **科研助理**：本科学历以上，精通Python/Java，熟悉机器学习，特别是深度学习模型。\n'
    advertise_str += '- **博士后**：博士研究人工智能相关方向，发表至少3篇高水平论文。\n'
    advertise_str += '- **讲师、副教授、教授等教职** \n\n'
    advertise_str += '如果您对我们的研究工作感兴趣并满足以上要求，欢迎您与[漆桂林](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm)教授联系。\n'


    f.write(advertise_str)
