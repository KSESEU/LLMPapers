# Resources on ChatGPT and Large Language Models
Collection of  papers and related works for Large Language Models (ChatGPT, GPT-3, Codex etc.).
## Contributors
This repository is contributed by the following contributors.
- **Organizers**: [Guilin Qi (漆桂林)](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm), [Xiaofang Qi (戚晓芳)](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm)
- **Paper Collectors**: Zafar Ali, [Sheng Bi (毕胜)](https://github.com/bisheng), [Yongrui Chen (陈永锐)](https://github.com/Bahuia), Zizhuo Chen (陈孜卓), [Xinbang Dai (戴鑫邦)](https://github.com/OBriennnnn), Huan Gao (高桓), [Nan Hu (胡楠)](https://github.com/HuuuNan), Shilong Hu (胡世龙), [Jingqi Kang (康婧淇)](https://github.com/JingqiKang), [Jiaqi Li (李嘉琦)](https://github.com/aoluming), Dehai Min (闵德海), Yiming Tan (谭亦鸣), [Tongtong Wu (吴桐桐)](http://wutong8023.site/), [Songlin Zhai (翟松林)](https://github.com/SonglinZhai), [Yuxin Zhang (张裕欣)](https://github.com/Zzyx1996)
- **Maintainers**: [Runzhe Wang (王润哲)](https://github.com/sid0527), [Shenyu Zhang (张沈昱)](https://github.com/ZSY-SZ) 

The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git). If you'd like to commit to this repo, please modify [bibtex.bib](https://github.com/KSESEU/LLMPapers/blob/main/bibtex.bib) or [related_works.json](https://github.com/KSESEU/LLMPapers/blob/main/related_works.json) and re-generate [README.md](https://github.com/KSESEU/LLMPapers/blob/main/README.md) using `python scripts/run.py`.

This page categorizes the literature by the **Author**

## Papers

### Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hyperlink)
- [![](https://img.shields.io/badge/Luke_Zettlemoyer-9-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luke-zettlemoyer)
- [![](https://img.shields.io/badge/Nan_Duan-8-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nan-duan)
- [![](https://img.shields.io/badge/Denny_Zhou-8-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#denny-zhou)
- [![](https://img.shields.io/badge/Xuezhi_Wang-8-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xuezhi-wang)
- [![](https://img.shields.io/badge/Ed_H._Chi-8-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ed-h.-chi)
- [![](https://img.shields.io/badge/Jason_Wei-8-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jason-wei)
- [![](https://img.shields.io/badge/Ming_Zhou-7-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-zhou)
- [![](https://img.shields.io/badge/Ji_Rong_Wen-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ji-rong-wen)
- [![](https://img.shields.io/badge/Fei_Huang-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#fei-huang)
- [![](https://img.shields.io/badge/Furu_Wei-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#furu-wei)
- [![](https://img.shields.io/badge/Jianfeng_Gao-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jianfeng-gao)
- [![](https://img.shields.io/badge/Mike_Lewis-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mike-lewis)
- [![](https://img.shields.io/badge/Dustin_Tran-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dustin-tran)
- [![](https://img.shields.io/badge/Neel_Sundaresan-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neel-sundaresan)
- [![](https://img.shields.io/badge/Dawn_Drain-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dawn-drain)
- [![](https://img.shields.io/badge/Wayne_Xin_Zhao-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wayne-xin-zhao)
- [![](https://img.shields.io/badge/Yi_Tay-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yi-tay)
- [![](https://img.shields.io/badge/Quoc_V._Le-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#quoc-v.-le)
- [![](https://img.shields.io/badge/Maarten_Bosma-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maarten-bosma)
- [![](https://img.shields.io/badge/Percy_Liang-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#percy-liang)
- [![](https://img.shields.io/badge/Sewon_Min-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sewon-min)
- [![](https://img.shields.io/badge/Noah_A._Smith-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noah-a.-smith)
- [![](https://img.shields.io/badge/Jun_Zhao-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jun-zhao)
- [![](https://img.shields.io/badge/Shengyu_Fu-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shengyu-fu)
- [![](https://img.shields.io/badge/Alexey_Svyatkovskiy-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alexey-svyatkovskiy)
- [![](https://img.shields.io/badge/Daya_Guo-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daya-guo)
- [![](https://img.shields.io/badge/Shuai_Lu-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuai-lu)
- [![](https://img.shields.io/badge/Shafiq_R._Joty-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shafiq-r.-joty)
- [![](https://img.shields.io/badge/Yue_Wang-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-wang)
- [![](https://img.shields.io/badge/Shuohang_Wang-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuohang-wang)
- [![](https://img.shields.io/badge/Daxin_Jiang-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#daxin-jiang)
- [![](https://img.shields.io/badge/Weizhu_Chen-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weizhu-chen)
- [![](https://img.shields.io/badge/Junyi_Li-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#junyi-li)
- [![](https://img.shields.io/badge/Li_Dong-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#li-dong)
- [![](https://img.shields.io/badge/Jingjing_Liu-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jingjing-liu)
- [![](https://img.shields.io/badge/Zhe_Gan-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhe-gan)
- [![](https://img.shields.io/badge/Wenhu_Chen-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wenhu-chen)
- [![](https://img.shields.io/badge/Asli_Celikyilmaz-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#asli-celikyilmaz)
- [![](https://img.shields.io/badge/Huajun_Chen-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#huajun-chen)
- [![](https://img.shields.io/badge/Dale_Schuurmans-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dale-schuurmans)
- [![](https://img.shields.io/badge/Veselin_Stoyanov-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#veselin-stoyanov)
- [![](https://img.shields.io/badge/Ramakanth_Pasunuru-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ramakanth-pasunuru)
- [![](https://img.shields.io/badge/Dario_Amodei-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dario-amodei)
- [![](https://img.shields.io/badge/Jared_Kaplan-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jared-kaplan)
- [![](https://img.shields.io/badge/Pascale_Fung-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pascale-fung)
- [![](https://img.shields.io/badge/Hannaneh_Hajishirzi-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hannaneh-hajishirzi)
- [![](https://img.shields.io/badge/Kang_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kang-liu)
- [![](https://img.shields.io/badge/Shizhu_He-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shizhu-he)
- [![](https://img.shields.io/badge/Bing_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bing-liu)
- [![](https://img.shields.io/badge/Myle_Ott-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#myle-ott)
- [![](https://img.shields.io/badge/Lidong_Bing-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lidong-bing)
- [![](https://img.shields.io/badge/Linlin_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linlin-liu)
- [![](https://img.shields.io/badge/Balaji_Lakshminarayanan-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#balaji-lakshminarayanan)
- [![](https://img.shields.io/badge/Neil_Houlsby-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neil-houlsby)
- [![](https://img.shields.io/badge/Thien_Huu_Nguyen-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#thien-huu-nguyen)
- [![](https://img.shields.io/badge/Shijin_Wang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shijin-wang)
- [![](https://img.shields.io/badge/Chengwei_Qin-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chengwei-qin)
- [![](https://img.shields.io/badge/Pengcheng_He-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengcheng-he)
- [![](https://img.shields.io/badge/Mohit_Bansal-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mohit-bansal)
- [![](https://img.shields.io/badge/David_Lo-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-lo)
- [![](https://img.shields.io/badge/Shao_Kun_Deng-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shao-kun-deng)
- [![](https://img.shields.io/badge/Duyu_Tang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#duyu-tang)
- [![](https://img.shields.io/badge/Colin_B._Clement-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#colin-b.-clement)
- [![](https://img.shields.io/badge/Steven_C._H._Hoi-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#steven-c.-h.-hoi)
- [![](https://img.shields.io/badge/Yao_Wan-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-wan)
- [![](https://img.shields.io/badge/Bill_Dolan-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bill-dolan)
- [![](https://img.shields.io/badge/Michael_Zeng-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-zeng)
- [![](https://img.shields.io/badge/Chenguang_Zhu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chenguang-zhu)
- [![](https://img.shields.io/badge/Michel_Galley-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michel-galley)
- [![](https://img.shields.io/badge/Wei_Wang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wei-wang)
- [![](https://img.shields.io/badge/Nicholas_Jing_Yuan-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nicholas-jing-yuan)
- [![](https://img.shields.io/badge/Zhicheng_Wei-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhicheng-wei)
- [![](https://img.shields.io/badge/Naman_Goyal-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#naman-goyal)
- [![](https://img.shields.io/badge/Yu_Sun-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-sun)
- [![](https://img.shields.io/badge/Xiaodong_Gu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaodong-gu)
- [![](https://img.shields.io/badge/Zhou_Yu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhou-yu)
- [![](https://img.shields.io/badge/Ting_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ting-liu)
- [![](https://img.shields.io/badge/Iryna_Gurevych-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#iryna-gurevych)
- [![](https://img.shields.io/badge/Leonardo_F._R._Ribeiro-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#leonardo-f.-r.-ribeiro)
- [![](https://img.shields.io/badge/Andrea_Madotto-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#andrea-madotto)
- [![](https://img.shields.io/badge/Wenhui_Wang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wenhui-wang)
- [![](https://img.shields.io/badge/Yen_Chun_Chen-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yen-chun-chen)
- [![](https://img.shields.io/badge/Haifeng_Wang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#haifeng-wang)
- [![](https://img.shields.io/badge/Hua_Wu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hua-wu)
- [![](https://img.shields.io/badge/Ningyu_Zhang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ningyu-zhang)
- [![](https://img.shields.io/badge/Yasheng_Wang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yasheng-wang)
- [![](https://img.shields.io/badge/Xiang_Ren-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-ren)
- [![](https://img.shields.io/badge/Xisen_Jin-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xisen-jin)
- [![](https://img.shields.io/badge/Maosong_Sun-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#maosong-sun)
- [![](https://img.shields.io/badge/Zhiyuan_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhiyuan-liu)
- [![](https://img.shields.io/badge/Yang_Liu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yang-liu)
- [![](https://img.shields.io/badge/Noah_Constant-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noah-constant)
- [![](https://img.shields.io/badge/Kang_Min_Yoo-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kang-min-yoo)
- [![](https://img.shields.io/badge/Ashish_Sabharwal-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ashish-sabharwal)
- [![](https://img.shields.io/badge/Hao_Peng-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-peng)
- [![](https://img.shields.io/badge/Huan_Sun-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#huan-sun)
- [![](https://img.shields.io/badge/Omer_Levy-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#omer-levy)
- [![](https://img.shields.io/badge/Swaroop_Mishra-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#swaroop-mishra)
- [![](https://img.shields.io/badge/Jacob_Devlin-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jacob-devlin)
- [![](https://img.shields.io/badge/Jeff_Dean-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jeff-dean)
- [![](https://img.shields.io/badge/Shixiang_Shane_Gu-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shixiang-shane-gu)
- [![](https://img.shields.io/badge/Mostafa_Dehghani-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mostafa-dehghani)
- [![](https://img.shields.io/badge/Barret_Zoph-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#barret-zoph)
- [![](https://img.shields.io/badge/Le_Hou-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#le-hou)
- [![](https://img.shields.io/badge/Quoc_Le-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#quoc-le)
- [![](https://img.shields.io/badge/Adam_Roberts-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#adam-roberts)
- [![](https://img.shields.io/badge/Andrew_M._Dai-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#andrew-m.-dai)
- [![](https://img.shields.io/badge/Brian_Lester-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#brian-lester)
- [![](https://img.shields.io/badge/Jingfei_Du-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jingfei-du)
- [![](https://img.shields.io/badge/Lei_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lei-li)
- [![](https://img.shields.io/badge/Amanda_Askell-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amanda-askell)
- [![](https://img.shields.io/badge/others-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#others)
- [![](https://img.shields.io/badge/Noam_Shazeer-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#noam-shazeer)
- [![](https://img.shields.io/badge/Gholamreza_Haffari-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gholamreza-haffari)
- [![](https://img.shields.io/badge/Ilya_Sutskever-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ilya-sutskever)
- [![](https://img.shields.io/badge/Sam_McCandlish-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sam-mccandlish)
- [![](https://img.shields.io/badge/Alec_Radford-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alec-radford)
- [![](https://img.shields.io/badge/Jie_Tang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jie-tang)
- [![](https://img.shields.io/badge/Nicholas_Joseph-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nicholas-joseph)
- [![](https://img.shields.io/badge/Aston_Zhang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aston-zhang)
- [![](https://img.shields.io/badge/Zhuosheng_Zhang-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhuosheng-zhang)
- [![](https://img.shields.io/badge/Christopher_D._Manning-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#christopher-d.-manning)
- [![](https://img.shields.io/badge/Michihiro_Yasunaga-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michihiro-yasunaga)
- [![](https://img.shields.io/badge/Greg_Durrett-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#greg-durrett)
- [![](https://img.shields.io/badge/Graham_Neubig-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#graham-neubig)
- [![](https://img.shields.io/badge/Uri_Alon-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#uri-alon)
- [![](https://img.shields.io/badge/Shuyan_Zhou-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuyan-zhou)
- [![](https://img.shields.io/badge/Aman_Madaan-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aman-madaan)
- [![](https://img.shields.io/badge/Mari_Ostendorf-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mari-ostendorf)
- [![](https://img.shields.io/badge/George_Karypis-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#george-karypis)
- [![](https://img.shields.io/badge/Tuo_Zhao-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tuo-zhao)
- [![](https://img.shields.io/badge/Chen_Liang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chen-liang)
- [![](https://img.shields.io/badge/Qingru_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qingru-zhang)
- [![](https://img.shields.io/badge/Simiao_Zuo-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#simiao-zuo)
- [![](https://img.shields.io/badge/Dani_Yogatama-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dani-yogatama)
- [![](https://img.shields.io/badge/Pengfei_Cao-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengfei-cao)
- [![](https://img.shields.io/badge/Qingbin_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#qingbin-liu)
- [![](https://img.shields.io/badge/Lei_Shu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lei-shu)
- [![](https://img.shields.io/badge/Hu_Xu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hu-xu)
- [![](https://img.shields.io/badge/Zixuan_Ke-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zixuan-ke)
- [![](https://img.shields.io/badge/Wanxiang_Che-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#wanxiang-che)
- [![](https://img.shields.io/badge/Yiming_Cui-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yiming-cui)
- [![](https://img.shields.io/badge/Jack_Clark-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jack-clark)
- [![](https://img.shields.io/badge/Zac_Hatfield_Dodds-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zac-hatfield-dodds)
- [![](https://img.shields.io/badge/Yuntao_Bai-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yuntao-bai)
- [![](https://img.shields.io/badge/Tristan_Hume-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tristan-hume)
- [![](https://img.shields.io/badge/Tom_Henighan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-henighan)
- [![](https://img.shields.io/badge/Sheer_El_Showk-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sheer-el-showk)
- [![](https://img.shields.io/badge/Shauna_Kravec-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shauna-kravec)
- [![](https://img.shields.io/badge/Scott_Johnston-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#scott-johnston)
- [![](https://img.shields.io/badge/Saurav_Kadavath-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#saurav-kadavath)
- [![](https://img.shields.io/badge/Nova_DasSarma-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nova-dassarma)
- [![](https://img.shields.io/badge/Nelson_Elhage-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nelson-elhage)
- [![](https://img.shields.io/badge/Liane_Lovitt-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#liane-lovitt)
- [![](https://img.shields.io/badge/Kamal_Ndousse-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kamal-ndousse)
- [![](https://img.shields.io/badge/Jackson_Kernion-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jackson-kernion)
- [![](https://img.shields.io/badge/Danny_Hernandez-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#danny-hernandez)
- [![](https://img.shields.io/badge/Catherine_Olsson-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#catherine-olsson)
- [![](https://img.shields.io/badge/Anna_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#anna-chen)
- [![](https://img.shields.io/badge/Deep_Ganguli-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#deep-ganguli)
- [![](https://img.shields.io/badge/Bosheng_Ding-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bosheng-ding)
- [![](https://img.shields.io/badge/Jasper_Snoek-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jasper-snoek)
- [![](https://img.shields.io/badge/Michael_W._Dusenberry-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-w.-dusenberry)
- [![](https://img.shields.io/badge/Xiaohua_Zhai-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaohua-zhai)
- [![](https://img.shields.io/badge/Mario_Lucic-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mario-lucic)
- [![](https://img.shields.io/badge/Joan_Puigcerver-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#joan-puigcerver)
- [![](https://img.shields.io/badge/Matthias_Minderer-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#matthias-minderer)
- [![](https://img.shields.io/badge/Rodolphe_Jenatton-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rodolphe-jenatton)
- [![](https://img.shields.io/badge/Basil_Mustafa-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#basil-mustafa)
- [![](https://img.shields.io/badge/Josip_Djolonga-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#josip-djolonga)
- [![](https://img.shields.io/badge/Yoon_Kim-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yoon-kim)
- [![](https://img.shields.io/badge/Chuanqi_Tan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chuanqi-tan)
- [![](https://img.shields.io/badge/Tong_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tong-zhang)
- [![](https://img.shields.io/badge/Shizhe_Diao-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shizhe-diao)
- [![](https://img.shields.io/badge/Shaohan_Huang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shaohan-huang)
- [![](https://img.shields.io/badge/Yunzhi_Yao-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yunzhi-yao)
- [![](https://img.shields.io/badge/Jian_Pei-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-pei)
- [![](https://img.shields.io/badge/Sean_Welleck-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sean-welleck)
- [![](https://img.shields.io/badge/Pan_Lu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pan-lu)
- [![](https://img.shields.io/badge/Hanlin_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hanlin-zhang)
- [![](https://img.shields.io/badge/Guilin_Qi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#guilin-qi)
- [![](https://img.shields.io/badge/Tongtong_Wu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tongtong-wu)
- [![](https://img.shields.io/badge/Muhao_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#muhao-chen)
- [![](https://img.shields.io/badge/Linh_Ngo_Van-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linh-ngo-van)
- [![](https://img.shields.io/badge/Hieu_Man-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hieu-man)
- [![](https://img.shields.io/badge/Thien_Nguyen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#thien-nguyen)
- [![](https://img.shields.io/badge/Franck_Dernoncourt-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#franck-dernoncourt)
- [![](https://img.shields.io/badge/Bonan_Min-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bonan-min)
- [![](https://img.shields.io/badge/Minh_Van_Nguyen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minh-van-nguyen)
- [![](https://img.shields.io/badge/Amir_Pouran_Ben_Veyseh-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#amir-pouran-ben-veyseh)
- [![](https://img.shields.io/badge/Orhan_Firat-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#orhan-firat)
- [![](https://img.shields.io/badge/Xavier_Garcia-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xavier-garcia)
- [![](https://img.shields.io/badge/Jing_Sha-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jing-sha)
- [![](https://img.shields.io/badge/Kun_Zhou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kun-zhou)
- [![](https://img.shields.io/badge/Zheng_Gong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zheng-gong)
- [![](https://img.shields.io/badge/Nathanael_Sch{\"{a}}rli-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nathanael-sch{\"{a}}rli)
- [![](https://img.shields.io/badge/David_Dohan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-dohan)
- [![](https://img.shields.io/badge/Nathan_Scales-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nathan-scales)
- [![](https://img.shields.io/badge/Lingpeng_Kong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lingpeng-kong)
- [![](https://img.shields.io/badge/Diyi_Yang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#diyi-yang)
- [![](https://img.shields.io/badge/Jiaao_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiaao-chen)
- [![](https://img.shields.io/badge/Xi_Ye-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xi-ye)
- [![](https://img.shields.io/badge/Hongxia_Jin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongxia-jin)
- [![](https://img.shields.io/badge/Yilin_Shen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yilin-shen)
- [![](https://img.shields.io/badge/Janghoon_Han-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#janghoon-han)
- [![](https://img.shields.io/badge/Erik_Cambria-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#erik-cambria)
- [![](https://img.shields.io/badge/Jinjie_Ni-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jinjie-ni)
- [![](https://img.shields.io/badge/Vlad_Pandelea-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vlad-pandelea)
- [![](https://img.shields.io/badge/Tom_Young-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tom-young)
- [![](https://img.shields.io/badge/Zhaojiang_Lin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhaojiang-lin)
- [![](https://img.shields.io/badge/Kevin_Murphy-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kevin-murphy)
- [![](https://img.shields.io/badge/Luowei_Zhou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luowei-zhou)
- [![](https://img.shields.io/badge/Linjie_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linjie-li)
- [![](https://img.shields.io/badge/Yue_Yu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-yu)
- [![](https://img.shields.io/badge/Hongyu_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongyu-zhang)
- [![](https://img.shields.io/badge/Zhou_Yang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhou-yang)
- [![](https://img.shields.io/badge/Jieke_Shi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jieke-shi)
- [![](https://img.shields.io/badge/Bowen_Xu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bowen-xu)
- [![](https://img.shields.io/badge/Hongzhi_Yin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongzhi-yin)
- [![](https://img.shields.io/badge/Jian_Yin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-yin)
- [![](https://img.shields.io/badge/Jin_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jin-liu)
- [![](https://img.shields.io/badge/Hao_Wu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-wu)
- [![](https://img.shields.io/badge/Li_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#li-li)
- [![](https://img.shields.io/badge/Pingyi_Zhou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pingyi-zhou)
- [![](https://img.shields.io/badge/Xin_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xin-wang)
- [![](https://img.shields.io/badge/Kai_Wei_Chang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kai-wei-chang)
- [![](https://img.shields.io/badge/Baishakhi_Ray-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#baishakhi-ray)
- [![](https://img.shields.io/badge/Saikat_Chakraborty-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#saikat-chakraborty)
- [![](https://img.shields.io/badge/Shujie_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shujie-liu)
- [![](https://img.shields.io/badge/Michele_Tufano-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michele-tufano)
- [![](https://img.shields.io/badge/Long_Zhou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#long-zhou)
- [![](https://img.shields.io/badge/Ge_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ge-li)
- [![](https://img.shields.io/badge/Shuo_Ren-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuo-ren)
- [![](https://img.shields.io/badge/Akhilesh_Deepak_Gotmare-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#akhilesh-deepak-gotmare)
- [![](https://img.shields.io/badge/Hung_Le-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hung-le)
- [![](https://img.shields.io/badge/Panos_Kalnis-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#panos-kalnis)
- [![](https://img.shields.io/badge/Lichao_Sun-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lichao-sun)
- [![](https://img.shields.io/badge/Hai_Jin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hai-jin)
- [![](https://img.shields.io/badge/Dejing_Dou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dejing-dou)
- [![](https://img.shields.io/badge/Ji_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ji-liu)
- [![](https://img.shields.io/badge/Lingjuan_Lyu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lingjuan-lyu)
- [![](https://img.shields.io/badge/Michael_Tschannen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#michael-tschannen)
- [![](https://img.shields.io/badge/Oriol_Vinyals-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#oriol-vinyals)
- [![](https://img.shields.io/badge/Chris_Brockett-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chris-brockett)
- [![](https://img.shields.io/badge/Yizhe_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yizhe-zhang)
- [![](https://img.shields.io/badge/Jian_Yun_Nie-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jian-yun-nie)
- [![](https://img.shields.io/badge/Yan_Zeng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yan-zeng)
- [![](https://img.shields.io/badge/Anima_Anandkumar-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#anima-anandkumar)
- [![](https://img.shields.io/badge/Eric_P._Xing-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-p.-xing)
- [![](https://img.shields.io/badge/Hao_Tian-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hao-tian)
- [![](https://img.shields.io/badge/Dianhai_Yu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dianhai-yu)
- [![](https://img.shields.io/badge/Weibao_Gong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#weibao-gong)
- [![](https://img.shields.io/badge/Shikun_Feng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shikun-feng)
- [![](https://img.shields.io/badge/Shuohuan_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shuohuan-wang)
- [![](https://img.shields.io/badge/Tie_Yan_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tie-yan-liu)
- [![](https://img.shields.io/badge/Tao_Qin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tao-qin)
- [![](https://img.shields.io/badge/Xu_Tan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xu-tan)
- [![](https://img.shields.io/badge/Kaitao_Song-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#kaitao-song)
- [![](https://img.shields.io/badge/Yejin_Choi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yejin-choi)
- [![](https://img.shields.io/badge/Baolin_Peng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#baolin-peng)
- [![](https://img.shields.io/badge/Julian_J._McAuley-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#julian-j.-mcauley)
- [![](https://img.shields.io/badge/Bodhisattwa_Prasad_Majumder-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bodhisattwa-prasad-majumder)
- [![](https://img.shields.io/badge/Tianrui_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianrui-li)
- [![](https://img.shields.io/badge/Luo_Si-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#luo-si)
- [![](https://img.shields.io/badge/Songfang_Huang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#songfang-huang)
- [![](https://img.shields.io/badge/Yijia_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yijia-liu)
- [![](https://img.shields.io/badge/Ruofei_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ruofei-zhang)
- [![](https://img.shields.io/badge/Jiusheng_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jiusheng-chen)
- [![](https://img.shields.io/badge/Pengcheng_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#pengcheng-wang)
- [![](https://img.shields.io/badge/Ming_Gong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ming-gong)
- [![](https://img.shields.io/badge/Linjun_Shou-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#linjun-shou)
- [![](https://img.shields.io/badge/Yeyun_Gong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yeyun-gong)
- [![](https://img.shields.io/badge/Yu_Yan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-yan)
- [![](https://img.shields.io/badge/Piji_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#piji-li)
- [![](https://img.shields.io/badge/Tianyi_Tang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianyi-tang)
- [![](https://img.shields.io/badge/Gaole_He-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gaole-he)
- [![](https://img.shields.io/badge/Yinhan_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yinhan-liu)
- [![](https://img.shields.io/badge/Richard_Socher-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#richard-socher)
- [![](https://img.shields.io/badge/Caiming_Xiong-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#caiming-xiong)
- [![](https://img.shields.io/badge/Bryan_McCann-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bryan-mccann)
- [![](https://img.shields.io/badge/Jianzhong_Qi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jianzhong-qi)
- [![](https://img.shields.io/badge/Xiaoyan_Zhu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaoyan-zhu)
- [![](https://img.shields.io/badge/Minlie_Huang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#minlie-huang)
- [![](https://img.shields.io/badge/Xiaojiang_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiaojiang-liu)
- [![](https://img.shields.io/badge/Bing_Qin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#bing-qin)
- [![](https://img.shields.io/badge/Yue_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yue-zhang)
- [![](https://img.shields.io/badge/Xiao_Liu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiao-liu)
- [![](https://img.shields.io/badge/Yu_Cheng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-cheng)
- [![](https://img.shields.io/badge/William_Yang_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-yang-wang)
- [![](https://img.shields.io/badge/Yu_Su-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yu-su)
- [![](https://img.shields.io/badge/Lu_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lu-wang)
- [![](https://img.shields.io/badge/Geoffrey_E._Hinton-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#geoffrey-e.-hinton)
- [![](https://img.shields.io/badge/Hui_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hui-chen)
- [![](https://img.shields.io/badge/Xiang_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-chen)
- [![](https://img.shields.io/badge/Shumin_Deng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shumin-deng)
- [![](https://img.shields.io/badge/Hongbin_Ye-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongbin-ye)
- [![](https://img.shields.io/badge/Yadao_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yadao-wang)
- [![](https://img.shields.io/badge/Mikel_Artetxe-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mikel-artetxe)
- [![](https://img.shields.io/badge/Hai_Tao_Zheng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hai-tao-zheng)
- [![](https://img.shields.io/badge/Shengding_Hu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#shengding-hu)
- [![](https://img.shields.io/badge/Ning_Ding-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ning-ding)
- [![](https://img.shields.io/badge/Yujia_Qin-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yujia-qin)
- [![](https://img.shields.io/badge/Sebastian_Riedel-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sebastian-riedel)
- [![](https://img.shields.io/badge/Yao_Lu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-lu)
- [![](https://img.shields.io/badge/Tushar_Khot-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tushar-khot)
- [![](https://img.shields.io/badge/Peter_Clark-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#peter-clark)
- [![](https://img.shields.io/badge/Yao_Fu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yao-fu)
- [![](https://img.shields.io/badge/Xiang_Deng-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xiang-deng)
- [![](https://img.shields.io/badge/Boshi_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#boshi-wang)
- [![](https://img.shields.io/badge/Samuel_R._Bowman-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#samuel-r.-bowman)
- [![](https://img.shields.io/badge/Yeganeh_Kordi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yeganeh-kordi)
- [![](https://img.shields.io/badge/Yizhong_Wang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yizhong-wang)
- [![](https://img.shields.io/badge/Slav_Petrov-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#slav-petrov)
- [![](https://img.shields.io/badge/Hongkun_Yu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongkun-yu)
- [![](https://img.shields.io/badge/Gaurav_Mishra-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#gaurav-mishra)
- [![](https://img.shields.io/badge/Sharan_Narang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sharan-narang)
- [![](https://img.shields.io/badge/Aakanksha_Chowdhery-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#aakanksha-chowdhery)
- [![](https://img.shields.io/badge/Xinyun_Chen-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#xinyun-chen)
- [![](https://img.shields.io/badge/William_Fedus-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#william-fedus)
- [![](https://img.shields.io/badge/Hyung_Won_Chung-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hyung-won-chung)
- [![](https://img.shields.io/badge/Ben_Hutchinson-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ben-hutchinson)
- [![](https://img.shields.io/badge/Mark_Diaz-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mark-diaz)
- [![](https://img.shields.io/badge/Vinodkumar_Prabhakaran-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vinodkumar-prabhakaran)
- [![](https://img.shields.io/badge/Toju_Duke-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#toju-duke)
- [![](https://img.shields.io/badge/Yanping_Huang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yanping-huang)
- [![](https://img.shields.io/badge/Nan_Du-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nan-du)
- [![](https://img.shields.io/badge/Vincent_Y._Zhao-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vincent-y.-zhao)
- [![](https://img.shields.io/badge/Zornitsa_Kozareva-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zornitsa-kozareva)
- [![](https://img.shields.io/badge/Srini_Iyer-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#srini-iyer)
- [![](https://img.shields.io/badge/Todor_Mihaylov-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#todor-mihaylov)
- [![](https://img.shields.io/badge/Zhifang_Sui-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhifang-sui)
- [![](https://img.shields.io/badge/Zhiyong_Wu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhiyong-wu)
- [![](https://img.shields.io/badge/Damai_Dai-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#damai-dai)
- [![](https://img.shields.io/badge/Benjamin_Mann-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#benjamin-mann)
- [![](https://img.shields.io/badge/David_Luan-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#david-luan)
- [![](https://img.shields.io/badge/Rewon_Child-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rewon-child)
- [![](https://img.shields.io/badge/Ryan_Sepassi-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#ryan-sepassi)
- [![](https://img.shields.io/badge/Zhuang_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#zhuang-li)
- [![](https://img.shields.io/badge/Vedant_Misra-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#vedant-misra)
- [![](https://img.shields.io/badge/Lukasz_Kaiser-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#lukasz-kaiser)
- [![](https://img.shields.io/badge/Nick_Ryder-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#nick-ryder)
- [![](https://img.shields.io/badge/Girish_Sastry-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#girish-sastry)
- [![](https://img.shields.io/badge/Raul_Puri-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#raul-puri)
- [![](https://img.shields.io/badge/Dan_Roth-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#dan-roth)
- [![](https://img.shields.io/badge/Hongming_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongming-zhang)
- [![](https://img.shields.io/badge/Alex_Smola-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#alex-smola)
- [![](https://img.shields.io/badge/Mu_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mu-li)
- [![](https://img.shields.io/badge/Tianyi_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tianyi-zhang)
- [![](https://img.shields.io/badge/Tatsunori_Hashimoto-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tatsunori-hashimoto)
- [![](https://img.shields.io/badge/Sang_Michael_Xie-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#sang-michael-xie)
- [![](https://img.shields.io/badge/Neel_Guha-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#neel-guha)
- [![](https://img.shields.io/badge/Mirac_Suzgun-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#mirac-suzgun)
- [![](https://img.shields.io/badge/Laurel_J._Orr-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#laurel-j.-orr)
- [![](https://img.shields.io/badge/Eric_Zelikman-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#eric-zelikman)
- [![](https://img.shields.io/badge/Christopher_R{\'{e}}-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#christopher-r{\'{e}})
- [![](https://img.shields.io/badge/Rishi_Bommasani-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rishi-bommasani)
- [![](https://img.shields.io/badge/Jonathan_Berant-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#jonathan-berant)
- [![](https://img.shields.io/badge/Rui_Zhang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#rui-zhang)
- [![](https://img.shields.io/badge/Hongjin_Su-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongjin-su)
- [![](https://img.shields.io/badge/Hongyu_Ren-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#hongyu-ren)
- [![](https://img.shields.io/badge/Junyi_Jessy_Li-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#junyi-jessy-li)
- [![](https://img.shields.io/badge/Albert_Webson-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#albert-webson)
- [![](https://img.shields.io/badge/Yiming_Yang-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#yiming-yang)
- [![](https://img.shields.io/badge/Tao_Yu-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#tao-yu)
- [![](https://img.shields.io/badge/Chia_Hsuan_Lee-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#chia-hsuan-lee)
- [![](https://img.shields.io/badge/Heng_Ji-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#heng-ji)
- [![](https://img.shields.io/badge/He_He-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author\README.md#he-he)
### Hyperlinks 
- [[Overview]](https://github.com/KSESEU/LLMPapers/blob/main/README.md) -- [Homepage](https://github.com/KSESEU/LLMPapers/blob/main/README.md)
-  -- [Summary](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/./)
-  -- [Author](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author)
-  -- [Techniques](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/techniques)
-  -- [Published Time](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time)
-  -- [Published Venue](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/venue)

### Luke Zettlemoyer

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [[Code]](https://github.com/facebookresearch/MetaICL) ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>```MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Nan Duan

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>```We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
and supports the development of versatile
knowledge-infused model.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
### Denny Zhou

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Xuezhi Wang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>```Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.```<br><br>
### Ed H. Chi

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Jason Wei

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Ming Zhou

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>```We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
and supports the development of versatile
knowledge-infused model.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Ji Rong Wen

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Fei Huang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.13808) [**Large Language Models are Versatile Decomposers: Decompose Evidence
and Questions for Table-based Reasoning**](https://doi.org/10.48550/arXiv.2301.13808),<br> by *Yunhu Ye, Binyuan Hui, Min Yang, Binhua Li, Fei Huang and Yongbin Li*
<br><br>
- [![](https://img.shields.io/badge/IJCAI-2022-blue)](https://doi.org/10.24963/ijcai.2022/273) [**Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in
the Federated Setting**](https://doi.org/10.24963/ijcai.2022/273),<br> by *Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Furu Wei

- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=SygXPaEYvH) [**VL-BERT: Pre-training of Generic Visual-Linguistic Representations**](https://openreview.net/forum?id=SygXPaEYvH),<br> by *Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu, Furu Wei and Jifeng Dai*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Jianfeng Gao

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Mike Lewis

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [[Code]](https://github.com/facebookresearch/MetaICL) ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>```MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Dustin Tran

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html) [**Soft Calibration Objectives for Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html),<br> by *Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer and Becca Roelofs*
<br><br>
### Neel Sundaresan

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
- [![](https://img.shields.io/badge/FSE-2020-blue)](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: code generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Dawn Drain

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
### Wayne Xin Zhao

- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Yi Tay

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Quoc V. Le

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=r1xMH1BtvB) [**ELECTRA: Pre-training Text Encoders as Discriminators Rather Than
Generators**](https://openreview.net/forum?id=r1xMH1BtvB), ![](https://img.shields.io/badge/ELECTRA-yellow) <br> by *Kevin Clark, Minh-Thang Luong, Quoc V. Le and Christopher D. Manning*
<br><br>
### Maarten Bosma

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Percy Liang

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=RdJVFCHjUMI) [**An Explanation of In-context Learning as Implicit Bayesian Inference**](https://openreview.net/forum?id=RdJVFCHjUMI),<br> by *Sang Michael Xie, Aditi Raghunathan, Percy Liang and Tengyu Ma*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.353) [**Prefix-Tuning: Optimizing Continuous Prompts for Generation**](https://doi.org/10.18653/v1/2021.acl-long.353),<br> by *Xiang Lisa Li and Percy Liang*
<br><br>
### Sewon Min

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [[Code]](https://github.com/facebookresearch/MetaICL) ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>```MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Noah A. Smith

- [![](https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7_11,_2022-2022-blue)](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
### Jun Zhao

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>```This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task```<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>```We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://www.aclweb.org/anthology/2020.emnlp-main.52) [**Incremental Event Detection via Knowledge Consolidation Networks**](https://www.aclweb.org/anthology/2020.emnlp-main.52),<br> by *Cao, Pengfei , Chen, Yubo , Zhao, Jun  and Wang, Taifeng*
<br>```Proposing a hybrid continual learning method for event detection, combining experience replay and Knowledge Distillation, focusing on (1) semantic ambiguity in NLP and (2) data imbalance between memory and current task.```<br><br>
### Shengyu Fu

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/FSE-2020-blue)](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: code generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Alexey Svyatkovskiy

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/FSE-2020-blue)](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: code generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Daya Guo

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Shuai Lu

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Shafiq R. Joty

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.737) [**A Unified Speaker Adaptation Approach for ASR**](https://aclanthology.org/2021.emnlp-main.737),<br> by *Yingzhu Zhao, Chongjia Ni, Cheung-Chi Leung, Shafiq R. Joty, Eng Siong Chng and Bin Ma*
<br>```Prefix-based user identifier, Continual ASR / Architecture Search / Network Pruning.```<br><br>
### Yue Wang

- [![](https://img.shields.io/badge/openreview-2023-blue)](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.57) [**Detect-Localize-Repair: A Unified Framework for Learning to Debug
with CodeT5**](https://aclanthology.org/2022.findings-emnlp.57),<br> by *Nghi Bui, Yue Wang and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
### Shuohang Wang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.09150) [**Prompting GPT-3 To Be Reliable**](https://doi.org/10.48550/arXiv.2210.09150),<br> by *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan L. Boyd-Graber and Lijuan Wang*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.495) [**T3: Tree-Autoencoder Constrained Adversarial Text Generation for
Targeted Attack**](https://doi.org/10.18653/v1/2020.emnlp-main.495),<br> by *Boxin Wang, Hengzhi Pei, Boyuan Pan, Qian Chen, Shuohang Wang and Bo Li*
<br><br>
### Daxin Jiang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>```We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
and supports the development of versatile
knowledge-infused model.```<br><br>
### Weizhu Chen

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10),<br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
### Junyi Li

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Li Dong

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Jingjing Liu

- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Zhe Gan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.09150) [**Prompting GPT-3 To Be Reliable**](https://doi.org/10.48550/arXiv.2210.09150),<br> by *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan L. Boyd-Graber and Lijuan Wang*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Wenhu Chen

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.06710) [**Large Language Models are few(1)-shot Table Reasoners**](https://doi.org/10.48550/arXiv.2210.06710),<br> by *Wenhu Chen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.190) [**Logic2Text: High-Fidelity Natural Language Generation from Logical
Forms**](https://doi.org/10.18653/v1/2020.findings-emnlp.190),<br> by *Zhiyu Chen, Wenhu Chen, Hanwen Zha, Xiyou Zhou, Yunkai Zhang, Sairam Sundaresan and William Yang Wang*
<br><br>
### Asli Celikyilmaz

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
### Huajun Chen

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/IJCAI-2022-blue)](https://doi.org/10.24963/ijcai.2022/273) [**Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in
the Federated Setting**](https://doi.org/10.24963/ijcai.2022/273),<br> by *Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Dale Schuurmans

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.00747) [**Rationale-Augmented Ensembles in Language Models**](https://doi.org/10.48550/arXiv.2207.00747),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
### Veselin Stoyanov

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Ramakanth Pasunuru

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07842) [**Augmented Language Models: a Survey**](https://doi.org/10.48550/arXiv.2302.07842),<br> by *Gr\'egoire Mialon, Roberto Dess\`\i, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Rozi\`ere, Timo Schick et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Dario Amodei

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
### Jared Kaplan

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
### Pascale Fung

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>```本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。```<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>```Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.```<br><br>
### Hannaneh Hajishirzi

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201), [[Code]](https://github.com/facebookresearch/MetaICL) ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br>```MetaICL proposes a supervised meta-training framework to enable LMs to more effectively learn a new task in context. In MetaICL, each meta-training example includes several training examples from one task that will be presented together as a single sequence to the LM, and the prediction of the final example is used to calculate the loss.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
### Kang Liu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>```This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task```<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>```We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.```<br><br>
### Shizhu He

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09561) [**Large Language Models are reasoners with Self-Verification**](https://doi.org/10.48550/arXiv.2212.09561),<br> by *Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu and Jun Zhao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>```This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task```<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>```We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.```<br><br>
### Bing Liu

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>```NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.```<br><br>
- [![](https://img.shields.io/badge/EACL-2021-blue)](https://doi.org/10.18653/v1/2021.eacl-main.95) [**Analyzing the Forgetting Problem in Pretrain-Finetuning of Open-domain
Dialogue Response Models**](https://doi.org/10.18653/v1/2021.eacl-main.95),<br> by *Tianxing He, Jun Liu, Kyunghyun Cho, Myle Ott, Bing Liu, James R. Glass and Fuchun Peng*
<br>```Our major finding is that after standard finetuning, the model forgets some of the important language generation skills acquired during large-scale pretraining. We propose an intuitive finetuning strategy named “mix-review”: : For each finetuning epoch, we mix the target dialogue data with a random subset of the pretraining data, mix_ratio is 4, decay is 0.9.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>```The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.```<br><br>
### Myle Ott

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [![](https://img.shields.io/badge/EACL-2021-blue)](https://doi.org/10.18653/v1/2021.eacl-main.95) [**Analyzing the Forgetting Problem in Pretrain-Finetuning of Open-domain
Dialogue Response Models**](https://doi.org/10.18653/v1/2021.eacl-main.95),<br> by *Tianxing He, Jun Liu, Kyunghyun Cho, Myle Ott, Bing Liu, James R. Glass and Fuchun Peng*
<br>```Our major finding is that after standard finetuning, the model forgets some of the important language generation skills acquired during large-scale pretraining. We propose an intuitive finetuning strategy named “mix-review”: : For each finetuning epoch, we mix the target dialogue data with a random subset of the pretraining data, mix_ratio is 4, decay is 0.9.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Lidong Bing

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>```we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness:  it tends
to outperform fine-tuning on both low-resource and
cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to
fine-tuning.```<br><br>
### Linlin Liu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10529) [**Is GPT-3 a Psychopath? Evaluating Large Language Models from a Psychological
Perspective**](https://doi.org/10.48550/arXiv.2212.10529),<br> by *Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing and Shafiq R. Joty*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>```we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness:  it tends
to outperform fine-tuning on both low-resource and
cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to
fine-tuning.```<br><br>
### Balaji Lakshminarayanan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html) [**Soft Calibration Objectives for Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html),<br> by *Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer and Becca Roelofs*
<br><br>
### Neil Houlsby

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Thien Huu Nguyen

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.starsem-1.11) [**Word-Label Alignment for Event Detection: A New Perspective via
Optimal Transport**](https://doi.org/10.18653/v1/2022.starsem-1.11),<br> by *Amir Pouran Ben Veyseh and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/ECML-2021-blue)](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Shijin Wang

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
### Chengwei Qin

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=HCRVf71PMF) [**LFPT5: A Unified Framework for Lifelong Few-shot Language Learning Based on Prompt Tuning of T5**](https://openreview.net/forum?id=HCRVf71PMF),<br> by *Chengwei Qin and Shafiq Joty*
<br>```We define a challenging yet practical problem as Lifelong Few-shot Language Learning and propose a unified framework for it based on prompt tuning of T5.```<br><br>
### Pengcheng He

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Mohit Bansal

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.162) [**Vokenization: Improving Language Understanding with Contextualized,
Visual-Grounded Supervision**](https://doi.org/10.18653/v1/2020.emnlp-main.162),<br> by *Hao Tan and Mohit Bansal*
<br><br>
### David Lo

- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICSME-2020-blue)](https://ieeexplore.ieee.org/abstract/document/9240704/) [**Sentiment analysis for software engineering: How far can pre-trained transformer models go?**](https://ieeexplore.ieee.org/abstract/document/9240704/),<br> by *Zhang, Ting, Xu, Bowen, Thung, Ferdian, Haryono, Stefanus Agus, Lo, David and Jiang, Lingxiao*
<br><br>
### Shao Kun Deng

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/FSE-2020-blue)](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: code generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
### Duyu Tang

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.121) [**K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters**](https://doi.org/10.18653/v1/2021.findings-acl.121),<br> by *Ruize Wang, Duyu Tang, Nan Duan, Zhongyu Wei, Xuanjing Huang, Jianshu Ji, Guihong Cao, Daxin Jiang et al.*
<br>```We propose KADAPTER, a framework that retains the original parameters of the pre-trained model fixed
and supports the development of versatile
knowledge-infused model.```<br><br>
### Colin B. Clement

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
### Steven C. H. Hoi

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.57) [**Detect-Localize-Repair: A Unified Framework for Learning to Debug
with CodeT5**](https://aclanthology.org/2022.findings-emnlp.57),<br> by *Nghi Bui, Yue Wang and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
### Yao Wan

- [![](https://img.shields.io/badge/TIST-2022-blue)](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Bill Dolan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10),<br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
### Michael Zeng

- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Chenguang Zhu

- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Michel Galley

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
### Wei Wang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/ECIR-2021-blue)](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.140) [**StyleDGPT: Stylized Response Generation with Pre-trained Language
Models**](https://doi.org/10.18653/v1/2020.findings-emnlp.140),<br> by *Ze Yang, Wei Wu, Can Xu, Xinnian Liang, Jiaqi Bai, Liran Wang, Wei Wang and Zhoujun Li*
<br><br>
### Nicholas Jing Yuan

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Zhicheng Wei

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Naman Goyal

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Yu Sun

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Xiaodong Gu

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549094) [**Diet code is healthy: simplifying programs for pre-trained models
of code**](https://doi.org/10.1145/3540250.3549094),<br> by *Zhaowei Zhang, Hongyu Zhang, Beijun Shen and Xiaodong Gu*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/17527) [**DialogBERT: Discourse-Aware Response Generation via Learning to Recover
and Rank Utterances**](https://ojs.aaai.org/index.php/AAAI/article/view/17527),<br> by *Xiaodong Gu, Kang Min Yoo and Jung-Woo Ha*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2111.02643) [**Response Generation with Context-Aware Prompt Learning**](https://arxiv.org/abs/2111.02643),<br> by *Xiaodong Gu, Kang Min Yoo and Sang-Woo Lee*
<br><br>
### Zhou Yu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-short.40) [**PRAL: A Tailored Pre-Training Model for Task-Oriented Dialog Generation**](https://doi.org/10.18653/v1/2021.acl-short.40),<br> by *Jing Gu, Qingyang Wu, Chongruo Wu, Weiyan Shi and Zhou Yu*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.239) [**Action-Based Conversations Dataset: A Corpus for Building More In-Depth
Task-Oriented Dialogue Systems**](https://doi.org/10.18653/v1/2021.naacl-main.239),<br> by *Derek Chen, Howard Chen, Yi Yang, Alexander Lin and Zhou Yu*
<br><br>
### Ting Liu

- [![](https://img.shields.io/badge/COLING-2020-blue)](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>```We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.```<br><br>
### Iryna Gurevych

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2007.08426) [**Investigating Pretrained Language Models for Graph-to-Text Generation**](https://arxiv.org/abs/2007.08426),<br> by *Leonardo F. R. Ribeiro, Martin Schmitt, Hinrich Sch\"utze and Iryna Gurevych*
<br><br>
### Leonardo F. R. Ribeiro

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2007.08426) [**Investigating Pretrained Language Models for Graph-to-Text Generation**](https://arxiv.org/abs/2007.08426),<br> by *Leonardo F. R. Ribeiro, Martin Schmitt, Hinrich Sch\"utze and Iryna Gurevych*
<br><br>
### Andrea Madotto

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=H1edEyBKDS) [**Plug and Play Language Models: A Simple Approach to Controlled Text
Generation**](https://openreview.net/forum?id=H1edEyBKDS),<br> by *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski and Rosanne Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>```Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.```<br><br>
### Wenhui Wang

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
### Yen Chun Chen

- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Haifeng Wang

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.9) [**PLATO: Pre-trained Dialogue Generation Model with Discrete Latent
Variable**](https://doi.org/10.18653/v1/2020.acl-main.9),<br> by *Siqi Bao, Huang He, Fan Wang, Hua Wu and Haifeng Wang*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Hua Wu

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.9) [**PLATO: Pre-trained Dialogue Generation Model with Discrete Latent
Variable**](https://doi.org/10.18653/v1/2020.acl-main.9),<br> by *Siqi Bao, Huang He, Fan Wang, Hua Wu and Haifeng Wang*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Ningyu Zhang

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Yasheng Wang

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Xiang Ren

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.351) [**Lifelong Pretraining: Continually Adapting Language Models to Emerging
Corpora**](https://doi.org/10.18653/v1/2022.naacl-main.351),<br> by *Xisen Jin, Dejiao Zhang, Henghui Zhu, Wei Xiao, Shang-Wen Li, Xiaokai Wei, Andrew O. Arnold and Xiang Ren*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://aclanthology.org/2021.findings-emnlp.62) [**Learn Continually, Generalize Rapidly: Lifelong Knowledge Accumulation for Few-shot Learning**](https://aclanthology.org/2021.findings-emnlp.62),<br> by *Jin, Xisen , Lin, Bill Yuchen , Rostami, Mohammad  and Ren, Xiang*
<br>```We present a new learning setup, Continual Learning of Few-Shot Learners, to address challenges of both learning settings in a unified setup, with a hyper-network for task-specific adapter generation.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://www.aclweb.org/anthology/2020.emnlp-main.158) [**Visually Grounded Continual Learning of Compositional Phrases**](https://www.aclweb.org/anthology/2020.emnlp-main.158),<br> by *Jin, Xisen , Du, Junyi , Sadhu, Arka , Nevatia, Ram  and Ren, Xiang*
<br>```A novel continual learning setting and a new benchmark for continual caption generation, evaluated with exiting rehearsal-based methods```<br><br>
### Xisen Jin

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.351) [**Lifelong Pretraining: Continually Adapting Language Models to Emerging
Corpora**](https://doi.org/10.18653/v1/2022.naacl-main.351),<br> by *Xisen Jin, Dejiao Zhang, Henghui Zhu, Wei Xiao, Shang-Wen Li, Xiaokai Wei, Andrew O. Arnold and Xiang Ren*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://aclanthology.org/2021.findings-emnlp.62) [**Learn Continually, Generalize Rapidly: Lifelong Knowledge Accumulation for Few-shot Learning**](https://aclanthology.org/2021.findings-emnlp.62),<br> by *Jin, Xisen , Lin, Bill Yuchen , Rostami, Mohammad  and Ren, Xiang*
<br>```We present a new learning setup, Continual Learning of Few-Shot Learners, to address challenges of both learning settings in a unified setup, with a hyper-network for task-specific adapter generation.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://www.aclweb.org/anthology/2020.emnlp-main.158) [**Visually Grounded Continual Learning of Compositional Phrases**](https://www.aclweb.org/anthology/2020.emnlp-main.158),<br> by *Jin, Xisen , Du, Junyi , Sadhu, Arka , Nevatia, Ram  and Ren, Xiang*
<br>```A novel continual learning setting and a new benchmark for continual caption generation, evaluated with exiting rehearsal-based methods```<br><br>
### Maosong Sun

- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Zhiyuan Liu

- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Yang Liu

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.424) [**MSP: Multi-Stage Prompting for Making Pre-trained Language Models
Better Translators**](https://doi.org/10.18653/v1/2022.acl-long.424),<br> by *Zhixing Tan, Xiangwen Zhang, Shuo Wang and Yang Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.354) [**Want To Reduce Labeling Cost? GPT-3 Can Help**](https://doi.org/10.18653/v1/2021.findings-emnlp.354),<br> by *Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu and Michael Zeng*
<br><br>
### Noah Constant

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.346) [**SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer**](https://doi.org/10.18653/v1/2022.acl-long.346),<br> by *Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou' and Daniel Cer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.243) [**The Power of Scale for Parameter-Efficient Prompt Tuning**](https://doi.org/10.18653/v1/2021.emnlp-main.243),<br> by *Brian Lester, Rami Al-Rfou and Noah Constant*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>```Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.```<br><br>
### Kang Min Yoo

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.08082) [**Self-Generated In-Context Learning: Leveraging Auto-regressive Language
Models as a Demonstration Generator**](https://doi.org/10.48550/arXiv.2206.08082),<br> by *Hyuhng Joon Kim, Hyunsoo Cho, Junyeob Kim, Taeuk Kim, Kang Min Yoo and Sang-goo Lee*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/17527) [**DialogBERT: Discourse-Aware Response Generation via Learning to Recover
and Rank Utterances**](https://ojs.aaai.org/index.php/AAAI/article/view/17527),<br> by *Xiaodong Gu, Kang Min Yoo and Jung-Woo Ha*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2111.02643) [**Response Generation with Context-Aware Prompt Learning**](https://arxiv.org/abs/2111.02643),<br> by *Xiaodong Gu, Kang Min Yoo and Sang-Woo Lee*
<br><br>
### Ashish Sabharwal

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
### Hao Peng

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Huan Sun

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.329) [**Thinking about GPT-3 In-Context Learning for Biomedical IE? Think
Again**](https://aclanthology.org/2022.findings-emnlp.329),<br> by *Bernal Jimenez Gutierrez, Nikolas McNeal, Clayton Washington, You Chen, Lang Li, Huan Sun and Yu Su*
<br><br>
### Omer Levy

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Swaroop Mishra

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
### Jacob Devlin

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2019-blue)](https://doi.org/10.18653/v1/n19-1423) [**BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding**](https://doi.org/10.18653/v1/n19-1423), ![](https://img.shields.io/badge/BERT-yellow) <br> by *Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova*
<br><br>
### Jeff Dean

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Shixiang Shane Gu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.11916) [**Large Language Models are Zero-Shot Reasoners**](https://doi.org/10.48550/arXiv.2205.11916),<br> by *Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo and Yusuke Iwasawa*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Mostafa Dehghani

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Barret Zoph

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Le Hou

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Quoc Le

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
### Adam Roberts

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Andrew M. Dai

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Brian Lester

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.346) [**SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer**](https://doi.org/10.18653/v1/2022.acl-long.346),<br> by *Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou' and Daniel Cer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.243) [**The Power of Scale for Parameter-Efficient Prompt Tuning**](https://doi.org/10.18653/v1/2021.emnlp-main.243),<br> by *Brian Lester, Rami Al-Rfou and Noah Constant*
<br><br>
### Jingfei Du

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Lei Li

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.06950) [**Pre-trained Language Models can be Fully Zero-Shot Learners**](https://doi.org/10.48550/arXiv.2212.06950),<br> by *Xuandong Zhao, Siqi Ouyang, Zhiguo Yu, Ming Wu and Lei Li*
<br><br>
### Amanda Askell

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
### others

- [![](https://img.shields.io/badge/PLOS_Digital_Health-2023-blue)](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198&trk=public_post_comment-text) [**Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models**](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198&trk=public_post_comment-text),<br> by *Kung, Tiffany H, Cheatham, Morgan, Medenilla, Arielle, Sillos, Czarina, De Leon, Lorie, Elepa\~no, Camille, Madriaga, Maria, Aggabao, Rimel et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2018-blue)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), ![](https://img.shields.io/badge/GPT--1-yellow) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Noam Shazeer

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2018-blue)](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Gholamreza Haffari

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>```To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.233) [**Lifelong Explainer for Lifelong Learners**](https://aclanthology.org/2021.emnlp-main.233),<br> by *Situ, Xuelin , Maruf, Sameen , Zukerman, Ingrid , Paris, Cecile  and Haffari, Gholamreza*
<br>```We propose a novel Lifelong Explanation approach that continuously trains a student explainer under the supervision of a teacher – an arbitrary explanation algorithm – on different tasks undertaken in LL. We also leverage the Experience Replay mechanism to prevent catastrophic forgetting in the student explainer.```<br><br>
### Ilya Sutskever

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2018-blue)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), ![](https://img.shields.io/badge/GPT--1-yellow) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Sam McCandlish

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Alec Radford

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2018-blue)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), ![](https://img.shields.io/badge/GPT--1-yellow) <br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Jie Tang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
### Nicholas Joseph

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Aston Zhang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Zhuosheng Zhang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Christopher D. Manning

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=r1xMH1BtvB) [**ELECTRA: Pre-training Text Encoders as Discriminators Rather Than
Generators**](https://openreview.net/forum?id=r1xMH1BtvB), ![](https://img.shields.io/badge/ELECTRA-yellow) <br> by *Kevin Clark, Minh-Thang Luong, Quoc V. Le and Christopher D. Manning*
<br><br>
### Michihiro Yasunaga

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
### Greg Durrett

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04813) [**Explanation Selection Using Unlabeled Data for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.04813),<br> by *Xi Ye and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356),<br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://par.nsf.gov/biblio/10380030) [**The unreliability of explanations in few-shot prompting for textual reasoning**](https://par.nsf.gov/biblio/10380030),<br> by *Ye, Xi and Durrett, Greg*
<br><br>
### Graham Neubig

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Uri Alon

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Shuyan Zhou

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Aman Madaan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.07686) [**Text and Patterns: For Effective Chain of Thought, It Takes Two to
Tango**](https://doi.org/10.48550/arXiv.2209.07686),<br> by *Aman Madaan and Amir Yazdanbakhsh*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Mari Ostendorf

- [![](https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7_11,_2022-2022-blue)](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
### George Karypis

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53),<br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br><br>
- [![](https://img.shields.io/badge/IA3-2020-blue)](https://doi.org/10.1109/IA351965.2020.00011) [**DistDGL: Distributed Graph Neural Network Training for Billion-Scale
Graphs**](https://doi.org/10.1109/IA351965.2020.00011),<br> by *Da Zheng, Chao Ma, Minjie Wang, Jinjing Zhou, Qidong Su, Xiang Song, Quan Gan, Zheng Zhang et al.*
<br><br>
### Tuo Zhao

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Chen Liang

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Qingru Zhang

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Simiao Zuo

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.116) [**MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation**](https://doi.org/10.18653/v1/2022.naacl-main.116),<br> by *Simiao Zuo, Qingru Zhang, Chen Liang, Pengcheng He, Tuo Zhao and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01351) [**Less is More: Task-aware Layer-wise Distillation for Language Model
Compression**](https://doi.org/10.48550/arXiv.2210.01351),<br> by *Chen Liang, Simiao Zuo, Qingru Zhang, Pengcheng He, Weizhu Chen and Tuo Zhao*
<br><br>
### Dani Yogatama

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html) [**Episodic Memory in Lifelong Language Learning**](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html),<br> by *Cyprien de Masson d'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama*
<br>```MbPA++. This paper proposes the use of memory (a fixed memory network) in life-long learning to prevent catastrophic forgetting by means of  experience replay and local adaptation. ```<br><br>
### Pengfei Cao

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>```This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://www.aclweb.org/anthology/2020.emnlp-main.52) [**Incremental Event Detection via Knowledge Consolidation Networks**](https://www.aclweb.org/anthology/2020.emnlp-main.52),<br> by *Cao, Pengfei , Chen, Yubo , Zhao, Jun  and Wang, Taifeng*
<br>```Proposing a hybrid continual learning method for event detection, combining experience replay and Knowledge Distillation, focusing on (1) semantic ambiguity in NLP and (2) data imbalance between memory and current task.```<br><br>
### Qingbin Liu

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.176) [**Domain-Lifelong Learning for Dialogue State Tracking via Knowledge Preservation Networks**](https://aclanthology.org/2021.emnlp-main.176),<br> by *Liu, Qingbin , Cao, Pengfei , Liu, Cao , Chen, Jiansong , Cai, Xunliang , Yang, Fan , He, Shizhu , Liu, Kang  et al.*
<br>```This paper explores Domain-Lifelong Learning for Dialogue State Tracking, we propose Knowledge Preservation Network, which consists of multi-prototype enhanced retrospection and multi-strategy knowledge distillation, to solve the problems of expression diversity and combinatorial explosion in the DLL-DST task```<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04445) [**Lifelong Intent Detection via Multi-Strategy Rebalancing**](https://arxiv.org/abs/2108.04445),<br> by *Qingbin Liu, Xiaoyan Yu, Shizhu He, Kang Liu and Jun Zhao*
<br>```We propose the lifelong intent detection task to handle continually emerging user intents. And, we propose multistrategy rebalancing to address multiple adverse effects caused by the data imbalance problem.```<br><br>
### Lei Shu

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>```NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>```The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.```<br><br>
### Hu Xu

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>```NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>```The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.```<br><br>
### Zixuan Ke

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html) [**Achieving Forgetting Prevention and Knowledge Transfer in Continual
Learning**](https://proceedings.neurips.cc/paper/2021/hash/bcd0049c35799cdf57d06eaf2eb3cff6-Abstract.html),<br> by *Zixuan Ke, Bing Liu, Nianzu Ma, Hu Xu and Lei Shu*
<br>```NeurIPS 2021, The key component of CTR is the CL-plugin inserted in BERT. A CL-plugin is a capsule network with a new transfer routing mechanism to encourage knowledge transfer among tasks and also to isolate task-specific knowledge to avoid forgetting.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://aclanthology.org/2021.emnlp-main.550) [**CLASSIC: Continual and Contrastive Learning of Aspect Sentiment Classification Tasks**](https://aclanthology.org/2021.emnlp-main.550),<br> by *Ke, Zixuan , Liu, Bing , Xu, Hu  and Shu, Lei*
<br>```The key novelty is a contrastive continual learning method that enables both knowledge transfer across tasks and knowledge distillation from old tasks to the new task, which eliminates the need for task ids in testing.```<br><br>
### Wanxiang Che

- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>```We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.```<br><br>
### Yiming Cui

- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.634) [**Recall and Learn: Fine-tuning Deep Pretrained Language Models with
Less Forgetting**](https://doi.org/10.18653/v1/2020.emnlp-main.634),<br> by *Sanyuan Chen, Yutai Hou, Yiming Cui, Wanxiang Che, Ting Liu and Xiangzhan Yu*
<br>```We propose a recall and learn mechanism, which adopts the idea of multi-task learning and jointly learns pretraining tasks and downstream tasks. Specifically, we introduce a Pretraining Simulation mechanism to recall the knowledge from pretraining tasks without data, and an Objective Shifting mechanism to focus the learning on downstream tasks gradually.```<br><br>
### Jack Clark

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Zac Hatfield Dodds

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Yuntao Bai

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Tristan Hume

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Tom Henighan

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Sheer El Showk

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Shauna Kravec

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Scott Johnston

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Saurav Kadavath

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Nova DasSarma

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Nelson Elhage

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Liane Lovitt

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Kamal Ndousse

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Jackson Kernion

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Danny Hernandez

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Catherine Olsson

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Anna Chen

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Deep Ganguli

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
### Bosheng Ding

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10450) [**Is GPT-3 a Good Data Annotator?**](https://doi.org/10.48550/arXiv.2212.10450),<br> by *Bosheng Ding, Chengwei Qin, Linlin Liu, Lidong Bing, Shafiq R. Joty and Boyang Li*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>```we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness:  it tends
to outperform fine-tuning on both low-resource and
cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to
fine-tuning.```<br><br>
### Jasper Snoek

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
### Michael W. Dusenberry

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=g11CZSghXyY) [**Combining Ensembles and Data Augmentation Can Harm Your Calibration**](https://openreview.net/forum?id=g11CZSghXyY),<br> by *Yeming Wen, Ghassen Jerfel, Rafael Muller, Michael W. Dusenberry, Jasper Snoek, Balaji Lakshminarayanan and Dustin Tran*
<br><br>
### Xiaohua Zhai

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Mario Lucic

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Joan Puigcerver

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Matthias Minderer

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Rodolphe Jenatton

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
### Basil Mustafa

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.05055) [**Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints**](https://doi.org/10.48550/arXiv.2212.05055),<br> by *Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa, Joshua Ainslie, Yi Tay, Mostafa Dehghani et al.*
<br><br>
### Josip Djolonga

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) [**Revisiting the Calibration of Modern Neural Networks**](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html),<br> by *Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran and Mario Lucic*
<br><br>
### Yoon Kim

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.130) [**Large language models are few-shot clinical information extractors**](https://aclanthology.org/2022.emnlp-main.130),<br> by *Monica Agrawal, Stefan Hegselmann, Hunter Lang, Yoon Kim and David A. Sontag*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://aclanthology.org/2021.acl-long.378) [**Parameter-Efficient Transfer Learning with Diff Pruning**](https://aclanthology.org/2021.acl-long.378),<br> by *Guo, Demi , Rush, Alexander  and Kim, Yoon*
<br>```The approach learns a task-specific “diff” vector that extends the original pretrained parameters. As the number of tasks increases, diff pruning remains parameter-efficient, as it requires storing only a small diff vector for each task.```<br><br>
### Chuanqi Tan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Tong Zhang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Shizhe Diao

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Shaohan Huang

- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.163) [**Snapshot-Guided Domain Adaptation for ELECTRA**](https://aclanthology.org/2022.findings-emnlp.163),<br> by *Daixuan Cheng, Shaohan Huang, Jianfeng Liu, Yuefeng Zhan, Hao Sun, Furu Wei, Denvy Deng and Qi Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
### Yunzhi Yao

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.40) [**Adapt-and-Distill: Developing Small, Fast and Effective Pretrained
Language Models for Domains**](https://doi.org/10.18653/v1/2021.findings-acl.40),<br> by *Yunzhi Yao, Shaohan Huang, Wenhui Wang, Li Dong and Furu Wei*
<br><br>
### Jian Pei

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.02093) [**Knowledge-enhanced Neural Machine Reasoning: A Review**](https://doi.org/10.48550/arXiv.2302.02093),<br> by *Tanmoy Chowdhury, Chen Ling, Xuchao Zhang, Xujiang Zhao, Guangji Bai, Jian Pei, Haifeng Chen and Liang Zhao*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
### Sean Welleck

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
### Pan Lu

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.218) [**UniGeo: Unifying Geometry Logical Reasoning via Reformulating Mathematical
Expression**](https://aclanthology.org/2022.emnlp-main.218),<br> by *Jiaqi Chen, Tong Li, Jinghui Qin, Pan Lu, Liang Lin, Chongyu Chen and Xiaodan Liang*
<br><br>
### Hanlin Zhang

- [![](https://img.shields.io/badge/ICML-2022-blue)](https://openreview.net/forum?id=8lNy3QCaxHX) [**Improved logical reasoning of language models via differentiable symbolic programming**](https://openreview.net/forum?id=8lNy3QCaxHX),<br> by *Zhang, Hanlin, Li, Ziyang, Huang, Jiani, Naik, Mayur and Xing, Eric*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
### Guilin Qi

- [![](https://img.shields.io/badge/COLING-2022-blue)](https://aclanthology.org/2022.coling-1.200) [**Event Causality Identification via Derivative Prompt Joint Learning**](https://aclanthology.org/2022.coling-1.200),<br> by *Shirong Shen, Heng Zhou, Tongtong Wu and Guilin Qi*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>```To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.```<br><br>
### Tongtong Wu

- [![](https://img.shields.io/badge/COLING-2022-blue)](https://aclanthology.org/2022.coling-1.200) [**Event Causality Identification via Derivative Prompt Joint Learning**](https://aclanthology.org/2022.coling-1.200),<br> by *Shirong Shen, Heng Zhou, Tongtong Wu and Guilin Qi*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>```To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.```<br><br>
### Muhao Chen

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.107) [**Salience-Aware Event Chain Modeling for Narrative Understanding**](https://doi.org/10.18653/v1/2021.emnlp-main.107),<br> by *Xiyang Zhang, Muhao Chen and Jonathan May*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Linh Ngo Van

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Hieu Man

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Thien Nguyen

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Franck Dernoncourt

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
### Bonan Min

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/ECML-2021-blue)](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Minh Van Nguyen

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/ECML-2021-blue)](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Amir Pouran Ben Veyseh

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.starsem-1.11) [**Word-Label Alignment for Event Detection: A New Perspective via
Optimal Transport**](https://doi.org/10.18653/v1/2022.starsem-1.11),<br> by *Amir Pouran Ben Veyseh and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/ECML-2021-blue)](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
### Orhan Firat

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>```Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.```<br><br>
### Xavier Garcia

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.93) [**Towards Continual Learning for Multilingual Machine Translation via Vocabulary Substitution**](https://www.aclweb.org/anthology/2021.naacl-main.93),<br> by *Garcia, Xavier , Constant, Noah , Parikh, Ankur  and Firat, Orhan*
<br>```Introducing the catastrophic forgetting problem in incremental multi-language translation, and utilizing a vocabulary substitution manner to alleviate the above problem.```<br><br>
### Jing Sha

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Kun Zhou

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Zheng Gong

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/KDD-2022-blue)](https://doi.org/10.1145/3534678.3539131) [**JiuZhang: A Chinese Pre-trained Language Model for Mathematical
Problem Understanding**](https://doi.org/10.1145/3534678.3539131),<br> by *Wayne Xin Zhao, Kun Zhou, Zheng Gong, Beichen Zhang, Yuanhang Zhou, Jing Sha, Zhigang Chen, Shijin Wang et al.*
<br><br>
### Nathanael Sch{\"{a}}rli

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
### David Dohan

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Nathan Scales

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
### Lingpeng Kong

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html) [**Episodic Memory in Lifelong Language Learning**](https://proceedings.neurips.cc/paper/2019/hash/f8d2e80c1458ea2501f98a2cafadb397-Abstract.html),<br> by *Cyprien de Masson d'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama*
<br>```MbPA++. This paper proposes the use of memory (a fixed memory network) in life-long learning to prevent catastrophic forgetting by means of  experience replay and local adaptation. ```<br><br>
### Diyi Yang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>```Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.```<br><br>
### Jiaao Chen

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.218) [**Continual Learning for Text Classification with Information Disentanglement Based Regularization**](https://www.aclweb.org/anthology/2021.naacl-main.218),<br> by *Huang, Yufan , Zhang, Yanzhe , Chen, Jiaao , Wang, Xuezhi  and Yang, Diyi*
<br>```Proposing a regularization-based method for continual text classification, introducing the next sentence prediction and task id prediction as auxiliary tasks.```<br><br>
### Xi Ye

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04813) [**Explanation Selection Using Unlabeled Data for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.04813),<br> by *Xi Ye and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://par.nsf.gov/biblio/10380030) [**The unreliability of explanations in few-shot prompting for textual reasoning**](https://par.nsf.gov/biblio/10380030),<br> by *Ye, Xi and Durrett, Greg*
<br><br>
### Hongxia Jin

- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.212) [**Hyperparameter-free Continuous Learning for Domain Classification in Natural Language Understanding**](https://www.aclweb.org/anthology/2021.naacl-main.212),<br> by *Hua, Ting , Shen, Yilin , Zhao, Changsheng , Hsu, Yen-Chang  and Jin, Hongxia*
<br>```Inspired by EWC and proposing a hyperparameter-free (Fisher information-based) sampling method for memory replay.```<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/5465) [**Towards Hands-Free Visual Dialog Interactive Recommendation**](https://ojs.aaai.org/index.php/AAAI/article/view/5465),<br> by *Tong Yu, Yilin Shen and Hongxia Jin*
<br><br>
### Yilin Shen

- [![](https://img.shields.io/badge/NAACL_HLT-2021-blue)](https://www.aclweb.org/anthology/2021.naacl-main.212) [**Hyperparameter-free Continuous Learning for Domain Classification in Natural Language Understanding**](https://www.aclweb.org/anthology/2021.naacl-main.212),<br> by *Hua, Ting , Shen, Yilin , Zhao, Changsheng , Hsu, Yen-Chang  and Jin, Hongxia*
<br>```Inspired by EWC and proposing a hyperparameter-free (Fisher information-based) sampling method for memory replay.```<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/5465) [**Towards Hands-Free Visual Dialog Interactive Recommendation**](https://ojs.aaai.org/index.php/AAAI/article/view/5465),<br> by *Tong Yu, Yilin Shen and Hongxia Jin*
<br><br>
### Janghoon Han

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=vfsRB5MImo9) [**Towards Continual Knowledge Learning of Language Models**](https://openreview.net/forum?id=vfsRB5MImo9),<br> by *Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, Gyeonghun KIM, Stanley Jungkyu Choi and Minjoon Seo*
<br>```We propose a novel continual learning formulation named Continual Knowledge Learning which allows large language models to constantly obtain new and updated knowledge while mitigating forgetting of previous learned time-invariant knowledge.```<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.122) [**Fine-grained Post-training for Improving Retrieval-based Dialogue
Systems**](https://doi.org/10.18653/v1/2021.naacl-main.122),<br> by *Janghoon Han, Taesuk Hong, Byoungjae Kim, Youngjoong Ko and Jungyun Seo*
<br><br>
### Erik Cambria

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Jinjie Ni

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Vlad Pandelea

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Tom Young

- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
### Zhaojiang Lin

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.41) [**Exploring Versatile Generative Language Model Via Parameter-Efficient
Transfer Learning**](https://doi.org/10.18653/v1/2020.findings-emnlp.41),<br> by *Zhaojiang Lin, Andrea Madotto and Pascale Fung*
<br>```Proposing an adapter-based method for continual learning in text generation. One of the insights is a frozen PLM can be well-applied in continual learning.```<br><br>
### Kevin Murphy

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.07411) [**Plex: Towards Reliability using Pretrained Large Model Extensions**](https://doi.org/10.48550/arXiv.2207.07411),<br> by *Dustin Tran, Jeremiah Z. Liu, Michael W. Dusenberry, Du Phan, Mark Collier, Jie Ren, Kehang Han, Zi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/ICCV-2019-blue)](https://doi.org/10.1109/ICCV.2019.00756) [**VideoBERT: A Joint Model for Video and Language Representation Learning**](https://doi.org/10.1109/ICCV.2019.00756),<br> by *Chen Sun, Austin Myers, Carl Vondrick, Kevin Murphy and Cordelia Schmid*
<br><br>
### Luowei Zhou

- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
### Linjie Li

- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### Yue Yu

- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510062) [**Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding**](https://doi.org/10.1145/3510003.3510062),<br> by *Deze Wang, Zhouyang Jia, Shanshan Li, Yue Yu, Yun Xiong, Wei Dong and Xiangke Liao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.691) [**SeqMix: Augmenting Active Sequence Labeling via Sequence Mixup**](https://doi.org/10.18653/v1/2020.emnlp-main.691),<br> by *Rongzhi Zhang, Yue Yu and Chao Zhang*
<br><br>
### Hongyu Zhang

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549094) [**Diet code is healthy: simplifying programs for pre-trained models
of code**](https://doi.org/10.1145/3540250.3549094),<br> by *Zhaowei Zhang, Hongyu Zhang, Beijun Shen and Xiaodong Gu*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Zhou Yang

- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
### Jieke Shi

- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
### Bowen Xu

- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICSME-2020-blue)](https://ieeexplore.ieee.org/abstract/document/9240704/) [**Sentiment analysis for software engineering: How far can pre-trained transformer models go?**](https://ieeexplore.ieee.org/abstract/document/9240704/),<br> by *Zhang, Ting, Xu, Bowen, Thung, Ferdian, Haryono, Stefanus Agus, Lo, David and Jiang, Lingxiao*
<br><br>
### Hongzhi Yin

- [![](https://img.shields.io/badge/ISSTA-2022-blue)](https://doi.org/10.1145/3533767.3534219) [**CIRCLE: continual repair across programming languages**](https://doi.org/10.1145/3533767.3534219),<br> by *Wei Yuan, Quanjun Zhang, Tieke He, Chunrong Fang, Nguyen Quoc Viet Hung, Xiaodong Hao and Hongzhi Yin*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2022-blue)](https://doi.org/10.1145/3477495.3531937) [**Are Graph Augmentations Necessary?: Simple Graph Contrastive Learning
for Recommendation**](https://doi.org/10.1145/3477495.3531937),<br> by *Junliang Yu, Hongzhi Yin, Xin Xia, Tong Chen, Lizhen Cui and Quoc Viet Hung Nguyen*
<br><br>
### Jian Yin

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Jin Liu

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Hao Wu

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Li Li

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Pingyi Zhou

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Xin Wang

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Kai Wei Chang

- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.03557) [**VisualBERT: A Simple and Performant Baseline for Vision and Language**](http://arxiv.org/abs/1908.03557),<br> by *Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh and Kai-Wei Chang*
<br><br>
### Baishakhi Ray

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549162) [**NatGen: generative pre-training by "naturalizing" source code**](https://doi.org/10.1145/3540250.3549162),<br> by *Saikat Chakraborty, Toufique Ahmed, Yangruibo Ding, Premkumar T. Devanbu and Baishakhi Ray*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
### Saikat Chakraborty

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549162) [**NatGen: generative pre-training by "naturalizing" source code**](https://doi.org/10.1145/3540250.3549162),<br> by *Saikat Chakraborty, Toufique Ahmed, Yangruibo Ding, Premkumar T. Devanbu and Baishakhi Ray*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
### Shujie Liu

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Michele Tufano

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Long Zhou

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Ge Li

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ASE-2020-blue)](https://doi.org/10.1145/3324884.3416591) [**Multi-task Learning based Pre-trained Language Model for Code Completion**](https://doi.org/10.1145/3324884.3416591),<br> by *Fang Liu, Ge Li, Yunfei Zhao and Zhi Jin*
<br><br>
### Shuo Ren

- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
### Akhilesh Deepak Gotmare

- [![](https://img.shields.io/badge/openreview-2023-blue)](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
### Hung Le

- [![](https://img.shields.io/badge/openreview-2023-blue)](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
### Panos Kalnis

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.06466) [**ChatGPT versus Traditional Question Answering for Knowledge Graphs:
Current Status and Future Directions Towards Knowledge Graph Chatbots**](https://doi.org/10.48550/arXiv.2302.06466),<br> by *Reham Omar, Omij Mangukiya, Panos Kalnis and Essam Mansour*
<br><br>
- [![](https://img.shields.io/badge/ICDCS-2021-blue)](https://doi.org/10.1109/ICDCS51616.2021.00060) [**GRACE: A Compressed Communication Framework for Distributed Machine
Learning**](https://doi.org/10.1109/ICDCS51616.2021.00060),<br> by *Hang Xu, Chen-Yu Ho, Ahmed M. Abdelmoniem, Aritra Dutta, El Houcine Bergou, Konstantinos Karatsenidis, Marco Canini and Panos Kalnis*
<br><br>
### Lichao Sun

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/TIST-2022-blue)](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
### Hai Jin

- [![](https://img.shields.io/badge/TIST-2022-blue)](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Dejing Dou

- [![](https://img.shields.io/badge/KIS-2022-blue)](https://doi.org/10.1007/s10115-022-01664-x) [**From distributed machine learning to federated learning: a survey**](https://doi.org/10.1007/s10115-022-01664-x),<br> by *Ji Liu, Jizhou Huang, Yang Zhou, Xuhong Li, Shilei Ji, Haoyi Xiong and Dejing Dou*
<br><br>
- [![](https://img.shields.io/badge/Euro_Par-2021-blue)](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Ji Liu

- [![](https://img.shields.io/badge/KIS-2022-blue)](https://doi.org/10.1007/s10115-022-01664-x) [**From distributed machine learning to federated learning: a survey**](https://doi.org/10.1007/s10115-022-01664-x),<br> by *Ji Liu, Jizhou Huang, Yang Zhou, Xuhong Li, Shilei Ji, Haoyi Xiong and Dejing Dou*
<br><br>
- [![](https://img.shields.io/badge/Euro_Par-2021-blue)](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Lingjuan Lyu

- [![](https://img.shields.io/badge/TIST-2022-blue)](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [![](https://img.shields.io/badge/FLPI-2020-blue)](https://doi.org/10.1007/978-3-030-63076-8\_14) [**Collaborative Fairness in Federated Learning**](https://doi.org/10.1007/978-3-030-63076-8\_14),<br> by *Lingjuan Lyu, Xinyi Xu, Qian Wang and Han Yu*
<br><br>
### Michael Tschannen

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.05442) [**Scaling Vision Transformers to 22 Billion Parameters**](https://doi.org/10.48550/arXiv.2302.05442),<br> by *Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron et al.*
<br><br>
- [![](https://img.shields.io/badge/ICML-2018-blue)](http://proceedings.mlr.press/v80/furlanello18a.html) [**Born-Again Neural Networks**](http://proceedings.mlr.press/v80/furlanello18a.html), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Tommaso Furlanello, Zachary Chase Lipton, Michael Tschannen, Laurent Itti and Anima Anandkumar*
<br><br>
### Oriol Vinyals

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2015-blue)](http://arxiv.org/abs/1503.02531) [**Distilling the Knowledge in a Neural Network**](http://arxiv.org/abs/1503.02531), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Geoffrey E. Hinton, Oriol Vinyals and Jeffrey Dean*
<br><br>
### Chris Brockett

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
### Yizhe Zhang

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10),<br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
### Jian Yun Nie

- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.392) [**A Simple and Efficient Multi-Task Learning Approach for Conditioned
Dialogue Generation**](https://doi.org/10.18653/v1/2021.naacl-main.392),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2010.11140) [**Generalized Conditioned Dialogue Generation Based on Pre-trained Language
Model**](https://arxiv.org/abs/2010.11140),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
### Yan Zeng

- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.392) [**A Simple and Efficient Multi-Task Learning Approach for Conditioned
Dialogue Generation**](https://doi.org/10.18653/v1/2021.naacl-main.392),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2010.11140) [**Generalized Conditioned Dialogue Generation Based on Pre-trained Language
Model**](https://arxiv.org/abs/2010.11140),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
### Anima Anandkumar

- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [![](https://img.shields.io/badge/ICML-2018-blue)](http://proceedings.mlr.press/v80/furlanello18a.html) [**Born-Again Neural Networks**](http://proceedings.mlr.press/v80/furlanello18a.html), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Tommaso Furlanello, Zachary Chase Lipton, Michael Tschannen, Laurent Itti and Anima Anandkumar*
<br><br>
### Eric P. Xing

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.341) [**Progressive Generation of Long Text with Pretrained Language Models**](https://doi.org/10.18653/v1/2021.naacl-main.341),<br> by *Bowen Tan, Zichao Yang, Maruan Al-Shedivat, Eric P. Xing and Zhiting Hu*
<br><br>
### Hao Tian

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Dianhai Yu

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/Euro_Par-2021-blue)](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Weibao Gong

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/Euro_Par-2021-blue)](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
### Shikun Feng

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Shuohuan Wang

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6428) [**ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding**](https://ojs.aaai.org/index.php/AAAI/article/view/6428),<br> by *Sun, Yu, Wang, Shuohuan, Li, Yukun, Feng, Shikun, Tian, Hao, Wu, Hua and Wang, Haifeng*
<br>```In order to extract the lexical, syntactic and semantic information from training corpora,
we propose a continual pre-training framework named ERNIE
2.0 which incrementally builds pre-training tasks and then
learn pre-trained models on these constructed tasks via continual multi-task learning.```<br><br>
### Tie Yan Liu

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ICML-2019-blue)](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Tao Qin

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ICML-2019-blue)](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Xu Tan

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ICML-2019-blue)](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Kaitao Song

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ICML-2019-blue)](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
### Yejin Choi

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
### Baolin Peng

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
### Julian J. McAuley

- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2019-blue)](https://doi.org/10.18653/v1/D19-1615) [**Improving Neural Story Generation by Targeted Common Sense Grounding**](https://doi.org/10.18653/v1/D19-1615),<br> by *Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian J. McAuley and Garrison W. Cottrell*
<br><br>
### Bodhisattwa Prasad Majumder

- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2019-blue)](https://doi.org/10.18653/v1/D19-1615) [**Improving Neural Story Generation by Targeted Common Sense Grounding**](https://doi.org/10.18653/v1/D19-1615),<br> by *Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian J. McAuley and Garrison W. Cottrell*
<br><br>
### Tianrui Li

- [![](https://img.shields.io/badge/JIS-2022-blue)](https://doi.org/10.1016/j.ins.2021.12.102) [**Fairness and accuracy in horizontal federated learning**](https://doi.org/10.1016/j.ins.2021.12.102),<br> by *Wei Huang, Tianrui Li, Dexian Wang, Shengdong Du, Junbo Zhang and Tianqiang Huang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
### Luo Si

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://aclanthology.org/2021.acl-long.172) [**On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation**](https://aclanthology.org/2021.acl-long.172),<br> by *He, Ruidan , Liu, Linlin , Ye, Hai , Tan, Qingyu , Ding, Bosheng , Cheng, Liying , Low, Jiawei , Bing, Lidong  et al.*
<br>```we first show that adapter-based tuning better mitigates forgetting issues than fine-tuning since it yields representations with less deviation from those generated by the initial PrLM. Effectiveness:  it tends
to outperform fine-tuning on both low-resource and
cross-lingual tasks; 2 it demonstrates higher stability under different learning rates compared to
fine-tuning.```<br><br>
### Songfang Huang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Yijia Liu

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.bionlp-1.20) [**Improving Biomedical Pretrained Language Models with Knowledge**](https://doi.org/10.18653/v1/2021.bionlp-1.20),<br> by *Zheng Yuan, Yijia Liu, Chuanqi Tan, Songfang Huang and Fei Huang*
<br><br>
### Ruofei Zhang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Jiusheng Chen

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Pengcheng Wang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.12246) [**Active Prompting with Chain-of-Thought for Large Language Models**](https://doi.org/10.48550/arXiv.2302.12246),<br> by *Shizhe Diao, Pengcheng Wang, Yong Lin and Tong Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
### Ming Gong

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
### Linjun Shou

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
### Yeyun Gong

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Yu Yan

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
### Piji Li

- [![](https://img.shields.io/badge/ECIR-2021-blue)](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
### Tianyi Tang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Gaole He

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
### Yinhan Liu

- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1907.11692) [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](http://arxiv.org/abs/1907.11692), ![](https://img.shields.io/badge/RoBERTa-yellow) <br> by *Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis et al.*
<br><br>
### Richard Socher

- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Caiming Xiong

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.09419) [**A Comprehensive Survey on Pretrained Foundation Models: A History
from BERT to ChatGPT**](https://doi.org/10.48550/arXiv.2302.09419),<br> by *Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Bryan McCann

- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Jianzhong Qi

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
- [![](https://img.shields.io/badge/IJCAI-2021-blue)](https://doi.org/10.24963/ijcai.2021/223) [**Federated Learning with Fair Averaging**](https://doi.org/10.24963/ijcai.2021/223),<br> by *Zheng Wang, Xiaoliang Fan, Jianzhong Qi, Chenglu Wen, Cheng Wang and Rongshan Yu*
<br><br>
### Xiaoyan Zhu

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Minlie Huang

- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
### Xiaojiang Liu

- [![](https://img.shields.io/badge/COLING-2020-blue)](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
### Bing Qin

- [![](https://img.shields.io/badge/COLING-2020-blue)](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.58) [**Revisiting Pre-Trained Models for Chinese Natural Language Processing**](https://doi.org/10.18653/v1/2020.findings-emnlp.58),<br> by *Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Shijin Wang and Guoping Hu*
<br><br>
### Yue Zhang

- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
### Xiao Liu

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Yu Cheng

- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
### William Yang Wang

- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.190) [**Logic2Text: High-Fidelity Natural Language Generation from Logical
Forms**](https://doi.org/10.18653/v1/2020.findings-emnlp.190),<br> by *Zhiyu Chen, Wenhu Chen, Hanwen Zha, Xiyou Zhou, Yunkai Zhang, Sairam Sundaresan and William Yang Wang*
<br><br>
### Yu Su

- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.329) [**Thinking about GPT-3 In-Context Learning for Biomedical IE? Think
Again**](https://aclanthology.org/2022.findings-emnlp.329),<br> by *Bernal Jimenez Gutierrez, Nikolas McNeal, Clayton Washington, You Chen, Lang Li, Huan Sun and Yu Su*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
### Lu Wang

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.502) [**Controllable Open-ended Question Generation with A New Question
Type Ontology**](https://doi.org/10.18653/v1/2021.acl-long.502),<br> by *Shuyang Cao and Lu Wang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.501) [**DYPLOC: Dynamic Planning of Content Using Mixed Language Models
for Text Generation**](https://doi.org/10.18653/v1/2021.acl-long.501),<br> by *Xinyu Hua, Ashwin Sreevatsa and Lu Wang*
<br><br>
### Geoffrey E. Hinton

- [![](https://img.shields.io/badge/CoRR-2015-blue)](http://arxiv.org/abs/1503.02531) [**Distilling the Knowledge in a Neural Network**](http://arxiv.org/abs/1503.02531), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Geoffrey E. Hinton, Oriol Vinyals and Jeffrey Dean*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2009-blue)](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html) [**Zero-shot Learning with Semantic Output Codes**](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html),<br> by *Mark Palatucci, Dean Pomerleau, Geoffrey E. Hinton and Tom M. Mitchell*
<br><br>
### Hui Chen

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
### Xiang Chen

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Shumin Deng

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09597) [**Reasoning with Language Model Prompting: A Survey**](https://doi.org/10.48550/arXiv.2212.09597),<br> by *Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen, Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang et al.*
<br><br>
### Hongbin Ye

- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
### Yadao Wang

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
### Mikel Artetxe

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Hai Tao Zheng

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/ECIR-2021-blue)](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
### Shengding Hu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Ning Ding

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
### Yujia Qin

- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
### Sebastian Riedel

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.556) [**Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot
Prompt Order Sensitivity**](https://doi.org/10.18653/v1/2022.acl-long.556),<br> by *Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel and Pontus Stenetorp*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
### Yao Lu

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.556) [**Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot
Prompt Order Sensitivity**](https://doi.org/10.18653/v1/2022.acl-long.556),<br> by *Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel and Pontus Stenetorp*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1903.12136) [**Distilling Task-Specific Knowledge from BERT into Simple Neural
Networks**](http://arxiv.org/abs/1903.12136), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Raphael Tang, Yao Lu, Linqing Liu, Lili Mou, Olga Vechtomova and Jimmy Lin*
<br><br>
### Tushar Khot

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Peter Clark

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
### Yao Fu

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
### Xiang Deng

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Boshi Wang

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
### Samuel R. Bowman

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.07459) [**The Capacity for Moral Self-Correction in Large Language Models**](https://doi.org/10.48550/arXiv.2302.07459),<br> by *Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamile Lukosiute, Anna Chen, Anna Goldie, Azalia Mirhoseini et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br><br>
### Yeganeh Kordi

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
### Yizhong Wang

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
### Slav Petrov

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Hongkun Yu

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11610) [**Large Language Models Can Self-Improve**](https://doi.org/10.48550/arXiv.2210.11610),<br> by *Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu and Jiawei Han*
<br><br>
### Gaurav Mishra

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Sharan Narang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Aakanksha Chowdhery

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Xinyun Chen

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### William Fedus

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Hyung Won Chung

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Ben Hutchinson

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Mark Diaz

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Vinodkumar Prabhakaran

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Toju Duke

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Yanping Huang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Nan Du

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
### Vincent Y. Zhao

- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Zornitsa Kozareva

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Srini Iyer

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
### Todor Mihaylov

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260), ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br>```This paper proposes to use self-supervision (MLM, NSP, CL, etc.) between pre-training and downstream usage to teach the LM to perform in-context learning. Analysis reveals that: 1) benefits of self-supervised depends on the amount of training data; 2) semantic similarity between training and evaluation tasks matters; 3) adding training objectives without diversity does not help; 4) model performance improves when choosing similar templates for both self-supervised and downstream tasks; 5) self-supervised  tasks and human-annotated datasets are complementary; 6) self-supervised-trained models are better at following task instructions.```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.804) [**Efficient Large Scale Language Modeling with Mixtures of Experts**](https://aclanthology.org/2022.emnlp-main.804), [[Code]](https://github.com/facebookresearch/fairseq/tree/main/examples/moe_lm) ![](https://img.shields.io/badge/MoE-yellow) <br> by *Mikel Artetxe, Shruti Bhosale, Naman Goyal, Todor Mihaylov, Myle Ott, Sam Shleifer, Xi Victoria Lin, Jingfei Du et al.*
<br><br>
### Zhifang Sui

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br><br>
### Zhiyong Wu

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br><br>
### Damai Dai

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10559) [**Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient
Descent as Meta-Optimizers**](https://doi.org/10.48550/arXiv.2212.10559),<br> by *Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Zhifang Sui and Furu Wei*
<br><br>
### Benjamin Mann

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.05862) [**Training a Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback**](https://doi.org/10.48550/arXiv.2204.05862),<br> by *Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
### David Luan

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
### Rewon Child

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), ![](https://img.shields.io/badge/GPT--2-yellow) <br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
### Ryan Sepassi

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2018-blue)](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Zhuang Li

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=figzpGMrdD) [**Pretrained Language Model in Continual Learning: A Comparative Study**](https://openreview.net/forum?id=figzpGMrdD),<br> by *Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi and Gholamreza Haffari*
<br>```To explore the layer-wise property of pretrained languge models in continual learning, we thoroughly compare the continual learning performance over the combination of 5 PLMs and 4 veins of CL methods on 3 benchmarks in 2 typical incremental settings.```<br><br>
### Vedant Misra

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
### Lukasz Kaiser

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2018-blue)](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
### Nick Ryder

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
### Girish Sastry

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf), ![](https://img.shields.io/badge/GPT--3-yellow) <br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
### Raul Puri

- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
### Dan Roth

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303),<br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>```本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Hongming Zhang

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303),<br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>```本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Alex Smola

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Mu Li

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
### Tianyi Zhang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=SkeHuCVFDr) [**BERTScore: Evaluating Text Generation with BERT**](https://openreview.net/forum?id=SkeHuCVFDr),<br> by *Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi*
<br><br>
### Tatsunori Hashimoto

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Sang Michael Xie

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=RdJVFCHjUMI) [**An Explanation of In-context Learning as Implicit Bayesian Inference**](https://openreview.net/forum?id=RdJVFCHjUMI),<br> by *Sang Michael Xie, Aditi Raghunathan, Percy Liang and Tengyu Ma*
<br><br>
### Neel Guha

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Mirac Suzgun

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Laurel J. Orr

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Eric Zelikman

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://research.google/pubs/pub51694/) [**Star: Self-taught reasoner bootstrapping reasoning with reasoning**](https://research.google/pubs/pub51694/),<br> by *Zelikman, Eric, Mu, Jesse, Goodman, Noah D and Wu, Yuhuai Tony*
<br><br>
### Christopher R{\'{e}}

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.02441) [**Ask Me Anything: A simple strategy for prompting language models**](https://doi.org/10.48550/arXiv.2210.02441),<br> by *Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala et al.*
<br><br>
### Rishi Bommasani

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.07682) [**Emergent Abilities of Large Language Models**](https://doi.org/10.48550/arXiv.2206.07682),<br> by *Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma et al.*
<br><br>
### Jonathan Berant

- [![](https://img.shields.io/badge/EACL-2023-blue)](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>```本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。 TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.191) [**Learning To Retrieve Prompts for In-Context Learning**](https://doi.org/10.18653/v1/2022.naacl-main.191),<br> by *Ohad Rubin, Jonathan Herzig and Jonathan Berant*
<br><br>
### Rui Zhang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
### Hongjin Su

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.259) [**Taming Pre-trained Language Models with N-gram Representations for
Low-Resource Domain Adaptation**](https://doi.org/10.18653/v1/2021.acl-long.259),<br> by *Shizhe Diao, Ruijia Xu, Hongjin Su, Yilei Jiang, Yan Song and Tong Zhang*
<br><br>
### Hongyu Ren

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
### Junyi Jessy Li

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356),<br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556955) [**CoditT5: Pretraining for Source Code and Natural Language Editing**](https://doi.org/10.1145/3551349.3556955),<br> by *Jiyang Zhang, Sheena Panthaplackel, Pengyu Nie, Junyi Jessy Li and Milos Gligoric*
<br><br>
### Albert Webson

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.167) [**Do Prompt-Based Models Really Understand the Meaning of Their Prompts?**](https://doi.org/10.18653/v1/2022.naacl-main.167),<br> by *Albert Webson and Ellie Pavlick*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
### Yiming Yang

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10435) [**PAL: Program-aided Language Models**](https://doi.org/10.48550/arXiv.2211.10435),<br> by *Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig*
<br><br>
### Tao Yu

- [![](https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7_11,_2022-2022-blue)](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
### Chia Hsuan Lee

- [![](https://img.shields.io/badge/Findings_of_the_Association_for_Computational_Linguistics:_{EMNLP}
2022,_Abu_Dhabi,_United_Arab_Emirates,_December_7_11,_2022-2022-blue)](https://aclanthology.org/2022.findings-emnlp.193) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://aclanthology.org/2022.findings-emnlp.193),<br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
### Heng Ji

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.12810) [**Code4Struct: Code Generation for Few-Shot Structured Prediction from
Natural Language**](https://doi.org/10.48550/arXiv.2210.12810),<br> by *Xingyao Wang, Sha Li and Heng Ji*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
### He He

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53),<br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.01240) [**Language Models Are Greedy Reasoners: A Systematic Formal Analysis
of Chain-of-Thought**](https://doi.org/10.48550/arXiv.2210.01240),<br> by *Abulhair Saparov and He He*
<br><br>