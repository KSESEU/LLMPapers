# Resources on ChatGPT and Large Language Models
Collection of  papers and related works for Large Language Models (ChatGPT, GPT-3, Codex etc.).
## Contributors
This repository is contributed by the following contributors.
- **Organizers**: [Guilin Qi (漆桂林)](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm), [Xiaofang Qi (戚晓芳)](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm)
- **Paper Collectors**: Zafar Ali, [Sheng Bi (毕胜)](https://github.com/bisheng), [Yongrui Chen (陈永锐)](https://github.com/Bahuia), Zizhuo Chen (陈孜卓), [Xinbang Dai (戴鑫邦)](https://github.com/OBriennnnn), Huan Gao (高桓), [Nan Hu (胡楠)](https://github.com/HuuuNan), Shilong Hu (胡世龙), [Jingqi Kang (康婧淇)](https://github.com/JingqiKang), [Jiaqi Li (李嘉琦)](https://github.com/aoluming), [Dehai Min (闵德海)](https://github.com/ZhishanQ), [Guilin Qi (漆桂林)](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm), Yiming Tan (谭亦鸣), [Tongtong Wu (吴桐桐)](http://wutong8023.site/), [Songlin Zhai (翟松林)](https://github.com/SonglinZhai), [Shenyu Zhang (张沈昱)](https://github.com/ZSY-SZ), [Yuxin Zhang (张裕欣)](https://github.com/Zzyx1996)
- **Maintainers**: [Runzhe Wang (王润哲)](https://github.com/sid0527), [Shenyu Zhang (张沈昱)](https://github.com/ZSY-SZ) 

The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git). If you'd like to commit to this repo, please modify [bibtex.bib](https://github.com/KSESEU/LLMPapers/blob/main/bibtex.bib) or [related_works.json](https://github.com/KSESEU/LLMPapers/blob/main/related_works.json) and re-generate [README.md](https://github.com/KSESEU/LLMPapers/blob/main/README.md) using `python scripts/run.py`.

This page categorizes the literature by the **Author**

## Papers

### Outline 
- [<img src=https://img.shields.io/badge/Luke_Zettlemoyer-15-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luke-zettlemoyer)
- [<img src=https://img.shields.io/badge/Yejin_Choi-14-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yejin-choi)
- [<img src=https://img.shields.io/badge/Ji_Rong_Wen-11-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ji-rong-wen)
- [<img src=https://img.shields.io/badge/Nan_Duan-10-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nan-duan)
- [<img src=https://img.shields.io/badge/Wayne_Xin_Zhao-10-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wayne-xin-zhao)
- [<img src=https://img.shields.io/badge/Jianfeng_Gao-10-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jianfeng-gao)
- [<img src=https://img.shields.io/badge/Dario_Amodei-9-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dario-amodei)
- [<img src=https://img.shields.io/badge/Hannaneh_Hajishirzi-9-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hannaneh-hajishirzi)
- [<img src=https://img.shields.io/badge/Mike_Lewis-9-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mike-lewis)
- [<img src=https://img.shields.io/badge/Xiang_Ren-8-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-ren)
- [<img src=https://img.shields.io/badge/Denny_Zhou-8-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#denny-zhou)
- [<img src=https://img.shields.io/badge/Xuezhi_Wang-8-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xuezhi-wang)
- [<img src=https://img.shields.io/badge/Ed_H._Chi-8-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ed-h.-chi)
- [<img src=https://img.shields.io/badge/Jason_Wei-8-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jason-wei)
- [<img src=https://img.shields.io/badge/Sean_Welleck-7-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sean-welleck)
- [<img src=https://img.shields.io/badge/Ming_Zhou-7-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-zhou)
- [<img src=https://img.shields.io/badge/Percy_Liang-7-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#percy-liang)
- [<img src=https://img.shields.io/badge/Noah_A._Smith-7-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noah-a.-smith)
- [<img src=https://img.shields.io/badge/Ximing_Lu-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ximing-lu)
- [<img src=https://img.shields.io/badge/Ronan_Le_Bras-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ronan-le-bras)
- [<img src=https://img.shields.io/badge/Dawn_Drain-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dawn-drain)
- [<img src=https://img.shields.io/badge/Michel_Galley-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michel-galley)
- [<img src=https://img.shields.io/badge/Junyi_Li-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#junyi-li)
- [<img src=https://img.shields.io/badge/Fei_Huang-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fei-huang)
- [<img src=https://img.shields.io/badge/Furu_Wei-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#furu-wei)
- [<img src=https://img.shields.io/badge/Alec_Radford-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alec-radford)
- [<img src=https://img.shields.io/badge/Christopher_D._Manning-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#christopher-d.-manning)
- [<img src=https://img.shields.io/badge/Michihiro_Yasunaga-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michihiro-yasunaga)
- [<img src=https://img.shields.io/badge/Sewon_Min-6-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sewon-min)
- [<img src=https://img.shields.io/badge/Paul_F._Christiano-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#paul-f.-christiano)
- [<img src=https://img.shields.io/badge/Peter_West-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-west)
- [<img src=https://img.shields.io/badge/Jun_Zhao-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jun-zhao)
- [<img src=https://img.shields.io/badge/Minjoon_Seo-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minjoon-seo)
- [<img src=https://img.shields.io/badge/Dustin_Tran-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dustin-tran)
- [<img src=https://img.shields.io/badge/Chandra_Bhagavatula-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chandra-bhagavatula)
- [<img src=https://img.shields.io/badge/Lingpeng_Kong-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lingpeng-kong)
- [<img src=https://img.shields.io/badge/Pengcheng_He-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengcheng-he)
- [<img src=https://img.shields.io/badge/Neel_Sundaresan-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neel-sundaresan)
- [<img src=https://img.shields.io/badge/Shuohang_Wang-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuohang-wang)
- [<img src=https://img.shields.io/badge/Chenguang_Zhu-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chenguang-zhu)
- [<img src=https://img.shields.io/badge/Weizhu_Chen-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weizhu-chen)
- [<img src=https://img.shields.io/badge/Naman_Goyal-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#naman-goyal)
- [<img src=https://img.shields.io/badge/Asli_Celikyilmaz-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#asli-celikyilmaz)
- [<img src=https://img.shields.io/badge/Sebastian_Riedel-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sebastian-riedel)
- [<img src=https://img.shields.io/badge/Swaroop_Mishra-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#swaroop-mishra)
- [<img src=https://img.shields.io/badge/Yi_Tay-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yi-tay)
- [<img src=https://img.shields.io/badge/Adam_Roberts-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#adam-roberts)
- [<img src=https://img.shields.io/badge/Quoc_V._Le-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#quoc-v.-le)
- [<img src=https://img.shields.io/badge/Maarten_Bosma-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maarten-bosma)
- [<img src=https://img.shields.io/badge/Zhiyong_Wu-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhiyong-wu)
- [<img src=https://img.shields.io/badge/Amanda_Askell-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amanda-askell)
- [<img src=https://img.shields.io/badge/Sam_McCandlish-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sam-mccandlish)
- [<img src=https://img.shields.io/badge/Jared_Kaplan-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jared-kaplan)
- [<img src=https://img.shields.io/badge/Pascale_Fung-5-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pascale-fung)
- [<img src=https://img.shields.io/badge/Long_Ouyang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#long-ouyang)
- [<img src=https://img.shields.io/badge/Geoffrey_Irving-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#geoffrey-irving)
- [<img src=https://img.shields.io/badge/Le_Sun-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#le-sun)
- [<img src=https://img.shields.io/badge/Xianpei_Han-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xianpei-han)
- [<img src=https://img.shields.io/badge/Hongyu_Lin-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongyu-lin)
- [<img src=https://img.shields.io/badge/Kang_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kang-liu)
- [<img src=https://img.shields.io/badge/Seonghyeon_Ye-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#seonghyeon-ye)
- [<img src=https://img.shields.io/badge/Bing_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bing-liu)
- [<img src=https://img.shields.io/badge/Myle_Ott-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#myle-ott)
- [<img src=https://img.shields.io/badge/Lidong_Bing-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lidong-bing)
- [<img src=https://img.shields.io/badge/Chitta_Baral-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chitta-baral)
- [<img src=https://img.shields.io/badge/Kun_Zhou-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kun-zhou)
- [<img src=https://img.shields.io/badge/Mohit_Bansal-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mohit-bansal)
- [<img src=https://img.shields.io/badge/David_Lo-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-lo)
- [<img src=https://img.shields.io/badge/Kai_Wei_Chang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kai-wei-chang)
- [<img src=https://img.shields.io/badge/Shengyu_Fu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shengyu-fu)
- [<img src=https://img.shields.io/badge/Alexey_Svyatkovskiy-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alexey-svyatkovskiy)
- [<img src=https://img.shields.io/badge/Daya_Guo-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daya-guo)
- [<img src=https://img.shields.io/badge/Shuai_Lu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuai-lu)
- [<img src=https://img.shields.io/badge/Shafiq_R._Joty-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shafiq-r.-joty)
- [<img src=https://img.shields.io/badge/Yue_Wang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-wang)
- [<img src=https://img.shields.io/badge/Bill_Dolan-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bill-dolan)
- [<img src=https://img.shields.io/badge/Jian_Yun_Nie-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-yun-nie)
- [<img src=https://img.shields.io/badge/Michael_Zeng-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-zeng)
- [<img src=https://img.shields.io/badge/Baolin_Peng-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#baolin-peng)
- [<img src=https://img.shields.io/badge/Daxin_Jiang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daxin-jiang)
- [<img src=https://img.shields.io/badge/Tianyi_Tang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianyi-tang)
- [<img src=https://img.shields.io/badge/Minlie_Huang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minlie-huang)
- [<img src=https://img.shields.io/badge/Zhou_Yu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhou-yu)
- [<img src=https://img.shields.io/badge/Ting_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ting-liu)
- [<img src=https://img.shields.io/badge/Iryna_Gurevych-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#iryna-gurevych)
- [<img src=https://img.shields.io/badge/Andrea_Madotto-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#andrea-madotto)
- [<img src=https://img.shields.io/badge/Li_Dong-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#li-dong)
- [<img src=https://img.shields.io/badge/Jingjing_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jingjing-liu)
- [<img src=https://img.shields.io/badge/Zhe_Gan-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhe-gan)
- [<img src=https://img.shields.io/badge/William_Yang_Wang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-yang-wang)
- [<img src=https://img.shields.io/badge/Wenhu_Chen-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wenhu-chen)
- [<img src=https://img.shields.io/badge/Huajun_Chen-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#huajun-chen)
- [<img src=https://img.shields.io/badge/Ningyu_Zhang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ningyu-zhang)
- [<img src=https://img.shields.io/badge/Maosong_Sun-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maosong-sun)
- [<img src=https://img.shields.io/badge/Zhiyuan_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhiyuan-liu)
- [<img src=https://img.shields.io/badge/Yang_Liu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yang-liu)
- [<img src=https://img.shields.io/badge/Fabio_Petroni-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fabio-petroni)
- [<img src=https://img.shields.io/badge/Eric_Wallace-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-wallace)
- [<img src=https://img.shields.io/badge/Dale_Schuurmans-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dale-schuurmans)
- [<img src=https://img.shields.io/badge/Hao_Peng-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-peng)
- [<img src=https://img.shields.io/badge/Shixiang_Shane_Gu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shixiang-shane-gu)
- [<img src=https://img.shields.io/badge/Veselin_Stoyanov-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#veselin-stoyanov)
- [<img src=https://img.shields.io/badge/Ramakanth_Pasunuru-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ramakanth-pasunuru)
- [<img src=https://img.shields.io/badge/Lei_Li-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lei-li)
- [<img src=https://img.shields.io/badge/Jack_Clark-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jack-clark)
- [<img src=https://img.shields.io/badge/Daniel_M._Ziegler-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daniel-m.-ziegler)
- [<img src=https://img.shields.io/badge/Tom_Henighan-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-henighan)
- [<img src=https://img.shields.io/badge/Tom_B._Brown-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-b.-brown)
- [<img src=https://img.shields.io/badge/Jeffrey_Wu-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jeffrey-wu)
- [<img src=https://img.shields.io/badge/Noam_Shazeer-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noam-shazeer)
- [<img src=https://img.shields.io/badge/Ilya_Sutskever-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ilya-sutskever)
- [<img src=https://img.shields.io/badge/Jan_Leike-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jan-leike)
- [<img src=https://img.shields.io/badge/Jie_Tang-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jie-tang)
- [<img src=https://img.shields.io/badge/Nicholas_Joseph-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nicholas-joseph)
- [<img src=https://img.shields.io/badge/Weijia_Shi-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weijia-shi)
- [<img src=https://img.shields.io/badge/Antoine_Bosselut-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#antoine-bosselut)
- [<img src=https://img.shields.io/badge/Graham_Neubig-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#graham-neubig)
- [<img src=https://img.shields.io/badge/Uri_Alon-4-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#uri-alon)
- [<img src=https://img.shields.io/badge/Jiacheng_Ye-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiacheng-ye)
- [<img src=https://img.shields.io/badge/Ryan_Lowe-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ryan-lowe)
- [<img src=https://img.shields.io/badge/John_Schulman-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#john-schulman)
- [<img src=https://img.shields.io/badge/Jeff_Wu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jeff-wu)
- [<img src=https://img.shields.io/badge/Jacob_Hilton-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jacob-hilton)
- [<img src=https://img.shields.io/badge/Nisan_Stiennon-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nisan-stiennon)
- [<img src=https://img.shields.io/badge/Yufei_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yufei-wang)
- [<img src=https://img.shields.io/badge/Jena_D._Hwang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jena-d.-hwang)
- [<img src=https://img.shields.io/badge/Jack_Hessel-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jack-hessel)
- [<img src=https://img.shields.io/badge/Wen_tau_Yih-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wen-tau-yih)
- [<img src=https://img.shields.io/badge/Boxi_Cao-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#boxi-cao)
- [<img src=https://img.shields.io/badge/Susannah_Young-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#susannah-young)
- [<img src=https://img.shields.io/badge/Colin_Raffel-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#colin-raffel)
- [<img src=https://img.shields.io/badge/Mona_T._Diab-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mona-t.-diab)
- [<img src=https://img.shields.io/badge/Shizhu_He-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shizhu-he)
- [<img src=https://img.shields.io/badge/Sohee_Yang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sohee-yang)
- [<img src=https://img.shields.io/badge/Joel_Jang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#joel-jang)
- [<img src=https://img.shields.io/badge/Bill_Yuchen_Lin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bill-yuchen-lin)
- [<img src=https://img.shields.io/badge/Zixuan_Ke-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zixuan-ke)
- [<img src=https://img.shields.io/badge/Zac_Hatfield_Dodds-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zac-hatfield-dodds)
- [<img src=https://img.shields.io/badge/Yuntao_Bai-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yuntao-bai)
- [<img src=https://img.shields.io/badge/Tristan_Hume-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tristan-hume)
- [<img src=https://img.shields.io/badge/Sheer_El_Showk-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sheer-el-showk)
- [<img src=https://img.shields.io/badge/Shauna_Kravec-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shauna-kravec)
- [<img src=https://img.shields.io/badge/Scott_Johnston-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#scott-johnston)
- [<img src=https://img.shields.io/badge/Saurav_Kadavath-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#saurav-kadavath)
- [<img src=https://img.shields.io/badge/Nova_DasSarma-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nova-dassarma)
- [<img src=https://img.shields.io/badge/Nelson_Elhage-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nelson-elhage)
- [<img src=https://img.shields.io/badge/Liane_Lovitt-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#liane-lovitt)
- [<img src=https://img.shields.io/badge/Kamal_Ndousse-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kamal-ndousse)
- [<img src=https://img.shields.io/badge/Jackson_Kernion-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jackson-kernion)
- [<img src=https://img.shields.io/badge/Ethan_Perez-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ethan-perez)
- [<img src=https://img.shields.io/badge/Danny_Hernandez-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#danny-hernandez)
- [<img src=https://img.shields.io/badge/Catherine_Olsson-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#catherine-olsson)
- [<img src=https://img.shields.io/badge/Anna_Chen-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#anna-chen)
- [<img src=https://img.shields.io/badge/Deep_Ganguli-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#deep-ganguli)
- [<img src=https://img.shields.io/badge/Linlin_Liu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linlin-liu)
- [<img src=https://img.shields.io/badge/Balaji_Lakshminarayanan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#balaji-lakshminarayanan)
- [<img src=https://img.shields.io/badge/Neil_Houlsby-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neil-houlsby)
- [<img src=https://img.shields.io/badge/Hao_Sun-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-sun)
- [<img src=https://img.shields.io/badge/Yoon_Kim-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yoon-kim)
- [<img src=https://img.shields.io/badge/Chuanqi_Tan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chuanqi-tan)
- [<img src=https://img.shields.io/badge/Tong_Zhang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tong-zhang)
- [<img src=https://img.shields.io/badge/Shizhe_Diao-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shizhe-diao)
- [<img src=https://img.shields.io/badge/Pan_Lu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pan-lu)
- [<img src=https://img.shields.io/badge/Guilin_Qi-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#guilin-qi)
- [<img src=https://img.shields.io/badge/Muhao_Chen-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#muhao-chen)
- [<img src=https://img.shields.io/badge/Thien_Huu_Nguyen-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#thien-huu-nguyen)
- [<img src=https://img.shields.io/badge/Shijin_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shijin-wang)
- [<img src=https://img.shields.io/badge/David_Dohan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-dohan)
- [<img src=https://img.shields.io/badge/Chengwei_Qin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chengwei-qin)
- [<img src=https://img.shields.io/badge/Janghoon_Han-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#janghoon-han)
- [<img src=https://img.shields.io/badge/Zhou_Yang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhou-yang)
- [<img src=https://img.shields.io/badge/Li_Li-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#li-li)
- [<img src=https://img.shields.io/badge/Shao_Kun_Deng-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shao-kun-deng)
- [<img src=https://img.shields.io/badge/Duyu_Tang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#duyu-tang)
- [<img src=https://img.shields.io/badge/Colin_B._Clement-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#colin-b.-clement)
- [<img src=https://img.shields.io/badge/Steven_C._H._Hoi-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#steven-c.-h.-hoi)
- [<img src=https://img.shields.io/badge/Hang_Xu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hang-xu)
- [<img src=https://img.shields.io/badge/Hai_Jin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hai-jin)
- [<img src=https://img.shields.io/badge/Yao_Wan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-wan)
- [<img src=https://img.shields.io/badge/Dejing_Dou-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dejing-dou)
- [<img src=https://img.shields.io/badge/Oriol_Vinyals-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#oriol-vinyals)
- [<img src=https://img.shields.io/badge/Chris_Brockett-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chris-brockett)
- [<img src=https://img.shields.io/badge/Yizhe_Zhang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yizhe-zhang)
- [<img src=https://img.shields.io/badge/Bryan_Catanzaro-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bryan-catanzaro)
- [<img src=https://img.shields.io/badge/Anima_Anandkumar-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#anima-anandkumar)
- [<img src=https://img.shields.io/badge/Mohammad_Shoeybi-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mohammad-shoeybi)
- [<img src=https://img.shields.io/badge/Chunyuan_Li-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chunyuan-li)
- [<img src=https://img.shields.io/badge/Julian_J._McAuley-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#julian-j.-mcauley)
- [<img src=https://img.shields.io/badge/Songfang_Huang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#songfang-huang)
- [<img src=https://img.shields.io/badge/Wei_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wei-wang)
- [<img src=https://img.shields.io/badge/Nicholas_Jing_Yuan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nicholas-jing-yuan)
- [<img src=https://img.shields.io/badge/Zhicheng_Wei-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhicheng-wei)
- [<img src=https://img.shields.io/badge/Marjan_Ghazvininejad-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#marjan-ghazvininejad)
- [<img src=https://img.shields.io/badge/Caiming_Xiong-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#caiming-xiong)
- [<img src=https://img.shields.io/badge/Yu_Sun-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-sun)
- [<img src=https://img.shields.io/badge/Xiaoyan_Zhu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaoyan-zhu)
- [<img src=https://img.shields.io/badge/Yue_Zhang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-zhang)
- [<img src=https://img.shields.io/badge/Leonardo_F._R._Ribeiro-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#leonardo-f.-r.-ribeiro)
- [<img src=https://img.shields.io/badge/Xiao_Liu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiao-liu)
- [<img src=https://img.shields.io/badge/Wenhui_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wenhui-wang)
- [<img src=https://img.shields.io/badge/Yen_Chun_Chen-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yen-chun-chen)
- [<img src=https://img.shields.io/badge/Haifeng_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#haifeng-wang)
- [<img src=https://img.shields.io/badge/Hua_Wu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hua-wu)
- [<img src=https://img.shields.io/badge/Yasheng_Wang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yasheng-wang)
- [<img src=https://img.shields.io/badge/Xisen_Jin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xisen-jin)
- [<img src=https://img.shields.io/badge/Mikel_Artetxe-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mikel-artetxe)
- [<img src=https://img.shields.io/badge/Ari_Holtzman-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ari-holtzman)
- [<img src=https://img.shields.io/badge/Shengding_Hu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shengding-hu)
- [<img src=https://img.shields.io/badge/Ning_Ding-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ning-ding)
- [<img src=https://img.shields.io/badge/Jie_Zhou-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jie-zhou)
- [<img src=https://img.shields.io/badge/Yankai_Lin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yankai-lin)
- [<img src=https://img.shields.io/badge/Yujia_Qin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yujia-qin)
- [<img src=https://img.shields.io/badge/Noah_Constant-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noah-constant)
- [<img src=https://img.shields.io/badge/Hila_Gonen-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hila-gonen)
- [<img src=https://img.shields.io/badge/Kang_Min_Yoo-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kang-min-yoo)
- [<img src=https://img.shields.io/badge/Tushar_Khot-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tushar-khot)
- [<img src=https://img.shields.io/badge/Ashish_Sabharwal-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ashish-sabharwal)
- [<img src=https://img.shields.io/badge/Yao_Fu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-fu)
- [<img src=https://img.shields.io/badge/Huan_Sun-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#huan-sun)
- [<img src=https://img.shields.io/badge/Daniel_Khashabi-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daniel-khashabi)
- [<img src=https://img.shields.io/badge/Omer_Levy-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#omer-levy)
- [<img src=https://img.shields.io/badge/Jacob_Devlin-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jacob-devlin)
- [<img src=https://img.shields.io/badge/Jeff_Dean-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jeff-dean)
- [<img src=https://img.shields.io/badge/Sharan_Narang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sharan-narang)
- [<img src=https://img.shields.io/badge/Aakanksha_Chowdhery-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aakanksha-chowdhery)
- [<img src=https://img.shields.io/badge/Mostafa_Dehghani-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mostafa-dehghani)
- [<img src=https://img.shields.io/badge/Barret_Zoph-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#barret-zoph)
- [<img src=https://img.shields.io/badge/Le_Hou-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#le-hou)
- [<img src=https://img.shields.io/badge/Quoc_Le-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#quoc-le)
- [<img src=https://img.shields.io/badge/Andrew_M._Dai-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#andrew-m.-dai)
- [<img src=https://img.shields.io/badge/Brian_Lester-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#brian-lester)
- [<img src=https://img.shields.io/badge/Todor_Mihaylov-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#todor-mihaylov)
- [<img src=https://img.shields.io/badge/Jingfei_Du-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jingfei-du)
- [<img src=https://img.shields.io/badge/Zhifang_Sui-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhifang-sui)
- [<img src=https://img.shields.io/badge/Damai_Dai-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#damai-dai)
- [<img src=https://img.shields.io/badge/Rewon_Child-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rewon-child)
- [<img src=https://img.shields.io/badge/others-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#others)
- [<img src=https://img.shields.io/badge/Gholamreza_Haffari-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gholamreza-haffari)
- [<img src=https://img.shields.io/badge/Vedant_Misra-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vedant-misra)
- [<img src=https://img.shields.io/badge/Christopher_Hesse-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#christopher-hesse)
- [<img src=https://img.shields.io/badge/Gretchen_Krueger-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gretchen-krueger)
- [<img src=https://img.shields.io/badge/Dan_Roth-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dan-roth)
- [<img src=https://img.shields.io/badge/Aston_Zhang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aston-zhang)
- [<img src=https://img.shields.io/badge/Zhuosheng_Zhang-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhuosheng-zhang)
- [<img src=https://img.shields.io/badge/Jonathan_Berant-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jonathan-berant)
- [<img src=https://img.shields.io/badge/Nayeon_Lee-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nayeon-lee)
- [<img src=https://img.shields.io/badge/Jure_Leskovec-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jure-leskovec)
- [<img src=https://img.shields.io/badge/Hongyu_Ren-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongyu-ren)
- [<img src=https://img.shields.io/badge/Greg_Durrett-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#greg-durrett)
- [<img src=https://img.shields.io/badge/Shuyan_Zhou-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuyan-zhou)
- [<img src=https://img.shields.io/badge/Aman_Madaan-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aman-madaan)
- [<img src=https://img.shields.io/badge/Mari_Ostendorf-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mari-ostendorf)
- [<img src=https://img.shields.io/badge/Tao_Yu-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tao-yu)
- [<img src=https://img.shields.io/badge/Heng_Ji-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#heng-ji)
- [<img src=https://img.shields.io/badge/George_Karypis-3-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#george-karypis)
- [<img src=https://img.shields.io/badge/Peiyu_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peiyu-liu)
- [<img src=https://img.shields.io/badge/Junjie_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#junjie-zhang)
- [<img src=https://img.shields.io/badge/Yupeng_Hou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yupeng-hou)
- [<img src=https://img.shields.io/badge/Jiawei_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiawei-zhang)
- [<img src=https://img.shields.io/badge/Jiahui_Gao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiahui-gao)
- [<img src=https://img.shields.io/badge/Peter_Hase-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-hase)
- [<img src=https://img.shields.io/badge/Xipeng_Qiu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xipeng-qiu)
- [<img src=https://img.shields.io/badge/Dorsa_Sadigh-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dorsa-sadigh)
- [<img src=https://img.shields.io/badge/Erdem_Biyik-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#erdem-biyik)
- [<img src=https://img.shields.io/badge/Craig_Boutilier-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#craig-boutilier)
- [<img src=https://img.shields.io/badge/Moonkyung_Ryu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#moonkyung-ryu)
- [<img src=https://img.shields.io/badge/Nat_McAleese-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nat-mcaleese)
- [<img src=https://img.shields.io/badge/Lucy_Campbell_Gillingham-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lucy-campbell-gillingham)
- [<img src=https://img.shields.io/badge/Martin_Chadwick-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#martin-chadwick)
- [<img src=https://img.shields.io/badge/John_Aslanides-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#john-aslanides)
- [<img src=https://img.shields.io/badge/Maja_Trebacz-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maja-trebacz)
- [<img src=https://img.shields.io/badge/Xu_Jiang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xu-jiang)
- [<img src=https://img.shields.io/badge/Wangchunshu_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wangchunshu-zhou)
- [<img src=https://img.shields.io/badge/Hritik_Bansal-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hritik-bansal)
- [<img src=https://img.shields.io/badge/Seyeon_Lee-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#seyeon-lee)
- [<img src=https://img.shields.io/badge/Pei_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pei-zhou)
- [<img src=https://img.shields.io/badge/Prithviraj_Ammanabrolu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#prithviraj-ammanabrolu)
- [<img src=https://img.shields.io/badge/Keisuke_Sakaguchi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#keisuke-sakaguchi)
- [<img src=https://img.shields.io/badge/Liwei_Jiang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#liwei-jiang)
- [<img src=https://img.shields.io/badge/Jiacheng_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiacheng-liu)
- [<img src=https://img.shields.io/badge/OpenAI-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#openai)
- [<img src=https://img.shields.io/badge/Nazneen_Rajani-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nazneen-rajani)
- [<img src=https://img.shields.io/badge/Prafulla_Kumar_Choubey-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#prafulla-kumar-choubey)
- [<img src=https://img.shields.io/badge/Chenfei_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chenfei-wu)
- [<img src=https://img.shields.io/badge/Jacob_Menick-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jacob-menick)
- [<img src=https://img.shields.io/badge/Wei_Ping-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wei-ping)
- [<img src=https://img.shields.io/badge/Edouard_Grave-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#edouard-grave)
- [<img src=https://img.shields.io/badge/Timo_Schick-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#timo-schick)
- [<img src=https://img.shields.io/badge/Maria_Lomeli-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maria-lomeli)
- [<img src=https://img.shields.io/badge/Rich_James-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rich-james)
- [<img src=https://img.shields.io/badge/Lemao_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lemao-liu)
- [<img src=https://img.shields.io/badge/Chelsea_Finn-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chelsea-finn)
- [<img src=https://img.shields.io/badge/Charles_Lin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#charles-lin)
- [<img src=https://img.shields.io/badge/Eric_Mitchell-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-mitchell)
- [<img src=https://img.shields.io/badge/Kentaro_Inui-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kentaro-inui)
- [<img src=https://img.shields.io/badge/Amnon_Shashua-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amnon-shashua)
- [<img src=https://img.shields.io/badge/Yoav_Levine-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yoav-levine)
- [<img src=https://img.shields.io/badge/Dongyan_Zhao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dongyan-zhao)
- [<img src=https://img.shields.io/badge/Patrick_S._H._Lewis-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#patrick-s.-h.-lewis)
- [<img src=https://img.shields.io/badge/Tim_Rockt{\"{a}}schel-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tim-rockt{\"{a}}schel)
- [<img src=https://img.shields.io/badge/Tuo_Zhao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tuo-zhao)
- [<img src=https://img.shields.io/badge/Chen_Liang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chen-liang)
- [<img src=https://img.shields.io/badge/Qingru_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qingru-zhang)
- [<img src=https://img.shields.io/badge/Simiao_Zuo-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#simiao-zuo)
- [<img src=https://img.shields.io/badge/Jiawei_Han-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiawei-han)
- [<img src=https://img.shields.io/badge/Jiaxin_Huang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiaxin-huang)
- [<img src=https://img.shields.io/badge/Beichen_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#beichen-zhang)
- [<img src=https://img.shields.io/badge/Sebastian_Borgeaud-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sebastian-borgeaud)
- [<img src=https://img.shields.io/badge/Douglas_C._Schmidt-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#douglas-c.-schmidt)
- [<img src=https://img.shields.io/badge/Jesse_Spencer_Smith-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jesse-spencer-smith)
- [<img src=https://img.shields.io/badge/Sam_Hays-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sam-hays)
- [<img src=https://img.shields.io/badge/Quchen_Fu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#quchen-fu)
- [<img src=https://img.shields.io/badge/Jules_White-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jules-white)
- [<img src=https://img.shields.io/badge/Chris_Olah-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chris-olah)
- [<img src=https://img.shields.io/badge/Tom_Conerly-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-conerly)
- [<img src=https://img.shields.io/badge/Stanislav_Fort-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#stanislav-fort)
- [<img src=https://img.shields.io/badge/Andy_Jones-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#andy-jones)
- [<img src=https://img.shields.io/badge/Punit_Singh_Koura-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#punit-singh-koura)
- [<img src=https://img.shields.io/badge/Shuohui_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuohui-chen)
- [<img src=https://img.shields.io/badge/Xian_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xian-li)
- [<img src=https://img.shields.io/badge/Xi_Victoria_Lin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xi-victoria-lin)
- [<img src=https://img.shields.io/badge/Sam_Shleifer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sam-shleifer)
- [<img src=https://img.shields.io/badge/Dani_Yogatama-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dani-yogatama)
- [<img src=https://img.shields.io/badge/Cyprien_de_Masson_d'Autume-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#cyprien-de-masson-d'autume)
- [<img src=https://img.shields.io/badge/Yubo_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yubo-chen)
- [<img src=https://img.shields.io/badge/Liying_Cheng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#liying-cheng)
- [<img src=https://img.shields.io/badge/Fan_Yang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fan-yang)
- [<img src=https://img.shields.io/badge/Pengfei_Cao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengfei-cao)
- [<img src=https://img.shields.io/badge/Qingbin_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qingbin-liu)
- [<img src=https://img.shields.io/badge/Joongbo_Shin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#joongbo-shin)
- [<img src=https://img.shields.io/badge/Xuanjing_Huang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xuanjing-huang)
- [<img src=https://img.shields.io/badge/Lei_Shu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lei-shu)
- [<img src=https://img.shields.io/badge/Hu_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hu-xu)
- [<img src=https://img.shields.io/badge/Wanxiang_Che-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wanxiang-che)
- [<img src=https://img.shields.io/badge/Yiming_Cui-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yiming-cui)
- [<img src=https://img.shields.io/badge/Danqi_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#danqi-chen)
- [<img src=https://img.shields.io/badge/Kenton_Lee-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kenton-lee)
- [<img src=https://img.shields.io/badge/Ming_Wei_Chang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-wei-chang)
- [<img src=https://img.shields.io/badge/Tom_Brown-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-brown)
- [<img src=https://img.shields.io/badge/Ben_Mann-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ben-mann)
- [<img src=https://img.shields.io/badge/Sam_Ringer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sam-ringer)
- [<img src=https://img.shields.io/badge/Eli_Tran_Johnson-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eli-tran-johnson)
- [<img src=https://img.shields.io/badge/Nicholas_Schiefer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nicholas-schiefer)
- [<img src=https://img.shields.io/badge/Xingxuan_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xingxuan-li)
- [<img src=https://img.shields.io/badge/Bosheng_Ding-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bosheng-ding)
- [<img src=https://img.shields.io/badge/Yichong_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yichong-xu)
- [<img src=https://img.shields.io/badge/Jasper_Snoek-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jasper-snoek)
- [<img src=https://img.shields.io/badge/Michael_W._Dusenberry-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-w.-dusenberry)
- [<img src=https://img.shields.io/badge/Xiaohua_Zhai-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaohua-zhai)
- [<img src=https://img.shields.io/badge/Mario_Lucic-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mario-lucic)
- [<img src=https://img.shields.io/badge/Joan_Puigcerver-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#joan-puigcerver)
- [<img src=https://img.shields.io/badge/Matthias_Minderer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#matthias-minderer)
- [<img src=https://img.shields.io/badge/Rodolphe_Jenatton-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rodolphe-jenatton)
- [<img src=https://img.shields.io/badge/Basil_Mustafa-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#basil-mustafa)
- [<img src=https://img.shields.io/badge/Josip_Djolonga-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#josip-djolonga)
- [<img src=https://img.shields.io/badge/Qi_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qi-zhang)
- [<img src=https://img.shields.io/badge/Ming_Gao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-gao)
- [<img src=https://img.shields.io/badge/Xiang_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-li)
- [<img src=https://img.shields.io/badge/Qiuhui_Shi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qiuhui-shi)
- [<img src=https://img.shields.io/badge/Minghui_Qiu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minghui-qiu)
- [<img src=https://img.shields.io/badge/Jianing_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jianing-wang)
- [<img src=https://img.shields.io/badge/Shaohan_Huang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shaohan-huang)
- [<img src=https://img.shields.io/badge/Yunzhi_Yao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yunzhi-yao)
- [<img src=https://img.shields.io/badge/Xiaodan_Liang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaodan-liang)
- [<img src=https://img.shields.io/badge/Litu_Ou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#litu-ou)
- [<img src=https://img.shields.io/badge/William_W._Cohen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-w.-cohen)
- [<img src=https://img.shields.io/badge/Xinyi_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xinyi-wang)
- [<img src=https://img.shields.io/badge/Swarnadeep_Saha-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#swarnadeep-saha)
- [<img src=https://img.shields.io/badge/Deepak_Ramachandran-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#deepak-ramachandran)
- [<img src=https://img.shields.io/badge/Xin_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xin-xu)
- [<img src=https://img.shields.io/badge/Haifeng_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#haifeng-chen)
- [<img src=https://img.shields.io/badge/Jian_Pei-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-pei)
- [<img src=https://img.shields.io/badge/Faeze_Brahman-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#faeze-brahman)
- [<img src=https://img.shields.io/badge/Lianhui_Qin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lianhui-qin)
- [<img src=https://img.shields.io/badge/Hanlin_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hanlin-zhang)
- [<img src=https://img.shields.io/badge/Tongtong_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tongtong-wu)
- [<img src=https://img.shields.io/badge/Haoyu_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#haoyu-wang)
- [<img src=https://img.shields.io/badge/Linh_Ngo_Van-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linh-ngo-van)
- [<img src=https://img.shields.io/badge/Hieu_Man-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hieu-man)
- [<img src=https://img.shields.io/badge/Thien_Nguyen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#thien-nguyen)
- [<img src=https://img.shields.io/badge/Franck_Dernoncourt-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#franck-dernoncourt)
- [<img src=https://img.shields.io/badge/Bonan_Min-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bonan-min)
- [<img src=https://img.shields.io/badge/Minh_Van_Nguyen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minh-van-nguyen)
- [<img src=https://img.shields.io/badge/Amir_Pouran_Ben_Veyseh-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amir-pouran-ben-veyseh)
- [<img src=https://img.shields.io/badge/Orhan_Firat-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#orhan-firat)
- [<img src=https://img.shields.io/badge/Katherine_Lee-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#katherine-lee)
- [<img src=https://img.shields.io/badge/Aitor_Lewkowycz-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aitor-lewkowycz)
- [<img src=https://img.shields.io/badge/Xavier_Garcia-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xavier-garcia)
- [<img src=https://img.shields.io/badge/Henryk_Michalewski-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#henryk-michalewski)
- [<img src=https://img.shields.io/badge/Guy_Gur_Ari-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#guy-gur-ari)
- [<img src=https://img.shields.io/badge/Sebastian_Gehrmann-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sebastian-gehrmann)
- [<img src=https://img.shields.io/badge/Jing_Sha-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jing-sha)
- [<img src=https://img.shields.io/badge/Zheng_Gong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zheng-gong)
- [<img src=https://img.shields.io/badge/Nathanael_Sch{\"{a}}rli-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nathanael-sch{\"{a}}rli)
- [<img src=https://img.shields.io/badge/Nathan_Scales-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nathan-scales)
- [<img src=https://img.shields.io/badge/Jiangtao_Feng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiangtao-feng)
- [<img src=https://img.shields.io/badge/Diyi_Yang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#diyi-yang)
- [<img src=https://img.shields.io/badge/Jiaao_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiaao-chen)
- [<img src=https://img.shields.io/badge/Xi_Ye-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xi-ye)
- [<img src=https://img.shields.io/badge/Hongxia_Jin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongxia-jin)
- [<img src=https://img.shields.io/badge/Yilin_Shen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yilin-shen)
- [<img src=https://img.shields.io/badge/Phil_Blunsom-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#phil-blunsom)
- [<img src=https://img.shields.io/badge/Chien_Sheng_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chien-sheng-wu)
- [<img src=https://img.shields.io/badge/Derek_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#derek-chen)
- [<img src=https://img.shields.io/badge/Erik_Cambria-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#erik-cambria)
- [<img src=https://img.shields.io/badge/Jinjie_Ni-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jinjie-ni)
- [<img src=https://img.shields.io/badge/Vlad_Pandelea-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vlad-pandelea)
- [<img src=https://img.shields.io/badge/Tom_Young-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-young)
- [<img src=https://img.shields.io/badge/Zhaojiang_Lin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhaojiang-lin)
- [<img src=https://img.shields.io/badge/Hao_Cheng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-cheng)
- [<img src=https://img.shields.io/badge/Xing_Xie-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xing-xie)
- [<img src=https://img.shields.io/badge/Kevin_Murphy-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kevin-murphy)
- [<img src=https://img.shields.io/badge/Da_Yin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#da-yin)
- [<img src=https://img.shields.io/badge/Liunian_Harold_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#liunian-harold-li)
- [<img src=https://img.shields.io/badge/Luowei_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luowei-zhou)
- [<img src=https://img.shields.io/badge/Linjie_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linjie-li)
- [<img src=https://img.shields.io/badge/Guandong_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#guandong-xu)
- [<img src=https://img.shields.io/badge/Yun_Xiong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yun-xiong)
- [<img src=https://img.shields.io/badge/Yue_Yu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-yu)
- [<img src=https://img.shields.io/badge/Meng_Jiang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#meng-jiang)
- [<img src=https://img.shields.io/badge/Hongyu_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongyu-zhang)
- [<img src=https://img.shields.io/badge/Jieke_Shi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jieke-shi)
- [<img src=https://img.shields.io/badge/Bowen_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bowen-xu)
- [<img src=https://img.shields.io/badge/Xiapu_Luo-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiapu-luo)
- [<img src=https://img.shields.io/badge/Vincent_Ng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vincent-ng)
- [<img src=https://img.shields.io/badge/Hongzhi_Yin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongzhi-yin)
- [<img src=https://img.shields.io/badge/Xin_Jiang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xin-jiang)
- [<img src=https://img.shields.io/badge/Fei_Mi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fei-mi)
- [<img src=https://img.shields.io/badge/Jian_Yin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-yin)
- [<img src=https://img.shields.io/badge/Jin_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jin-liu)
- [<img src=https://img.shields.io/badge/Hao_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-wu)
- [<img src=https://img.shields.io/badge/Pingyi_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pingyi-zhou)
- [<img src=https://img.shields.io/badge/Xin_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xin-wang)
- [<img src=https://img.shields.io/badge/Baishakhi_Ray-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#baishakhi-ray)
- [<img src=https://img.shields.io/badge/Saikat_Chakraborty-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#saikat-chakraborty)
- [<img src=https://img.shields.io/badge/Shujie_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shujie-liu)
- [<img src=https://img.shields.io/badge/Michele_Tufano-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michele-tufano)
- [<img src=https://img.shields.io/badge/Long_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#long-zhou)
- [<img src=https://img.shields.io/badge/Ge_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ge-li)
- [<img src=https://img.shields.io/badge/Shuo_Ren-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuo-ren)
- [<img src=https://img.shields.io/badge/Akhilesh_Deepak_Gotmare-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#akhilesh-deepak-gotmare)
- [<img src=https://img.shields.io/badge/Hung_Le-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hung-le)
- [<img src=https://img.shields.io/badge/Panos_Kalnis-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#panos-kalnis)
- [<img src=https://img.shields.io/badge/Xingjian_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xingjian-li)
- [<img src=https://img.shields.io/badge/Zheng_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zheng-zhang)
- [<img src=https://img.shields.io/badge/Lichao_Sun-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lichao-sun)
- [<img src=https://img.shields.io/badge/Ji_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ji-liu)
- [<img src=https://img.shields.io/badge/Lingjuan_Lyu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lingjuan-lyu)
- [<img src=https://img.shields.io/badge/Kimin_Lee-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kimin-lee)
- [<img src=https://img.shields.io/badge/Michael_Tschannen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-tschannen)
- [<img src=https://img.shields.io/badge/Xiang_Gao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-gao)
- [<img src=https://img.shields.io/badge/Yan_Zeng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yan-zeng)
- [<img src=https://img.shields.io/badge/Wei_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wei-wu)
- [<img src=https://img.shields.io/badge/Mostofa_Patwary-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mostofa-patwary)
- [<img src=https://img.shields.io/badge/Peng_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peng-xu)
- [<img src=https://img.shields.io/badge/Bo_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bo-li)
- [<img src=https://img.shields.io/badge/Eric_P._Xing-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-p.-xing)
- [<img src=https://img.shields.io/badge/Hao_Tian-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-tian)
- [<img src=https://img.shields.io/badge/Dianhai_Yu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dianhai-yu)
- [<img src=https://img.shields.io/badge/Wei_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wei-liu)
- [<img src=https://img.shields.io/badge/Weibao_Gong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weibao-gong)
- [<img src=https://img.shields.io/badge/Shikun_Feng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shikun-feng)
- [<img src=https://img.shields.io/badge/Shuohuan_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuohuan-wang)
- [<img src=https://img.shields.io/badge/Tie_Yan_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tie-yan-liu)
- [<img src=https://img.shields.io/badge/Tao_Qin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tao-qin)
- [<img src=https://img.shields.io/badge/Xu_Tan-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xu-tan)
- [<img src=https://img.shields.io/badge/Kaitao_Song-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kaitao-song)
- [<img src=https://img.shields.io/badge/Bodhisattwa_Prasad_Majumder-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bodhisattwa-prasad-majumder)
- [<img src=https://img.shields.io/badge/Tianrui_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianrui-li)
- [<img src=https://img.shields.io/badge/Luo_Si-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luo-si)
- [<img src=https://img.shields.io/badge/Yijia_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yijia-liu)
- [<img src=https://img.shields.io/badge/Fuli_Luo-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fuli-luo)
- [<img src=https://img.shields.io/badge/Ruofei_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ruofei-zhang)
- [<img src=https://img.shields.io/badge/Jiusheng_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiusheng-chen)
- [<img src=https://img.shields.io/badge/Pengcheng_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengcheng-wang)
- [<img src=https://img.shields.io/badge/Ming_Gong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-gong)
- [<img src=https://img.shields.io/badge/Linjun_Shou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linjun-shou)
- [<img src=https://img.shields.io/badge/Jie_Fu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jie-fu)
- [<img src=https://img.shields.io/badge/Weizhen_Qi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weizhen-qi)
- [<img src=https://img.shields.io/badge/Yeyun_Gong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yeyun-gong)
- [<img src=https://img.shields.io/badge/Yu_Yan-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-yan)
- [<img src=https://img.shields.io/badge/Piji_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#piji-li)
- [<img src=https://img.shields.io/badge/Zhipeng_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhipeng-chen)
- [<img src=https://img.shields.io/badge/Jinhao_Jiang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jinhao-jiang)
- [<img src=https://img.shields.io/badge/Gaole_He-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gaole-he)
- [<img src=https://img.shields.io/badge/Yinhan_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yinhan-liu)
- [<img src=https://img.shields.io/badge/Mohit_Iyyer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mohit-iyyer)
- [<img src=https://img.shields.io/badge/Richard_Socher-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#richard-socher)
- [<img src=https://img.shields.io/badge/Bryan_McCann-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bryan-mccann)
- [<img src=https://img.shields.io/badge/Pei_Ke-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pei-ke)
- [<img src=https://img.shields.io/badge/Jianzhong_Qi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jianzhong-qi)
- [<img src=https://img.shields.io/badge/Xiaodong_Gu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaodong-gu)
- [<img src=https://img.shields.io/badge/Xiaojiang_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaojiang-liu)
- [<img src=https://img.shields.io/badge/Bing_Qin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bing-qin)
- [<img src=https://img.shields.io/badge/Jiezhong_Qiu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiezhong-qiu)
- [<img src=https://img.shields.io/badge/Xiaodong_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaodong-liu)
- [<img src=https://img.shields.io/badge/Sumanth_Dathathri-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sumanth-dathathri)
- [<img src=https://img.shields.io/badge/Yu_Cheng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-cheng)
- [<img src=https://img.shields.io/badge/Yu_Su-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-su)
- [<img src=https://img.shields.io/badge/Lu_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lu-wang)
- [<img src=https://img.shields.io/badge/Geoffrey_E._Hinton-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#geoffrey-e.-hinton)
- [<img src=https://img.shields.io/badge/Irina_Rish-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#irina-rish)
- [<img src=https://img.shields.io/badge/Hui_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hui-chen)
- [<img src=https://img.shields.io/badge/Xiang_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-chen)
- [<img src=https://img.shields.io/badge/Shumin_Deng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shumin-deng)
- [<img src=https://img.shields.io/badge/Hongbin_Ye-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongbin-ye)
- [<img src=https://img.shields.io/badge/Yadao_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yadao-wang)
- [<img src=https://img.shields.io/badge/Zhen_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhen-zhang)
- [<img src=https://img.shields.io/badge/Hai_Tao_Zheng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hai-tao-zheng)
- [<img src=https://img.shields.io/badge/Weilin_Zhao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weilin-zhao)
- [<img src=https://img.shields.io/badge/Jing_Yi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jing-yi)
- [<img src=https://img.shields.io/badge/Weize_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weize-chen)
- [<img src=https://img.shields.io/badge/Yusheng_Su-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yusheng-su)
- [<img src=https://img.shields.io/badge/Sameer_Singh-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sameer-singh)
- [<img src=https://img.shields.io/badge/Robert_L._Logan_IV-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#robert-l.-logan-iv)
- [<img src=https://img.shields.io/badge/Terra_Blevins-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#terra-blevins)
- [<img src=https://img.shields.io/badge/Yao_Lu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-lu)
- [<img src=https://img.shields.io/badge/Peter_Clark-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-clark)
- [<img src=https://img.shields.io/badge/Xiang_Deng-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-deng)
- [<img src=https://img.shields.io/badge/Boshi_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#boshi-wang)
- [<img src=https://img.shields.io/badge/Alisa_Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alisa-liu)
- [<img src=https://img.shields.io/badge/Samuel_R._Bowman-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#samuel-r.-bowman)
- [<img src=https://img.shields.io/badge/Ravsehaj_Singh_Puri-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ravsehaj-singh-puri)
- [<img src=https://img.shields.io/badge/Mihir_Parmar-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mihir-parmar)
- [<img src=https://img.shields.io/badge/Yeganeh_Kordi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yeganeh-kordi)
- [<img src=https://img.shields.io/badge/Yizhong_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yizhong-wang)
- [<img src=https://img.shields.io/badge/Slav_Petrov-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#slav-petrov)
- [<img src=https://img.shields.io/badge/Hongkun_Yu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongkun-yu)
- [<img src=https://img.shields.io/badge/Gaurav_Mishra-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gaurav-mishra)
- [<img src=https://img.shields.io/badge/Xinyun_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xinyun-chen)
- [<img src=https://img.shields.io/badge/William_Fedus-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-fedus)
- [<img src=https://img.shields.io/badge/Hyung_Won_Chung-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hyung-won-chung)
- [<img src=https://img.shields.io/badge/Ben_Hutchinson-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ben-hutchinson)
- [<img src=https://img.shields.io/badge/Mark_Diaz-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mark-diaz)
- [<img src=https://img.shields.io/badge/Vinodkumar_Prabhakaran-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vinodkumar-prabhakaran)
- [<img src=https://img.shields.io/badge/Toju_Duke-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#toju-duke)
- [<img src=https://img.shields.io/badge/Yanqi_Zhou-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yanqi-zhou)
- [<img src=https://img.shields.io/badge/Yanping_Huang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yanping-huang)
- [<img src=https://img.shields.io/badge/Nan_Du-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nan-du)
- [<img src=https://img.shields.io/badge/Kelvin_Guu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kelvin-guu)
- [<img src=https://img.shields.io/badge/Vincent_Y._Zhao-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vincent-y.-zhao)
- [<img src=https://img.shields.io/badge/Zornitsa_Kozareva-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zornitsa-kozareva)
- [<img src=https://img.shields.io/badge/Srini_Iyer-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#srini-iyer)
- [<img src=https://img.shields.io/badge/Jingjing_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jingjing-xu)
- [<img src=https://img.shields.io/badge/Qingxiu_Dong-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qingxiu-dong)
- [<img src=https://img.shields.io/badge/Benjamin_Chess-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#benjamin-chess)
- [<img src=https://img.shields.io/badge/Sandhini_Agarwal-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sandhini-agarwal)
- [<img src=https://img.shields.io/badge/Benjamin_Mann-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#benjamin-mann)
- [<img src=https://img.shields.io/badge/David_Luan-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-luan)
- [<img src=https://img.shields.io/badge/Ryan_Sepassi-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ryan-sepassi)
- [<img src=https://img.shields.io/badge/Peter_J._Liu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-j.-liu)
- [<img src=https://img.shields.io/badge/Zhuang_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhuang-li)
- [<img src=https://img.shields.io/badge/Peter_Welinder-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-welinder)
- [<img src=https://img.shields.io/badge/Matthew_Knight-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#matthew-knight)
- [<img src=https://img.shields.io/badge/William_Saunders-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-saunders)
- [<img src=https://img.shields.io/badge/Shantanu_Jain-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shantanu-jain)
- [<img src=https://img.shields.io/badge/Suchir_Balaji-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#suchir-balaji)
- [<img src=https://img.shields.io/badge/Ariel_Herbert_Voss-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ariel-herbert-voss)
- [<img src=https://img.shields.io/badge/Clemens_Winter-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#clemens-winter)
- [<img src=https://img.shields.io/badge/Lukasz_Kaiser-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lukasz-kaiser)
- [<img src=https://img.shields.io/badge/Nick_Ryder-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nick-ryder)
- [<img src=https://img.shields.io/badge/Scott_Gray-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#scott-gray)
- [<img src=https://img.shields.io/badge/Pamela_Mishkin-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pamela-mishkin)
- [<img src=https://img.shields.io/badge/Girish_Sastry-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#girish-sastry)
- [<img src=https://img.shields.io/badge/Raul_Puri-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#raul-puri)
- [<img src=https://img.shields.io/badge/Alex_Ray-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alex-ray)
- [<img src=https://img.shields.io/badge/Mark_Chen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mark-chen)
- [<img src=https://img.shields.io/badge/Hongming_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongming-zhang)
- [<img src=https://img.shields.io/badge/Alex_Smola-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alex-smola)
- [<img src=https://img.shields.io/badge/Mu_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mu-li)
- [<img src=https://img.shields.io/badge/Tianyi_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianyi-zhang)
- [<img src=https://img.shields.io/badge/Tatsunori_Hashimoto-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tatsunori-hashimoto)
- [<img src=https://img.shields.io/badge/Sang_Michael_Xie-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sang-michael-xie)
- [<img src=https://img.shields.io/badge/Neel_Guha-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neel-guha)
- [<img src=https://img.shields.io/badge/Mirac_Suzgun-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mirac-suzgun)
- [<img src=https://img.shields.io/badge/Laurel_J._Orr-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#laurel-j.-orr)
- [<img src=https://img.shields.io/badge/Eric_Zelikman-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-zelikman)
- [<img src=https://img.shields.io/badge/Christopher_R{\'{e}}-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#christopher-r{\'{e}})
- [<img src=https://img.shields.io/badge/Benjamin_Newman-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#benjamin-newman)
- [<img src=https://img.shields.io/badge/Yuhuai_Wu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yuhuai-wu)
- [<img src=https://img.shields.io/badge/Rishi_Bommasani-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rishi-bommasani)
- [<img src=https://img.shields.io/badge/Amir_Globerson-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amir-globerson)
- [<img src=https://img.shields.io/badge/Mor_Geva-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mor-geva)
- [<img src=https://img.shields.io/badge/Roi_Cohen-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#roi-cohen)
- [<img src=https://img.shields.io/badge/Yan_Xu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yan-xu)
- [<img src=https://img.shields.io/badge/Tiezheng_Yu-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tiezheng-yu)
- [<img src=https://img.shields.io/badge/Ziwei_Ji-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ziwei-ji)
- [<img src=https://img.shields.io/badge/Dan_Su-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dan-su)
- [<img src=https://img.shields.io/badge/Yejin_Bang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yejin-bang)
- [<img src=https://img.shields.io/badge/Rui_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rui-zhang)
- [<img src=https://img.shields.io/badge/Tianlu_Wang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianlu-wang)
- [<img src=https://img.shields.io/badge/Jungo_Kasai-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jungo-kasai)
- [<img src=https://img.shields.io/badge/Hongjin_Su-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongjin-su)
- [<img src=https://img.shields.io/badge/Xikun_Zhang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xikun-zhang)
- [<img src=https://img.shields.io/badge/Junyi_Jessy_Li-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#junyi-jessy-li)
- [<img src=https://img.shields.io/badge/Albert_Webson-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#albert-webson)
- [<img src=https://img.shields.io/badge/Yiming_Yang-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yiming-yang)
- [<img src=https://img.shields.io/badge/Chia_Hsuan_Lee-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chia-hsuan-lee)
- [<img src=https://img.shields.io/badge/He_He-2-blue style="zoom:100%; vertical-align: middle">](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#he-he)
### Hyperlinks 
- [[Overview]](https://github.com/KSESEU/LLMPapers/blob/main/README.md) -- [Homepage](https://github.com/KSESEU/LLMPapers/blob/main/README.md)
-  -- [Summary](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/./)
-  -- [Author](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author)
-  -- [Techniques](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/techniques)
-  -- [Published Time](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time)
-  -- [Published Venue](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/venue)

### Luke Zettlemoyer

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.367) [**Prompting Language Models for Linguistic Structure**](https://doi.org/10.18653/v1/2023.acl-long.367),<br> by *Terra Blevins, Hila Gonen and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/MetaICL) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>``
MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10539) [**Toward Human Readable Prompt Tuning: Kubrick's The Shining is a good
movie, and a good prompt too?**](https://doi.org/10.48550/arXiv.2212.10539),<br> by *Weijia Shi, Xiaochuang Han, Hila Gonen, Ari Holtzman, Yulia Tsvetkov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL/IJCNLP}
2021,_Online_Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.366) [**Prompting Contrastive Explanations for Commonsense Reasoning Tasks**](https://doi.org/10.18653/v1/2021.findings-acl.366),<br> by *Bhargavi Paranjape, Julian Michael, Marjan Ghazvininejad, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Yejin Choi

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.50) [**Reframing Instructional Prompts to GPTk's Language**](https://doi.org/10.18653/v1/2022.findings-acl.50),<br> by *Daniel Khashabi, Chitta Baral, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.611) [**Rainier: Reinforced Knowledge Introspector for Commonsense Question
Answering**](https://aclanthology.org/2022.emnlp-main.611),<br> by *Jiacheng Liu, Skyler Hallinan, Ximing Lu, Pengfei He, Sean Welleck, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01241) [**Is Reinforcement Learning (Not) for Natural Language Processing?:
Benchmarks, Baselines, and Building Blocks for Natural Language Policy
Optimization**](https://doi.org/10.48550/arXiv.2210.01241),<br> by *Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kiant\'e Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.418) [**Thinking Like a Skeptic: Defeasible Inference in Natural Language**](https://doi.org/10.18653/v1/2020.findings-emnlp.418),<br> by *Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/p19-1472) [**HellaSwag: Can a Machine Really Finish Your Sentence?**](https://doi.org/10.18653/v1/p19-1472), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://rowanzellers.com/hellaswag)<br> by *Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi and Yejin Choi*
<br><br>
### Ji Rong Wen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.11432) [**A Survey on Large Language Model based Autonomous Agents**](https://doi.org/10.48550/arXiv.2308.11432),<br> by *Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL}_2023,
Toronto,_Canada,_July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.findings-acl.46) [**The Web Can Be Your Oyster for Improving Language Models**](https://doi.org/10.18653/v1/2023.findings-acl.46),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jingyuan Wang, Jian-Yun Nie and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.212) [**Small Pre-trained Language Models Can be Fine-tuned as Large Models
via Over-Parameterization**](https://doi.org/10.18653/v1/2023.acl-long.212),<br> by *Ze-Feng Gao, Kun Zhou, Peiyu Liu, Wayne Xin Zhao and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.07001) [**Recommendation as Instruction Following: A Large Language Model
Empowered Recommendation Approach**](https://doi.org/10.48550/arXiv.2305.07001),<br> by *Junjie Zhang, Ruobing Xie, Yupeng Hou, Wayne Xin Zhao, Leyu Lin and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Nan Duan

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.04671) [**Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models**](https://arxiv.org/abs/2303.04671),<br> by *Wu, Chenfei, Yin, Shengming, Qi, Weizhen, Wang, Xiaodong, Tang, Zecheng and Duan, Nan*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.10464) [**Learning to Program with Natural Language**](https://doi.org/10.48550/arXiv.2304.10464),<br> by *Yiduo Guo, Yaobo Liang, Chenfei Wu, Wenshan Wu, Dongyan Zhao and Nan Duan*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>``
We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
``<br>``
and supports the development of versatile
``<br>``
knowledge-infused model.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
### Wayne Xin Zhao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.11432) [**A Survey on Large Language Model based Autonomous Agents**](https://doi.org/10.48550/arXiv.2308.11432),<br> by *Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL}_2023,
Toronto,_Canada,_July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.findings-acl.46) [**The Web Can Be Your Oyster for Improving Language Models**](https://doi.org/10.18653/v1/2023.findings-acl.46),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jingyuan Wang, Jian-Yun Nie and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.212) [**Small Pre-trained Language Models Can be Fine-tuned as Large Models
via Over-Parameterization**](https://doi.org/10.18653/v1/2023.acl-long.212),<br> by *Ze-Feng Gao, Kun Zhou, Peiyu Liu, Wayne Xin Zhao and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.07001) [**Recommendation as Instruction Following: A Large Language Model
Empowered Recommendation Approach**](https://doi.org/10.48550/arXiv.2305.07001),<br> by *Junjie Zhang, Ruobing Xie, Yupeng Hou, Wayne Xin Zhao, Leyu Lin and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Jianfeng Gao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.07094) [**Learning Customized Visual Models with Retrieval-Augmented Knowledge**](https://doi.org/10.48550/arXiv.2301.07094),<br> by *Haotian Liu, Kilho Son, Jianwei Yang, Ce Liu, Jianfeng Gao, Yong Jae Lee and Chunyuan Li*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.03277) [**Instruction Tuning with GPT-4**](https://doi.org/10.48550/arXiv.2304.03277),<br> by *Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [**DeBERTa: Decoding-enhanced BERT with Disentangled Attention**](https://arxiv.org/abs/2006.03654), [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) <br> by *Pengcheng He, Xiaodong Liu, Jianfeng Gao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Dario Amodei

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2017-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html) [**Deep Reinforcement Learning from Human Preferences**](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html),<br> by *Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg and Dario Amodei*
<br><br>
### Hannaneh Hajishirzi

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/MetaICL) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>``
MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.50) [**Reframing Instructional Prompts to GPTk's Language**](https://doi.org/10.18653/v1/2022.findings-acl.50),<br> by *Daniel Khashabi, Chitta Baral, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.611) [**Rainier: Reinforced Knowledge Introspector for Commonsense Question
Answering**](https://aclanthology.org/2022.emnlp-main.611),<br> by *Jiacheng Liu, Skyler Hallinan, Ximing Lu, Pengfei He, Sean Welleck, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01241) [**Is Reinforcement Learning (Not) for Natural Language Processing?:
Benchmarks, Baselines, and Building Blocks for Natural Language Policy
Optimization**](https://doi.org/10.48550/arXiv.2210.01241),<br> by *Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kiant\'e Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL/IJCNLP}
2021,_Online_Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.366) [**Prompting Contrastive Explanations for Commonsense Reasoning Tasks**](https://doi.org/10.18653/v1/2021.findings-acl.366),<br> by *Bhargavi Paranjape, Julian Michael, Marjan Ghazvininejad, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
### Mike Lewis

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/MetaICL) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>``
MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Xiang Ren

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.351) [**Lifelong Pretraining: Continually Adapting Language Models to Emerging
Corpora**](https://doi.org/10.18653/v1/2022.naacl-main.351),<br> by *Xisen Jin, Dejiao Zhang, Henghui Zhu, Wei Xiao, Shang-Wen Li, Xiaokai Wei, Andrew O. Arnold and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.653) [**RobustLR: A Diagnostic Benchmark for Evaluating Logical Robustness
of Deductive Reasoners**](https://aclanthology.org/2022.emnlp-main.653),<br> by *Soumya Sanyal, Zeyi Liao and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.findings-emnlp.62) [**Learn Continually, Generalize Rapidly: Lifelong Knowledge Accumulation for Few-shot Learning**](https://aclanthology.org/2021.findings-emnlp.62),<br> by *Jin, Xisen , Lin, Bill Yuchen , Rostami, Mohammad  and Ren, Xiang*
<br>``
We present a new learning setup, Continual Learning of Few-Shot Learners, to address challenges of both learning settings in a unified setup, with a hyper-network for task-specific adapter generation.
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.322) [**Do Language Models Perform Generalizable Commonsense Inference?**](https://doi.org/10.18653/v1/2021.findings-acl.322), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/wangpf3/LM-for-CommonsenseInference)<br> by *Peifeng Wang, Filip Ilievski, Muhao Chen and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.598) [**RICA: Evaluating Robust Inference Capabilities Based on Commonsense
Axioms**](https://doi.org/10.18653/v1/2021.emnlp-main.598),<br> by *Pei Zhou, Rahul Khanna, Seyeon Lee, Bill Yuchen Lin, Daniel Ho, Jay Pujara and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=3k20LAiHYL2) [**Pre-training Text-to-Text Transformers for Concept-centric Common
Sense**](https://openreview.net/forum?id=3k20LAiHYL2),<br> by *Wangchunshu Zhou, Dong-Ho Lee, Ravi Kiran Selvam, Seyeon Lee and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2020.emnlp-main.158) [**Visually Grounded Continual Learning of Compositional Phrases**](https://www.aclweb.org/anthology/2020.emnlp-main.158),<br> by *Jin, Xisen , Du, Junyi , Sadhu, Arka , Nevatia, Ram  and Ren, Xiang*
<br>``
A novel continual learning setting and a new benchmark for continual caption generation, evaluated with exiting rehearsal-based methods
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
### Denny Zhou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Xuezhi Wang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>``
Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.
``
<br><br>
### Ed H. Chi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Jason Wei

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Sean Welleck

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.611) [**Rainier: Reinforced Knowledge Introspector for Commonsense Question
Answering**](https://aclanthology.org/2022.emnlp-main.611),<br> by *Jiacheng Liu, Skyler Hallinan, Ximing Lu, Pengfei He, Sean Welleck, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Ming Zhou

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>``
We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
``<br>``
and supports the development of versatile
``<br>``
knowledge-infused model.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Percy Liang

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=RdJVFCHjUMI) [**An Explanation of In-context Learning as Implicit Bayesian Inference**](https://openreview.net/forum?id=RdJVFCHjUMI),<br> by *Sang Michael Xie, Aditi Raghunathan, Percy Liang and Tengyu Ma*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.353) [**Prefix-Tuning: Optimizing Continuous Prompts for Generation**](https://doi.org/10.18653/v1/2021.acl-long.353),<br> by *Xiang Lisa Li and Percy Liang*
<br><br>
### Noah A. Smith

- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.418) [**Thinking Like a Skeptic: Defeasible Inference in Natural Language**](https://doi.org/10.18653/v1/2020.findings-emnlp.418),<br> by *Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith and Yejin Choi*
<br><br>
### Ximing Lu

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.611) [**Rainier: Reinforced Knowledge Introspector for Commonsense Question
Answering**](https://aclanthology.org/2022.emnlp-main.611),<br> by *Jiacheng Liu, Skyler Hallinan, Ximing Lu, Pengfei He, Sean Welleck, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Ronan Le Bras

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.418) [**Thinking Like a Skeptic: Defeasible Inference in Natural Language**](https://doi.org/10.18653/v1/2020.findings-emnlp.418),<br> by *Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith and Yejin Choi*
<br><br>
### Dawn Drain

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
### Michel Galley

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.03277) [**Instruction Tuning with GPT-4**](https://doi.org/10.48550/arXiv.2304.03277),<br> by *Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.28) [**Dialogue Response Ranking Training with Large-Scale Human Feedback
Data**](https://doi.org/10.18653/v1/2020.emnlp-main.28),<br> by *Xiang Gao, Yizhe Zhang, Michel Galley, Chris Brockett and Bill Dolan*
<br><br>
### Junyi Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL}_2023,
Toronto,_Canada,_July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.findings-acl.46) [**The Web Can Be Your Oyster for Improving Language Models**](https://doi.org/10.18653/v1/2023.findings-acl.46),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jingyuan Wang, Jian-Yun Nie and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Fei Huang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.13808) [**Large Language Models are Versatile Decomposers: Decompose Evidence
and Questions for Table-based Reasoning**](https://doi.org/10.48550/arXiv.2301.13808),<br> by *Yunhu Ye, Binyuan Hui, Min Yang, Binhua Li, Fei Huang and Yongbin Li*
<br><br>
- [<img src=https://img.shields.io/badge/IJCAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.24963/ijcai.2022/273) [**Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in
the Federated Setting**](https://doi.org/10.24963/ijcai.2022/273),<br> by *Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
- [<img src=https://img.shields.io/badge/TACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Furu Wei

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br>``
(1) 与The Dual Form of Neural Networks Revisited结合一起看，可以进一步理解in-context learning，通过与NN线性层对偶形式的类比，可以将ICL流程描述为：1. 基于Transformer的预训练语言模型作为元优化器；2. 通过正向计算，根据示范例子产生元梯度；3. 通过关注，将元梯度应用于原始语言模型，建立一个ICL模型；
``<br>``
(2)与Fine-tune类似，ICL也是在zero-shot learning参数的基础上，提供了一个更新量。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=SygXPaEYvH) [**VL-BERT: Pre-training of Generic Visual-Linguistic Representations**](https://openreview.net/forum?id=SygXPaEYvH),<br> by *Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu, Furu Wei and Jifeng Dai*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Alec Radford

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), [<img src=https://img.shields.io/badge/GPT--1-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Christopher D. Manning

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=0DcZxeWfOPt) [**Fast Model Editing at Scale**](https://openreview.net/forum?id=0DcZxeWfOPt),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn and Christopher D. Manning*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/mitchell22a.html) [**Memory-Based Model Editing at Scale**](https://proceedings.mlr.press/v162/mitchell22a.html),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning and Chelsea Finn*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=r1xMH1BtvB) [**ELECTRA: Pre-training Text Encoders as Discriminators Rather Than
Generators**](https://openreview.net/forum?id=r1xMH1BtvB), [<img src=https://img.shields.io/badge/ELECTRA-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=r1xMH1BtvB) <br> by *Kevin Clark, Minh-Thang Luong, Quoc V. Le and Christopher D. Manning*
<br><br>
### Michihiro Yasunaga

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
### Sewon Min

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/MetaICL) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>``
MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Paul F. Christiano

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2017-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html) [**Deep Reinforcement Learning from Human Preferences**](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html),<br> by *Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg and Dario Amodei*
<br><br>
### Peter West

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Jun Zhao

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.628) [**CN-AutoMIC: Distilling Chinese Commonsense Knowledge from Pretrained
Language Models**](https://aclanthology.org/2022.emnlp-main.628),<br> by *Chenhao Wang, Jiachun Li, Yubo Chen, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>``
We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2020.emnlp-main.52) [**Incremental Event Detection via Knowledge Consolidation Networks**](https://www.aclweb.org/anthology/2020.emnlp-main.52),<br> by *Cao, Pengfei , Chen, Yubo , Zhao, Jun  and Wang, Taifeng*
<br>``
Proposing a hybrid continual learning method for event detection, combining experience replay and Knowledge Distillation, focusing on (1) semantic ambiguity in NLP and (2) data imbalance between memory and current task.
``
<br><br>
### Minjoon Seo

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.03202) [**Exploring the Benefits of Training Expert Language Models over Instruction Tuning**](https://arxiv.org/abs/2302.03202),<br> by *Joel Jang, Seungone Kim, Seonghyeon Ye, Doyoung Kim, Lajanugen Logeswaran, Moontae Lee, Kyungjae Lee and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.14691) [**In-Context Instruction Learning**](https://doi.org/10.48550/arXiv.2302.14691),<br> by *Seonghyeon Ye, Hyeonbin Hwang, Sohee Yang, Hyeongu Yun, Yireun Kim and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
### Dustin Tran

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html) [**Soft Calibration Objectives for Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html),<br> by *Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer and Becca Roelofs*
<br><br>
### Chandra Bhagavatula

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.418) [**Thinking Like a Skeptic: Defeasible Inference in Natural Language**](https://doi.org/10.18653/v1/2020.findings-emnlp.418),<br> by *Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith and Yejin Choi*
<br><br>
### Lingpeng Kong

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br>``
This paper proposes a LM named EvaLM to scale up the sequence length (trained with 8k tokens per batch line). Experiments based on EvaLM prove that in-context learning can achieve higher performance with more demonstrations under many-shot instruction tuning (8k) and further extending the length of instructions (16k) can further improve the upper bound of scaling in-context  learning.
``
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10375) [**Self-adaptive In-context Learning**](https://doi.org/10.48550/arXiv.2212.10375),<br> by *Zhiyong Wu, Yaoxiang Wang, Jiacheng Ye and Lingpeng Kong*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html) [**Episodic Memory in Lifelong Language Learning**](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html),<br> by *Cyprien de Masson d'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama*
<br>``
MbPA++. This paper proposes the use of memory (a fixed memory network) in life-long learning to prevent catastrophic forgetting by means of  experience replay and local adaptation. 
``
<br><br>
### Pengcheng He

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.03277) [**Instruction Tuning with GPT-4**](https://doi.org/10.48550/arXiv.2304.03277),<br> by *Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [**DeBERTa: Decoding-enhanced BERT with Disentangled Attention**](https://arxiv.org/abs/2006.03654), [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) <br> by *Pengcheng He, Xiaodong Liu, Jianfeng Gao and Weizhu Chen*
<br><br>
### Neel Sundaresan

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: Program&Code Generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Shuohang Wang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09150) [**Prompting GPT-3 To Be Reliable**](https://doi.org/10.48550/arXiv.2210.09150),<br> by *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan L. Boyd-Graber and Lijuan Wang*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.150) [**Dict-BERT: Enhancing Language Model Pre-training with Dictionary**](https://doi.org/10.18653/v1/2022.findings-acl.150),<br> by *Wenhao Yu, Chenguang Zhu, Yuwei Fang, Donghan Yu, Shuohang Wang, Yichong Xu, Michael Zeng and Meng Jiang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.495) [**T3: Tree-Autoencoder Constrained Adversarial Text Generation for
Targeted Attack**](https://doi.org/10.18653/v1/2020.emnlp-main.495),<br> by *Boxin Wang, Hengzhi Pei, Boyuan Pan, Qian Chen, Shuohang Wang and Bo Li*
<br><br>
### Chenguang Zhu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11521) [**How Does In-Context Learning Help Prompt Tuning?**](https://doi.org/10.48550/arXiv.2302.11521),<br> by *Simeng Sun, Yang Liu, Dan Iter, Chenguang Zhu and Mohit Iyyer*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.150) [**Dict-BERT: Enhancing Language Model Pre-training with Dictionary**](https://doi.org/10.18653/v1/2022.findings-acl.150),<br> by *Wenhao Yu, Chenguang Zhu, Yuwei Fang, Donghan Yu, Shuohang Wang, Yichong Xu, Michael Zeng and Meng Jiang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Weizhu Chen

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/jiachangliu/KATEGPT3) [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br>``
(1) 探索了在in-context learning中什么样的demonstration example可以对GPT-3的效果取得帮助；
``<br>``
(2) 利用roberta对样本进行编码，并计算demonstration与test example的向量距离（欧氏距离），最终发现与test example越相近的demonstration越能取得较好的效果。
``
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [**DeBERTa: Decoding-enhanced BERT with Disentangled Attention**](https://arxiv.org/abs/2006.03654), [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) <br> by *Pengcheng He, Xiaodong Liu, Jianfeng Gao and Weizhu Chen*
<br><br>
### Naman Goyal

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Asli Celikyilmaz

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.06031) [**A Review on Language Models as Knowledge Bases**](https://doi.org/10.48550/arXiv.2204.06031),<br> by *Badr AlKhamissi, Millicent Li, Asli Celikyilmaz, Mona T. Diab and Marjan Ghazvininejad*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
### Sebastian Riedel

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.556) [**Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot
Prompt Order Sensitivity**](https://doi.org/10.18653/v1/2022.acl-long.556), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel and Pontus Stenetorp*
<br>``
(1) This work demonstrates that few-shot prompts suffer from order sensitivity, in that for the same prompt the order in which samples are provided can make a difference to model performance.
``<br>``
(2) This work introduces a probing method which constructs an artificial development set by language models themselves to alleviate the order sensitivity problem.
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [<img src=https://img.shields.io/badge/arXiv_preprint_arXiv-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2208.03299) [**Atlas: Few-shot learning with retrieval augmented language models**](https://arxiv.org/abs/2208.03299),<br> by *Izacard, Gautier, Lewis, Patrick, Lomeli, Maria, Hosseini, Lucas, Petroni, Fabio, Schick, Timo, Dwivedi-Yu, Jane, Joulin, Armand et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1250) [**Language Models as Knowledge Bases?**](https://doi.org/10.18653/v1/D19-1250),<br> by *Fabio Petroni, Tim Rockt\"aschel, Sebastian Riedel, Patrick S. H. Lewis, Anton Bakhtin, Yuxiang Wu and Alexander H. Miller*
<br><br>
### Swaroop Mishra

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.09161) [**How Many Data Samples is an Additional Instruction Worth?**](https://doi.org/10.48550/arXiv.2203.09161),<br> by *Ravsehaj Singh Puri, Swaroop Mishra, Mihir Parmar and Chitta Baral*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07663) [**Pretrained Transformers Do not Always Improve Robustness**](https://doi.org/10.48550/arXiv.2210.07663),<br> by *Swaroop Mishra, Bhavdeep Singh Sachdeva and Chitta Baral*
<br><br>
### Yi Tay

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Adam Roberts

- [<img src=https://img.shields.io/badge/International_Conference_on_Machine_Learning,_{ICML}_2023,_23--29_July
2023,_Honolulu,_Hawaii,_{USA}-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v202/kandpal23a.html) [**Large Language Models Struggle to Learn Long-Tail Knowledge**](https://proceedings.mlr.press/v202/kandpal23a.html),<br> by *Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace and Colin Raffel*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
### Quoc V. Le

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=r1xMH1BtvB) [**ELECTRA: Pre-training Text Encoders as Discriminators Rather Than
Generators**](https://openreview.net/forum?id=r1xMH1BtvB), [<img src=https://img.shields.io/badge/ELECTRA-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=r1xMH1BtvB) <br> by *Kevin Clark, Minh-Thang Luong, Quoc V. Le and Christopher D. Manning*
<br><br>
### Maarten Bosma

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Zhiyong Wu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br>``
This paper proposes a LM named EvaLM to scale up the sequence length (trained with 8k tokens per batch line). Experiments based on EvaLM prove that in-context learning can achieve higher performance with more demonstrations under many-shot instruction tuning (8k) and further extending the length of instructions (16k) can further improve the upper bound of scaling in-context  learning.
``
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10375) [**Self-adaptive In-context Learning**](https://doi.org/10.48550/arXiv.2212.10375),<br> by *Zhiyong Wu, Yaoxiang Wang, Jiacheng Ye and Lingpeng Kong*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
### Amanda Askell

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Sam McCandlish

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Jared Kaplan

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Pascale Fung

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>``
Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.
``
<br><br>
### Long Ouyang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
### Geoffrey Irving

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/borgeaud22a.html) [**Improving Language Models by Retrieving from Trillions of Tokens**](https://proceedings.mlr.press/v162/borgeaud22a.html),<br> by *Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
### Le Sun

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07616) [**The Life Cycle of Knowledge in Big Language Models: A Survey**](https://doi.org/10.48550/arXiv.2303.07616),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.16421) [**ChatGPT is a Knowledgeable but Inexperienced Solver: An Investigation of Commonsense Problem in Large Language Models**](https://arxiv.org/abs/2303.16421),<br> by *Ning Bian, Xianpei Han, Le Sun, Hongyu Lin, Yaojie Lu and Ben He*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.398) [**Can Prompt Probe Pretrained Language Models? Understanding the Invisible
Risks from a Causal View**](https://doi.org/10.18653/v1/2022.acl-long.398),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Fangchao Liu and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/the_59th_Annual_Meeting_of_the_Association_for_Computational
Linguistics_and_the_11th_International_Joint_Conference_on_Natural
Language_Processing,_{ACL/IJCNLP}_2021,_(Volume_1:_Long_Papers),_Virtual
Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.146) [**Knowledgeable or Educated Guess? Revisiting Language Models as Knowledge
Bases**](https://doi.org/10.18653/v1/2021.acl-long.146),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Le Sun, Lingyong Yan, Meng Liao, Tong Xue and Jin Xu*
<br><br>
### Xianpei Han

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07616) [**The Life Cycle of Knowledge in Big Language Models: A Survey**](https://doi.org/10.48550/arXiv.2303.07616),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.16421) [**ChatGPT is a Knowledgeable but Inexperienced Solver: An Investigation of Commonsense Problem in Large Language Models**](https://arxiv.org/abs/2303.16421),<br> by *Ning Bian, Xianpei Han, Le Sun, Hongyu Lin, Yaojie Lu and Ben He*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.398) [**Can Prompt Probe Pretrained Language Models? Understanding the Invisible
Risks from a Causal View**](https://doi.org/10.18653/v1/2022.acl-long.398),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Fangchao Liu and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/the_59th_Annual_Meeting_of_the_Association_for_Computational
Linguistics_and_the_11th_International_Joint_Conference_on_Natural
Language_Processing,_{ACL/IJCNLP}_2021,_(Volume_1:_Long_Papers),_Virtual
Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.146) [**Knowledgeable or Educated Guess? Revisiting Language Models as Knowledge
Bases**](https://doi.org/10.18653/v1/2021.acl-long.146),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Le Sun, Lingyong Yan, Meng Liao, Tong Xue and Jin Xu*
<br><br>
### Hongyu Lin

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07616) [**The Life Cycle of Knowledge in Big Language Models: A Survey**](https://doi.org/10.48550/arXiv.2303.07616),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.16421) [**ChatGPT is a Knowledgeable but Inexperienced Solver: An Investigation of Commonsense Problem in Large Language Models**](https://arxiv.org/abs/2303.16421),<br> by *Ning Bian, Xianpei Han, Le Sun, Hongyu Lin, Yaojie Lu and Ben He*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.398) [**Can Prompt Probe Pretrained Language Models? Understanding the Invisible
Risks from a Causal View**](https://doi.org/10.18653/v1/2022.acl-long.398),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Fangchao Liu and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/the_59th_Annual_Meeting_of_the_Association_for_Computational
Linguistics_and_the_11th_International_Joint_Conference_on_Natural
Language_Processing,_{ACL/IJCNLP}_2021,_(Volume_1:_Long_Papers),_Virtual
Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.146) [**Knowledgeable or Educated Guess? Revisiting Language Models as Knowledge
Bases**](https://doi.org/10.18653/v1/2021.acl-long.146),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Le Sun, Lingyong Yan, Meng Liao, Tong Xue and Jin Xu*
<br><br>
### Kang Liu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.628) [**CN-AutoMIC: Distilling Chinese Commonsense Knowledge from Pretrained
Language Models**](https://aclanthology.org/2022.emnlp-main.628),<br> by *Chenhao Wang, Jiachun Li, Yubo Chen, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>``
We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.
``
<br><br>
### Seonghyeon Ye

- [<img src=https://img.shields.io/badge/-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.03202) [**Exploring the Benefits of Training Expert Language Models over Instruction Tuning**](https://arxiv.org/abs/2302.03202),<br> by *Joel Jang, Seungone Kim, Seonghyeon Ye, Doyoung Kim, Lajanugen Logeswaran, Moontae Lee, Kyungjae Lee and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.14691) [**In-Context Instruction Learning**](https://doi.org/10.48550/arXiv.2302.14691),<br> by *Seonghyeon Ye, Hyeonbin Hwang, Sohee Yang, Hyeongu Yun, Yireun Kim and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
### Bing Liu

- [<img src=https://img.shields.io/badge/The_Eleventh_International_Conference_on_Learning_Representations,
{ICLR}_2023,_Kigali,_Rwanda,_May_1--5,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/pdf?id=m\_GDIItaI3o) [**Continual Pre-training of Language Models**](https://openreview.net/pdf?id=m\_GDIItaI3o),<br> by *Zixuan Ke, Yijia Shao, Haowei Lin, Tatsuya Konishi, Gyuhak Kim and Bing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>``
NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.
``
<br><br>
- [<img src=https://img.shields.io/badge/EACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.eacl-main.95) [**Analyzing the Forgetting Problem in Pretrain-Finetuning of Open-domain
Dialogue Response Models**](https://doi.org/10.18653/v1/2021.eacl-main.95),<br> by *Tianxing He, Jun Liu, Kyunghyun Cho, Myle Ott, Bing Liu, James R. Glass and Fuchun Peng*
<br>``
Our major finding is that after standard finetuning, the model forgets some of the important language generation skills acquired during large-scale pretraining. We propose an intuitive finetuning strategy named “mix-review”: : For each finetuning epoch, we mix the target dialogue data with a random subset of the pretraining data, mix_ratio is 4, decay is 0.9.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>``
The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.
``
<br><br>
### Myle Ott

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.eacl-main.95) [**Analyzing the Forgetting Problem in Pretrain-Finetuning of Open-domain
Dialogue Response Models**](https://doi.org/10.18653/v1/2021.eacl-main.95),<br> by *Tianxing He, Jun Liu, Kyunghyun Cho, Myle Ott, Bing Liu, James R. Glass and Fuchun Peng*
<br>``
Our major finding is that after standard finetuning, the model forgets some of the important language generation skills acquired during large-scale pretraining. We propose an intuitive finetuning strategy named “mix-review”: : For each finetuning epoch, we mix the target dialogue data with a random subset of the pretraining data, mix_ratio is 4, decay is 0.9.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Lidong Bing

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.15038) [**Is GPT-4 a Good Data Analyst?**](https://doi.org/10.48550/arXiv.2305.15038),<br> by *Liying Cheng, Xingxuan Li and Lidong Bing*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>``
we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness: it tendsto outperform fine-tuning on both low-resource and cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to fine-tuning.
``
<br><br>
### Chitta Baral

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.50) [**Reframing Instructional Prompts to GPTk's Language**](https://doi.org/10.18653/v1/2022.findings-acl.50),<br> by *Daniel Khashabi, Chitta Baral, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.09161) [**How Many Data Samples is an Additional Instruction Worth?**](https://doi.org/10.48550/arXiv.2203.09161),<br> by *Ravsehaj Singh Puri, Swaroop Mishra, Mihir Parmar and Chitta Baral*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07663) [**Pretrained Transformers Do not Always Improve Robustness**](https://doi.org/10.48550/arXiv.2210.07663),<br> by *Swaroop Mishra, Bhavdeep Singh Sachdeva and Chitta Baral*
<br><br>
### Kun Zhou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.212) [**Small Pre-trained Language Models Can be Fine-tuned as Large Models
via Over-Parameterization**](https://doi.org/10.18653/v1/2023.acl-long.212),<br> by *Ze-Feng Gao, Kun Zhou, Peiyu Liu, Wayne Xin Zhao and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Mohit Bansal

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.137) [**Are Hard Examples also Harder to Explain? A Study with Human and
Model-Generated Explanations**](https://aclanthology.org/2022.emnlp-main.137),<br> by *Swarnadeep Saha, Peter Hase, Nazneen Rajani and Mohit Bansal*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.162) [**Vokenization: Improving Language Understanding with Contextualized,
Visual-Grounded Supervision**](https://doi.org/10.18653/v1/2020.emnlp-main.162),<br> by *Hao Tan and Mohit Bansal*
<br><br>
### David Lo

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.10620) [**Large Language Models for Software Engineering: A Systematic Literature
Review**](https://doi.org/10.48550/arXiv.2308.10620),<br> by *Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ASE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
- [<img src=https://img.shields.io/badge/ICSME-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ieeexplore.ieee.org/abstract/document/9240704/) [**Sentiment analysis for software engineering: How far can pre-trained transformer models go?**](https://ieeexplore.ieee.org/abstract/document/9240704/),<br> by *Zhang, Ting, Xu, Bowen, Thung, Ferdian, Haryono, Stefanus Agus, Lo, David and Jiang, Lingxiao*
<br><br>
### Kai Wei Chang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.132) [**GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained
Language Models**](https://aclanthology.org/2022.emnlp-main.132),<br> by *Da Yin, Hritik Bansal, Masoud Monajatipoor, Liunian Harold Li and Kai-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1908.03557) [**VisualBERT: A Simple and Performant Baseline for Vision and Language**](http://arxiv.org/abs/1908.03557),<br> by *Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh and Kai-Wei Chang*
<br><br>
### Shengyu Fu

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: Program&Code Generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Alexey Svyatkovskiy

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: Program&Code Generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Daya Guo

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Shuai Lu

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Shafiq R. Joty

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.737) [**A Unified Speaker Adaptation Approach for ASR**](https://aclanthology.org/2021.emnlp-main.737),<br> by *Yingzhu Zhao, Chongjia Ni, Cheung-Chi Leung, Shafiq R. Joty, Eng Siong Chng and Bin Ma*
<br>``
Prefix-based user identifier, Continual ASR / Architecture Search / Network Pruning.
``
<br><br>
### Yue Wang

- [<img src=https://img.shields.io/badge/openreview-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Program&Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.57) [**Detect-Localize-Repair: A Unified Framework for Learning to Debug
with CodeT5**](https://aclanthology.org/2022.findings-emnlp.57),<br> by *Nghi Bui, Yue Wang and Steven C. H. Hoi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
### Bill Dolan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/jiachangliu/KATEGPT3) [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br>``
(1) 探索了在in-context learning中什么样的demonstration example可以对GPT-3的效果取得帮助；
``<br>``
(2) 利用roberta对样本进行编码，并计算demonstration与test example的向量距离（欧氏距离），最终发现与test example越相近的demonstration越能取得较好的效果。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.28) [**Dialogue Response Ranking Training with Large-Scale Human Feedback
Data**](https://doi.org/10.18653/v1/2020.emnlp-main.28),<br> by *Xiang Gao, Yizhe Zhang, Michel Galley, Chris Brockett and Bill Dolan*
<br><br>
### Jian Yun Nie

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL}_2023,
Toronto,_Canada,_July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.findings-acl.46) [**The Web Can Be Your Oyster for Improving Language Models**](https://doi.org/10.18653/v1/2023.findings-acl.46),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jingyuan Wang, Jian-Yun Nie and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.392) [**A Simple and Efficient Multi-Task Learning Approach for Conditioned
Dialogue Generation**](https://doi.org/10.18653/v1/2021.naacl-main.392),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2010.11140) [**Generalized Conditioned Dialogue Generation Based on Pre-trained Language
Model**](https://arxiv.org/abs/2010.11140),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
### Michael Zeng

- [<img src=https://img.shields.io/badge/CVPR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.150) [**Dict-BERT: Enhancing Language Model Pre-training with Dictionary**](https://doi.org/10.18653/v1/2022.findings-acl.150),<br> by *Wenhao Yu, Chenguang Zhu, Yuwei Fang, Donghan Yu, Shuohang Wang, Yichong Xu, Michael Zeng and Meng Jiang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Baolin Peng

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.03277) [**Instruction Tuning with GPT-4**](https://doi.org/10.48550/arXiv.2304.03277),<br> by *Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Daxin Jiang

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>``
We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
``<br>``
and supports the development of versatile
``<br>``
knowledge-infused model.
``
<br><br>
### Tianyi Tang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL}_2023,
Toronto,_Canada,_July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.findings-acl.46) [**The Web Can Be Your Oyster for Improving Language Models**](https://doi.org/10.18653/v1/2023.findings-acl.46),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jingyuan Wang, Jian-Yun Nie and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Minlie Huang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.10436) [**Safety Assessment of Chinese Large Language Models**](https://doi.org/10.48550/arXiv.2304.10436),<br> by *Hao Sun, Zhexin Zhang, Jiawen Deng, Jiale Cheng and Minlie Huang*
<br><br>
- [<img src=https://img.shields.io/badge/Mach._Intell._Res.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s11633-022-1387-3) [**EVA2.0: Investigating Open-domain Chinese Dialogue Systems with
Large-scale Pre-training**](https://doi.org/10.1007/s11633-022-1387-3),<br> by *Yuxian Gu, Jiaxin Wen, Hao Sun, Yi Song, Pei Ke, Chujie Zheng, Zheng Zhang, Jianzhu Yao et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
- [<img src=https://img.shields.io/badge/TACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Zhou Yu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.01580) [**Mixture of Soft Prompts for Controllable Data Generation**](https://doi.org/10.48550/arXiv.2303.01580),<br> by *Derek Chen, Celine Lee, Yunan Lu, Domenic Rosati and Zhou Yu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-short.40) [**PRAL: A Tailored Pre-Training Model for Task-Oriented Dialog Generation**](https://doi.org/10.18653/v1/2021.acl-short.40),<br> by *Jing Gu, Qingyang Wu, Chongruo Wu, Weiyan Shi and Zhou Yu*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.239) [**Action-Based Conversations Dataset: A Corpus for Building More In-Depth
Task-Oriented Dialogue Systems**](https://doi.org/10.18653/v1/2021.naacl-main.239),<br> by *Derek Chen, Howard Chen, Yi Yang, Alexander Lin and Zhou Yu*
<br><br>
### Ting Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.07902) [**Through the Lens of Core Competency: Survey on Evaluation of Large
Language Models**](https://doi.org/10.48550/arXiv.2308.07902),<br> by *Ziyu Zhuang, Qiguang Chen, Longxuan Ma, Mingda Li, Yi Han, Yushan Qian, Haopeng Bai, Zixian Feng et al.*
<br><br>
- [<img src=https://img.shields.io/badge/COLING-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>``
We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.
``
<br><br>
### Iryna Gurevych

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2007.08426) [**Investigating Pretrained Language Models for Graph-to-Text Generation**](https://arxiv.org/abs/2007.08426),<br> by *Leonardo F. R. Ribeiro, Martin Schmitt, Hinrich Sch\"utze and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1410) [**Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks**](https://doi.org/10.18653/v1/D19-1410), [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) <br> by *Nils Reimers and Iryna Gurevych*
<br><br>
### Andrea Madotto

- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=H1edEyBKDS) [**Plug and Play Language Models: A Simple Approach to Controlled Text
Generation**](https://openreview.net/forum?id=H1edEyBKDS),<br> by *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski and Rosanne Liu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>``
Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.
``
<br><br>
### Li Dong

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br>``
(1) 与The Dual Form of Neural Networks Revisited结合一起看，可以进一步理解in-context learning，通过与NN线性层对偶形式的类比，可以将ICL流程描述为：1. 基于Transformer的预训练语言模型作为元优化器；2. 通过正向计算，根据示范例子产生元梯度；3. 通过关注，将元梯度应用于原始语言模型，建立一个ICL模型；
``<br>``
(2)与Fine-tune类似，ICL也是在zero-shot learning参数的基础上，提供了一个更新量。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Jingjing Liu

- [<img src=https://img.shields.io/badge/CVPR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Zhe Gan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09150) [**Prompting GPT-3 To Be Reliable**](https://doi.org/10.48550/arXiv.2210.09150),<br> by *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan L. Boyd-Graber and Lijuan Wang*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### William Yang Wang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.11916) [**Large Language Models Are Implicitly Topic Models: Explaining and
Finding Good Demonstrations for In-Context Learning**](https://doi.org/10.48550/arXiv.2301.11916),<br> by *Xinyi Wang, Wanrong Zhu and William Yang Wang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.13903) [**Let's Think Frame by Frame: Evaluating Video Chain of Thought with
Video Infilling and Prediction**](https://doi.org/10.48550/arXiv.2305.13903),<br> by *Vaishnavi Himakunthala, Andy Ouyang, Daniel Rose, Ryan He, Alex Mei, Yujie Lu, Chinmay Sonar, Michael Saxon et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.190) [**Logic2Text: High-Fidelity Natural Language Generation from Logical
Forms**](https://doi.org/10.18653/v1/2020.findings-emnlp.190),<br> by *Zhiyu Chen, Wenhu Chen, Hanwen Zha, Xiyou Zhou, Yunkai Zhang, Sairam Sundaresan and William Yang Wang*
<br><br>
### Wenhu Chen

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.06710) [**Large Language Models are few(1)-shot Table Reasoners**](https://doi.org/10.48550/arXiv.2210.06710),<br> by *Wenhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.190) [**Logic2Text: High-Fidelity Natural Language Generation from Logical
Forms**](https://doi.org/10.18653/v1/2020.findings-emnlp.190),<br> by *Zhiyu Chen, Wenhu Chen, Hanwen Zha, Xiyou Zhou, Yunkai Zhang, Sairam Sundaresan and William Yang Wang*
<br><br>
### Huajun Chen

- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/IJCAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.24963/ijcai.2022/273) [**Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in
the Federated Setting**](https://doi.org/10.24963/ijcai.2022/273),<br> by *Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Ningyu Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.01555) [**How to Unleash the Power of Large Language Models for Few-shot Relation
Extraction?**](https://doi.org/10.48550/arXiv.2305.01555),<br> by *Xin Xu, Yuqi Zhu, Xiaohan Wang and Ningyu Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Maosong Sun

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Zhiyuan Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Yang Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11521) [**How Does In-Context Learning Help Prompt Tuning?**](https://doi.org/10.48550/arXiv.2302.11521),<br> by *Simeng Sun, Yang Liu, Dan Iter, Chenguang Zhu and Mohit Iyyer*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.424) [**MSP: Multi-Stage Prompting for Making Pre-trained Language Models
Better Translators**](https://doi.org/10.18653/v1/2022.acl-long.424),<br> by *Zhixing Tan, Xiangwen Zhang, Shuo Wang and Yang Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
### Fabio Petroni

- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [<img src=https://img.shields.io/badge/arXiv_preprint_arXiv-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2208.03299) [**Atlas: Few-shot learning with retrieval augmented language models**](https://arxiv.org/abs/2208.03299),<br> by *Izacard, Gautier, Lewis, Patrick, Lomeli, Maria, Hosseini, Lucas, Petroni, Fabio, Schick, Timo, Dwivedi-Yu, Jane, Joulin, Armand et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1250) [**Language Models as Knowledge Bases?**](https://doi.org/10.18653/v1/D19-1250),<br> by *Fabio Petroni, Tim Rockt\"aschel, Sebastian Riedel, Patrick S. H. Lewis, Anton Bakhtin, Yuxiang Wu and Alexander H. Miller*
<br><br>
### Eric Wallace

- [<img src=https://img.shields.io/badge/International_Conference_on_Machine_Learning,_{ICML}_2023,_23--29_July
2023,_Honolulu,_Hawaii,_{USA}-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v202/kandpal23a.html) [**Large Language Models Struggle to Learn Long-Tail Knowledge**](https://proceedings.mlr.press/v202/kandpal23a.html),<br> by *Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace and Colin Raffel*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.346) [**AutoPrompt: Eliciting Knowledge from Language Models with Automatically
Generated Prompts**](https://doi.org/10.18653/v1/2020.emnlp-main.346),<br> by *Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric Wallace and Sameer Singh*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.244) [**Pretrained Transformers Improve Out-of-Distribution Robustness**](https://doi.org/10.18653/v1/2020.acl-main.244),<br> by *Dan Hendrycks, Xiaoyuan Liu, Eric Wallace, Adam Dziedzic, Rishabh Krishnan and Dawn Song*
<br><br>
### Dale Schuurmans

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
### Hao Peng

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.17306) [**Chain-of-Thought Hub: A Continuous Effort to Measure Large Language
Models' Reasoning Performance**](https://doi.org/10.48550/arXiv.2305.17306),<br> by *Yao Fu, Litu Ou, Mingyu Chen, Yuhao Wan, Hao Peng and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Shixiang Shane Gu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12192) [**Aligning Text-to-Image Models using Human Feedback**](https://doi.org/10.48550/arXiv.2302.12192),<br> by *Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.11916) [**Large Language Models are Zero-Shot Reasoners**](https://doi.org/10.48550/arXiv.2205.11916),<br> by *Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo and Yusuke Iwasawa*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Veselin Stoyanov

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Ramakanth Pasunuru

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Lei Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.06950) [**Pre-trained Language Models can be Fully Zero-Shot Learners**](https://doi.org/10.48550/arXiv.2212.06950),<br> by *Xuandong Zhao, Siqi Ouyang, Zhiguo Yu, Ming Wu and Lei Li*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.438) [**Calibrating Factual Knowledge in Pretrained Language Models**](https://aclanthology.org/2022.findings-emnlp.438),<br> by *Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui and Lei Li*
<br><br>
### Jack Clark

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Daniel M. Ziegler

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
### Tom Henighan

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Tom B. Brown

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2017-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html) [**Deep Reinforcement Learning from Human Preferences**](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html),<br> by *Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg and Dario Amodei*
<br><br>
### Jeffrey Wu

- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
### Noam Shazeer

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Ilya Sutskever

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), [<img src=https://img.shields.io/badge/GPT--1-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Jan Leike

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2017-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html) [**Deep Reinforcement Learning from Human Preferences**](https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html),<br> by *Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg and Dario Amodei*
<br><br>
### Jie Tang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539472) [**Mask and Reason: Pre-Training Knowledge Graph Transformers for Complex
Logical Queries**](https://doi.org/10.1145/3534678.3539472),<br> by *Xiao Liu, Shiyu Zhao, Kai Su, Yukuo Cen, Jiezhong Qiu, Mengdi Zhang, Wei Wu, Yuxiao Dong et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
### Nicholas Joseph

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Weijia Shi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10539) [**Toward Human Readable Prompt Tuning: Kubrick's The Shining is a good
movie, and a good prompt too?**](https://doi.org/10.48550/arXiv.2212.10539),<br> by *Weijia Shi, Xiaochuang Han, Hila Gonen, Ari Holtzman, Yulia Tsvetkov and Luke Zettlemoyer*
<br><br>
### Antoine Bosselut

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=0DcZxeWfOPt) [**Fast Model Editing at Scale**](https://openreview.net/forum?id=0DcZxeWfOPt),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn and Christopher D. Manning*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/mitchell22a.html) [**Memory-Based Model Editing at Scale**](https://proceedings.mlr.press/v162/mitchell22a.html),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning and Chelsea Finn*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
### Graham Neubig

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Program&Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2202.13169) [**A Systematic Evaluation of Large Language Models of Code**](https://arxiv.org/abs/2202.13169),<br> by *Frank F. Xu, Uri Alon, Graham Neubig and Vincent J. Hellendoorn*
<br><br>
### Uri Alon

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Program&Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2202.13169) [**A Systematic Evaluation of Large Language Models of Code**](https://arxiv.org/abs/2202.13169),<br> by *Frank F. Xu, Uri Alon, Graham Neubig and Vincent J. Hellendoorn*
<br><br>
### Jiacheng Ye

- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10375) [**Self-adaptive In-context Learning**](https://doi.org/10.48550/arXiv.2212.10375),<br> by *Zhiyong Wu, Yaoxiang Wang, Jiacheng Ye and Lingpeng Kong*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
### Ryan Lowe

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
### John Schulman

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2210.10760) [**Scaling Laws for Reward Model Overoptimization**](https://arxiv.org/abs/2210.10760),<br> by *Gao, Leo, Schulman, John and Hilton, Jacob*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Jeff Wu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
### Jacob Hilton

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2210.10760) [**Scaling Laws for Reward Model Overoptimization**](https://arxiv.org/abs/2210.10760),<br> by *Gao, Leo, Schulman, John and Hilton, Jacob*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Nisan Stiennon

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2109.10862) [**Recursively Summarizing Books with Human Feedback**](https://arxiv.org/abs/2109.10862),<br> by *Jeff Wu, Long Ouyang, Daniel M. Ziegler, Nisan Stiennon, Ryan Lowe, Jan Leike and Paul F. Christiano*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) [**Learning to summarize with human feedback**](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html),<br> by *Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.08593) [**Fine-Tuning Language Models from Human Preferences**](http://arxiv.org/abs/1909.08593),<br> by *Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul F. Christiano and Geoffrey Irving*
<br><br>
### Yufei Wang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.12966) [**Aligning Large Language Models with Human: A Survey**](https://doi.org/10.48550/arXiv.2307.12966),<br> by *Yufei Wang, Wanjun Zhong, Liangyou Li, Fei Mi, Xingshan Zeng, Wenyong Huang, Lifeng Shang, Xin Jiang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2306.08302) [**Unifying Large Language Models and Knowledge Graphs: A Roadmap**](https://doi.org/10.48550/arXiv.2306.08302),<br> by *Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang and Xindong Wu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.9) [**Mention Flags (MF): Constraining Transformer-based Text Generators**](https://doi.org/10.18653/v1/2021.acl-long.9),<br> by *Yufei Wang, Ian D. Wood, Stephen Wan, Mark Dras and Mark Johnson*
<br><br>
### Jena D. Hwang

- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.418) [**Thinking Like a Skeptic: Defeasible Inference in Natural Language**](https://doi.org/10.18653/v1/2020.findings-emnlp.418),<br> by *Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith and Yejin Choi*
<br><br>
### Jack Hessel

- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01241) [**Is Reinforcement Learning (Not) for Natural Language Processing?:
Benchmarks, Baselines, and Building Blocks for Natural Language Policy
Optimization**](https://doi.org/10.48550/arXiv.2210.01241),<br> by *Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kiant\'e Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Wen tau Yih

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
### Boxi Cao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07616) [**The Life Cycle of Knowledge in Big Language Models: A Survey**](https://doi.org/10.48550/arXiv.2303.07616),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.398) [**Can Prompt Probe Pretrained Language Models? Understanding the Invisible
Risks from a Causal View**](https://doi.org/10.18653/v1/2022.acl-long.398),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Fangchao Liu and Le Sun*
<br><br>
- [<img src=https://img.shields.io/badge/the_59th_Annual_Meeting_of_the_Association_for_Computational
Linguistics_and_the_11th_International_Joint_Conference_on_Natural
Language_Processing,_{ACL/IJCNLP}_2021,_(Volume_1:_Long_Papers),_Virtual
Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.146) [**Knowledgeable or Educated Guess? Revisiting Language Models as Knowledge
Bases**](https://doi.org/10.18653/v1/2021.acl-long.146),<br> by *Boxi Cao, Hongyu Lin, Xianpei Han, Le Sun, Lingyong Yan, Meng Liao, Tong Xue and Jin Xu*
<br><br>
### Susannah Young

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/liska22a.html) [**StreamingQA: A Benchmark for Adaptation to New Knowledge over Time
in Question Answering Models**](https://proceedings.mlr.press/v162/liska22a.html),<br> by *Adam Liska, Tom\'as Kocisk\'y, Elena Gribovskaya, Tayfun Terzi, Eren Sezener, Devang Agrawal, Cyprien de Masson d'Autume, Tim Scholtes et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### Colin Raffel

- [<img src=https://img.shields.io/badge/International_Conference_on_Machine_Learning,_{ICML}_2023,_23--29_July
2023,_Honolulu,_Hawaii,_{USA}-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v202/kandpal23a.html) [**Large Language Models Struggle to Learn Long-Tail Knowledge**](https://proceedings.mlr.press/v202/kandpal23a.html),<br> by *Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace and Colin Raffel*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
### Mona T. Diab

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.06031) [**A Review on Language Models as Knowledge Bases**](https://doi.org/10.48550/arXiv.2204.06031),<br> by *Badr AlKhamissi, Millicent Li, Asli Celikyilmaz, Mona T. Diab and Marjan Ghazvininejad*
<br><br>
### Shizhu He

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>``
We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.
``
<br><br>
### Sohee Yang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.14691) [**In-Context Instruction Learning**](https://doi.org/10.48550/arXiv.2302.14691),<br> by *Seonghyeon Ye, Hyeonbin Hwang, Sohee Yang, Hyeongu Yun, Yireun Kim and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
### Joel Jang

- [<img src=https://img.shields.io/badge/-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.03202) [**Exploring the Benefits of Training Expert Language Models over Instruction Tuning**](https://arxiv.org/abs/2302.03202),<br> by *Joel Jang, Seungone Kim, Seonghyeon Ye, Doyoung Kim, Lajanugen Logeswaran, Moontae Lee, Kyungjae Lee and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
### Bill Yuchen Lin

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.findings-emnlp.62) [**Learn Continually, Generalize Rapidly: Lifelong Knowledge Accumulation for Few-shot Learning**](https://aclanthology.org/2021.findings-emnlp.62),<br> by *Jin, Xisen , Lin, Bill Yuchen , Rostami, Mohammad  and Ren, Xiang*
<br>``
We present a new learning setup, Continual Learning of Few-Shot Learners, to address challenges of both learning settings in a unified setup, with a hyper-network for task-specific adapter generation.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.598) [**RICA: Evaluating Robust Inference Capabilities Based on Commonsense
Axioms**](https://doi.org/10.18653/v1/2021.emnlp-main.598),<br> by *Pei Zhou, Rahul Khanna, Seyeon Lee, Bill Yuchen Lin, Daniel Ho, Jay Pujara and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
### Zixuan Ke

- [<img src=https://img.shields.io/badge/The_Eleventh_International_Conference_on_Learning_Representations,
{ICLR}_2023,_Kigali,_Rwanda,_May_1--5,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/pdf?id=m\_GDIItaI3o) [**Continual Pre-training of Language Models**](https://openreview.net/pdf?id=m\_GDIItaI3o),<br> by *Zixuan Ke, Yijia Shao, Haowei Lin, Tatsuya Konishi, Gyuhak Kim and Bing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>``
NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>``
The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.
``
<br><br>
### Zac Hatfield Dodds

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Yuntao Bai

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Tristan Hume

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Sheer El Showk

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Shauna Kravec

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Scott Johnston

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Saurav Kadavath

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Nova DasSarma

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Nelson Elhage

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Liane Lovitt

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Kamal Ndousse

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Jackson Kernion

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Ethan Perez

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
### Danny Hernandez

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Catherine Olsson

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Anna Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Deep Ganguli

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Linlin Liu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>``
we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness: it tendsto outperform fine-tuning on both low-resource and cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to fine-tuning.
``
<br><br>
### Balaji Lakshminarayanan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html) [**Soft Calibration Objectives for Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html),<br> by *Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer and Becca Roelofs*
<br><br>
### Neil Houlsby

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Hao Sun

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.10436) [**Safety Assessment of Chinese Large Language Models**](https://doi.org/10.48550/arXiv.2304.10436),<br> by *Hao Sun, Zhexin Zhang, Jiawen Deng, Jiale Cheng and Minlie Huang*
<br><br>
- [<img src=https://img.shields.io/badge/Mach._Intell._Res.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s11633-022-1387-3) [**EVA2.0: Investigating Open-domain Chinese Dialogue Systems with
Large-scale Pre-training**](https://doi.org/10.1007/s11633-022-1387-3),<br> by *Yuxian Gu, Jiaxin Wen, Hao Sun, Yi Song, Pei Ke, Chujie Zheng, Zheng Zhang, Jianzhu Yao et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
### Yoon Kim

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.130) [**Large language models are few-shot clinical information extractors**](https://aclanthology.org/2022.emnlp-main.130),<br> by *Monica Agrawal, Stefan Hegselmann, Hunter Lang, Yoon Kim and David A. Sontag*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.11031) [**Aging with GRACE: Lifelong Model Editing with Discrete Key-Value
Adaptors**](https://doi.org/10.48550/arXiv.2211.11031),<br> by *Thomas Hartvigsen, Swami Sankaranarayanan, Hamid Palangi, Yoon Kim and Marzyeh Ghassemi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.378) [**Parameter-Efficient Transfer Learning with Diff Pruning**](https://aclanthology.org/2021.acl-long.378),<br> by *Guo, Demi , Rush, Alexander  and Kim, Yoon*
<br>``
The approach learns a task-specific “diff” vector that extends the original pretrained parameters. As the number of tasks increases, diff pruning remains parameter-efficient, as it requires storing only a small diff vector for each task.
``
<br><br>
### Chuanqi Tan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Tong Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12822) [**Automatic Prompt Augmentation and Selection with Chain-of-Thought
from Labeled Data**](https://doi.org/10.48550/arXiv.2302.12822),<br> by *Kashun Shum, Shizhe Diao and Tong Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Shizhe Diao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12822) [**Automatic Prompt Augmentation and Selection with Chain-of-Thought
from Labeled Data**](https://doi.org/10.48550/arXiv.2302.12822),<br> by *Kashun Shum, Shizhe Diao and Tong Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Pan Lu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.218) [**UniGeo: Unifying Geometry Logical Reasoning via Reformulating Mathematical
Expression**](https://aclanthology.org/2022.emnlp-main.218),<br> by *Jiaqi Chen, Tong Li, Jinghui Qin, Pan Lu, Liang Lin, Chongyu Chen and Xiaodan Liang*
<br><br>
### Guilin Qi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07992) [**Evaluation of ChatGPT as a Question Answering System for Answering
Complex Questions**](https://doi.org/10.48550/arXiv.2303.07992),<br> by *Yiming Tan, Dehai Min, Yu Li, Wenbo Li, Nan Hu, Yongrui Chen and Guilin Qi*
<br><br>
- [<img src=https://img.shields.io/badge/COLING-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.coling-1.200) [**Event Causality Identification via Derivative Prompt Joint Learning**](https://aclanthology.org/2022.coling-1.200),<br> by *Shirong Shen, Heng Zhou, Tongtong Wu and Guilin Qi*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>``
To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.
``
<br><br>
### Muhao Chen

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.107) [**Salience-Aware Event Chain Modeling for Narrative Understanding**](https://doi.org/10.18653/v1/2021.emnlp-main.107),<br> by *Xiyang Zhang, Muhao Chen and Jonathan May*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.322) [**Do Language Models Perform Generalizable Commonsense Inference?**](https://doi.org/10.18653/v1/2021.findings-acl.322), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/wangpf3/LM-for-CommonsenseInference)<br> by *Peifeng Wang, Filip Ilievski, Muhao Chen and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Thien Huu Nguyen

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.starsem-1.11) [**Word-Label Alignment for Event Detection: A New Perspective via
Optimal Transport**](https://doi.org/10.18653/v1/2022.starsem-1.11),<br> by *Amir Pouran Ben Veyseh and Thien Huu Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/ECML-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Shijin Wang

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
### David Dohan

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
### Chengwei Qin

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=HCRVf71PMF) [**LFPT5: A Unified Framework for Lifelong Few-shot Language Learning Based on Prompt Tuning of T5**](https://openreview.net/forum?id=HCRVf71PMF),<br> by *Chengwei Qin and Shafiq Joty*
<br>``
We define a challenging yet practical problem as Lifelong Few-shot Language Learning and propose a unified framework for it based on prompt tuning of T5.
``
<br><br>
### Janghoon Han

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.122) [**Fine-grained Post-training for Improving Retrieval-based Dialogue
Systems**](https://doi.org/10.18653/v1/2021.naacl-main.122),<br> by *Janghoon Han, Taesuk Hong, Byoungjae Kim, Youngjoong Ko and Jungyun Seo*
<br><br>
### Zhou Yang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.10620) [**Large Language Models for Software Engineering: A Systematic Literature
Review**](https://doi.org/10.48550/arXiv.2308.10620),<br> by *Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ASE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
### Li Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.10620) [**Large Language Models for Software Engineering: A Systematic Literature
Review**](https://doi.org/10.48550/arXiv.2308.10620),<br> by *Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Shao Kun Deng

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/FSE-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: Program&Code Generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Duyu Tang

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>``
We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
``<br>``
and supports the development of versatile
``<br>``
knowledge-infused model.
``
<br><br>
### Colin B. Clement

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
### Steven C. H. Hoi

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Program&Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.57) [**Detect-Localize-Repair: A Unified Framework for Learning to Debug
with CodeT5**](https://aclanthology.org/2022.findings-emnlp.57),<br> by *Nghi Bui, Yue Wang and Steven C. H. Hoi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
### Hang Xu

- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
- [<img src=https://img.shields.io/badge/ICDCS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/ICDCS51616.2021.00060) [**GRACE: A Compressed Communication Framework for Distributed Machine
Learning**](https://doi.org/10.1109/ICDCS51616.2021.00060),<br> by *Hang Xu, Chen-Yu Ho, Ahmed M. Abdelmoniem, Aritra Dutta, El Houcine Bergou, Konstantinos Karatsenidis, Marco Canini and Panos Kalnis*
<br><br>
### Hai Jin

- [<img src=https://img.shields.io/badge/TIST-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.147) [**Can Language Models Serve as Temporal Knowledge Bases?**](https://aclanthology.org/2022.findings-emnlp.147),<br> by *Ruilin Zhao, Feng Zhao, Guandong Xu, Sixiao Zhang and Hai Jin*
<br><br>
### Yao Wan

- [<img src=https://img.shields.io/badge/TIST-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Dejing Dou

- [<img src=https://img.shields.io/badge/KIS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s10115-022-01664-x) [**From distributed machine learning to federated learning: a survey**](https://doi.org/10.1007/s10115-022-01664-x),<br> by *Ji Liu, Jizhou Huang, Yang Zhou, Xuhong Li, Shilei Ji, Haoyi Xiong and Dejing Dou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.05658) [**Fine-tuning Pre-trained Language Models with Noise Stability Regularization**](https://doi.org/10.48550/arXiv.2206.05658),<br> by *Hang Hua, Xingjian Li, Dejing Dou, Cheng-Zhong Xu and Jiebo Luo*
<br><br>
- [<img src=https://img.shields.io/badge/Euro--Par-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Oriol Vinyals

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/borgeaud22a.html) [**Improving Language Models by Retrieving from Trillions of Tokens**](https://proceedings.mlr.press/v162/borgeaud22a.html),<br> by *Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2015-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1503.02531) [**Distilling the Knowledge in a Neural Network**](http://arxiv.org/abs/1503.02531), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Geoffrey E. Hinton, Oriol Vinyals and Jeffrey Dean*
<br><br>
### Chris Brockett

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.28) [**Dialogue Response Ranking Training with Large-Scale Human Feedback
Data**](https://doi.org/10.18653/v1/2020.emnlp-main.28),<br> by *Xiang Gao, Yizhe Zhang, Michel Galley, Chris Brockett and Bill Dolan*
<br><br>
### Yizhe Zhang

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/jiachangliu/KATEGPT3) [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br>``
(1) 探索了在in-context learning中什么样的demonstration example可以对GPT-3的效果取得帮助；
``<br>``
(2) 利用roberta对样本进行编码，并计算demonstration与test example的向量距离（欧氏距离），最终发现与test example越相近的demonstration越能取得较好的效果。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.28) [**Dialogue Response Ranking Training with Large-Scale Human Feedback
Data**](https://doi.org/10.18653/v1/2020.emnlp-main.28),<br> by *Xiang Gao, Yizhe Zhang, Michel Galley, Chris Brockett and Bill Dolan*
<br><br>
### Bryan Catanzaro

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04858) [**Re-ViLM: Retrieval-Augmented Visual Language Model for Zero and Few-Shot
Image Captioning**](https://doi.org/10.48550/arXiv.2302.04858),<br> by *Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti, Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Anima Anandkumar

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04858) [**Re-ViLM: Retrieval-Augmented Visual Language Model for Zero and Few-Shot
Image Captioning**](https://doi.org/10.48550/arXiv.2302.04858),<br> by *Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti, Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v80/furlanello18a.html) [**Born-Again Neural Networks**](http://proceedings.mlr.press/v80/furlanello18a.html), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Tommaso Furlanello, Zachary Chase Lipton, Michael Tschannen, Laurent Itti and Anima Anandkumar*
<br><br>
### Mohammad Shoeybi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04858) [**Re-ViLM: Retrieval-Augmented Visual Language Model for Zero and Few-Shot
Image Captioning**](https://doi.org/10.48550/arXiv.2302.04858),<br> by *Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti, Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Chunyuan Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.07094) [**Learning Customized Visual Models with Retrieval-Augmented Knowledge**](https://doi.org/10.48550/arXiv.2301.07094),<br> by *Haotian Liu, Kilho Son, Jianwei Yang, Ce Liu, Jianfeng Gao, Yong Jae Lee and Chunyuan Li*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.03277) [**Instruction Tuning with GPT-4**](https://doi.org/10.48550/arXiv.2304.03277),<br> by *Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Julian J. McAuley

- [<img src=https://img.shields.io/badge/CIKM-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3511808.3557459) [**SPOT: Knowledge-Enhanced Language Representations for Information
Extraction**](https://doi.org/10.1145/3511808.3557459),<br> by *Jiacheng Li, Yannis Katsis, Tyler Baldwin, Ho-Cheol Kim, Andrew Bartko, Julian J. McAuley and Chun-Nan Hsu*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1615) [**Improving Neural Story Generation by Targeted Common Sense Grounding**](https://doi.org/10.18653/v1/D19-1615),<br> by *Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian J. McAuley and Garrison W. Cottrell*
<br><br>
### Songfang Huang

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Wei Wang

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [<img src=https://img.shields.io/badge/ECIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.140) [**StyleDGPT: Stylized Response Generation with Pre-trained Language
Models**](https://doi.org/10.18653/v1/2020.findings-emnlp.140),<br> by *Ze Yang, Wei Wu, Can Xu, Xinnian Liang, Jiaqi Bai, Liran Wang, Wei Wang and Zhoujun Li*
<br><br>
### Nicholas Jing Yuan

- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Zhicheng Wei

- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Marjan Ghazvininejad

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.06031) [**A Review on Language Models as Knowledge Bases**](https://doi.org/10.48550/arXiv.2204.06031),<br> by *Badr AlKhamissi, Millicent Li, Asli Celikyilmaz, Mona T. Diab and Marjan Ghazvininejad*
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{ACL/IJCNLP}
2021,_Online_Event,_August_1--6,_2021-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.366) [**Prompting Contrastive Explanations for Commonsense Reasoning Tasks**](https://doi.org/10.18653/v1/2021.findings-acl.366),<br> by *Bhargavi Paranjape, Julian Michael, Marjan Ghazvininejad, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
### Caiming Xiong

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.12587) [**Model ensemble instead of prompt fusion: a sample-specific knowledge
transfer method for few-shot prompt tuning**](https://doi.org/10.48550/arXiv.2210.12587),<br> by *Xiangyu Peng, Chen Xing, Prafulla Kumar Choubey, Chien-Sheng Wu and Caiming Xiong*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Yu Sun

- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Xiaoyan Zhu

- [<img src=https://img.shields.io/badge/Mach._Intell._Res.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s11633-022-1387-3) [**EVA2.0: Investigating Open-domain Chinese Dialogue Systems with
Large-scale Pre-training**](https://doi.org/10.1007/s11633-022-1387-3),<br> by *Yuxian Gu, Jiaxin Wen, Hao Sun, Yi Song, Pei Ke, Chujie Zheng, Zheng Zhang, Jianzhu Yao et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
- [<img src=https://img.shields.io/badge/TACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Yue Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12095) [**On the Robustness of ChatGPT: An Adversarial and Out-of-distribution
Perspective**](https://doi.org/10.48550/arXiv.2302.12095),<br> by *Jindong Wang, Xixu Hu, Wenxin Hou, Hao Chen, Runkai Zheng, Yidong Wang, Linyi Yang, Haojun Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
### Leonardo F. R. Ribeiro

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2007.08426) [**Investigating Pretrained Language Models for Graph-to-Text Generation**](https://arxiv.org/abs/2007.08426),<br> by *Leonardo F. R. Ribeiro, Martin Schmitt, Hinrich Sch\"utze and Iryna Gurevych*
<br><br>
### Xiao Liu

- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539472) [**Mask and Reason: Pre-Training Knowledge Graph Transformers for Complex
Logical Queries**](https://doi.org/10.1145/3534678.3539472),<br> by *Xiao Liu, Shiyu Zhao, Kai Su, Yukuo Cen, Jiezhong Qiu, Mengdi Zhang, Wei Wu, Yuxiao Dong et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Wenhui Wang

- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Yen Chun Chen

- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Haifeng Wang

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.9) [**PLATO: Pre-trained Dialogue Generation Model with Discrete Latent
Variable**](https://doi.org/10.18653/v1/2020.acl-main.9),<br> by *Siqi Bao, Huang He, Fan Wang, Hua Wu and Haifeng Wang*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Hua Wu

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.9) [**PLATO: Pre-trained Dialogue Generation Model with Discrete Latent
Variable**](https://doi.org/10.18653/v1/2020.acl-main.9),<br> by *Siqi Bao, Huang He, Fan Wang, Hua Wu and Haifeng Wang*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Yasheng Wang

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Xisen Jin

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.351) [**Lifelong Pretraining: Continually Adapting Language Models to Emerging
Corpora**](https://doi.org/10.18653/v1/2022.naacl-main.351),<br> by *Xisen Jin, Dejiao Zhang, Henghui Zhu, Wei Xiao, Shang-Wen Li, Xiaokai Wei, Andrew O. Arnold and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.findings-emnlp.62) [**Learn Continually, Generalize Rapidly: Lifelong Knowledge Accumulation for Few-shot Learning**](https://aclanthology.org/2021.findings-emnlp.62),<br> by *Jin, Xisen , Lin, Bill Yuchen , Rostami, Mohammad  and Ren, Xiang*
<br>``
We present a new learning setup, Continual Learning of Few-Shot Learners, to address challenges of both learning settings in a unified setup, with a hyper-network for task-specific adapter generation.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2020.emnlp-main.158) [**Visually Grounded Continual Learning of Compositional Phrases**](https://www.aclweb.org/anthology/2020.emnlp-main.158),<br> by *Jin, Xisen , Du, Junyi , Sadhu, Arka , Nevatia, Ram  and Ren, Xiang*
<br>``
A novel continual learning setting and a new benchmark for continual caption generation, evaluated with exiting rehearsal-based methods
``
<br><br>
### Mikel Artetxe

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Ari Holtzman

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10539) [**Toward Human Readable Prompt Tuning: Kubrick's The Shining is a good
movie, and a good prompt too?**](https://doi.org/10.48550/arXiv.2212.10539),<br> by *Weijia Shi, Xiaochuang Han, Hila Gonen, Ari Holtzman, Yulia Tsvetkov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/p19-1472) [**HellaSwag: Can a Machine Really Finish Your Sentence?**](https://doi.org/10.18653/v1/p19-1472), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://rowanzellers.com/hellaswag)<br> by *Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi and Yejin Choi*
<br><br>
### Shengding Hu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Ning Ding

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Jie Zhou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.09785) [**Transformer-Patcher: One Mistake worth One Neuron**](https://doi.org/10.48550/arXiv.2301.09785),<br> by *Zeyu Huang, Yikang Shen, Xiaofeng Zhang, Jie Zhou, Wenge Rong and Zhang Xiong*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.10372) [**WeLM: A Well-Read Pre-trained Language Model for Chinese**](https://doi.org/10.48550/arXiv.2209.10372), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://welm.weixin.qq.com/docs/api/)<br> by *Hui Su, Xiao Zhou, Houjin Yu, Yuwen Chen, Zilin Zhu, Yang Yu and Jie Zhou*
<br><br>
### Yankai Lin

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.11432) [**A Survey on Large Language Model based Autonomous Agents**](https://doi.org/10.48550/arXiv.2308.11432),<br> by *Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
### Yujia Qin

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Noah Constant

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.346) [**SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer**](https://doi.org/10.18653/v1/2022.acl-long.346),<br> by *Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou' and Daniel Cer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.243) [**The Power of Scale for Parameter-Efficient Prompt Tuning**](https://doi.org/10.18653/v1/2021.emnlp-main.243),<br> by *Brian Lester, Rami Al-Rfou and Noah Constant*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>``
Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.
``
<br><br>
### Hila Gonen

- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.367) [**Prompting Language Models for Linguistic Structure**](https://doi.org/10.18653/v1/2023.acl-long.367),<br> by *Terra Blevins, Hila Gonen and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10539) [**Toward Human Readable Prompt Tuning: Kubrick's The Shining is a good
movie, and a good prompt too?**](https://doi.org/10.48550/arXiv.2212.10539),<br> by *Weijia Shi, Xiaochuang Han, Hila Gonen, Ari Holtzman, Yulia Tsvetkov and Luke Zettlemoyer*
<br><br>
### Kang Min Yoo

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.08082) [**Self-Generated In-Context Learning: Leveraging Auto-regressive Language
Models as a Demonstration Generator**](https://doi.org/10.48550/arXiv.2206.08082),<br> by *Hyuhng Joon Kim, Hyunsoo Cho, Junyeob Kim, Taeuk Kim, Kang Min Yoo and Sang-goo Lee*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/17527) [**DialogBERT: Discourse-Aware Response Generation via Learning to Recover
and Rank Utterances**](https://ojs.aaai.org/index.php/AAAI/article/view/17527),<br> by *Xiaodong Gu, Kang Min Yoo and Jung-Woo Ha*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.192) [**GPT3Mix: Leveraging Large-scale Language Models for Text Augmentation**](https://doi.org/10.18653/v1/2021.findings-emnlp.192),<br> by *Kang Min Yoo, Dongju Park, Jaewook Kang, Sang-Woo Lee and Woo-Myoung Park*
<br><br>
### Tushar Khot

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.17306) [**Chain-of-Thought Hub: A Continuous Effort to Measure Large Language
Models' Reasoning Performance**](https://doi.org/10.48550/arXiv.2305.17306),<br> by *Yao Fu, Litu Ou, Mingyu Chen, Yuhao Wan, Hao Peng and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Ashish Sabharwal

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
### Yao Fu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.17306) [**Chain-of-Thought Hub: A Continuous Effort to Measure Large Language
Models' Reasoning Performance**](https://doi.org/10.48550/arXiv.2305.17306),<br> by *Yao Fu, Litu Ou, Mingyu Chen, Yuhao Wan, Hao Peng and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Huan Sun

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br>``
(1) 提出了一种迭代式的prompt-tuning方法，他们认为soft prompt应该带有语境，即在自回归解码时不同时刻应该有不同的prompt向量；
``<br>``
(2) 利用BERT为encoder-decoder架构的PLM生成prompt，在每个解码时刻BERT都会根据先前时刻的上下文生成一组新的prompt向量，提供给PLM生成新的上下文，迭代往复。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.329) [**Thinking about GPT-3 In-Context Learning for Biomedical IE? Think
Again**](https://aclanthology.org/2022.findings-emnlp.329),<br> by *Bernal Jimenez Gutierrez, Nikolas McNeal, Clayton Washington, You Chen, Lang Li, Huan Sun and Yu Su*
<br><br>
### Daniel Khashabi

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.50) [**Reframing Instructional Prompts to GPTk's Language**](https://doi.org/10.18653/v1/2022.findings-acl.50),<br> by *Daniel Khashabi, Chitta Baral, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
### Omer Levy

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br>``
(1) 探索了利用LLM在几个样本的情况下归纳出任务指令的能力；
``<br>``
(2) 测量两个指标：1. 模型归纳指令与人类归纳的指令对比，2. 利用模型归纳的指令作为prompt进行预测的执行准确率；
``<br>``
(3) 相比于GPT-3，InstructGPT效果更好，理所当然。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Jacob Devlin

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/n19-1423) [**BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding**](https://doi.org/10.18653/v1/n19-1423), [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) <br> by *Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova*
<br><br>
### Jeff Dean

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Sharan Narang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
### Aakanksha Chowdhery

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.03378) [**PaLM-E: An Embodied Multimodal Language Model**](https://arxiv.org/abs/2303.03378), [<img src=https://img.shields.io/badge/PaLM--E-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.03378) <br> by *Driess, Danny, Xia, Fei, Sajjadi, Mehdi SM, Lynch, Corey, Chowdhery, Aakanksha, Ichter, Brian, Wahid, Ayzaan, Tompson, Jonathan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Mostafa Dehghani

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Barret Zoph

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Le Hou

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Quoc Le

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
### Andrew M. Dai

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Brian Lester

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.346) [**SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer**](https://doi.org/10.18653/v1/2022.acl-long.346),<br> by *Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou' and Daniel Cer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.243) [**The Power of Scale for Parameter-Efficient Prompt Tuning**](https://doi.org/10.18653/v1/2021.emnlp-main.243),<br> by *Brian Lester, Rami Al-Rfou and Noah Constant*
<br><br>
### Todor Mihaylov

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Jingfei Du

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Zhifang Sui

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br>``
(1) 与The Dual Form of Neural Networks Revisited结合一起看，可以进一步理解in-context learning，通过与NN线性层对偶形式的类比，可以将ICL流程描述为：1. 基于Transformer的预训练语言模型作为元优化器；2. 通过正向计算，根据示范例子产生元梯度；3. 通过关注，将元梯度应用于原始语言模型，建立一个ICL模型；
``<br>``
(2)与Fine-tune类似，ICL也是在zero-shot learning参数的基础上，提供了一个更新量。
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.438) [**Calibrating Factual Knowledge in Pretrained Language Models**](https://aclanthology.org/2022.findings-emnlp.438),<br> by *Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui and Lei Li*
<br><br>
### Damai Dai

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br>``
(1) 与The Dual Form of Neural Networks Revisited结合一起看，可以进一步理解in-context learning，通过与NN线性层对偶形式的类比，可以将ICL流程描述为：1. 基于Transformer的预训练语言模型作为元优化器；2. 通过正向计算，根据示范例子产生元梯度；3. 通过关注，将元梯度应用于原始语言模型，建立一个ICL模型；
``<br>``
(2)与Fine-tune类似，ICL也是在zero-shot learning参数的基础上，提供了一个更新量。
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.438) [**Calibrating Factual Knowledge in Pretrained Language Models**](https://aclanthology.org/2022.findings-emnlp.438),<br> by *Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui and Lei Li*
<br><br>
### Rewon Child

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
### others

- [<img src=https://img.shields.io/badge/PLOS_Digital_Health-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198&trk=public_post_comment-text) [**Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models**](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198&trk=public_post_comment-text),<br> by *Kung, Tiffany H, Cheatham, Morgan, Medenilla, Arielle, Sillos, Czarina, De Leon, Lorie, Elepa\~no, Camille, Madriaga, Maria, Aggabao, Rimel et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.03378) [**PaLM-E: An Embodied Multimodal Language Model**](https://arxiv.org/abs/2303.03378), [<img src=https://img.shields.io/badge/PaLM--E-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.03378) <br> by *Driess, Danny, Xia, Fei, Sajjadi, Mehdi SM, Lynch, Corey, Chowdhery, Aakanksha, Ichter, Brian, Wahid, Ayzaan, Tompson, Jonathan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), [<img src=https://img.shields.io/badge/GPT--1-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Gholamreza Haffari

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>``
To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.233) [**Lifelong Explainer for Lifelong Learners**](https://aclanthology.org/2021.emnlp-main.233),<br> by *Situ, Xuelin , Maruf, Sameen , Zukerman, Ingrid , Paris, Cecile  and Haffari, Gholamreza*
<br>``
We propose a novel Lifelong Explanation approach that continuously trains a student explainer under the supervision of a teacher – an arbitrary explanation algorithm – on different tasks undertaken in LL. We also leverage the Experience Replay mechanism to prevent catastrophic forgetting in the student explainer.
``
<br><br>
### Vedant Misra

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Christopher Hesse

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Gretchen Krueger

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Dan Roth

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303),<br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>``
本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09095) [**Rethinking the Role of Scale for In-Context Learning: An Interpretability-based
Case Study at 66 Billion Scale**](https://doi.org/10.48550/arXiv.2212.09095),<br> by *Hritik Bansal, Karthik Gopalakrishnan, Saket Dingliwal, Sravan Bodapati, Katrin Kirchhoff and Dan Roth*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Aston Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Zhuosheng Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Jonathan Berant

- [<img src=https://img.shields.io/badge/EACL-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>``
本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。
``
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EACL}
2023,_Dubrovnik,_Croatia,_May_2--6,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2023.findings-eacl.139) [**Crawling The Internal Knowledge-Base of Language Models**](https://aclanthology.org/2023.findings-eacl.139),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.191) [**Learning To Retrieve Prompts for In-Context Learning**](https://doi.org/10.18653/v1/2022.naacl-main.191), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) <br> by *Ohad Rubin, Jonathan Herzig and Jonathan Berant*
<br>``
This paper proposes a method to retrieve good contexts for in-context learning. Specifically, the method
``<br>``
(1) uses an unsupervised retriever (BM25/SBERT) to obtain a set of context candidates,
``<br>``
(2) passes the candidates to a scoring model (GPT-Neo/GPT-J/GPT-3/Codex) and select the top/bottom k as positive/negative examples,
``<br>``
(3) uses the examples to train a dense retriever (BERT-based).
``
<br><br>
### Nayeon Lee

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
### Jure Leskovec

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
### Hongyu Ren

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
### Greg Durrett

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04813) [**Explanation Selection Using Unlabeled Data for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.04813),<br> by *Xi Ye and Greg Durrett*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356),<br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://par.nsf.gov/biblio/10380030) [**The unreliability of explanations in few-shot prompting for textual reasoning**](https://par.nsf.gov/biblio/10380030),<br> by *Ye, Xi and Durrett, Greg*
<br><br>
### Shuyan Zhou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Program&Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Aman Madaan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07686) [**Text and Patterns: For Effective Chain of Thought, It Takes Two to
Tango**](https://doi.org/10.48550/arXiv.2209.07686),<br> by *Aman Madaan and Amir Yazdanbakhsh*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Mari Ostendorf

- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
### Tao Yu

- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
### Heng Ji

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.12810) [**Code4Struct: Program&Code Generation for Few-Shot Structured Prediction from
Natural Language**](https://doi.org/10.48550/arXiv.2210.12810),<br> by *Xingyao Wang, Sha Li and Heng Ji*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
### George Karypis

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53), [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br>``
This paper proposes in-context tuning, which recasts task adaptation and prediction as a simple sequence prediction problem: to form the input sequence,  concatenate the task instruction, labeled in-context examples, and the target input to predict; to meta train the model to learn from in-context examples, finetune a PLM to predict the target label given the input sequence on a collection of tasks (very similar to MetaICL). On LAMA and BinaryClfs, the proposed method outperforms MAML.
``
<br><br>
- [<img src=https://img.shields.io/badge/IA3-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/IA351965.2020.00011) [**DistDGL: Distributed Graph Neural Network Training for Billion-Scale
Graphs**](https://doi.org/10.1109/IA351965.2020.00011),<br> by *Da Zheng, Chao Ma, Minjie Wang, Jinjing Zhou, Qidong Su, Xiang Song, Quan Gan, Zheng Zhang et al.*
<br><br>
### Peiyu Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.212) [**Small Pre-trained Language Models Can be Fine-tuned as Large Models
via Over-Parameterization**](https://doi.org/10.18653/v1/2023.acl-long.212),<br> by *Ze-Feng Gao, Kun Zhou, Peiyu Liu, Wayne Xin Zhao and Ji-Rong Wen*
<br><br>
### Junjie Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.07001) [**Recommendation as Instruction Following: A Large Language Model
Empowered Recommendation Approach**](https://doi.org/10.48550/arXiv.2305.07001),<br> by *Junjie Zhang, Ruobing Xie, Yupeng Hou, Wayne Xin Zhao, Leyu Lin and Ji-Rong Wen*
<br><br>
### Yupeng Hou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.07001) [**Recommendation as Instruction Following: A Large Language Model
Empowered Recommendation Approach**](https://doi.org/10.48550/arXiv.2305.07001),<br> by *Junjie Zhang, Ruobing Xie, Yupeng Hou, Wayne Xin Zhao, Leyu Lin and Ji-Rong Wen*
<br><br>
### Jiawei Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.14524) [**Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender
System**](https://doi.org/10.48550/arXiv.2303.14524),<br> by *Yunfan Gao, Tao Sheng, Youlin Xiang, Yun Xiong, Haofen Wang and Jiawei Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.11116) [**Graph-ToolFormer: To Empower LLMs with Graph Reasoning Ability via
Prompt Augmented by ChatGPT**](https://doi.org/10.48550/arXiv.2304.11116),<br> by *Jiawei Zhang*
<br><br>
### Jiahui Gao

- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
### Peter Hase

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.15217) [**Open Problems and Fundamental Limitations of Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2307.15217),<br> by *Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, J\'er\'emy Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.137) [**Are Hard Examples also Harder to Explain? A Study with Human and
Model-Generated Explanations**](https://aclanthology.org/2022.emnlp-main.137),<br> by *Swarnadeep Saha, Peter Hase, Nazneen Rajani and Mohit Bansal*
<br><br>
### Xipeng Qiu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.13539) [**Finding Supporting Examples for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.13539),<br> by *Xiaonan Li and Xipeng Qiu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.04964) [**Secrets of RLHF in Large Language Models Part I: PPO**](https://doi.org/10.48550/arXiv.2307.04964),<br> by *Rui Zheng, Shihan Dou, Songyang Gao, Yuan Hua, Wei Shen, Binghai Wang, Yan Liu, Senjie Jin et al.*
<br><br>
### Dorsa Sadigh

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.15217) [**Open Problems and Fundamental Limitations of Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2307.15217),<br> by *Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, J\'er\'emy Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak et al.*
<br><br>
- [<img src=https://img.shields.io/badge/IJRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1177/02783649211041652) [**Learning reward functions from diverse sources of human feedback:
Optimally integrating demonstrations and preferences**](https://doi.org/10.1177/02783649211041652),<br> by *Erdem Biyik, Dylan P. Losey, Malayandi Palan, Nicholas C. Landolfi, Gleb Shevchuk and Dorsa Sadigh*
<br><br>
### Erdem Biyik

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.15217) [**Open Problems and Fundamental Limitations of Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2307.15217),<br> by *Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, J\'er\'emy Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak et al.*
<br><br>
- [<img src=https://img.shields.io/badge/IJRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1177/02783649211041652) [**Learning reward functions from diverse sources of human feedback:
Optimally integrating demonstrations and preferences**](https://doi.org/10.1177/02783649211041652),<br> by *Erdem Biyik, Dylan P. Losey, Malayandi Palan, Nicholas C. Landolfi, Gleb Shevchuk and Dorsa Sadigh*
<br><br>
### Craig Boutilier

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12192) [**Aligning Text-to-Image Models using Human Feedback**](https://doi.org/10.48550/arXiv.2302.12192),<br> by *Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2208.02294) [**Dynamic Planning in Open-Ended Dialogue using Reinforcement Learning**](https://doi.org/10.48550/arXiv.2208.02294),<br> by *Deborah Cohen, Moonkyung Ryu, Yinlam Chow, Orgad Keller, Ido Greenberg, Avinatan Hassidim, Michael Fink, Yossi Matias et al.*
<br><br>
### Moonkyung Ryu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12192) [**Aligning Text-to-Image Models using Human Feedback**](https://doi.org/10.48550/arXiv.2302.12192),<br> by *Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2208.02294) [**Dynamic Planning in Open-Ended Dialogue using Reinforcement Learning**](https://doi.org/10.48550/arXiv.2208.02294),<br> by *Deborah Cohen, Moonkyung Ryu, Yinlam Chow, Orgad Keller, Ido Greenberg, Avinatan Hassidim, Michael Fink, Yossi Matias et al.*
<br><br>
### Nat McAleese

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### Lucy Campbell Gillingham

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### Martin Chadwick

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### John Aslanides

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### Maja Trebacz

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
### Xu Jiang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Wangchunshu Zhou

- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=3k20LAiHYL2) [**Pre-training Text-to-Text Transformers for Concept-centric Common
Sense**](https://openreview.net/forum?id=3k20LAiHYL2),<br> by *Wangchunshu Zhou, Dong-Ho Lee, Ravi Kiran Selvam, Seyeon Lee and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
### Hritik Bansal

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.132) [**GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained
Language Models**](https://aclanthology.org/2022.emnlp-main.132),<br> by *Da Yin, Hritik Bansal, Masoud Monajatipoor, Liunian Harold Li and Kai-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09095) [**Rethinking the Role of Scale for In-Context Learning: An Interpretability-based
Case Study at 66 Billion Scale**](https://doi.org/10.48550/arXiv.2212.09095),<br> by *Hritik Bansal, Karthik Gopalakrishnan, Saket Dingliwal, Sravan Bodapati, Katrin Kirchhoff and Dan Roth*
<br><br>
### Seyeon Lee

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.598) [**RICA: Evaluating Robust Inference Capabilities Based on Commonsense
Axioms**](https://doi.org/10.18653/v1/2021.emnlp-main.598),<br> by *Pei Zhou, Rahul Khanna, Seyeon Lee, Bill Yuchen Lin, Daniel Ho, Jay Pujara and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=3k20LAiHYL2) [**Pre-training Text-to-Text Transformers for Concept-centric Common
Sense**](https://openreview.net/forum?id=3k20LAiHYL2),<br> by *Wangchunshu Zhou, Dong-Ho Lee, Ravi Kiran Selvam, Seyeon Lee and Xiang Ren*
<br><br>
### Pei Zhou

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.598) [**RICA: Evaluating Robust Inference Capabilities Based on Commonsense
Axioms**](https://doi.org/10.18653/v1/2021.emnlp-main.598),<br> by *Pei Zhou, Rahul Khanna, Seyeon Lee, Bill Yuchen Lin, Daniel Ho, Jay Pujara and Xiang Ren*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.165) [**CommonGen: A Constrained Text Generation Challenge for Generative
Commonsense Reasoning**](https://doi.org/10.18653/v1/2020.findings-emnlp.165),<br> by *Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi and Xiang Ren*
<br><br>
### Prithviraj Ammanabrolu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01241) [**Is Reinforcement Learning (Not) for Natural Language Processing?:
Benchmarks, Baselines, and Building Blocks for Natural Language Policy
Optimization**](https://doi.org/10.48550/arXiv.2210.01241),<br> by *Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kiant\'e Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Keisuke Sakaguchi

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09246) [**I2D2: Inductive Knowledge Distillation with NeuroLogic and Self-Imitation**](https://doi.org/10.48550/arXiv.2212.09246),<br> by *Chandra Bhagavatula, Jena D. Hwang, Doug Downey, Ronan Le Bras, Ximing Lu, Keisuke Sakaguchi, Swabha Swayamdipta, Peter West et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
### Liwei Jiang

- [<img src=https://img.shields.io/badge/the_2022_Conference_of_the_North_American_Chapter_of
the_Association_for_Computational_Linguistics:_Human_Language_Technologies,
{NAACL}_2022,_Seattle,_WA,_United_States,_July_10--15,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.341) [**Symbolic Knowledge Distillation: from General Language Models to Commonsense
Models**](https://doi.org/10.18653/v1/2022.naacl-main.341),<br> by *Peter West, Chandra Bhagavatula, Jack Hessel, Jena D. Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu, Sean Welleck et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Jiacheng Liu

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.611) [**Rainier: Reinforced Knowledge Introspector for Commonsense Question
Answering**](https://aclanthology.org/2022.emnlp-main.611),<br> by *Jiacheng Liu, Skyler Hallinan, Ximing Lu, Pengfei He, Sean Welleck, Hannaneh Hajishirzi and Yejin Choi*
<br><br>
### OpenAI

- [<img src=https://img.shields.io/badge/OpenAI-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/papers/gpt-4.pdf) [**GPT-4 Technical Report**](https://cdn.openai.com/papers/gpt-4.pdf), [<img src=https://img.shields.io/badge/GPT--4-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/papers/gpt-4.pdf) <br> by *OpenAI*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/papers/gpt-4-system-card.pdf) [**GPT-4 System Card**](https://cdn.openai.com/papers/gpt-4-system-card.pdf), [<img src=https://img.shields.io/badge/GPT--4-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/papers/gpt-4.pdf) <br> by *OpenAI*
<br><br>
### Nazneen Rajani

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=DhzIU48OcZh) [**P-Adapters: Robustly Extracting Factual Information from Language
Models with Diverse Prompts**](https://openreview.net/forum?id=DhzIU48OcZh),<br> by *Benjamin Newman, Prafulla Kumar Choubey and Nazneen Rajani*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.137) [**Are Hard Examples also Harder to Explain? A Study with Human and
Model-Generated Explanations**](https://aclanthology.org/2022.emnlp-main.137),<br> by *Swarnadeep Saha, Peter Hase, Nazneen Rajani and Mohit Bansal*
<br><br>
### Prafulla Kumar Choubey

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=DhzIU48OcZh) [**P-Adapters: Robustly Extracting Factual Information from Language
Models with Diverse Prompts**](https://openreview.net/forum?id=DhzIU48OcZh),<br> by *Benjamin Newman, Prafulla Kumar Choubey and Nazneen Rajani*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.12587) [**Model ensemble instead of prompt fusion: a sample-specific knowledge
transfer method for few-shot prompt tuning**](https://doi.org/10.48550/arXiv.2210.12587),<br> by *Xiangyu Peng, Chen Xing, Prafulla Kumar Choubey, Chien-Sheng Wu and Caiming Xiong*
<br><br>
### Chenfei Wu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.04671) [**Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models**](https://arxiv.org/abs/2303.04671),<br> by *Wu, Chenfei, Yin, Shengming, Qi, Weizhen, Wang, Xiaodong, Tang, Zecheng and Duan, Nan*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.10464) [**Learning to Program with Natural Language**](https://doi.org/10.48550/arXiv.2304.10464),<br> by *Yiduo Guo, Yaobo Liang, Chenfei Wu, Wenshan Wu, Dongyan Zhao and Nan Duan*
<br><br>
### Jacob Menick

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/borgeaud22a.html) [**Improving Language Models by Retrieving from Trillions of Tokens**](https://proceedings.mlr.press/v162/borgeaud22a.html),<br> by *Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.11147) [**Teaching language models to support answers with verified quotes**](https://doi.org/10.48550/arXiv.2203.11147),<br> by *Jacob Menick, Maja Trebacz, Vladimir Mikulik, John Aslanides, H. Francis Song, Martin Chadwick, Mia Glaese, Susannah Young et al.*
<br><br>
### Wei Ping

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04858) [**Re-ViLM: Retrieval-Augmented Visual Language Model for Zero and Few-Shot
Image Captioning**](https://doi.org/10.48550/arXiv.2302.04858),<br> by *Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti, Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
### Edouard Grave

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [<img src=https://img.shields.io/badge/arXiv_preprint_arXiv-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2208.03299) [**Atlas: Few-shot learning with retrieval augmented language models**](https://arxiv.org/abs/2208.03299),<br> by *Izacard, Gautier, Lewis, Patrick, Lomeli, Maria, Hosseini, Lucas, Petroni, Fabio, Schick, Timo, Dwivedi-Yu, Jane, Joulin, Armand et al.*
<br><br>
### Timo Schick

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [<img src=https://img.shields.io/badge/arXiv_preprint_arXiv-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2208.03299) [**Atlas: Few-shot learning with retrieval augmented language models**](https://arxiv.org/abs/2208.03299),<br> by *Izacard, Gautier, Lewis, Patrick, Lomeli, Maria, Hosseini, Lucas, Petroni, Fabio, Schick, Timo, Dwivedi-Yu, Jane, Joulin, Armand et al.*
<br><br>
### Maria Lomeli

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [<img src=https://img.shields.io/badge/arXiv_preprint_arXiv-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2208.03299) [**Atlas: Few-shot learning with retrieval augmented language models**](https://arxiv.org/abs/2208.03299),<br> by *Izacard, Gautier, Lewis, Patrick, Lomeli, Maria, Hosseini, Lucas, Petroni, Fabio, Schick, Timo, Dwivedi-Yu, Jane, Joulin, Armand et al.*
<br><br>
### Rich James

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12652) [**REPLUG: Retrieval-Augmented Black-Box Language Models**](https://doi.org/10.48550/arXiv.2301.12652),<br> by *Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer and Wen-tau Yih*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12561) [**Retrieval-Augmented Multimodal Language Modeling**](https://doi.org/10.48550/arXiv.2211.12561),<br> by *Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Rich James, Jure Leskovec, Percy Liang, Mike Lewis, Luke Zettlemoyer et al.*
<br><br>
### Lemao Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.13217) [**Fairness-guided Few-shot Prompting for Large Language Models**](https://doi.org/10.48550/arXiv.2303.13217),<br> by *Huan Ma, Changqing Zhang, Yatao Bian, Lemao Liu, Zhirui Zhang, Peilin Zhao, Shu Zhang, Huazhu Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2202.01110) [**A Survey on Retrieval-Augmented Text Generation**](https://arxiv.org/abs/2202.01110),<br> by *Huayang Li, Yixuan Su, Deng Cai, Yan Wang and Lemao Liu*
<br><br>
### Chelsea Finn

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=0DcZxeWfOPt) [**Fast Model Editing at Scale**](https://openreview.net/forum?id=0DcZxeWfOPt),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn and Christopher D. Manning*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/mitchell22a.html) [**Memory-Based Model Editing at Scale**](https://proceedings.mlr.press/v162/mitchell22a.html),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning and Chelsea Finn*
<br><br>
### Charles Lin

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=0DcZxeWfOPt) [**Fast Model Editing at Scale**](https://openreview.net/forum?id=0DcZxeWfOPt),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn and Christopher D. Manning*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/mitchell22a.html) [**Memory-Based Model Editing at Scale**](https://proceedings.mlr.press/v162/mitchell22a.html),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning and Chelsea Finn*
<br><br>
### Eric Mitchell

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=0DcZxeWfOPt) [**Fast Model Editing at Scale**](https://openreview.net/forum?id=0DcZxeWfOPt),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn and Christopher D. Manning*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/mitchell22a.html) [**Memory-Based Model Editing at Scale**](https://proceedings.mlr.press/v162/mitchell22a.html),<br> by *Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning and Chelsea Finn*
<br><br>
### Kentaro Inui

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.eacl-main.153) [**Language Models as Knowledge Bases: On Entity Representations, Storage
Capacity, and Paraphrased Queries**](https://doi.org/10.18653/v1/2021.eacl-main.153),<br> by *Benjamin Heinzerling and Kentaro Inui*
<br><br>
### Amnon Shashua

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00083) [**In-Context Retrieval-Augmented Language Models**](https://doi.org/10.48550/arXiv.2302.00083),<br> by *Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown and Yoav Shoham*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07895) [**The Learnability of In-Context Learning**](https://doi.org/10.48550/arXiv.2303.07895),<br> by *Noam Wies, Yoav Levine and Amnon Shashua*
<br><br>
### Yoav Levine

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00083) [**In-Context Retrieval-Augmented Language Models**](https://doi.org/10.48550/arXiv.2302.00083),<br> by *Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown and Yoav Shoham*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07895) [**The Learnability of In-Context Learning**](https://doi.org/10.48550/arXiv.2303.07895),<br> by *Noam Wies, Yoav Levine and Amnon Shashua*
<br><br>
### Dongyan Zhao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.01081) [**Can BERT Refrain from Forgetting on Sequential Tasks? A Probing
Study**](https://doi.org/10.48550/arXiv.2303.01081),<br> by *Mingxu Tao, Yansong Feng and Dongyan Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.10464) [**Learning to Program with Natural Language**](https://doi.org/10.48550/arXiv.2304.10464),<br> by *Yiduo Guo, Yaobo Liang, Chenfei Wu, Wenshan Wu, Dongyan Zhao and Nan Duan*
<br><br>
### Patrick S. H. Lewis

- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1250) [**Language Models as Knowledge Bases?**](https://doi.org/10.18653/v1/D19-1250),<br> by *Fabio Petroni, Tim Rockt\"aschel, Sebastian Riedel, Patrick S. H. Lewis, Anton Bakhtin, Yuxiang Wu and Alexander H. Miller*
<br><br>
### Tim Rockt{\"{a}}schel

- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html),<br> by *Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K\"uttler, Mike Lewis et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1250) [**Language Models as Knowledge Bases?**](https://doi.org/10.18653/v1/D19-1250),<br> by *Fabio Petroni, Tim Rockt\"aschel, Sebastian Riedel, Patrick S. H. Lewis, Anton Bakhtin, Yuxiang Wu and Alexander H. Miller*
<br><br>
### Tuo Zhao

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Chen Liang

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Qingru Zhang

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Simiao Zuo

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Jiawei Han

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2202.04538) [**Generating Training Data with Language Models: Towards Zero-Shot Language
Understanding**](https://arxiv.org/abs/2202.04538),<br> by *Yu Meng, Jiaxin Huang, Yu Zhang and Jiawei Han*
<br><br>
### Jiaxin Huang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2202.04538) [**Generating Training Data with Language Models: Towards Zero-Shot Language
Understanding**](https://arxiv.org/abs/2202.04538),<br> by *Yu Meng, Jiaxin Huang, Yu Zhang and Jiawei Han*
<br><br>
### Beichen Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Sebastian Borgeaud

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/borgeaud22a.html) [**Improving Language Models by Retrieving from Trillions of Tokens**](https://proceedings.mlr.press/v162/borgeaud22a.html),<br> by *Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau et al.*
<br><br>
### Douglas C. Schmidt

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11382) [**A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**](https://doi.org/10.48550/arXiv.2302.11382),<br> by *Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07839) [**ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements
Elicitation, and Software Design**](https://doi.org/10.48550/arXiv.2303.07839),<br> by *Jules White, Sam Hays, Quchen Fu, Jesse Spencer-Smith and Douglas C. Schmidt*
<br><br>
### Jesse Spencer Smith

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11382) [**A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**](https://doi.org/10.48550/arXiv.2302.11382),<br> by *Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07839) [**ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements
Elicitation, and Software Design**](https://doi.org/10.48550/arXiv.2303.07839),<br> by *Jules White, Sam Hays, Quchen Fu, Jesse Spencer-Smith and Douglas C. Schmidt*
<br><br>
### Sam Hays

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11382) [**A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**](https://doi.org/10.48550/arXiv.2302.11382),<br> by *Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07839) [**ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements
Elicitation, and Software Design**](https://doi.org/10.48550/arXiv.2303.07839),<br> by *Jules White, Sam Hays, Quchen Fu, Jesse Spencer-Smith and Douglas C. Schmidt*
<br><br>
### Quchen Fu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11382) [**A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**](https://doi.org/10.48550/arXiv.2302.11382),<br> by *Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07839) [**ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements
Elicitation, and Software Design**](https://doi.org/10.48550/arXiv.2303.07839),<br> by *Jules White, Sam Hays, Quchen Fu, Jesse Spencer-Smith and Douglas C. Schmidt*
<br><br>
### Jules White

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11382) [**A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**](https://doi.org/10.48550/arXiv.2302.11382),<br> by *Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse Spencer-Smith et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.07839) [**ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements
Elicitation, and Software Design**](https://doi.org/10.48550/arXiv.2303.07839),<br> by *Jules White, Sam Hays, Quchen Fu, Jesse Spencer-Smith and Douglas C. Schmidt*
<br><br>
### Chris Olah

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Tom Conerly

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Stanislav Fort

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Andy Jones

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Punit Singh Koura

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Shuohui Chen

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Xian Li

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Xi Victoria Lin

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Sam Shleifer

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Dani Yogatama

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html) [**Episodic Memory in Lifelong Language Learning**](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html),<br> by *Cyprien de Masson d'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama*
<br>``
MbPA++. This paper proposes the use of memory (a fixed memory network) in life-long learning to prevent catastrophic forgetting by means of  experience replay and local adaptation. 
``
<br><br>
### Cyprien de Masson d'Autume

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/liska22a.html) [**StreamingQA: A Benchmark for Adaptation to New Knowledge over Time
in Question Answering Models**](https://proceedings.mlr.press/v162/liska22a.html),<br> by *Adam Liska, Tom\'as Kocisk\'y, Elena Gribovskaya, Tayfun Terzi, Eren Sezener, Devang Agrawal, Cyprien de Masson d'Autume, Tim Scholtes et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html) [**Episodic Memory in Lifelong Language Learning**](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html),<br> by *Cyprien de Masson d'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama*
<br>``
MbPA++. This paper proposes the use of memory (a fixed memory network) in life-long learning to prevent catastrophic forgetting by means of  experience replay and local adaptation. 
``
<br><br>
### Yubo Chen

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.628) [**CN-AutoMIC: Distilling Chinese Commonsense Knowledge from Pretrained
Language Models**](https://aclanthology.org/2022.emnlp-main.628),<br> by *Chenhao Wang, Jiachun Li, Yubo Chen, Kang Liu and Jun Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2020.emnlp-main.52) [**Incremental Event Detection via Knowledge Consolidation Networks**](https://www.aclweb.org/anthology/2020.emnlp-main.52),<br> by *Cao, Pengfei , Chen, Yubo , Zhao, Jun  and Wang, Taifeng*
<br>``
Proposing a hybrid continual learning method for event detection, combining experience replay and Knowledge Distillation, focusing on (1) semantic ambiguity in NLP and (2) data imbalance between memory and current task.
``
<br><br>
### Liying Cheng

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.15038) [**Is GPT-4 a Good Data Analyst?**](https://doi.org/10.48550/arXiv.2305.15038),<br> by *Liying Cheng, Xingxuan Li and Lidong Bing*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>``
we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness: it tendsto outperform fine-tuning on both low-resource and cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to fine-tuning.
``
<br><br>
### Fan Yang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
### Pengfei Cao

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2020.emnlp-main.52) [**Incremental Event Detection via Knowledge Consolidation Networks**](https://www.aclweb.org/anthology/2020.emnlp-main.52),<br> by *Cao, Pengfei , Chen, Yubo , Zhao, Jun  and Wang, Taifeng*
<br>``
Proposing a hybrid continual learning method for event detection, combining experience replay and Knowledge Distillation, focusing on (1) semantic ambiguity in NLP and (2) data imbalance between memory and current task.
``
<br><br>
### Qingbin Liu

- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>``
This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>``
We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.
``
<br><br>
### Joongbo Shin

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>``
We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.418) [**TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving
Language Models**](https://aclanthology.org/2022.emnlp-main.418),<br> by *Joel Jang, Seonghyeon Ye, Changho Lee, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun Kim and Minjoon Seo*
<br><br>
### Xuanjing Huang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.04964) [**Secrets of RLHF in Large Language Models Part I: PPO**](https://doi.org/10.48550/arXiv.2307.04964),<br> by *Rui Zheng, Shihan Dou, Songyang Gao, Yuan Hua, Wei Shen, Binghai Wang, Yan Liu, Senjie Jin et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>``
We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
``<br>``
and supports the development of versatile
``<br>``
knowledge-infused model.
``
<br><br>
### Lei Shu

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>``
NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>``
The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.
``
<br><br>
### Hu Xu

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>``
NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>``
The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.
``
<br><br>
### Wanxiang Che

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>``
We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.
``
<br><br>
### Yiming Cui

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>``
We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.
``
<br><br>
### Danqi Chen

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.382) [**Training Language Models with Memory Augmentation**](https://aclanthology.org/2022.emnlp-main.382),<br> by *Zexuan Zhong, Tao Lei and Danqi Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Kenton Lee

- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.08909) [**REALM: Retrieval-Augmented Language Model Pre-Training**](https://arxiv.org/abs/2002.08909),<br> by *Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat and Ming-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/n19-1423) [**BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding**](https://doi.org/10.18653/v1/n19-1423), [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) <br> by *Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova*
<br><br>
### Ming Wei Chang

- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.08909) [**REALM: Retrieval-Augmented Language Model Pre-Training**](https://arxiv.org/abs/2002.08909),<br> by *Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat and Ming-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/n19-1423) [**BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding**](https://doi.org/10.18653/v1/n19-1423), [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) <br> by *Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova*
<br><br>
### Tom Brown

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Ben Mann

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Sam Ringer

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Eli Tran Johnson

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Nicholas Schiefer

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.07858) [**Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors,
and Lessons Learned**](https://doi.org/10.48550/arXiv.2209.07858),<br> by *Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez et al.*
<br><br>
### Xingxuan Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.15038) [**Is GPT-4 a Good Data Analyst?**](https://doi.org/10.48550/arXiv.2305.15038),<br> by *Liying Cheng, Xingxuan Li and Lidong Bing*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
### Bosheng Ding

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>``
we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness: it tendsto outperform fine-tuning on both low-resource and cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to fine-tuning.
``
<br><br>
### Yichong Xu

- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.150) [**Dict-BERT: Enhancing Language Model Pre-training with Dictionary**](https://doi.org/10.18653/v1/2022.findings-acl.150),<br> by *Wenhao Yu, Chenguang Zhu, Yuwei Fang, Donghan Yu, Shuohang Wang, Yichong Xu, Michael Zeng and Meng Jiang*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
### Jasper Snoek

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
### Michael W. Dusenberry

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
### Xiaohua Zhai

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Mario Lucic

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Joan Puigcerver

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Matthias Minderer

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Rodolphe Jenatton

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
### Basil Mustafa

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Josip Djolonga

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Qi Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.04964) [**Secrets of RLHF in Large Language Models Part I: PPO**](https://doi.org/10.48550/arXiv.2307.04964),<br> by *Rui Zheng, Shihan Dou, Songyang Gao, Yuan Hua, Wei Shen, Binghai Wang, Yan Liu, Senjie Jin et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
### Ming Gao

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.207) [**Knowledge Prompting in Pre-trained Language Model for Natural Language
Understanding**](https://aclanthology.org/2022.emnlp-main.207),<br> by *Jianing Wang, Wenkang Huang, Minghui Qiu, Qiuhui Shi, Hongbin Wang, Xiang Li and Ming Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
### Xiang Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.13007) [**ChatAug: Leveraging ChatGPT for Text Data Augmentation**](https://doi.org/10.48550/arXiv.2302.13007),<br> by *Haixing Dai, Zhengliang Liu, Wenxiong Liao, Xiaoke Huang, Zihao Wu, Lin Zhao, Wei Liu, Ninghao Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.207) [**Knowledge Prompting in Pre-trained Language Model for Natural Language
Understanding**](https://aclanthology.org/2022.emnlp-main.207),<br> by *Jianing Wang, Wenkang Huang, Minghui Qiu, Qiuhui Shi, Hongbin Wang, Xiang Li and Ming Gao*
<br><br>
### Qiuhui Shi

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.207) [**Knowledge Prompting in Pre-trained Language Model for Natural Language
Understanding**](https://aclanthology.org/2022.emnlp-main.207),<br> by *Jianing Wang, Wenkang Huang, Minghui Qiu, Qiuhui Shi, Hongbin Wang, Xiang Li and Ming Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
### Minghui Qiu

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.207) [**Knowledge Prompting in Pre-trained Language Model for Natural Language
Understanding**](https://aclanthology.org/2022.emnlp-main.207),<br> by *Jianing Wang, Wenkang Huang, Minghui Qiu, Qiuhui Shi, Hongbin Wang, Xiang Li and Ming Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
### Jianing Wang

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.207) [**Knowledge Prompting in Pre-trained Language Model for Natural Language
Understanding**](https://aclanthology.org/2022.emnlp-main.207),<br> by *Jianing Wang, Wenkang Huang, Minghui Qiu, Qiuhui Shi, Hongbin Wang, Xiang Li and Ming Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
### Shaohan Huang

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
### Yunzhi Yao

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
### Xiaodan Liang

- [<img src=https://img.shields.io/badge/ICLR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=h5OpjGd_lo6) [**Self-Guided Noise-Free Data Generation for Efficient Zero-Shot Learning**](https://openreview.net/forum?id=h5OpjGd_lo6),<br> by *Gao, Jiahui, Pi, Renjie, Yong, LIN, Xu, Hang, Ye, Jiacheng, Wu, Zhiyong, ZHANG, WEIZHONG, Liang, Xiaodan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.218) [**UniGeo: Unifying Geometry Logical Reasoning via Reformulating Mathematical
Expression**](https://aclanthology.org/2022.emnlp-main.218),<br> by *Jiaqi Chen, Tong Li, Jinghui Qin, Pan Lu, Liang Lin, Chongyu Chen and Xiaodan Liang*
<br><br>
### Litu Ou

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.17306) [**Chain-of-Thought Hub: A Continuous Effort to Measure Large Language
Models' Reasoning Performance**](https://doi.org/10.48550/arXiv.2305.17306),<br> by *Yao Fu, Litu Ou, Mingyu Chen, Yuhao Wan, Hao Peng and Tushar Khot*
<br><br>
### William W. Cohen

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
- [<img src=https://img.shields.io/badge/Trans._Assoc._Comput._Linguistics-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1162/tacl\_a\_00459) [**Time-Aware Language Models as Temporal Knowledge Bases**](https://doi.org/10.1162/tacl\_a\_00459),<br> by *Bhuwan Dhingra, Jeremy R. Cole, Julian Martin Eisenschlos, Daniel Gillick, Jacob Eisenstein and William W. Cohen*
<br><br>
### Xinyi Wang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.11916) [**Large Language Models Are Implicitly Topic Models: Explaining and
Finding Good Demonstrations for In-Context Learning**](https://doi.org/10.48550/arXiv.2301.11916),<br> by *Xinyi Wang, Wanrong Zhu and William Yang Wang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
### Swarnadeep Saha

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.137) [**Are Hard Examples also Harder to Explain? A Study with Human and
Model-Generated Explanations**](https://aclanthology.org/2022.emnlp-main.137),<br> by *Swarnadeep Saha, Peter Hase, Nazneen Rajani and Mohit Bansal*
<br><br>
### Deepak Ramachandran

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.11293) [**Understanding Finetuning for Factual Knowledge Extraction from Language
Models**](https://doi.org/10.48550/arXiv.2301.11293),<br> by *Mehran Kazemi, Sid Mittal and Deepak Ramachandran*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.13894) [**LAMBADA: Backward Chaining for Automated Reasoning in Natural Language**](https://doi.org/10.48550/arXiv.2212.13894),<br> by *Seyed Mehran Kazemi, Najoung Kim, Deepti Bhatia, Xin Xu and Deepak Ramachandran*
<br><br>
### Xin Xu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2305.01555) [**How to Unleash the Power of Large Language Models for Few-shot Relation
Extraction?**](https://doi.org/10.48550/arXiv.2305.01555),<br> by *Xin Xu, Yuqi Zhu, Xiaohan Wang and Ningyu Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.13894) [**LAMBADA: Backward Chaining for Automated Reasoning in Natural Language**](https://doi.org/10.48550/arXiv.2212.13894),<br> by *Seyed Mehran Kazemi, Najoung Kim, Deepti Bhatia, Xin Xu and Deepak Ramachandran*
<br><br>
### Haifeng Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.02093) [**Knowledge-enhanced Neural Machine Reasoning: A Review**](https://doi.org/10.48550/arXiv.2302.02093),<br> by *Tanmoy Chowdhury, Chen Ling, Xuchao Zhang, Xujiang Zhao, Guangji Bai, Jian Pei, Haifeng Chen and Liang Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.08081) [**Exploring the Limits of ChatGPT for Query or Aspect-based Text Summarization**](https://doi.org/10.48550/arXiv.2302.08081),<br> by *Xianjun Yang, Yan Li, Xinlu Zhang, Haifeng Chen and Wei Cheng*
<br><br>
### Jian Pei

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.02093) [**Knowledge-enhanced Neural Machine Reasoning: A Review**](https://doi.org/10.48550/arXiv.2302.02093),<br> by *Tanmoy Chowdhury, Chen Ling, Xuchao Zhang, Xujiang Zhao, Guangji Bai, Jian Pei, Haifeng Chen and Liang Zhao*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
### Faeze Brahman

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.00053) [**Generating Sequences by Learning to Self-Correct**](https://doi.org/10.48550/arXiv.2211.00053),<br> by *Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi and Yejin Choi*
<br><br>
### Lianhui Qin

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.13636) [**Quark: Controllable Text Generation with Reinforced Unlearning**](https://doi.org/10.48550/arXiv.2205.13636),<br> by *Ximing Lu, Sean Welleck, Liwei Jiang, Jack Hessel, Lianhui Qin, Peter West, Prithviraj Ammanabrolu and Yejin Choi*
<br><br>
### Hanlin Zhang

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=8lNy3QCaxHX) [**Improved logical reasoning of language models via differentiable symbolic programming**](https://openreview.net/forum?id=8lNy3QCaxHX),<br> by *Zhang, Hanlin, Li, Ziyang, Huang, Jiani, Naik, Mayur and Xing, Eric*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
### Tongtong Wu

- [<img src=https://img.shields.io/badge/COLING-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.coling-1.200) [**Event Causality Identification via Derivative Prompt Joint Learning**](https://aclanthology.org/2022.coling-1.200),<br> by *Shirong Shen, Heng Zhou, Tongtong Wu and Guilin Qi*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>``
To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.
``
<br><br>
### Haoyu Wang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.10620) [**Large Language Models for Software Engineering: A Systematic Literature
Review**](https://doi.org/10.48550/arXiv.2308.10620),<br> by *Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Linh Ngo Van

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Hieu Man

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Thien Nguyen

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Franck Dernoncourt

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Bonan Min

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/ECML-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Minh Van Nguyen

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/ECML-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Amir Pouran Ben Veyseh

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.starsem-1.11) [**Word-Label Alignment for Event Detection: A New Perspective via
Optimal Transport**](https://doi.org/10.18653/v1/2022.starsem-1.11),<br> by *Amir Pouran Ben Veyseh and Thien Huu Nguyen*
<br><br>
- [<img src=https://img.shields.io/badge/ECML-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Orhan Firat

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>``
Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.
``
<br><br>
### Katherine Lee

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
### Aitor Lewkowycz

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
### Xavier Garcia

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>``
Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.
``
<br><br>
### Henryk Michalewski

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
### Guy Gur Ari

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
### Sebastian Gehrmann

- [<img src=https://img.shields.io/badge/-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.17564) [**BloombergGPT: A Large Language Model for Finance**](https://arxiv.org/abs/2303.17564),<br> by *Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Jing Sha

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Zheng Gong

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Nathanael Sch{\"{a}}rli

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
### Nathan Scales

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br>``
(1) 两阶段的prompt，第一阶段问题分解（通过in-context learning实现，context中包含了其他问题的分解示例），对于每个问题，分解出回答该问题需要先回答什么子问题；
``<br>``
(2) 在第二阶段中，从后往前依次解决子问题，同样通过in-context learing得到，每次LLM的回答会参与组成下一个问题的prompt。
``
<br><br>
### Jiangtao Feng

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br>``
This paper proposes a LM named EvaLM to scale up the sequence length (trained with 8k tokens per batch line). Experiments based on EvaLM prove that in-context learning can achieve higher performance with more demonstrations under many-shot instruction tuning (8k) and further extending the length of instructions (16k) can further improve the upper bound of scaling in-context  learning.
``
<br><br>
- [<img src=https://img.shields.io/badge/the_2022_Conference_on_Empirical_Methods_in_Natural
Language_Processing,_{EMNLP}_2022,_Abu_Dhabi,_United_Arab_Emirates,
December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.801) [**ZeroGen: Efficient Zero-shot Learning via Dataset Generation**](https://aclanthology.org/2022.emnlp-main.801),<br> by *Jiacheng Ye, Jiahui Gao, Qintong Li, Hang Xu, Jiangtao Feng, Zhiyong Wu, Tao Yu and Lingpeng Kong*
<br><br>
### Diyi Yang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>``
Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.
``
<br><br>
### Jiaao Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>``
Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.
``
<br><br>
### Xi Ye

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04813) [**Explanation Selection Using Unlabeled Data for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.04813),<br> by *Xi Ye and Greg Durrett*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://par.nsf.gov/biblio/10380030) [**The unreliability of explanations in few-shot prompting for textual reasoning**](https://par.nsf.gov/biblio/10380030),<br> by *Ye, Xi and Durrett, Greg*
<br><br>
### Hongxia Jin

- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.212) [**Hyperparameter-free Continuous Learning for Domain Classification in Natural Language Understanding**](https://www.aclweb.org/anthology/2021.naacl-main.212),<br> by *Hua, Ting , Shen, Yilin , Zhao, Changsheng , Hsu, Yen-Chang  and Jin, Hongxia*
<br>``
Inspired by EWC and proposing a hyperparameter-free (Fisher information-based) sampling method for memory replay.
``
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/5465) [**Towards Hands-Free Visual Dialog Interactive Recommendation**](https://ojs.aaai.org/index.php/AAAI/article/view/5465),<br> by *Tong Yu, Yilin Shen and Hongxia Jin*
<br><br>
### Yilin Shen

- [<img src=https://img.shields.io/badge/NAACL--HLT-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://www.aclweb.org/anthology/2021.naacl-main.212) [**Hyperparameter-free Continuous Learning for Domain Classification in Natural Language Understanding**](https://www.aclweb.org/anthology/2021.naacl-main.212),<br> by *Hua, Ting , Shen, Yilin , Zhao, Changsheng , Hsu, Yen-Chang  and Jin, Hongxia*
<br>``
Inspired by EWC and proposing a hyperparameter-free (Fisher information-based) sampling method for memory replay.
``
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/5465) [**Towards Hands-Free Visual Dialog Interactive Recommendation**](https://ojs.aaai.org/index.php/AAAI/article/view/5465),<br> by *Tong Yu, Yilin Shen and Hongxia Jin*
<br><br>
### Phil Blunsom

- [<img src=https://img.shields.io/badge/ICML-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.mlr.press/v162/liska22a.html) [**StreamingQA: A Benchmark for Adaptation to New Knowledge over Time
in Question Answering Models**](https://proceedings.mlr.press/v162/liska22a.html),<br> by *Adam Liska, Tom\'as Kocisk\'y, Elena Gribovskaya, Tayfun Terzi, Eren Sezener, Devang Agrawal, Cyprien de Masson d'Autume, Tim Scholtes et al.*
<br><br>
- [<img src=https://img.shields.io/badge/TACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1162/tacl\_a\_00390) [**Pretraining the Noisy Channel Model for Task-Oriented Dialogue**](https://doi.org/10.1162/tacl\_a\_00390),<br> by *Qi Liu, Lei Yu, Laura Rimell and Phil Blunsom*
<br><br>
### Chien Sheng Wu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.12587) [**Model ensemble instead of prompt fusion: a sample-specific knowledge
transfer method for few-shot prompt tuning**](https://doi.org/10.48550/arXiv.2210.12587),<br> by *Xiangyu Peng, Chen Xing, Prafulla Kumar Choubey, Chien-Sheng Wu and Caiming Xiong*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
### Derek Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.01580) [**Mixture of Soft Prompts for Controllable Data Generation**](https://doi.org/10.48550/arXiv.2303.01580),<br> by *Derek Chen, Celine Lee, Yunan Lu, Domenic Rosati and Zhou Yu*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.239) [**Action-Based Conversations Dataset: A Corpus for Building More In-Depth
Task-Oriented Dialogue Systems**](https://doi.org/10.18653/v1/2021.naacl-main.239),<br> by *Derek Chen, Howard Chen, Yi Yang, Alexander Lin and Zhou Yu*
<br><br>
### Erik Cambria

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Jinjie Ni

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Vlad Pandelea

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Tom Young

- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Zhaojiang Lin

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>``
Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.
``
<br><br>
### Hao Cheng

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.09842) [**Chameleon: Plug-and-Play Compositional Reasoning with Large Language
Models**](https://doi.org/10.48550/arXiv.2304.09842),<br> by *Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu and Jianfeng Gao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
### Xing Xie

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12095) [**On the Robustness of ChatGPT: An Adversarial and Out-of-distribution
Perspective**](https://doi.org/10.48550/arXiv.2302.12095),<br> by *Jindong Wang, Xixu Hu, Wenxin Hou, Hao Chen, Runkai Zheng, Yidong Wang, Linyi Yang, Haojun Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/TKDE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/TKDE.2020.3028705) [**A Survey on Knowledge Graph-Based Recommender Systems**](https://doi.org/10.1109/TKDE.2020.3028705),<br> by *Qingyu Guo, Fuzhen Zhuang, Chuan Qin, Hengshu Zhu, Xing Xie, Hui Xiong and Qing He*
<br><br>
### Kevin Murphy

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICCV-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/ICCV.2019.00756) [**VideoBERT: A Joint Model for Video and Language Representation Learning**](https://doi.org/10.1109/ICCV.2019.00756),<br> by *Chen Sun, Austin Myers, Carl Vondrick, Kevin Murphy and Cordelia Schmid*
<br><br>
### Da Yin

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.132) [**GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained
Language Models**](https://aclanthology.org/2022.emnlp-main.132),<br> by *Da Yin, Hritik Bansal, Masoud Monajatipoor, Liunian Harold Li and Kai-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1908.03557) [**VisualBERT: A Simple and Performant Baseline for Vision and Language**](http://arxiv.org/abs/1908.03557),<br> by *Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh and Kai-Wei Chang*
<br><br>
### Liunian Harold Li

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.132) [**GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained
Language Models**](https://aclanthology.org/2022.emnlp-main.132),<br> by *Da Yin, Hritik Bansal, Masoud Monajatipoor, Liunian Harold Li and Kai-Wei Chang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1908.03557) [**VisualBERT: A Simple and Performant Baseline for Vision and Language**](http://arxiv.org/abs/1908.03557),<br> by *Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh and Kai-Wei Chang*
<br><br>
### Luowei Zhou

- [<img src=https://img.shields.io/badge/CVPR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
### Linjie Li

- [<img src=https://img.shields.io/badge/CVPR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Guandong Xu

- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.147) [**Can Language Models Serve as Temporal Knowledge Bases?**](https://aclanthology.org/2022.findings-emnlp.147),<br> by *Ruilin Zhao, Feng Zhao, Guandong Xu, Sixiao Zhang and Hai Jin*
<br><br>
### Yun Xiong

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.14524) [**Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender
System**](https://doi.org/10.48550/arXiv.2303.14524),<br> by *Yunfan Gao, Tao Sheng, Youlin Xiang, Yun Xiong, Haofen Wang and Jiawei Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510062) [**Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding**](https://doi.org/10.1145/3510003.3510062),<br> by *Deze Wang, Zhouyang Jia, Shanshan Li, Yue Yu, Yun Xiong, Wei Dong and Xiangke Liao*
<br><br>
### Yue Yu

- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510062) [**Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding**](https://doi.org/10.1145/3510003.3510062),<br> by *Deze Wang, Zhouyang Jia, Shanshan Li, Yue Yu, Yun Xiong, Wei Dong and Xiangke Liao*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.691) [**SeqMix: Augmenting Active Sequence Labeling via Sequence Mixup**](https://doi.org/10.18653/v1/2020.emnlp-main.691),<br> by *Rongzhi Zhang, Yue Yu and Chao Zhang*
<br><br>
### Meng Jiang

- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.150) [**Dict-BERT: Enhancing Language Model Pre-training with Dictionary**](https://doi.org/10.18653/v1/2022.findings-acl.150),<br> by *Wenhao Yu, Chenguang Zhu, Yuwei Fang, Donghan Yu, Shuohang Wang, Yichong Xu, Michael Zeng and Meng Jiang*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/ICSE43902.2021.00040) [**Traceability Transformed: Generating more Accurate Links with Pre-Trained
BERT Models**](https://doi.org/10.1109/ICSE43902.2021.00040),<br> by *Jinfeng Lin, Yalin Liu, Qingkai Zeng, Meng Jiang and Jane Cleland-Huang*
<br><br>
### Hongyu Zhang

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549094) [**Diet code is healthy: simplifying programs for pre-trained models
of code**](https://doi.org/10.1145/3540250.3549094),<br> by *Zhaowei Zhang, Hongyu Zhang, Beijun Shen and Xiaodong Gu*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Jieke Shi

- [<img src=https://img.shields.io/badge/ASE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [<img src=https://img.shields.io/badge/ICSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
### Bowen Xu

- [<img src=https://img.shields.io/badge/ASE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [<img src=https://img.shields.io/badge/ICSME-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ieeexplore.ieee.org/abstract/document/9240704/) [**Sentiment analysis for software engineering: How far can pre-trained transformer models go?**](https://ieeexplore.ieee.org/abstract/document/9240704/),<br> by *Zhang, Ting, Xu, Bowen, Thung, Ferdian, Haryono, Stefanus Agus, Lo, David and Jiang, Lingxiao*
<br><br>
### Xiapu Luo

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.10620) [**Large Language Models for Software Engineering: A Systematic Literature
Review**](https://doi.org/10.48550/arXiv.2308.10620),<br> by *Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10623) [**Do Pre-trained Language Models Indeed Understand Software Engineering
Tasks?**](https://doi.org/10.48550/arXiv.2211.10623),<br> by *Yao Li, Tao Zhang, Xiapu Luo, Haipeng Cai, Sen Fang and Dawei Yuan*
<br><br>
### Vincent Ng

- [<img src=https://img.shields.io/badge/IJCAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.24963/ijcai.2022/775) [**Deep Learning Meets Software Engineering: A Survey on Pre-Trained
Models of Source Code**](https://doi.org/10.24963/ijcai.2022/775),<br> by *Changan Niu, Chuanyi Li, Bin Luo and Vincent Ng*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/21496) [**Commonsense Knowledge Reasoning and Generation with Pre-trained Language
Models: A Survey**](https://ojs.aaai.org/index.php/AAAI/article/view/21496),<br> by *Prajjwal Bhargava and Vincent Ng*
<br><br>
### Hongzhi Yin

- [<img src=https://img.shields.io/badge/ISSTA-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3533767.3534219) [**CIRCLE: continual repair across programming languages**](https://doi.org/10.1145/3533767.3534219),<br> by *Wei Yuan, Quanjun Zhang, Tieke He, Chunrong Fang, Nguyen Quoc Viet Hung, Xiaodong Hao and Hongzhi Yin*
<br><br>
- [<img src=https://img.shields.io/badge/SIGIR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3477495.3531937) [**Are Graph Augmentations Necessary?: Simple Graph Contrastive Learning
for Recommendation**](https://doi.org/10.1145/3477495.3531937),<br> by *Junliang Yu, Hongzhi Yin, Xin Xia, Tong Chen, Lizhen Cui and Quoc Viet Hung Nguyen*
<br><br>
### Xin Jiang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.12966) [**Aligning Large Language Models with Human: A Survey**](https://doi.org/10.48550/arXiv.2307.12966),<br> by *Yufei Wang, Wanjun Zhong, Liangyou Li, Fei Mi, Xingshan Zeng, Wenyong Huang, Lifeng Shang, Xin Jiang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Fei Mi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2307.12966) [**Aligning Large Language Models with Human: A Survey**](https://doi.org/10.48550/arXiv.2307.12966),<br> by *Yufei Wang, Wanjun Zhong, Liangyou Li, Fei Mi, Xingshan Zeng, Wenyong Huang, Lifeng Shang, Xin Jiang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Jian Yin

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Jin Liu

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Hao Wu

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Pingyi Zhou

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Xin Wang

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Baishakhi Ray

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549162) [**NatGen: generative pre-training by "naturalizing" source code**](https://doi.org/10.1145/3540250.3549162),<br> by *Saikat Chakraborty, Toufique Ahmed, Yangruibo Ding, Premkumar T. Devanbu and Baishakhi Ray*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
### Saikat Chakraborty

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549162) [**NatGen: generative pre-training by "naturalizing" source code**](https://doi.org/10.1145/3540250.3549162),<br> by *Saikat Chakraborty, Toufique Ahmed, Yangruibo Ding, Premkumar T. Devanbu and Baishakhi Ray*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
### Shujie Liu

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Michele Tufano

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Long Zhou

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Ge Li

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ASE-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3324884.3416591) [**Multi-task Learning based Pre-trained Language Model for Code Completion**](https://doi.org/10.1145/3324884.3416591),<br> by *Fang Liu, Ge Li, Yunfei Zhao and Zhi Jin*
<br><br>
### Shuo Ren

- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Akhilesh Deepak Gotmare

- [<img src=https://img.shields.io/badge/openreview-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Program&Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
### Hung Le

- [<img src=https://img.shields.io/badge/openreview-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Program&Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
### Panos Kalnis

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.06466) [**ChatGPT versus Traditional Question Answering for Knowledge Graphs:
Current Status and Future Directions Towards Knowledge Graph Chatbots**](https://doi.org/10.48550/arXiv.2302.06466),<br> by *Reham Omar, Omij Mangukiya, Panos Kalnis and Essam Mansour*
<br><br>
- [<img src=https://img.shields.io/badge/ICDCS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/ICDCS51616.2021.00060) [**GRACE: A Compressed Communication Framework for Distributed Machine
Learning**](https://doi.org/10.1109/ICDCS51616.2021.00060),<br> by *Hang Xu, Chen-Yu Ho, Ahmed M. Abdelmoniem, Aritra Dutta, El Houcine Bergou, Konstantinos Karatsenidis, Marco Canini and Panos Kalnis*
<br><br>
### Xingjian Li

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.05658) [**Fine-tuning Pre-trained Language Models with Noise Stability Regularization**](https://doi.org/10.48550/arXiv.2206.05658),<br> by *Hang Hua, Xingjian Li, Dejing Dou, Cheng-Zhong Xu and Jiebo Luo*
<br><br>
- [<img src=https://img.shields.io/badge/Euro--Par-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Zheng Zhang

- [<img src=https://img.shields.io/badge/Mach._Intell._Res.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s11633-022-1387-3) [**EVA2.0: Investigating Open-domain Chinese Dialogue Systems with
Large-scale Pre-training**](https://doi.org/10.1007/s11633-022-1387-3),<br> by *Yuxian Gu, Jiaxin Wen, Hao Sun, Yi Song, Pei Ke, Chujie Zheng, Zheng Zhang, Jianzhu Yao et al.*
<br><br>
- [<img src=https://img.shields.io/badge/IA3-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1109/IA351965.2020.00011) [**DistDGL: Distributed Graph Neural Network Training for Billion-Scale
Graphs**](https://doi.org/10.1109/IA351965.2020.00011),<br> by *Da Zheng, Chao Ma, Minjie Wang, Jinjing Zhou, Qidong Su, Xiang Song, Quan Gan, Zheng Zhang et al.*
<br><br>
### Lichao Sun

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [<img src=https://img.shields.io/badge/TIST-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
### Ji Liu

- [<img src=https://img.shields.io/badge/KIS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s10115-022-01664-x) [**From distributed machine learning to federated learning: a survey**](https://doi.org/10.1007/s10115-022-01664-x),<br> by *Ji Liu, Jizhou Huang, Yang Zhou, Xuhong Li, Shilei Ji, Haoyi Xiong and Dejing Dou*
<br><br>
- [<img src=https://img.shields.io/badge/Euro--Par-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Lingjuan Lyu

- [<img src=https://img.shields.io/badge/TIST-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [<img src=https://img.shields.io/badge/FLPI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-63076-8\_14) [**Collaborative Fairness in Federated Learning**](https://doi.org/10.1007/978-3-030-63076-8\_14),<br> by *Lingjuan Lyu, Xinyi Xu, Qian Wang and Han Yu*
<br><br>
### Kimin Lee

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12192) [**Aligning Text-to-Image Models using Human Feedback**](https://doi.org/10.48550/arXiv.2302.12192),<br> by *Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CVPR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yun_Regularizing_Class-Wise_Predictions_via_Self-Knowledge_Distillation_CVPR_2020_paper.pdf) [**Regularizing Class-Wise Predictions via Self-Knowledge Distillation**](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yun_Regularizing_Class-Wise_Predictions_via_Self-Knowledge_Distillation_CVPR_2020_paper.pdf), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Sukmin Yun, Jongjin Park, Kimin Lee and Jinwoo Shin*
<br><br>
### Michael Tschannen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v80/furlanello18a.html) [**Born-Again Neural Networks**](http://proceedings.mlr.press/v80/furlanello18a.html), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Tommaso Furlanello, Zachary Chase Lipton, Michael Tschannen, Laurent Itti and Anima Anandkumar*
<br><br>
### Xiang Gao

- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.28) [**Dialogue Response Ranking Training with Large-Scale Human Feedback
Data**](https://doi.org/10.18653/v1/2020.emnlp-main.28),<br> by *Xiang Gao, Yizhe Zhang, Michel Galley, Chris Brockett and Bill Dolan*
<br><br>
### Yan Zeng

- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.392) [**A Simple and Efficient Multi-Task Learning Approach for Conditioned
Dialogue Generation**](https://doi.org/10.18653/v1/2021.naacl-main.392),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2010.11140) [**Generalized Conditioned Dialogue Generation Based on Pre-trained Language
Model**](https://arxiv.org/abs/2010.11140),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
### Wei Wu

- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539472) [**Mask and Reason: Pre-Training Knowledge Graph Transformers for Complex
Logical Queries**](https://doi.org/10.1145/3534678.3539472),<br> by *Xiao Liu, Shiyu Zhao, Kai Su, Yukuo Cen, Jiezhong Qiu, Mengdi Zhang, Wei Wu, Yuxiao Dong et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.140) [**StyleDGPT: Stylized Response Generation with Pre-trained Language
Models**](https://doi.org/10.18653/v1/2020.findings-emnlp.140),<br> by *Ze Yang, Wei Wu, Can Xu, Xinnian Liang, Jiaqi Bai, Liran Wang, Wei Wang and Zhoujun Li*
<br><br>
### Mostofa Patwary

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Peng Xu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.04624) [**Factuality Enhanced Language Models for Open-Ended Text Generation**](https://doi.org/10.48550/arXiv.2206.04624),<br> by *Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi and Bryan Catanzaro*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Bo Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04858) [**Re-ViLM: Retrieval-Augmented Visual Language Model for Zero and Few-Shot
Image Captioning**](https://doi.org/10.48550/arXiv.2302.04858),<br> by *Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti, Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.495) [**T3: Tree-Autoencoder Constrained Adversarial Text Generation for
Targeted Attack**](https://doi.org/10.18653/v1/2020.emnlp-main.495),<br> by *Boxin Wang, Hengzhi Pei, Boyuan Pan, Qian Chen, Shuohang Wang and Bo Li*
<br><br>
### Eric P. Xing

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.341) [**Progressive Generation of Long Text with Pretrained Language Models**](https://doi.org/10.18653/v1/2021.naacl-main.341),<br> by *Bowen Tan, Zichao Yang, Maruan Al-Shedivat, Eric P. Xing and Zhiting Hu*
<br><br>
### Hao Tian

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Dianhai Yu

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Euro--Par-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Wei Liu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.13007) [**ChatAug: Leveraging ChatGPT for Text Data Augmentation**](https://doi.org/10.48550/arXiv.2302.13007),<br> by *Haixing Dai, Zhengliang Liu, Wenxiong Liao, Xiaoke Huang, Zihao Wu, Lin Zhao, Wei Liu, Ninghao Liu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
### Weibao Gong

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/Euro--Par-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Shikun Feng

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Shuohuan Wang

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>``
In order to extract the lexical, syntactic and semantic information from training corpora, we propose a continual pre-training framework named ERNIE 2.0 which incrementally builds pre-training tasks and then learn pre-trained models on these constructed tasks via continual multi-task learning.
``
<br><br>
### Tie Yan Liu

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Tao Qin

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Xu Tan

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Kaitao Song

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ICML-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Bodhisattwa Prasad Majumder

- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/D19-1615) [**Improving Neural Story Generation by Targeted Common Sense Grounding**](https://doi.org/10.18653/v1/D19-1615),<br> by *Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian J. McAuley and Garrison W. Cottrell*
<br><br>
### Tianrui Li

- [<img src=https://img.shields.io/badge/JIS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1016/j.ins.2021.12.102) [**Fairness and accuracy in horizontal federated learning**](https://doi.org/10.1016/j.ins.2021.12.102),<br> by *Wei Huang, Tianrui Li, Dexian Wang, Shengdong Du, Junbo Zhang and Tianqiang Huang*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
### Luo Si

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>``
we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness: it tendsto outperform fine-tuning on both low-resource and cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to fine-tuning.
``
<br><br>
### Yijia Liu

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [<img src=https://img.shields.io/badge/NAACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Fuli Luo

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.37) [**Towards Unified Prompt Tuning for Few-shot Text Classification**](https://aclanthology.org/2022.findings-emnlp.37),<br> by *Jianing Wang, Chengyu Wang, Fuli Luo, Chuanqi Tan, Minghui Qiu, Fei Yang, Qiuhui Shi, Songfang Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
### Ruofei Zhang

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Jiusheng Chen

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Pengcheng Wang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
### Ming Gong

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
### Linjun Shou

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
### Jie Fu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.07987) [**Chinese Open Instruction Generalist: A Preliminary Release**](https://doi.org/10.48550/arXiv.2304.07987),<br> by *Ge Zhang, Yemin Shi, Ruibo Liu, Ruibin Yuan, Yizhi Li, Siwei Dong, Yu Shu, Zhaoqun Li et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
### Weizhen Qi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2303.04671) [**Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models**](https://arxiv.org/abs/2303.04671),<br> by *Wu, Chenfei, Yin, Shengming, Qi, Weizhen, Wang, Xiaodong, Tang, Zecheng and Duan, Nan*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
### Yeyun Gong

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Yu Yan

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Piji Li

- [<img src=https://img.shields.io/badge/ECIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
### Zhipeng Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
### Jinhao Jiang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2303.18223) [**A Survey of Large Language Models**](https://doi.org/10.48550/arXiv.2303.18223),<br> by *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
### Gaole He

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CIKM-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Yinhan Liu

- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), [<img src=https://img.shields.io/badge/RoBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/1907.11692) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Mohit Iyyer

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.11521) [**How Does In-Context Learning Help Prompt Tuning?**](https://doi.org/10.48550/arXiv.2302.11521),<br> by *Simeng Sun, Yang Liu, Dan Iter, Chenguang Zhu and Mohit Iyyer*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.55) [**Reformulating Unsupervised Style Transfer as Paraphrase Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.55),<br> by *Kalpesh Krishna, John Wieting and Mohit Iyyer*
<br><br>
### Richard Socher

- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Bryan McCann

- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Pei Ke

- [<img src=https://img.shields.io/badge/Mach._Intell._Res.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/s11633-022-1387-3) [**EVA2.0: Investigating Open-domain Chinese Dialogue Systems with
Large-scale Pre-training**](https://doi.org/10.1007/s11633-022-1387-3),<br> by *Yuxian Gu, Jiaxin Wen, Hao Sun, Yi Song, Pei Ke, Chujie Zheng, Zheng Zhang, Jianzhu Yao et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
### Jianzhong Qi

- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
- [<img src=https://img.shields.io/badge/IJCAI-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.24963/ijcai.2021/223) [**Federated Learning with Fair Averaging**](https://doi.org/10.24963/ijcai.2021/223),<br> by *Zheng Wang, Xiaoliang Fan, Jianzhong Qi, Chenglu Wen, Cheng Wang and Rongshan Yu*
<br><br>
### Xiaodong Gu

- [<img src=https://img.shields.io/badge/FSE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3540250.3549094) [**Diet code is healthy: simplifying programs for pre-trained models
of code**](https://doi.org/10.1145/3540250.3549094),<br> by *Zhaowei Zhang, Hongyu Zhang, Beijun Shen and Xiaodong Gu*
<br><br>
- [<img src=https://img.shields.io/badge/AAAI-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://ojs.aaai.org/index.php/AAAI/article/view/17527) [**DialogBERT: Discourse-Aware Response Generation via Learning to Recover
and Rank Utterances**](https://ojs.aaai.org/index.php/AAAI/article/view/17527),<br> by *Xiaodong Gu, Kang Min Yoo and Jung-Woo Ha*
<br><br>
### Xiaojiang Liu

- [<img src=https://img.shields.io/badge/COLING-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
### Bing Qin

- [<img src=https://img.shields.io/badge/COLING-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
### Jiezhong Qiu

- [<img src=https://img.shields.io/badge/KDD-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3534678.3539472) [**Mask and Reason: Pre-Training Knowledge Graph Transformers for Complex
Logical Queries**](https://doi.org/10.1145/3534678.3539472),<br> by *Xiao Liu, Shiyu Zhao, Kai Su, Yukuo Cen, Jiezhong Qiu, Mengdi Zhang, Wei Wu, Yuxiao Dong et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
### Xiaodong Liu

- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [**DeBERTa: Decoding-enhanced BERT with Disentangled Attention**](https://arxiv.org/abs/2006.03654), [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) <br> by *Pengcheng He, Xiaodong Liu, Jianfeng Gao and Weizhu Chen*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Sumanth Dathathri

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.14375) [**Improving alignment of dialogue agents via targeted human judgements**](https://doi.org/10.48550/arXiv.2209.14375),<br> by *Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=H1edEyBKDS) [**Plug and Play Language Models: A Simple Approach to Controlled Text
Generation**](https://openreview.net/forum?id=H1edEyBKDS),<br> by *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski and Rosanne Liu*
<br><br>
### Yu Cheng

- [<img src=https://img.shields.io/badge/ACL-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Yu Su

- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.329) [**Thinking about GPT-3 In-Context Learning for Biomedical IE? Think
Again**](https://aclanthology.org/2022.findings-emnlp.329),<br> by *Bernal Jimenez Gutierrez, Nikolas McNeal, Clayton Washington, You Chen, Lang Li, Huan Sun and Yu Su*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
### Lu Wang

- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.502) [**Controllable Open-ended Question Generation with A New Question
Type Ontology**](https://doi.org/10.18653/v1/2021.acl-long.502),<br> by *Shuyang Cao and Lu Wang*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.501) [**DYPLOC: Dynamic Planning of Content Using Mixed Language Models
for Text Generation**](https://doi.org/10.18653/v1/2021.acl-long.501),<br> by *Xinyu Hua, Ashwin Sreevatsa and Lu Wang*
<br><br>
### Geoffrey E. Hinton

- [<img src=https://img.shields.io/badge/CoRR-2015-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1503.02531) [**Distilling the Knowledge in a Neural Network**](http://arxiv.org/abs/1503.02531), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Geoffrey E. Hinton, Oriol Vinyals and Jeffrey Dean*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2009-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html) [**Zero-shot Learning with Semantic Output Codes**](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html),<br> by *Mark Palatucci, Dean Pomerleau, Geoffrey E. Hinton and Tom M. Mitchell*
<br><br>
### Irina Rish

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2308.04014) [**Continual Pre-Training of Large Language Models: How to (re)warm your
model?**](https://doi.org/10.48550/arXiv.2308.04014),<br> by *Kshitij Gupta, Benjamin Th\'erien, Adam Ibrahim, Mats L. Richter, Quentin Anthony, Eugene Belilovsky, Irina Rish and Timoth\'ee Lesort*
<br><br>
- [<img src=https://img.shields.io/badge/JAIR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1613/jair.1.13673) [**Towards Continual Reinforcement Learning: A Review and Perspectives**](https://doi.org/10.1613/jair.1.13673),<br> by *Khimya Khetarpal, Matthew Riemer, Irina Rish and Doina Precup*
<br><br>
### Hui Chen

- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
### Xiang Chen

- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Shumin Deng

- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Hongbin Ye

- [<img src=https://img.shields.io/badge/WWW-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
### Yadao Wang

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Zhen Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Hai Tao Zheng

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ECIR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
### Weilin Zhao

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Jing Yi

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Weize Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Yusheng Su

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2304.08354) [**Tool Learning with Foundation Models**](https://doi.org/10.48550/arXiv.2304.08354),<br> by *Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Sameer Singh

- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.346) [**AutoPrompt: Eliciting Knowledge from Language Models with Automatically
Generated Prompts**](https://doi.org/10.18653/v1/2020.emnlp-main.346),<br> by *Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric Wallace and Sameer Singh*
<br><br>
### Robert L. Logan IV

- [<img src=https://img.shields.io/badge/ACL_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.346) [**AutoPrompt: Eliciting Knowledge from Language Models with Automatically
Generated Prompts**](https://doi.org/10.18653/v1/2020.emnlp-main.346),<br> by *Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric Wallace and Sameer Singh*
<br><br>
### Terra Blevins

- [<img src=https://img.shields.io/badge/the_61st_Annual_Meeting_of_the_Association_for_Computational
Linguistics_(Volume_1:_Long_Papers),_{ACL}_2023,_Toronto,_Canada,
July_9--14,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2023.acl-long.367) [**Prompting Language Models for Linguistic Structure**](https://doi.org/10.18653/v1/2023.acl-long.367),<br> by *Terra Blevins, Hila Gonen and Luke Zettlemoyer*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
### Yao Lu

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.556) [**Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot
Prompt Order Sensitivity**](https://doi.org/10.18653/v1/2022.acl-long.556), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel and Pontus Stenetorp*
<br>``
(1) This work demonstrates that few-shot prompts suffer from order sensitivity, in that for the same prompt the order in which samples are provided can make a difference to model performance.
``<br>``
(2) This work introduces a probing method which constructs an artificial development set by language models themselves to alleviate the order sensitivity problem.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://arxiv.org/abs/1903.12136) [**Distilling Task-Specific Knowledge from BERT into Simple Neural
Networks**](http://arxiv.org/abs/1903.12136), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/SforAiDl/KD_Lib)<br> by *Raphael Tang, Yao Lu, Linqing Liu, Lili Mou, Olga Vechtomova and Jimmy Lin*
<br><br>
### Peter Clark

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
### Xiang Deng

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br>``
(1) 提出了一种迭代式的prompt-tuning方法，他们认为soft prompt应该带有语境，即在自回归解码时不同时刻应该有不同的prompt向量；
``<br>``
(2) 利用BERT为encoder-decoder架构的PLM生成prompt，在每个解码时刻BERT都会根据先前时刻的上下文生成一组新的prompt向量，提供给PLM生成新的上下文，迭代往复。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Boshi Wang

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br>``
(1) 提出了一种迭代式的prompt-tuning方法，他们认为soft prompt应该带有语境，即在自回归解码时不同时刻应该有不同的prompt向量；
``<br>``
(2) 利用BERT为encoder-decoder架构的PLM生成prompt，在每个解码时刻BERT都会根据先前时刻的上下文生成一组新的prompt向量，提供给PLM生成新的上下文，迭代往复。
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Alisa Liu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.225) [**Generated Knowledge Prompting for Commonsense Reasoning**](https://doi.org/10.18653/v1/2022.acl-long.225),<br> by *Jiacheng Liu, Alisa Liu, Ximing Lu, Sean Welleck, Peter West, Ronan Le Bras, Yejin Choi and Hannaneh Hajishirzi*
<br><br>
### Samuel R. Bowman

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br>``
(1) 探索了利用LLM在几个样本的情况下归纳出任务指令的能力；
``<br>``
(2) 测量两个指标：1. 模型归纳指令与人类归纳的指令对比，2. 利用模型归纳的指令作为prompt进行预测的执行准确率；
``<br>``
(3) 相比于GPT-3，InstructGPT效果更好，理所当然。
``
<br><br>
### Ravsehaj Singh Puri

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.09161) [**How Many Data Samples is an Additional Instruction Worth?**](https://doi.org/10.48550/arXiv.2203.09161),<br> by *Ravsehaj Singh Puri, Swaroop Mishra, Mihir Parmar and Chitta Baral*
<br><br>
### Mihir Parmar

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.09161) [**How Many Data Samples is an Additional Instruction Worth?**](https://doi.org/10.48550/arXiv.2203.09161),<br> by *Ravsehaj Singh Puri, Swaroop Mishra, Mihir Parmar and Chitta Baral*
<br><br>
### Yeganeh Kordi

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
### Yizhong Wang

- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
### Slav Petrov

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Hongkun Yu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Gaurav Mishra

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Xinyun Chen

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### William Fedus

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Hyung Won Chung

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Ben Hutchinson

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Mark Diaz

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Vinodkumar Prabhakaran

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Toju Duke

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Yanqi Zhou

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
### Yanping Huang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Nan Du

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Kelvin Guu

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2002.08909) [**REALM: Retrieval-Augmented Language Model Pre-Training**](https://arxiv.org/abs/2002.08909),<br> by *Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat and Ming-Wei Chang*
<br><br>
### Vincent Y. Zhao

- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Zornitsa Kozareva

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.emnlp-main.804) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Srini Iyer

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), [<img src=https://img.shields.io/badge/MoE-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.260) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>``
This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that:
``<br>``
(1) benefits of self-supervised depends on the amount of training data,
``<br>``
(2) semantic similarity between training and evaluation tasks matters,
``<br>``
(3) adding training objectives without diversity does not help,
``<br>``
(4) model performance improves when choosing similar templates for both self-supervised and downstream tasks,
``<br>``
(5) self-supervised  tasks and human-annotated datasets are complementary,
``<br>``
(6) self-supervised-trained models are better at following task instructions.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
### Jingjing Xu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.438) [**Calibrating Factual Knowledge in Pretrained Language Models**](https://aclanthology.org/2022.findings-emnlp.438),<br> by *Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui and Lei Li*
<br><br>
### Qingxiu Dong

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br>``
This paper surveys and summarizes the progress and challenges of ICL, including ICL's formal definition, correlation to related studies, advanced techniques (training strategies, related analysis) and potential directions.
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP_Findings-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.438) [**Calibrating Factual Knowledge in Pretrained Language Models**](https://aclanthology.org/2022.findings-emnlp.438),<br> by *Qingxiu Dong, Damai Dai, Yifan Song, Jingjing Xu, Zhifang Sui and Lei Li*
<br><br>
### Benjamin Chess

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Sandhini Agarwal

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Benjamin Mann

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### David Luan

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/OpenAI-2019-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
### Ryan Sepassi

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Peter J. Liu

- [<img src=https://img.shields.io/badge/JMLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer**](http://jmlr.org/papers/v21/20-074.html), [<img src=https://img.shields.io/badge/T5-yellow alt="img" style="zoom:100%; vertical-align: middle" />](http://jmlr.org/papers/v21/20-074.html) <br> by *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Zhuang Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>``
To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.
``
<br><br>
### Peter Welinder

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Matthew Knight

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### William Saunders

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Shantanu Jain

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Suchir Balaji

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2112.09332) [**WebGPT: Browser-assisted question-answering with human feedback**](https://arxiv.org/abs/2112.09332),<br> by *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain et al.*
<br><br>
### Ariel Herbert Voss

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Clemens Winter

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Lukasz Kaiser

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2018-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Nick Ryder

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Scott Gray

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Pamela Mishkin

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Girish Sastry

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Raul Puri

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Alex Ray

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2203.02155) [**Training language models to follow instructions with human feedback**](https://doi.org/10.48550/arXiv.2203.02155),<br> by *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Mark Chen

- [<img src=https://img.shields.io/badge/CoRR-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [**Language Models are Few-Shot Learners**](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) <br> by *Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam et al.*
<br><br>
### Hongming Zhang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303),<br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>``
本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。
``
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Alex Smola

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Mu Li

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Tianyi Zhang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2020-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=SkeHuCVFDr) [**BERTScore: Evaluating Text Generation with BERT**](https://openreview.net/forum?id=SkeHuCVFDr),<br> by *Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi*
<br><br>
### Tatsunori Hashimoto

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Sang Michael Xie

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=RdJVFCHjUMI) [**An Explanation of In-context Learning as Implicit Bayesian Inference**](https://openreview.net/forum?id=RdJVFCHjUMI),<br> by *Sang Michael Xie, Aditi Raghunathan, Percy Liang and Tengyu Ma*
<br><br>
### Neel Guha

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Mirac Suzgun

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Laurel J. Orr

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Eric Zelikman

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://research.google/pubs/pub51694/) [**Star: Self-taught reasoner bootstrapping reasoning with reasoning**](https://research.google/pubs/pub51694/),<br> by *Zelikman, Eric, Mu, Jesse, Goodman, Noah D and Wu, Yuhuai Tony*
<br><br>
### Christopher R{\'{e}}

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Benjamin Newman

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=DhzIU48OcZh) [**P-Adapters: Robustly Extracting Factual Information from Language
Models with Diverse Prompts**](https://openreview.net/forum?id=DhzIU48OcZh),<br> by *Benjamin Newman, Prafulla Kumar Choubey and Nazneen Rajani*
<br><br>
### Yuhuai Wu

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.14858) [**Solving Quantitative Reasoning Problems with Language Models**](https://doi.org/10.48550/arXiv.2206.14858),<br> by *Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V. Ramasesh, Ambrose Slone, Cem Anil et al.*
<br><br>
### Rishi Bommasani

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Amir Globerson

- [<img src=https://img.shields.io/badge/EACL-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>``
本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。
``
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EACL}
2023,_Dubrovnik,_Croatia,_May_2--6,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2023.findings-eacl.139) [**Crawling The Internal Knowledge-Base of Language Models**](https://aclanthology.org/2023.findings-eacl.139),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br><br>
### Mor Geva

- [<img src=https://img.shields.io/badge/EACL-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>``
本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。
``
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EACL}
2023,_Dubrovnik,_Croatia,_May_2--6,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2023.findings-eacl.139) [**Crawling The Internal Knowledge-Base of Language Models**](https://aclanthology.org/2023.findings-eacl.139),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br><br>
### Roi Cohen

- [<img src=https://img.shields.io/badge/EACL-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>``
本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。
``
<br><br>
- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EACL}
2023,_Dubrovnik,_Croatia,_May_2--6,_2023-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2023.findings-eacl.139) [**Crawling The Internal Knowledge-Base of Language Models**](https://aclanthology.org/2023.findings-eacl.139),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br><br>
### Yan Xu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
### Tiezheng Yu

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
### Ziwei Ji

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
### Dan Su

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
### Yejin Bang

- [<img src=https://img.shields.io/badge/CoRR-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>``
本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。
``
<br><br>
- [<img src=https://img.shields.io/badge/ACM_Comput._Surv.-2023-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3571730) [**Survey of Hallucination in Natural Language Generation**](https://doi.org/10.1145/3571730),<br> by *Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang et al.*
<br><br>
### Rui Zhang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL_Findings-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
### Tianlu Wang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2205.01068) [**OPT: Open Pre-trained Transformer Language Models**](https://doi.org/10.48550/arXiv.2205.01068), [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona T. Diab et al.*
<br><br>
### Jungo Kasai

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2207.13332) [**RealTime QA: What's the Answer Right Now?**](https://doi.org/10.48550/arXiv.2207.13332),<br> by *Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir R. Radev, Noah A. Smith et al.*
<br><br>
### Hongjin Su

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975), [<img src=https://img.shields.io/badge/Code-skyblue alt="img" style="zoom:100%; vertical-align: middle" />](https://github.com/HKUNLP/icl-selective-annotation) [<img src=https://img.shields.io/badge/SBERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/D19-1410/) [<img src=https://img.shields.io/badge/GPT--J-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gptj) [<img src=https://img.shields.io/badge/GPT--Neo-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://huggingface.co/docs/transformers/model_doc/gpt_neo) [<img src=https://img.shields.io/badge/GPT--3-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) [<img src=https://img.shields.io/badge/Codex-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2107.03374) [<img src=https://img.shields.io/badge/OPT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2205.01068) <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br>``
This paper proposes a graph-based selective annotation method named vote-k to
``<br>``
(1) select a pool of examples to annotate from unlabeled data,
``<br>``
(2) retrieve prompts (contexts) from the annotated data pool for in-context learning.
``<br>``
Specifically, the selection method first selects a small set of unlabeled examples iteratively and then labels them to serve as contexts for LLMs to predict the labels of the rest unlabeled data. The method selects the predictions with highest confidence (log probability of generation output) to fill up the selective annotation pool.
``
<br><br>
- [<img src=https://img.shields.io/badge/ACL-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Xikun Zhang

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br><br>
- [<img src=https://img.shields.io/badge/ICLR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://openreview.net/forum?id=41e9o6cQPj) [**GreaseLM: Graph REASoning Enhanced Language Models**](https://openreview.net/forum?id=41e9o6cQPj),<br> by *Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning and Jure Leskovec*
<br><br>
### Junyi Jessy Li

- [<img src=https://img.shields.io/badge/NeurIPS-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356),<br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [<img src=https://img.shields.io/badge/ASE-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.1145/3551349.3556955) [**CoditT5: Pretraining for Source Code and Natural Language Editing**](https://doi.org/10.1145/3551349.3556955),<br> by *Jiyang Zhang, Sheena Panthaplackel, Pengyu Nie, Junyi Jessy Li and Milos Gligoric*
<br><br>
### Albert Webson

- [<img src=https://img.shields.io/badge/NAACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.naacl-main.167) [**Do Prompt-Based Models Really Understand the Meaning of Their Prompts?**](https://doi.org/10.18653/v1/2022.naacl-main.167),<br> by *Albert Webson and Ellie Pavlick*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Yiming Yang

- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Chia Hsuan Lee

- [<img src=https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7--11,_2022-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [<img src=https://img.shields.io/badge/EMNLP-2021-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
### He He

- [<img src=https://img.shields.io/badge/ACL-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53), [<img src=https://img.shields.io/badge/BERT-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://aclanthology.org/N19-1423/) [<img src=https://img.shields.io/badge/DeBERTa-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://arxiv.org/abs/2006.03654) [<img src=https://img.shields.io/badge/GPT--2-yellow alt="img" style="zoom:100%; vertical-align: middle" />](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) <br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br>``
This paper proposes in-context tuning, which recasts task adaptation and prediction as a simple sequence prediction problem: to form the input sequence,  concatenate the task instruction, labeled in-context examples, and the target input to predict; to meta train the model to learn from in-context examples, finetune a PLM to predict the target label given the input sequence on a collection of tasks (very similar to MetaICL). On LAMA and BinaryClfs, the proposed method outperforms MAML.
``
<br><br>
- [<img src=https://img.shields.io/badge/CoRR-2022-blue alt="img" style="zoom:100%; vertical-align: middle" />](https://doi.org/10.48550/arXiv.2210.01240) [**Language Models Are Greedy Reasoners: A Systematic Formal Analysis
of Chain-of-Thought**](https://doi.org/10.48550/arXiv.2210.01240),<br> by *Abulhair Saparov and He He*
<br><br>