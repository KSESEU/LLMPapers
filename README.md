# LLM Papers & Related Works
Collection of  papers and related works for Large Language Models (ChatGPT, GPT-3, Codex etc.).
## Contributors
This repository is contributed by the following contributors.
- **Organizers**: [Guilin Qi (漆桂林)](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm), [Xiaofang Qi (戚晓芳)](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm)
- **Paper Collectors**: Zafar Ali, Sheng Bi (毕胜), Yongrui Chen (陈永锐), Zizhuo Chen (陈孜卓), Xinbang Dai (戴鑫邦), Huan Gao (高桓), Shilong Hu (胡世龙), Jiaqi Li (李嘉琦), Dehai Min (闵德海), Yiming Tan (谭亦鸣), Songlin Zhai (翟松林), Yuxin Zhang (张裕欣)
- **Maintainers**: Runzhe Wang (王润哲), Shenyu Zhang (张沈昱) 

The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).



## Papers

### Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#hyperlink)
- [![](https://img.shields.io/badge/Evaluation-10-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#evaluation)
- [![](https://img.shields.io/badge/In_Context_Learning-18-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#in-context-learning)
- [![](https://img.shields.io/badge/Instruction_Tuning-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#instruction-tuning)
- [![](https://img.shields.io/badge/Knowledge_Enhanced-14-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#knowledge-enhanced)
- [![](https://img.shields.io/badge/Knowledge_Distillation-17-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#knowledge-distillation)
- [![](https://img.shields.io/badge/Knowledge_Graph_Generation-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#knowledge-graph-generation)
- [![](https://img.shields.io/badge/Reasoning-34-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#reasoning)
  - [![](https://img.shields.io/badge/Chain_of_Thought-13-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#chain-of-thought)
  - [![](https://img.shields.io/badge/Multi_Step_Reasoning-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#multi-step-reasoning)
  - [![](https://img.shields.io/badge/Arithmetic_Reasoning-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#arithmetic-reasoning)
  - [![](https://img.shields.io/badge/Symbolic_Reasoning-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#symbolic-reasoning)
- [![](https://img.shields.io/badge/Federated_Learning-14-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#federated-learning)
- [![](https://img.shields.io/badge/Distributed_AI-9-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#distributed-ai)
- [![](https://img.shields.io/badge/Selective_Annotation-2-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#selective-annotation)
- [![](https://img.shields.io/badge/Code_Generation-40-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#code-generation)
  - [![](https://img.shields.io/badge/Code_Representation-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#code-representation)
  - [![](https://img.shields.io/badge/Code_Fixing-7-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#code-fixing)
  - [![](https://img.shields.io/badge/Code_Review-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#code-review)
- [![](https://img.shields.io/badge/Software_Engineering-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#software-engineering)
- [![](https://img.shields.io/badge/Text_Generation-77-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#text-generation)
  - [![](https://img.shields.io/badge/Controllable_Text_Generation-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#controllable-text-generation)
- [![](https://img.shields.io/badge/Continual_Learning-6-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#continual-learning)
- [![](https://img.shields.io/badge/Prompt_Learning-21-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#prompt-learning)
- [![](https://img.shields.io/badge/Natural_Language_Understanding-3-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#natural-language-understanding)
- [![](https://img.shields.io/badge/Multimodal-13-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#multimodal)
- [![](https://img.shields.io/badge/LLM_Reliability-1-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#llm-reliability)
- [![](https://img.shields.io/badge/Dialogue_System-15-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#dialogue-system)
- [![](https://img.shields.io/badge/Recommender_System-7-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#recommender-system)
- [![](https://img.shields.io/badge/Event_Extraction-7-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#event-extraction)
- [![](https://img.shields.io/badge/Event_Relation_Extraction-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#event-relation-extraction)
- [![](https://img.shields.io/badge/Data_Argumentation-1-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#data-argumentation)
- [![](https://img.shields.io/badge/Others-5-blue)](https://github.com/KSESEU/LLMPapers/blob/main/./README.md#others)
### Hyperlinks 
- [[Overview]](https://github.com/KSESEU/LLMPapers/blob/main/README.md) -- [Homepage](https://github.com/KSESEU/LLMPapers/blob/main/README.md)
-  -- [Summary](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/./)
-  -- [Author](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author)
-  -- [Techniques](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/techniques)
-  -- [Published Time](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time)
-  -- [Published Venue](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/venue)

### Evaluation

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023),<br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji et al.*
<br>```本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。```<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.06476) [**Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**](https://arxiv.org/abs/2302.06476),<br> by *Qin, Chengwei, Zhang, Aston, Zhang, Zhuosheng, Chen, Jiaao, Yasunaga, Michihiro and Yang, Diyi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110),<br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.00498) [**Evaluating the Text-to-SQL Capabilities of Large Language Models**](https://doi.org/10.48550/arXiv.2204.00498),<br> by *Nitarshan Rajkumar, Raymond Li and Dzmitry Bahdanau*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2104.05861) [**Evaluating Pre-Trained Models for User Feedback Analysis in Software
Engineering: A Study on Classification of App-Reviews**](https://arxiv.org/abs/2104.05861),<br> by *Mohammad Abdul Hadi and Fatemeh H. Fard*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2007.15780) [**Neural Language Generation: Formulation, Methods, and Evaluation**](https://arxiv.org/abs/2007.15780),<br> by *Cristina Garbacea and Qiaozhu Mei*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=SkeHuCVFDr) [**BERTScore: Evaluating Text Generation with BERT**](https://openreview.net/forum?id=SkeHuCVFDr),<br> by *Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi*
<br><br>
### In-Context Learning

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00234) [**A Survey for In-context Learning**](https://doi.org/10.48550/arXiv.2301.00234),<br> by *Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04813) [**Explanation Selection Using Unlabeled Data for In-Context Learning**](https://doi.org/10.48550/arXiv.2302.04813),<br> by *Xi Ye and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04931) [**In-Context Learning with Many Demonstration Examples**](https://doi.org/10.48550/arXiv.2302.04931),<br> by *Mukai Li, Shansan Gong, Jiangtao Feng, Yiheng Xu, Jun Zhang, Zhiyong Wu and Lingpeng Kong*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53),<br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201),<br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.260) [**Improving In-Context Few-Shot Learning via Self-Supervised Training**](https://doi.org/10.18653/v1/2022.naacl-main.260),<br> by *Mingda Chen, Jingfei Du, Ramakanth Pasunuru, Todor Mihaylov, Srini Iyer, Veselin Stoyanov and Zornitsa Kozareva*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.556) [**Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot
Prompt Order Sensitivity**](https://doi.org/10.18653/v1/2022.acl-long.556),<br> by *Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel and Pontus Stenetorp*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.deelio-1.10) [**What Makes Good In-Context Examples for GPT-3?**](https://doi.org/10.18653/v1/2022.deelio-1.10),<br> by *Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin and Weizhu Chen*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.191) [**Learning To Retrieve Prompts for In-Context Learning**](https://doi.org/10.18653/v1/2022.naacl-main.191),<br> by *Ohad Rubin, Jonathan Herzig and Jonathan Berant*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.622) [**Active Example Selection for In-Context Learning**](https://aclanthology.org/2022.emnlp-main.622),<br> by *Yiming Zhang, Shi Feng and Chenhao Tan*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.08082) [**Self-Generated In-Context Learning: Leveraging Auto-regressive Language
Models as a Demonstration Generator**](https://doi.org/10.48550/arXiv.2206.08082),<br> by *Hyuhng Joon Kim, Hyunsoo Cho, Junyeob Kim, Taeuk Kim, Kang Min Yoo and Sang-goo Lee*
<br><br>
- [![](https://img.shields.io/badge/ISoLA-2022-blue)](https://doi.org/10.1007/978-3-031-19759-8\_15) [**Measuring Convergence Inertia: Online Learning in Self-adaptive Systems
with Context Shifts**](https://doi.org/10.1007/978-3-031-19759-8\_15),<br> by *Elvin Alberts and Ilias Gerostathopoulos*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=RdJVFCHjUMI) [**An Explanation of In-context Learning as Implicit Bayesian Inference**](https://openreview.net/forum?id=RdJVFCHjUMI),<br> by *Sang Michael Xie, Aditi Raghunathan, Percy Liang and Tengyu Ma*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.759) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://aclanthology.org/2022.emnlp-main.759),<br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2111.02643) [**Response Generation with Context-Aware Prompt Learning**](https://arxiv.org/abs/2111.02643),<br> by *Xiaodong Gu, Kang Min Yoo and Sang-Woo Lee*
<br><br>
### Instruction Tuning

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00093) [**Large Language Models Can Be Easily Distracted by Irrelevant Context**](https://doi.org/10.48550/arXiv.2302.00093),<br> by *Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Sch\"arli and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2022-blue)](https://openreview.net/forum?id=gEZrGCozdqR) [**Finetuned Language Models are Zero-Shot Learners**](https://openreview.net/forum?id=gEZrGCozdqR),<br> by *Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.08239) [**LaMDA: Language Models for Dialog Applications**](https://arxiv.org/abs/2201.08239),<br> by *Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.11416) [**Scaling Instruction-Finetuned Language Models**](https://doi.org/10.48550/arXiv.2210.11416),<br> by *Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.340) [**Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks**](https://aclanthology.org/2022.emnlp-main.340),<br> by *Yizhong Wang, Swaroop Mishra, Pegah Alipoormolabashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva Naik, Arjun Ashok, Arut Selvan Dhanasekaran et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10560) [**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://doi.org/10.48550/arXiv.2212.10560),<br> by *Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi and Hannaneh Hajishirzi*
<br><br>
### Knowledge Enhanced

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.02093) [**Knowledge-enhanced Neural Machine Reasoning: A Review**](https://doi.org/10.48550/arXiv.2302.02093),<br> by *Tanmoy Chowdhury, Chen Ling, Xuchao Zhang, Xujiang Zhao, Guangji Bai, Jian Pei, Haifeng Chen and Liang Zhao*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338),<br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/TKDE-2022-blue)](https://doi.org/10.48550/arXiv.2212.13428) [**A Survey on Knowledge-Enhanced Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2212.13428),<br> by *Chaoqi Zhen, Yanlei Shang, Xiangyu Liu, Yifei Li, Yong Chen and Dell Zhang*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/FCST-2022-blue)](https://doi.org/10.3778/j.issn.1673-9418.2108105) [**Review of Knowledge-Enhanced Pre-trained Language Models**](https://doi.org/10.3778/j.issn.1673-9418.2108105),<br> by *Yi, HAN, Linbo, QIAO, Dongsheng, LI and Xiangke, LIAO*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09252) [**Mind the Knowledge Gap: A Survey of Knowledge-enhanced Dialogue
Systems**](https://doi.org/10.48550/arXiv.2212.09252),<br> by *Sagi Shaier, Lawrence Hunter and Katharina Kann*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.173) [**A Three-Stage Learning Framework for Low-Resource Knowledge-Grounded
Dialogue Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.173),<br> by *Shilei Liu, Xiaofeng Zhao, Bochao Li, Feiliang Ren, Longhui Zhang and Shujuan Yin*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2009-blue)](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html) [**Zero-shot Learning with Semantic Output Codes**](https://proceedings.neurips.cc/paper/2009/hash/1543843a4723ed2ab08e18053ae6dc5b-Abstract.html),<br> by *Mark Palatucci, Dean Pomerleau, Geoffrey E. Hinton and Tom M. Mitchell*
<br><br>
### Knowledge Distillation

- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/Neurocomputing-2021-blue)](https://doi.org/10.1016/j.neucom.2021.04.102) [**Preparing lessons: Improve knowledge distillation with better supervision**](https://doi.org/10.1016/j.neucom.2021.04.102), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Tiancheng Wen, Shenqi Lai and Xueming Qian*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/5963) [**Improved Knowledge Distillation via Teacher Assistant**](https://ojs.aaai.org/index.php/AAAI/article/view/5963), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Seyed-Iman Mirzadeh, Mehrdad Farajtabar, Ang Li, Nir Levine, Akihiro Matsukawa and Hassan Ghasemzadeh*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2020-blue)](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yun_Regularizing_Class-Wise_Predictions_via_Self-Knowledge_Distillation_CVPR_2020_paper.pdf) [**Regularizing Class-Wise Predictions via Self-Knowledge Distillation**](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yun_Regularizing_Class-Wise_Predictions_via_Self-Knowledge_Distillation_CVPR_2020_paper.pdf), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Sukmin Yun, Jongjin Park, Kimin Lee and Jinwoo Shin*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2019-blue)](http://openaccess.thecvf.com/content\_CVPR\_2019/html/Park\_Relational\_Knowledge\_Distillation\_CVPR\_2019\_paper.html) [**Relational Knowledge Distillation**](http://openaccess.thecvf.com/content\_CVPR\_2019/html/Park\_Relational\_Knowledge\_Distillation\_CVPR\_2019\_paper.html), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Wonpyo Park, Dongju Kim, Yan Lu and Minsu Cho*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.11723) [**Revisit Knowledge Distillation: a Teacher-free Framework**](http://arxiv.org/abs/1909.11723), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Li Yuan, Francis E. H. Tay, Guilin Li, Tao Wang and Jiashi Feng*
<br><br>
- [![](https://img.shields.io/badge/ICCV-2019-blue)](https://doi.org/10.1109/ICCV.2019.00143) [**Knowledge Distillation via Route Constrained Optimization**](https://doi.org/10.1109/ICCV.2019.00143), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Xiao Jin, Baoyun Peng, Yichao Wu, Yu Liu, Jiaheng Liu, Ding Liang, Junjie Yan and Xiaolin Hu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1910.05057) [**Improving Generalization and Robustness with Noisy Collaboration in
Knowledge Distillation**](http://arxiv.org/abs/1910.05057), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Elahe Arani, Fahad Sarfraz and Bahram Zonooz*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1903.12136) [**Distilling Task-Specific Knowledge from BERT into Simple Neural
Networks**](http://arxiv.org/abs/1903.12136), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Raphael Tang, Yao Lu, Linqing Liu, Lili Mou, Olga Vechtomova and Jimmy Lin*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2019-blue)](https://openreview.net/forum?id=rJl-b3RcF7) [**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks**](https://openreview.net/forum?id=rJl-b3RcF7), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Jonathan Frankle and Michael Carbin*
<br><br>
- [![](https://img.shields.io/badge/ICML-2018-blue)](http://proceedings.mlr.press/v80/furlanello18a.html) [**Born-Again Neural Networks**](http://proceedings.mlr.press/v80/furlanello18a.html), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Tommaso Furlanello, Zachary Chase Lipton, Michael Tschannen, Laurent Itti and Anima Anandkumar*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2017-blue)](https://openreview.net/forum?id=Sks9\_ajex) [**Paying More Attention to Attention: Improving the Performance of Convolutional
Neural Networks via Attention Transfer**](https://openreview.net/forum?id=Sks9\_ajex), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Sergey Zagoruyko and Nikos Komodakis*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2017-blue)](https://openreview.net/forum?id=ry8u21rtl) [**Mean teachers are better role models: Weight-averaged consistency
targets improve semi-supervised deep learning results**](https://openreview.net/forum?id=ry8u21rtl), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Antti Tarvainen and Harri Valpola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1706.00384) [**Deep Mutual Learning**](http://arxiv.org/abs/1706.00384), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Ying Zhang, Tao Xiang, Timothy M. Hospedales and Huchuan Lu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2016-blue)](http://arxiv.org/abs/1610.09650) [**Deep Model Compression: Distilling Knowledge from Noisy Teachers**](http://arxiv.org/abs/1610.09650), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Bharat Bhusan Sau and Vineeth N. Balasubramanian*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2015-blue)](http://arxiv.org/abs/1503.02531) [**Distilling the Knowledge in a Neural Network**](http://arxiv.org/abs/1503.02531), [[Code]](https://github.com/SforAiDl/KD_Lib)<br> by *Geoffrey E. Hinton, Oriol Vinyals and Jeffrey Dean*
<br><br>
### Knowledge Graph Generation

- [![](https://img.shields.io/badge/EACL-2023-blue)](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810),<br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>```本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。 TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.1) [**Generative Knowledge Graph Construction: A Review**](https://aclanthology.org/2022.emnlp-main.1),<br> by *Hongbin Ye, Ningyu Zhang, Hui Chen and Huajun Chen*
<br><br>
### Reasoning

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.11596) [**ThoughtSource: A central hub for large language model reasoning
data**](https://doi.org/10.48550/arXiv.2301.11596),<br> by *Simon Ott, Konstantin Hebenstreit, Valentin Li\'evin, Christoffer Egeberg Hother, Milad Moradi, Maximilian Mayrhauser, Robert Praas, Ole Winther et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.02093) [**Knowledge-enhanced Neural Machine Reasoning: A Review**](https://doi.org/10.48550/arXiv.2302.02093),<br> by *Tanmoy Chowdhury, Chen Ling, Xuchao Zhang, Xujiang Zhao, Guangji Bai, Jian Pei, Haifeng Chen and Liang Zhao*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.13808) [**Large Language Models are Versatile Decomposers: Decompose Evidence
and Questions for Table-based Reasoning**](https://doi.org/10.48550/arXiv.2301.13808),<br> by *Yunhu Ye, Binyuan Hui, Min Yang, Binhua Li, Fei Huang and Yongbin Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/ICML-2022-blue)](https://openreview.net/forum?id=8lNy3QCaxHX) [**Improved logical reasoning of language models via differentiable symbolic programming**](https://openreview.net/forum?id=8lNy3QCaxHX),<br> by *Zhang, Hanlin, Li, Ziyang, Huang, Jiani, Naik, Mayur and Xing, Eric*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10403) [**Towards Reasoning in Large Language Models: A Survey**](https://doi.org/10.48550/arXiv.2212.10403),<br> by *Jie Huang and Kevin Chen-Chuan Chang*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.218) [**UniGeo: Unifying Geometry Logical Reasoning via Reformulating Mathematical
Expression**](https://aclanthology.org/2022.emnlp-main.218),<br> by *Jiaqi Chen, Tong Li, Jinghui Qin, Pan Lu, Liang Lin, Chongyu Chen and Xiaodan Liang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
#### Chain of Thought

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303),<br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>```本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10782) [**Instruction Induction: From Few Examples to Natural Language Task
Descriptions**](https://doi.org/10.48550/arXiv.2205.10782),<br> by *Or Honovich, Uri Shaham, Samuel R. Bowman and Omer Levy*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.174) [**Iteratively Prompt Pre-trained Language Models for Chain of Thought**](https://aclanthology.org/2022.emnlp-main.174),<br> by *Boshi Wang, Xiang Deng and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.00720) [**Complexity-Based Prompting for Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2210.00720),<br> by *Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03350) [**Measuring and Narrowing the Compositionality Gap in Language Models**](https://doi.org/10.48550/arXiv.2210.03350),<br> by *Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith and Mike Lewis*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.03493) [**Automatic Chain of Thought Prompting in Large Language Models**](https://doi.org/10.48550/arXiv.2210.03493),<br> by *Zhuosheng Zhang, Aston Zhang, Mu Li and Alex Smola*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://arxiv.org/abs/2201.11903) [**Chain of Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903),<br> by *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, Quoc Le and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.11171) [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2203.11171),<br> by *Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi and Denny Zhou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.07686) [**Text and Patterns: For Effective Chain of Thought, It Takes Two to
Tango**](https://doi.org/10.48550/arXiv.2209.07686),<br> by *Aman Madaan and Amir Yazdanbakhsh*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.10001) [**Towards Understanding Chain-of-Thought Prompting: An Empirical Study
of What Matters**](https://doi.org/10.48550/arXiv.2212.10001),<br> by *Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer and Huan Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.02311) [**PaLM: Scaling Language Modeling with Pathways**](https://doi.org/10.48550/arXiv.2204.02311),<br> by *Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.13894) [**LAMBADA: Backward Chaining for Automated Reasoning in Natural Language**](https://doi.org/10.48550/arXiv.2212.13894),<br> by *Seyed Mehran Kazemi, Najoung Kim, Deepti Bhatia, Xin Xu and Deepak Ramachandran*
<br><br>
#### Multi-Step Reasoning

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12726) [**Specializing Smaller Language Models towards Multi-Step Reasoning**](https://doi.org/10.48550/arXiv.2301.12726),<br> by *Yao Fu, Hao Peng, Litu Ou, Ashish Sabharwal and Tushar Khot*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08607) [**MURMUR: Modular Multi-Step Reasoning for Semi-Structured Data-to-Text
Generation**](https://doi.org/10.48550/arXiv.2212.08607),<br> by *Swarnadeep Saha, Xinyan Velocity Yu, Mohit Bansal, Ramakanth Pasunuru and Asli Celikyilmaz*
<br><br>
#### Arithmetic Reasoning

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.392) [**LILA: A Unified Benchmark for Mathematical Reasoning**](https://aclanthology.org/2022.emnlp-main.392),<br> by *Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean Welleck, Chitta Baral, Tanmay Rajpurohit, Oyvind Tafjord et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.12588) [**Program of Thoughts Prompting: Disentangling Computation from Reasoning
for Numerical Reasoning Tasks**](https://doi.org/10.48550/arXiv.2211.12588),<br> by *Wenhu Chen, Xueguang Ma, Xinyi Wang and William W. Cohen*
<br><br>
#### Symbolic Reasoning

- [![](https://img.shields.io/badge/ICML-2022-blue)](https://openreview.net/forum?id=8lNy3QCaxHX) [**Improved logical reasoning of language models via differentiable symbolic programming**](https://openreview.net/forum?id=8lNy3QCaxHX),<br> by *Zhang, Hanlin, Li, Ziyang, Huang, Jiani, Naik, Mayur and Xing, Eric*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.82) [**Maieutic Prompting: Logically Consistent Reasoning with Recursive
Explanations**](https://aclanthology.org/2022.emnlp-main.82),<br> by *Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brahman, Chandra Bhagavatula, Ronan Le Bras and Yejin Choi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.08686) [**The Impact of Symbolic Representations on In-context Learning for
Few-shot Reasoning**](https://doi.org/10.48550/arXiv.2212.08686),<br> by *Hanlin Zhang, Yi-Fan Zhang, Li Erran Li and Eric P. Xing*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.218) [**UniGeo: Unifying Geometry Logical Reasoning via Reformulating Mathematical
Expression**](https://aclanthology.org/2022.emnlp-main.218),<br> by *Jiaqi Chen, Tong Li, Jinghui Qin, Pan Lu, Liang Lin, Chongyu Chen and Xiaodan Liang*
<br><br>
### Federated Learning

- [![](https://img.shields.io/badge/JIS-2022-blue)](https://doi.org/10.1016/j.ins.2021.12.102) [**Fairness and accuracy in horizontal federated learning**](https://doi.org/10.1016/j.ins.2021.12.102),<br> by *Wei Huang, Tianrui Li, Dexian Wang, Shengdong Du, Junbo Zhang and Tianqiang Huang*
<br><br>
- [![](https://img.shields.io/badge/IEEE_Trans._Netw._Sci._Eng.-2022-blue)](https://doi.org/10.1109/TNSE.2022.3169117) [**Federated Learning Meets Multi-Objective Optimization**](https://doi.org/10.1109/TNSE.2022.3169117),<br> by *Zeou Hu, Kiarash Shaloudegi, Guojun Zhang and Yaoliang Yu*
<br><br>
- [![](https://img.shields.io/badge/KIS-2022-blue)](https://doi.org/10.1007/s10115-022-01664-x) [**From distributed machine learning to federated learning: a survey**](https://doi.org/10.1007/s10115-022-01664-x),<br> by *Ji Liu, Jizhou Huang, Yang Zhou, Xuhong Li, Shilei Ji, Haoyi Xiong and Dejing Dou*
<br><br>
- [![](https://img.shields.io/badge/IJCAI-2022-blue)](https://doi.org/10.24963/ijcai.2022/273) [**Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in
the Federated Setting**](https://doi.org/10.24963/ijcai.2022/273),<br> by *Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2022-blue)](https://doi.org/10.1145/3511808.3557108) [**Mitigating Biases in Student Performance Prediction via Attention-Based
Personalized Federated Learning**](https://doi.org/10.1145/3511808.3557108),<br> by *Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura M. Cruz Castro, Kerrie A. Douglas, Andrew Lan and Christopher G. Brinton*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.101) [**Pretrained Models for Multilingual Federated Learning**](https://doi.org/10.18653/v1/2022.naacl-main.101),<br> by *Orion Weller, Marc Marone, Vladimir Braverman, Dawn J. Lawrie and Benjamin Van Durme*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.00982) [**Rethinking Architecture Design for Tackling Data Heterogeneity in
Federated Learning**](https://doi.org/10.1109/CVPR52688.2022.00982),<br> by *Liangqiong Qu, Yuyin Zhou, Paul Pu Liang, Yingda Xia, Feifei Wang, Ehsan Adeli, Li Fei-Fei and Daniel L. Rubin*
<br><br>
- [![](https://img.shields.io/badge/TIST-2022-blue)](https://doi.org/10.1145/3510033) [**FedBERT: When Federated Learning Meets Pre-training**](https://doi.org/10.1145/3510033),<br> by *Yuanyishu Tian, Yao Wan, Lingjuan Lyu, Dezhong Yao, Hai Jin and Lichao Sun*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.08090) [**Where to Begin? On the Impact of Pre-Training and Initialization in
Federated Learning**](https://doi.org/10.48550/arXiv.2210.08090),<br> by *John Nguyen, Jianyu Wang, Kshitiz Malik, Maziar Sanjabi and Michael Rabbat*
<br><br>
- [![](https://img.shields.io/badge/ICML-2021-blue)](http://proceedings.mlr.press/v139/li21h.html) [**Ditto: Fair and Robust Federated Learning Through Personalization**](http://proceedings.mlr.press/v139/li21h.html),<br> by *Tian Li, Shengyuan Hu, Ahmad Beirami and Virginia Smith*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.07313) [**Fine-tuning is Fine in Federated Learning**](https://arxiv.org/abs/2108.07313),<br> by *Gary Cheng, Karan N. Chadha and John C. Duchi*
<br><br>
- [![](https://img.shields.io/badge/IJCAI-2021-blue)](https://doi.org/10.24963/ijcai.2021/223) [**Federated Learning with Fair Averaging**](https://doi.org/10.24963/ijcai.2021/223),<br> by *Zheng Wang, Xiaoliang Fan, Jianzhong Qi, Chenglu Wen, Cheng Wang and Rongshan Yu*
<br><br>
- [![](https://img.shields.io/badge/FLPI-2020-blue)](https://doi.org/10.1007/978-3-030-63076-8\_14) [**Collaborative Fairness in Federated Learning**](https://doi.org/10.1007/978-3-030-63076-8\_14),<br> by *Lingjuan Lyu, Xinyi Xu, Qian Wang and Han Yu*
<br><br>
- [![](https://img.shields.io/badge/ECCV-2020-blue)](https://doi.org/10.1007/978-3-030-58607-2\_5) [**Federated Visual Classification with Real-World Data Distribution**](https://doi.org/10.1007/978-3-030-58607-2\_5),<br> by *Tzu-Ming Harry Hsu, Hang Qi and Matthew Brown*
<br><br>
### Distributed AI

- [![](https://img.shields.io/badge/EDBT-2022-blue)](https://doi.org/10.48786/edbt.2022.48) [**Distributed Training of Knowledge Graph Embedding Models using Ray**](https://doi.org/10.48786/edbt.2022.48),<br> by *Nasrullah Sheikh, Xiao Qin, Yaniv Gur and Berthold Reinwald*
<br><br>
- [![](https://img.shields.io/badge/IEEE_-2022-blue)](https://doi.org/10.1109/JSTSP.2022.3162989) [**Distributed Learning With Sparsified Gradient Differences**](https://doi.org/10.1109/JSTSP.2022.3162989),<br> by *Yicheng Chen, Rick S. Blum, Martin Tak\'ac and Brian M. Sadler*
<br><br>
- [![](https://img.shields.io/badge/AIIoT-2022-blue)](https://ieeexplore.ieee.org/document/9817156) [**Graph Attention Neural Network Distributed Model Training**](https://ieeexplore.ieee.org/document/9817156),<br> by *Esmaeilzadeh, Armin, Zadeh Nojoo Kambar, Mina Esmail and Heidari, Maryam*
<br><br>
- [![](https://img.shields.io/badge/Euro_Par-2021-blue)](https://doi.org/10.1007/978-3-031-06156-1\_10) [**Elastic Deep Learning Using Knowledge Distillation with Heterogeneous
Computing Resources**](https://doi.org/10.1007/978-3-031-06156-1\_10),<br> by *Daxiang Dong, Ji Liu, Xi Wang, Weibao Gong, An Qin, Xingjian Li, Dianhai Yu, Patrick Valduriez et al.*
<br><br>
- [![](https://img.shields.io/badge/ICDCS-2021-blue)](https://doi.org/10.1109/ICDCS51616.2021.00060) [**GRACE: A Compressed Communication Framework for Distributed Machine
Learning**](https://doi.org/10.1109/ICDCS51616.2021.00060),<br> by *Hang Xu, Chen-Yu Ho, Ahmed M. Abdelmoniem, Aritra Dutta, El Houcine Bergou, Konstantinos Karatsenidis, Marco Canini and Panos Kalnis*
<br><br>
- [![](https://img.shields.io/badge/ICPADS-2021-blue)](https://doi.org/10.1109/ICPADS53394.2021.00109) [**Load Balancing Optimization for Transformer in Distributed Environment**](https://doi.org/10.1109/ICPADS53394.2021.00109),<br> by *Delu Ma, Zhou Lei, Shengbo Chen and Peng Wang*
<br><br>
- [![](https://img.shields.io/badge/IA3-2020-blue)](https://doi.org/10.1109/IA351965.2020.00011) [**DistDGL: Distributed Graph Neural Network Training for Billion-Scale
Graphs**](https://doi.org/10.1109/IA351965.2020.00011),<br> by *Da Zheng, Chao Ma, Minjie Wang, Jinjing Zhou, Qidong Su, Xiang Song, Quan Gan, Zheng Zhang et al.*
<br><br>
- [![](https://img.shields.io/badge/VLDB-2020-blue)](http://www.vldb.org/pvldb/vol13/p3005-li.pdf) [**PyTorch Distributed: Experiences on Accelerating Data Parallel Training**](http://www.vldb.org/pvldb/vol13/p3005-li.pdf),<br> by *Shen Li, Yanli Zhao, Rohan Varma, Omkar Salpekar, Pieter Noordhuis, Teng Li, Adam Paszke, Jeff Smith et al.*
<br><br>
- [![](https://img.shields.io/badge/OSDI-2018-blue)](https://www.usenix.org/conference/osdi18/presentation/nishihara) [**Ray: A Distributed Framework for Emerging AI Applications**](https://www.usenix.org/conference/osdi18/presentation/nishihara),<br> by *Philipp Moritz, Robert Nishihara, Stephanie Wang, Alexey Tumanov, Richard Liaw, Eric Liang, Melih Elibol, Zongheng Yang et al.*
<br><br>
### Selective Annotation

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975),<br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf et al.*
<br><br>
- [![](https://img.shields.io/badge/VLDB-2022-blue)](https://www.vldb.org/pvldb/vol15/p1466-li.pdf) [**Selective Data Acquisition in the Wild for Model Charging**](https://www.vldb.org/pvldb/vol15/p1466-li.pdf),<br> by *Chengliang Chai, Jiabin Liu, Nan Tang, Guoliang Li and Yuyu Luo*
<br><br>
### Code Generation

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [![](https://img.shields.io/badge/openreview-2023-blue)](https://openreview.net/pdf?id=VPCi3STZcaO) [**CodeT5Mix: A Pretrained Mixture of Encoder-decoder Transformers for Code Understanding and Generation**](https://openreview.net/pdf?id=VPCi3STZcaO),<br> by *Wang, Yue, Le, Hung, Gotmare, Akhilesh Deepak, Li, Junnan and Hoi, Steven*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://arxiv.org/abs/2302.05527) [**CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code**](https://arxiv.org/abs/2302.05527),<br> by *Zhou, Shuyan, Alon, Uri, Agarwal, Sumit and Neubig, Graham*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.12810) [**Code4Struct: Code Generation for Few-Shot Structured Prediction from
Natural Language**](https://doi.org/10.48550/arXiv.2210.12810),<br> by *Xingyao Wang, Sha Li and Heng Ji*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128),<br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09420) [**When Neural Model Meets NL2Code: A Survey**](https://doi.org/10.48550/arXiv.2212.09420),<br> by *Daoguang Zan, Bei Chen, Fengji Zhang, Dianjie Lu, Bingchao Wu, Bei Guan, Yongji Wang and Jian-Guang Lou*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2204.00498) [**Evaluating the Text-to-SQL Capabilities of Large Language Models**](https://doi.org/10.48550/arXiv.2204.00498),<br> by *Nitarshan Rajkumar, Raymond Li and Dzmitry Bahdanau*
<br><br>
- [![](https://img.shields.io/badge/ISSTA-2022-blue)](https://doi.org/10.1145/3533767.3534390) [**An extensive study on pre-trained models for program understanding
and generation**](https://doi.org/10.1145/3533767.3534390),<br> by *Zhengran Zeng, Hanzhuo Tan, Haotian Zhang, Jing Li, Yuqun Zhang and Lingming Zhang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2207.01780) [**CodeRL: Mastering Code Generation through Pretrained Models and Deep
Reinforcement Learning**](https://doi.org/10.48550/arXiv.2207.01780),<br> by *Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556955) [**CoditT5: Pretraining for Source Code and Natural Language Editing**](https://doi.org/10.1145/3551349.3556955),<br> by *Jiyang Zhang, Sheena Panthaplackel, Pengyu Nie, Junyi Jessy Li and Milos Gligoric*
<br><br>
- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556964) [**Compressing Pre-trained Models of Code into 3 MB**](https://doi.org/10.1145/3551349.3556964),<br> by *Jieke Shi, Zhou Yang, Bowen Xu, Hong Jin Kang and David Lo*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549094) [**Diet code is healthy: simplifying programs for pre-trained models
of code**](https://doi.org/10.1145/3540250.3549094),<br> by *Zhaowei Zhang, Hongyu Zhang, Beijun Shen and Xiaodong Gu*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549162) [**NatGen: generative pre-training by "naturalizing" source code**](https://doi.org/10.1145/3540250.3549162),<br> by *Saikat Chakraborty, Toufique Ahmed, Yangruibo Ding, Premkumar T. Devanbu and Baishakhi Ray*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510203) [**Jigsaw: Large Language Models meet Program Synthesis**](https://doi.org/10.1145/3510003.3510203),<br> by *Naman Jain, Skanda Vaidyanath, Arun Shankar Iyer, Nagarajan Natarajan, Suresh Parthasarathy, Sriram K. Rajamani and Rahul Sharma*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510146) [**Natural Attack for Pre-trained Models of Code**](https://doi.org/10.1145/3510003.3510146),<br> by *Zhou Yang, Jieke Shi, Junda He and David Lo*
<br><br>
- [![](https://img.shields.io/badge/ICER-2022-blue)](https://doi.org/10.1145/3501385.3543957) [**Automatic Generation of Programming Exercises and Code Explanations
Using Large Language Models**](https://doi.org/10.1145/3501385.3543957),<br> by *Sami Sarsa, Paul Denny, Arto Hellas and Juho Leinonen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.03374) [**Evaluating Large Language Models Trained on Code**](https://arxiv.org/abs/2107.03374),<br> by *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pond\'e de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.685) [**CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.685),<br> by *Yue Wang, Weishi Wang, Shafiq R. Joty and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2021-blue)](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) [**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding
and Generation**](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html),<br> by *Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin B. Clement, Dawn Drain et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.211) [**Unified Pre-training for Program Understanding and Generation**](https://doi.org/10.18653/v1/2021.naacl-main.211),<br> by *Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray and Kai-Wei Chang*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2021-blue)](https://doi.org/10.1109/ICSE43902.2021.00040) [**Traceability Transformed: Generating more Accurate Links with Pre-Trained
BERT Models**](https://doi.org/10.1109/ICSE43902.2021.00040),<br> by *Jinfeng Lin, Yalin Liu, Qingkai Zeng, Meng Jiang and Jane Cleland-Huang*
<br><br>
- [![](https://img.shields.io/badge/FSE-2020-blue)](https://doi.org/10.1145/3368089.3417058) [**IntelliCode compose: code generation using transformer**](https://doi.org/10.1145/3368089.3417058),<br> by *Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu and Neel Sundaresan*
<br><br>
- [![](https://img.shields.io/badge/ASE-2020-blue)](https://doi.org/10.1145/3324884.3416591) [**Multi-task Learning based Pre-trained Language Model for Code Completion**](https://doi.org/10.1145/3324884.3416591),<br> by *Fang Liu, Ge Li, Yunfei Zhao and Zhi Jin*
<br><br>
#### Code Representation

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.findings-naacl.80) [**CODE-MVP: Learning to Represent Source Code from Multiple Views
with Contrastive Pre-Training**](https://doi.org/10.18653/v1/2022.findings-naacl.80),<br> by *Xin Wang, Yasheng Wang, Yao Wan, Jiawei Wang, Pingyi Zhou, Li Li, Hao Wu and Jin Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.499) [**UniXcoder: Unified Cross-Modal Pre-training for Code Representation**](https://doi.org/10.18653/v1/2022.acl-long.499),<br> by *Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou and Jian Yin*
<br><br>
- [![](https://img.shields.io/badge/ASE-2022-blue)](https://doi.org/10.1145/3551349.3556900) [**AST-Probe: Recovering abstract syntax trees from hidden representations
of pre-trained language models**](https://doi.org/10.1145/3551349.3556900),<br> by *Jos\'e Antonio Hern\'andez L\'opez, Martin Weyssow, Jes\'us S\'anchez Cuadrado and Houari A. Sahraoui*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jLoC4ez43PZ) [**GraphCodeBERT: Pre-training Code Representations with Data Flow**](https://openreview.net/forum?id=jLoC4ez43PZ),<br> by *Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
#### Code Fixing

- [![](https://img.shields.io/badge/ISSTA-2022-blue)](https://doi.org/10.1145/3533767.3534219) [**CIRCLE: continual repair across programming languages**](https://doi.org/10.1145/3533767.3534219),<br> by *Wei Yuan, Quanjun Zhang, Tieke He, Chunrong Fang, Nguyen Quoc Viet Hung, Xiaodong Hao and Hongzhi Yin*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.57) [**Detect-Localize-Repair: A Unified Framework for Learning to Debug
with CodeT5**](https://aclanthology.org/2022.findings-emnlp.57),<br> by *Nghi Bui, Yue Wang and Steven C. H. Hoi*
<br><br>
- [![](https://img.shields.io/badge/WASA-2022-blue)](https://doi.org/10.1007/978-3-031-19211-1\_11) [**Multi-view Pre-trained Model for Code Vulnerability Identification**](https://doi.org/10.1007/978-3-031-19211-1\_11),<br> by *Xuxiang Jiang, Yinhao Xiao, Jun Wang and Wei Zhang*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3524459.3527350) [**Towards JavaScript program repair with Generative Pre-trained Transformer
(GPT-2)**](https://doi.org/10.1145/3524459.3527350),<br> by *M\'ark Lajk\'o, Viktor Csuvik and L\'aszl\'o Vid\'acs*
<br><br>
- [![](https://img.shields.io/badge/MSR-2021-blue)](https://doi.org/10.1109/MSR52588.2021.00063) [**Applying CodeBERT for Automated Program Repair of Java Simple Bugs**](https://doi.org/10.1109/MSR52588.2021.00063),<br> by *Ehsan Mashhadi and Hadi Hemmati*
<br><br>
- [![](https://img.shields.io/badge/Applied_Sciences-2021-blue)](https://www.mdpi.com/2076-3417/11/11/4755) [**A model with iterative trials for correcting logic errors in source code**](https://www.mdpi.com/2076-3417/11/11/4755),<br> by *Matsumoto, Taku, Watanobe, Yutaka and Nakamura, Keita*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.09352) [**DeepDebug: Fixing Python Bugs Using Stack Traces, Backtranslation,
and Code Skeletons**](https://arxiv.org/abs/2105.09352),<br> by *Dawn Drain, Colin B. Clement, Guillermo Serrato and Neel Sundaresan*
<br><br>
#### Code Review

- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549099) [**AUGER: automatically generating review comments with pre-training
models**](https://doi.org/10.1145/3540250.3549099),<br> by *Lingwei Li, Li Yang, Huaxi Jiang, Jun Yan, Tiejian Luo, Zihan Hua, Geng Liang and Chun Zuo*
<br><br>
- [![](https://img.shields.io/badge/FSE-2022-blue)](https://doi.org/10.1145/3540250.3549081) [**Automating code review activities by large-scale pre-training**](https://doi.org/10.1145/3540250.3549081),<br> by *Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green et al.*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510062) [**Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding**](https://doi.org/10.1145/3510003.3510062),<br> by *Deze Wang, Zhouyang Jia, Shanshan Li, Yue Yu, Yun Xiong, Wei Dong and Xiangke Liao*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510621) [**Using Pre-Trained Models to Boost Code Review Automation**](https://doi.org/10.1145/3510003.3510621),<br> by *Rosalia Tufano, Simone Masiero, Antonio Mastropaolo, Luca Pascarella, Denys Poshyvanyk and Gabriele Bavota*
<br><br>
- [![](https://img.shields.io/badge/ICSE-2022-blue)](https://doi.org/10.1145/3510003.3510050) [**What Do They Capture? - A Structural Analysis of Pre-Trained Language
Models for Source Code**](https://doi.org/10.1145/3510003.3510050),<br> by *Yao Wan, Wei Zhao, Hongyu Zhang, Yulei Sui, Guandong Xu and Hai Jin*
<br><br>
### Software Engineering

- [![](https://img.shields.io/badge/IJCAI-2022-blue)](https://doi.org/10.24963/ijcai.2022/775) [**Deep Learning Meets Software Engineering: A Survey on Pre-Trained
Models of Source Code**](https://doi.org/10.24963/ijcai.2022/775),<br> by *Changan Niu, Chuanyi Li, Bin Luo and Vincent Ng*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.10623) [**Do Pre-trained Language Models Indeed Understand Software Engineering
Tasks?**](https://doi.org/10.48550/arXiv.2211.10623),<br> by *Yao Li, Tao Zhang, Xiapu Luo, Haipeng Cai, Sen Fang and Dawei Yuan*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2104.05861) [**Evaluating Pre-Trained Models for User Feedback Analysis in Software
Engineering: A Study on Classification of App-Reviews**](https://arxiv.org/abs/2104.05861),<br> by *Mohammad Abdul Hadi and Fatemeh H. Fard*
<br><br>
- [![](https://img.shields.io/badge/ASE-2021-blue)](https://doi.org/10.1109/ASE51524.2021.9678927) [**What do pre-trained code models know about code?**](https://doi.org/10.1109/ASE51524.2021.9678927),<br> by *Anjan Karmakar and Romain Robbes*
<br><br>
- [![](https://img.shields.io/badge/ICSME-2020-blue)](https://ieeexplore.ieee.org/abstract/document/9240704/) [**Sentiment analysis for software engineering: How far can pre-trained transformer models go?**](https://ieeexplore.ieee.org/abstract/document/9240704/),<br> by *Zhang, Ting, Xu, Bowen, Thung, Ferdian, Haryono, Stefanus Agus, Lo, David and Jiang, Lingxiao*
<br><br>
### Text Generation

- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356),<br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.471) [**Fine-Grained Controllable Text Generation Using Non-Residual Prompting**](https://doi.org/10.18653/v1/2022.acl-long.471),<br> by *Fredrik Carlsson, Joey \"Ohman, Fangyu Liu, Severine Verlinden, Joakim Nivre and Magnus Sahlgren*
<br><br>
- [![](https://img.shields.io/badge/JKSUCIS-2022-blue)](https://doi.org/10.1016/j.jksuci.2020.04.001) [**The survey: Text generation models in deep learning**](https://doi.org/10.1016/j.jksuci.2020.04.001),<br> by *Touseef Iqbal and Shaima Qureshi*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.491) [**FewshotQA: A simple framework for few-shot learning of question
answering tasks using pre-trained text-to-text models**](https://doi.org/10.18653/v1/2021.emnlp-main.491),<br> by *Rakesh Chada and Pradeep Natarajan*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.502) [**Controllable Open-ended Question Generation with A New Question
Type Ontology**](https://doi.org/10.18653/v1/2021.acl-long.502),<br> by *Shuyang Cao and Lu Wang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2103.10360) [**All NLP Tasks Are Generation Tasks: A General Pretraining Framework**](https://arxiv.org/abs/2103.10360),<br> by *Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang and Jie Tang*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.57) [**Smelting Gold and Silver for Improved Multilingual AMR-to-Text Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.57),<br> by *Leonardo F. R. Ribeiro, Jonas Pfeiffer, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-short.40) [**PRAL: A Tailored Pre-Training Model for Task-Oriented Dialog Generation**](https://doi.org/10.18653/v1/2021.acl-short.40),<br> by *Jing Gu, Qingyang Wu, Chongruo Wu, Weiyan Shi and Zhou Yu*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/17527) [**DialogBERT: Discourse-Aware Response Generation via Learning to Recover
and Rank Utterances**](https://ojs.aaai.org/index.php/AAAI/article/view/17527),<br> by *Xiaodong Gu, Kang Min Yoo and Jung-Woo Ha*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2111.02643) [**Response Generation with Context-Aware Prompt Learning**](https://arxiv.org/abs/2111.02643),<br> by *Xiaodong Gu, Kang Min Yoo and Sang-Woo Lee*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.501) [**DYPLOC: Dynamic Planning of Content Using Mixed Language Models
for Text Generation**](https://doi.org/10.18653/v1/2021.acl-long.501),<br> by *Xinyu Hua, Ashwin Sreevatsa and Lu Wang*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.265) [**Latent Reasoning for Low-Resource Question Generation**](https://doi.org/10.18653/v1/2021.findings-acl.265),<br> by *Xinting Huang, Jianzhong Qi, Yu Sun and Rui Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.223) [**JointGT: Graph-Text Joint Representation Learning for Text Generation
from Knowledge Graphs**](https://doi.org/10.18653/v1/2021.findings-acl.223),<br> by *Pei Ke, Haozhe Ji, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu and Minlie Huang*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jWkw45-9AbL) [**A Distributional Approach to Controlled Text Generation**](https://openreview.net/forum?id=jWkw45-9AbL),<br> by *Muhammad Khalifa, Hady Elsahar and Marc Dymetman*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.4) [**TextBox: A Unified, Modularized, and Extensible Framework for Text
Generation**](https://doi.org/10.18653/v1/2021.acl-demo.4),<br> by *Junyi Li, Tianyi Tang, Gaole He, Jinhao Jiang, Xiaoxuan Hu, Puzhao Xie, Zhipeng Chen, Zhuohao Yu et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.136) [**Few-shot Knowledge Graph-to-Text Generation with Pretrained Language
Models**](https://doi.org/10.18653/v1/2021.findings-acl.136),<br> by *Junyi Li, Tianyi Tang, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3462865) [**Knowledge-based Review Generation by Coherence Enhanced Text Planning**](https://doi.org/10.1145/3404835.3462865),<br> by *Junyi Li, Wayne Xin Zhao, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.353) [**Prefix-Tuning: Optimizing Continuous Prompts for Generation**](https://doi.org/10.18653/v1/2021.acl-long.353),<br> by *Xiang Lisa Li and Percy Liang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.36) [**GLGE: A New General Language Generation Evaluation Benchmark**](https://doi.org/10.18653/v1/2021.findings-acl.36),<br> by *Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.173) [**A Three-Stage Learning Framework for Low-Resource Knowledge-Grounded
Dialogue Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.173),<br> by *Shilei Liu, Xiaofeng Zhao, Bochao Li, Feiliang Ren, Longhui Zhang and Shujuan Yin*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.340) [**Ask what's missing and what's useful: Improving Clarification Question
Generation using Global Knowledge**](https://doi.org/10.18653/v1/2021.naacl-main.340),<br> by *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley and Julian J. McAuley*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.248) [**ZmBART: An Unsupervised Cross-lingual Transfer Framework for Language
Generation**](https://doi.org/10.18653/v1/2021.findings-acl.248),<br> by *Kaushal Kumar Maurya, Maunendra Sankar Desarkar, Yoshinobu Kano and Kumari Deepshikha*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.334) [**A Plug-and-Play Method for Controlled Text Generation**](https://doi.org/10.18653/v1/2021.findings-emnlp.334),<br> by *Damian Pascual, Beni Egressy, Clara Meister, Ryan Cotterell and Roger Wattenhofer*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.351) [**Structural Adapters in Pretrained Language Models for AMR-to-Text
Generation**](https://doi.org/10.18653/v1/2021.emnlp-main.351),<br> by *Leonardo F. R. Ribeiro, Yue Zhang and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.115) [**Towards Table-to-Text Generation with Numerical Reasoning**](https://doi.org/10.18653/v1/2021.acl-long.115),<br> by *Lya Hulliyyatus Suadaa, Hidetaka Kamigaito, Kotaro Funakoshi, Manabu Okumura and Hiroya Takamura*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2107.02137) [**ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language
Understanding and Generation**](https://arxiv.org/abs/2107.02137),<br> by *Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.341) [**Progressive Generation of Long Text with Pretrained Language Models**](https://doi.org/10.18653/v1/2021.naacl-main.341),<br> by *Bowen Tan, Zichao Yang, Maruan Al-Shedivat, Eric P. Xing and Zhiting Hu*
<br><br>
- [![](https://img.shields.io/badge/ECIR-2021-blue)](https://doi.org/10.1007/978-3-030-72113-8\_46) [**Consistency and Coherency Enhanced Story Generation**](https://doi.org/10.1007/978-3-030-72113-8\_46),<br> by *Wei Wang, Piji Li and Hai-Tao Zheng*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-acl.200) [**Structure-Aware Pre-Training for Table-to-Text Generation**](https://doi.org/10.18653/v1/2021.findings-acl.200),<br> by *Xinyu Xing and Xiaojun Wan*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.95) [**AugNLG: Few-shot Natural Language Generation using Self-trained Data
Augmentation**](https://doi.org/10.18653/v1/2021.acl-long.95),<br> by *Xinnuo Xu, Guoyin Wang, Young-Bum Kim and Sungjin Lee*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.6) [**DeepRapper: Neural Rap Generation with Rhyme and Rhythm Modeling**](https://doi.org/10.18653/v1/2021.acl-long.6),<br> by *Lanqing Xue, Kaitao Song, Duocai Wu, Xu Tan, Nevin L. Zhang, Tao Qin, Wei-Qiang Zhang and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-demo.26) [**FastSeq: Make Sequence Generation Faster**](https://doi.org/10.18653/v1/2021.acl-demo.26),<br> by *Yu Yan, Fei Hu, Jiusheng Chen, Nikhil Bhendawade, Ting Ye, Yeyun Gong, Nan Duan, Desheng Cui et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.392) [**A Simple and Efficient Multi-Task Learning Approach for Conditioned
Dialogue Generation**](https://doi.org/10.18653/v1/2021.naacl-main.392),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2021-blue)](https://doi.org/10.1145/3404835.3463037) [**DSGPT: Domain-Specific Generative Pre-Training of Transformers for
Text Generation in E-commerce Title and Review Summarization**](https://doi.org/10.1145/3404835.3463037),<br> by *Xueying Zhang, Yunjiang Jiang, Yue Shang, Zhaomeng Cheng, Chi Zhang, Xiaochuan Fan, Yun Xiao and Bo Long*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2020-blue)](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf) [**Language Models are Few-Shot Learners**](https://ailab-ua.github.io/courses/resources/GPT3_Brown_2020.pdf),<br> by *Brown, Tom B, Mann, Benjamin, Ryder, Nick, Subbiah, Melanie, Kaplan, Jared, Dhariwal, Prafulla, Neelakantan, Arvind, Shyam, Pranav et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.9) [**PLATO: Pre-trained Dialogue Generation Model with Discrete Latent
Variable**](https://doi.org/10.18653/v1/2020.acl-main.9),<br> by *Siqi Bao, Huang He, Fan Wang, Hua Wu and Haifeng Wang*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2006.14799) [**Evaluation of Text Generation: A Survey**](https://arxiv.org/abs/2006.14799),<br> by *Asli Celikyilmaz, Elizabeth Clark and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.697) [**KGPT: Knowledge-Grounded Pre-Training for Data-to-Text Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.697),<br> by *Wenhu Chen, Yu Su, Xifeng Yan and William Yang Wang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.705) [**Distilling Knowledge Learned in BERT for Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.705),<br> by *Yen-Chun Chen, Zhe Gan, Yu Cheng, Jingzhou Liu and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.190) [**Logic2Text: High-Fidelity Natural Language Generation from Logical
Forms**](https://doi.org/10.18653/v1/2020.findings-emnlp.190),<br> by *Zhiyu Chen, Wenhu Chen, Hanwen Zha, Xiyou Zhou, Yunkai Zhang, Sairam Sundaresan and William Yang Wang*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6256) [**Cross-Lingual Natural Language Generation via Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/6256),<br> by *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao and Heyan Huang*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=H1edEyBKDS) [**Plug and Play Language Models: A Simple Approach to Controlled Text
Generation**](https://openreview.net/forum?id=H1edEyBKDS),<br> by *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski and Rosanne Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2007.15780) [**Neural Language Generation: Formulation, Methods, and Evaluation**](https://arxiv.org/abs/2007.15780),<br> by *Cristina Garbacea and Qiaozhu Mei*
<br><br>
- [![](https://img.shields.io/badge/COLING-2020-blue)](https://doi.org/10.18653/v1/2020.coling-main.179) [**TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction
and Content Matching**](https://doi.org/10.18653/v1/2020.coling-main.179),<br> by *Heng Gong, Yawei Sun, Xiaocheng Feng, Bing Qin, Wei Bi, Xiaojiang Liu and Ting Liu*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00302) [**A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation**](https://doi.org/10.1162/tacl\_a\_00302),<br> by *Jian Guan, Fei Huang, Minlie Huang, Zhihao Zhao and Xiaoyan Zhu*
<br><br>
- [![](https://img.shields.io/badge/COLING-2020-blue)](https://doi.org/10.18653/v1/2020.coling-main.218) [**Have Your Text and Use It Too! End-to-End Neural Data-to-Text Generation
with Semantic Fidelity**](https://doi.org/10.18653/v1/2020.coling-main.218),<br> by *Hamza Harkous, Isabel Groves and Amir Saffari*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.55) [**Reformulating Unsupervised Style Transfer as Paraphrase Generation**](https://doi.org/10.18653/v1/2020.emnlp-main.55),<br> by *Kalpesh Krishna, John Wieting and Mohit Iyyer*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.703) [**BART: Denoising Sequence-to-Sequence Pre-training for Natural Language
Generation, Translation, and Comprehension**](https://doi.org/10.18653/v1/2020.acl-main.703),<br> by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/CIKM-2020-blue)](https://doi.org/10.1145/3340531.3411893) [**Knowledge-Enhanced Personalized Review Generation with Capsule Graph
Neural Network**](https://doi.org/10.1145/3340531.3411893),<br> by *Junyi Li, Siqing Li, Wayne Xin Zhao, Gaole He, Zhicheng Wei, Nicholas Jing Yuan and Ji-Rong Wen*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.167) [**GPT-too: A Language-Model-First Approach for AMR-to-Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.167),<br> by *Manuel Mager, Ram\'on Fernandez Astudillo, Tahira Naseem, Md. Arafat Sultan, Young-Suk Lee, Radu Florian and Salim Roukos*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.17) [**Few-shot Natural Language Generation for Task-Oriented Dialog**](https://doi.org/10.18653/v1/2020.findings-emnlp.17),<br> by *Baolin Peng, Chenguang Zhu, Chunyuan Li, Xiujun Li, Jinchao Li, Michael Zeng and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.349) [**PlotMachines: Outline-Conditioned Generation with Dynamic Plot State
Tracking**](https://doi.org/10.18653/v1/2020.emnlp-main.349),<br> by *Hannah Rashkin, Asli Celikyilmaz, Yejin Choi and Jianfeng Gao*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2007.08426) [**Investigating Pretrained Language Models for Graph-to-Text Generation**](https://arxiv.org/abs/2007.08426),<br> by *Leonardo F. R. Ribeiro, Martin Schmitt, Hinrich Sch\"utze and Iryna Gurevych*
<br><br>
- [![](https://img.shields.io/badge/TACL-2020-blue)](https://doi.org/10.1162/tacl\_a\_00313) [**Leveraging Pre-trained Checkpoints for Sequence Generation Tasks**](https://doi.org/10.1162/tacl\_a\_00313),<br> by *Sascha Rothe, Shashi Narayan and Aliaksei Severyn*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.495) [**T3: Tree-Autoencoder Constrained Adversarial Text Generation for
Targeted Attack**](https://doi.org/10.18653/v1/2020.emnlp-main.495),<br> by *Boxin Wang, Hengzhi Pei, Boyuan Pan, Qian Chen, Shuohang Wang and Bo Li*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.226) [**MEGATRON-CNTRL: Controllable Story Generation with External Knowledge
Using Large-Scale Language Models**](https://doi.org/10.18653/v1/2020.emnlp-main.226),<br> by *Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar and Bryan Catanzaro*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.140) [**StyleDGPT: Stylized Response Generation with Pre-trained Language
Models**](https://doi.org/10.18653/v1/2020.findings-emnlp.140),<br> by *Ze Yang, Wei Wu, Can Xu, Xinnian Liang, Jiaqi Bai, Liran Wang, Wei Wang and Zhoujun Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2010.11140) [**Generalized Conditioned Dialogue Generation Based on Pre-trained Language
Model**](https://arxiv.org/abs/2010.11140),<br> by *Yan Zeng and Jian-Yun Nie*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=SkeHuCVFDr) [**BERTScore: Evaluating Text Generation with BERT**](https://openreview.net/forum?id=SkeHuCVFDr),<br> by *Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-demos.30) [**DIALOGPT : Large-Scale Generative Pre-training for Conversational
Response Generation**](https://doi.org/10.18653/v1/2020.acl-demos.30),<br> by *Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing Liu et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2019-blue)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf),<br> by *Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario and Sutskever, Ilya*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
- [![](https://img.shields.io/badge/ACL-2019-blue)](https://doi.org/10.18653/v1/p19-1608) [**Large-Scale Transfer Learning for Natural Language Generation**](https://doi.org/10.18653/v1/p19-1608),<br> by *Sergey Golovanov, Rauf Kurbanov, Sergey I. Nikolenko, Kyryl Truskovskyi, Alexander Tselousov and Thomas Wolf*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2019-blue)](https://doi.org/10.18653/v1/D19-1615) [**Improving Neural Story Generation by Targeted Common Sense Grounding**](https://doi.org/10.18653/v1/D19-1615),<br> by *Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian J. McAuley and Garrison W. Cottrell*
<br><br>
- [![](https://img.shields.io/badge/ICML-2019-blue)](http://proceedings.mlr.press/v97/song19d.html) [**MASS: Masked Sequence to Sequence Pre-training for Language Generation**](http://proceedings.mlr.press/v97/song19d.html),<br> by *Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2018-blue)](https://openreview.net/forum?id=Hyg0vbWC-) [**Generating Wikipedia by Summarizing Long Sequences**](https://openreview.net/forum?id=Hyg0vbWC-),<br> by *Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser and Noam Shazeer*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2018-blue)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf),<br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
#### Controllable Text Generation

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.502) [**Controllable Open-ended Question Generation with A New Question
Type Ontology**](https://doi.org/10.18653/v1/2021.acl-long.502),<br> by *Shuyang Cao and Lu Wang*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=jWkw45-9AbL) [**A Distributional Approach to Controlled Text Generation**](https://openreview.net/forum?id=jWkw45-9AbL),<br> by *Muhammad Khalifa, Hady Elsahar and Marc Dymetman*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2021-blue)](https://doi.org/10.18653/v1/2021.findings-emnlp.334) [**A Plug-and-Play Method for Controlled Text Generation**](https://doi.org/10.18653/v1/2021.findings-emnlp.334),<br> by *Damian Pascual, Beni Egressy, Clara Meister, Ryan Cotterell and Roger Wattenhofer*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=H1edEyBKDS) [**Plug and Play Language Models: A Simple Approach to Controlled Text
Generation**](https://openreview.net/forum?id=H1edEyBKDS),<br> by *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski and Rosanne Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.68) [**Rigid Formats Controlled Text Generation**](https://doi.org/10.18653/v1/2020.acl-main.68),<br> by *Piji Li, Haisong Zhang, Xiaojiang Liu and Shuming Shi*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1909.05858) [**CTRL: A Conditional Transformer Language Model for Controllable
Generation**](http://arxiv.org/abs/1909.05858),<br> by *Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong and Richard Socher*
<br><br>
### Continual Learning

- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.00024) [**Learning to Prompt for Continual Learning**](https://doi.org/10.1109/CVPR52688.2022.00024),<br> by *Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot et al.*
<br><br>
- [![](https://img.shields.io/badge/T_PAMI-2022-blue)](https://doi.org/10.1109/TPAMI.2021.3057446) [**A Continual Learning Survey: Defying Forgetting in Classification
Tasks**](https://doi.org/10.1109/TPAMI.2021.3057446),<br> by *Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory G. Slabaugh and Tinne Tuytelaars*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.220) [**ELLE: Efficient Lifelong Pre-training for Emerging Data**](https://doi.org/10.18653/v1/2022.findings-acl.220),<br> by *Yujia Qin, Jiajie Zhang, Yankai Lin, Zhiyuan Liu, Peng Li, Maosong Sun and Jie Zhou*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.351) [**Lifelong Pretraining: Continually Adapting Language Models to Emerging
Corpora**](https://doi.org/10.18653/v1/2022.naacl-main.351),<br> by *Xisen Jin, Dejiao Zhang, Henghui Zhu, Wei Xiao, Shang-Wen Li, Xiaokai Wei, Andrew O. Arnold and Xiang Ren*
<br><br>
- [![](https://img.shields.io/badge/JAIR-2022-blue)](https://doi.org/10.1613/jair.1.13673) [**Towards Continual Reinforcement Learning: A Review and Perspectives**](https://doi.org/10.1613/jair.1.13673),<br> by *Khimya Khetarpal, Matthew Riemer, Irina Rish and Doina Precup*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.408) [**Continual Pre-training of Language Models for Math Problem Understanding
with Syntax-Aware Memory Network**](https://doi.org/10.18653/v1/2022.acl-long.408),<br> by *Zheng Gong, Kun Zhou, Xin Zhao, Jing Sha, Shijin Wang and Ji-Rong Wen*
<br><br>
### Prompt Learning

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.12868) [**On Robustness of Prompt-based Semantic Parsing with Large Pre-trained
Language Model: An Empirical Study on Codex**](https://doi.org/10.48550/arXiv.2301.12868),<br> by *Terry Yue Zhuo, Zhuang Li, Yujin Huang, Yuan-Fang Li, Weiqing Wang, Gholamreza Haffari and Fatemeh Shiri*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.00024) [**Learning to Prompt for Continual Learning**](https://doi.org/10.1109/CVPR52688.2022.00024),<br> by *Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot et al.*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.167) [**Do Prompt-Based Models Really Understand the Meaning of Their Prompts?**](https://doi.org/10.18653/v1/2022.naacl-main.167),<br> by *Albert Webson and Ellie Pavlick*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.01910) [**Large Language Models Are Human-Level Prompt Engineers**](https://doi.org/10.48550/arXiv.2211.01910),<br> by *Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan and Jimmy Ba*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.60) [**An Information-theoretic Approach to Prompt Engineering Without Ground
Truth Labels**](https://doi.org/10.18653/v1/2022.acl-long.60),<br> by *Taylor Sorensen, Joshua Robinson, Christopher Michael Rytting, Alexander Glenn Shaw, Kyle Jeffrey Rogers, Alexia Pauline Delorey, Mahmoud Khalil, Nancy Fulda et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.04037) [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://doi.org/10.48550/arXiv.2212.04037),<br> by *Hila Gonen, Srini Iyer, Terra Blevins, Noah A. Smith and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/ACL_Findings-2022-blue)](https://doi.org/10.18653/v1/2022.findings-acl.222) [**Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with
Language Models**](https://doi.org/10.18653/v1/2022.findings-acl.222),<br> by *Robert L. Logan IV, Ivana Balazevic, Eric Wallace, Fabio Petroni, Sameer Singh and Sebastian Riedel*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.174) [**Adversarial Soft Prompt Tuning for Cross-Domain Sentiment Analysis**](https://doi.org/10.18653/v1/2022.acl-long.174),<br> by *Hui Wu and Xiaodong Shi*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.471) [**Fine-Grained Controllable Text Generation Using Non-Residual Prompting**](https://doi.org/10.18653/v1/2022.acl-long.471),<br> by *Fredrik Carlsson, Joey \"Ohman, Fangyu Liu, Severine Verlinden, Joakim Nivre and Magnus Sahlgren*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.424) [**MSP: Multi-Stage Prompting for Making Pre-trained Language Models
Better Translators**](https://doi.org/10.18653/v1/2022.acl-long.424),<br> by *Zhixing Tan, Xiangwen Zhang, Shuo Wang and Yang Liu*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.365) [**Noisy Channel Language Model Prompting for Few-Shot Text Classification**](https://doi.org/10.18653/v1/2022.acl-long.365),<br> by *Sewon Min, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br><br>
- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.346) [**SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer**](https://doi.org/10.18653/v1/2022.acl-long.346),<br> by *Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou' and Daniel Cer*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2203.06904) [**Delta Tuning: A Comprehensive Study of Parameter Efficient Methods
for Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2203.06904),<br> by *Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen et al.*
<br><br>
- [![](https://img.shields.io/badge/AutoML-2022-blue)](https://proceedings.mlr.press/v188/bansal22a.html) [**Meta-Adapters: Parameter Efficient Few-shot Fine-tuning through Meta-Learning**](https://proceedings.mlr.press/v188/bansal22a.html),<br> by *Trapit Bansal, Salaheddin Alzubi, Tong Wang, Jay-Yoon Lee and Andrew McCallum*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://openreview.net/forum?id=oOte_397Q4P) [**Sparse Structure Search for Delta Tuning**](https://openreview.net/forum?id=oOte_397Q4P),<br> by *Shengding Hu, Zhen Zhang, Ning Ding, Yadao Wang, Yasheng Wang, Zhiyuan Liu and Maosong Sun*
<br><br>
- [![](https://img.shields.io/badge/WWW-2022-blue)](https://doi.org/10.1145/3485447.3511921) [**Ontology-enhanced Prompt-tuning for Few-shot Learning**](https://doi.org/10.1145/3485447.3511921),<br> by *Hongbin Ye, Ningyu Zhang, Shumin Deng, Xiang Chen, Hui Chen, Feiyu Xiong, Xi Chen and Huajun Chen*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.06950) [**Pre-trained Language Models can be Fully Zero-Shot Learners**](https://doi.org/10.48550/arXiv.2212.06950),<br> by *Xuandong Zhao, Siqi Ouyang, Zhiguo Yu, Ming Wu and Lei Li*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2205.10625) [**Least-to-Most Prompting Enables Complex Reasoning in Large Language
Models**](https://doi.org/10.48550/arXiv.2205.10625),<br> by *Denny Zhou, Nathanael Sch\"arli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet et al.*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.491) [**FewshotQA: A simple framework for few-shot learning of question
answering tasks using pre-trained text-to-text models**](https://doi.org/10.18653/v1/2021.emnlp-main.491),<br> by *Rakesh Chada and Pradeep Natarajan*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.243) [**The Power of Scale for Parameter-Efficient Prompt Tuning**](https://doi.org/10.18653/v1/2021.emnlp-main.243),<br> by *Brian Lester, Rami Al-Rfou and Noah Constant*
<br><br>
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.353) [**Prefix-Tuning: Optimizing Continuous Prompts for Generation**](https://doi.org/10.18653/v1/2021.acl-long.353),<br> by *Xiang Lisa Li and Percy Liang*
<br><br>
### Natural Language Understanding

- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.308) [**VECO: Variable and Flexible Cross-lingual Pre-training for Language
Understanding and Generation**](https://doi.org/10.18653/v1/2021.acl-long.308),<br> by *Fuli Luo, Wei Wang, Jiahao Liu, Yijia Liu, Bin Bi, Songfang Huang, Fei Huang and Luo Si*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html) [**Unified Language Model Pre-training for Natural Language Understanding
and Generation**](https://proceedings.neurips.cc/paper/2019/hash/c20bb2d9a50d5ac1f713f8b34d9aac5a-Abstract.html),<br> by *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou et al.*
<br><br>
- [![](https://img.shields.io/badge/OpenAI-2018-blue)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) [**Improving language understanding by generative pre-training**](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf),<br> by *Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya and others*
<br><br>
### Multimodal

- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2108.04556) [**CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained
Model**](https://arxiv.org/abs/2108.04556),<br> by *Xin Wang, Yasheng Wang, Pingyi Zhou, Fei Mi, Meng Xiao, Yadao Wang, Li Li, Xiao Liu et al.*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2021-blue)](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html) [**Less Is More: ClipBERT for Video-and-Language Learning via Sparse
Sampling**](https://openaccess.thecvf.com/content/CVPR2021/html/Lei_Less_Is_More_ClipBERT_for_Video-and-Language_Learning_via_Sparse_Sampling_CVPR_2021_paper.html),<br> by *Jie Lei, Linjie Li, Luowei Zhou, Zhe Gan, Tamara L. Berg, Mohit Bansal and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2102.10772) [**Transformer is All You Need: Multimodal Multitask Learning with a
Unified Transformer**](https://arxiv.org/abs/2102.10772),<br> by *Ronghang Hu and Amanpreet Singh*
<br><br>
- [![](https://img.shields.io/badge/MM-2021-blue)](https://doi.org/10.1145/3474085.3475709) [**Pre-training Graph Transformer with Multimodal Side Information for
Recommendation**](https://doi.org/10.1145/3474085.3475709),<br> by *Yong Liu, Susen Yang, Chenyi Lei, Guoxin Wang, Haihong Tang, Juyong Zhang, Aixin Sun and Chunyan Miao*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2002.06353) [**UniViLM: A Unified Video and Language Pre-Training Model for Multimodal
Understanding and Generation**](https://arxiv.org/abs/2002.06353),<br> by *Huaishao Luo, Lei Ji, Botian Shi, Haoyang Huang, Nan Duan, Tianrui Li, Xilin Chen and Ming Zhou*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html) [**Large-Scale Adversarial Training for Vision-and-Language Representation
Learning**](https://proceedings.neurips.cc/paper/2020/hash/49562478de4c54fafd4ec46fdb297de5-Abstract.html),<br> by *Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng and Jingjing Liu*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.162) [**Vokenization: Improving Language Understanding with Contextualized,
Visual-Grounded Supervision**](https://doi.org/10.18653/v1/2020.emnlp-main.162),<br> by *Hao Tan and Mohit Bansal*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.214) [**Integrating Multimodal Information in Large Pretrained Transformers**](https://doi.org/10.18653/v1/2020.acl-main.214),<br> by *Wasifur Rahman, Md. Kamrul Hasan, Sangwu Lee, AmirAli Bagher Zadeh, Chengfeng Mao, Louis-Philippe Morency and Mohammed E. Hoque*
<br><br>
- [![](https://img.shields.io/badge/ICLR-2020-blue)](https://openreview.net/forum?id=SygXPaEYvH) [**VL-BERT: Pre-training of Generic Visual-Linguistic Representations**](https://openreview.net/forum?id=SygXPaEYvH),<br> by *Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu, Furu Wei and Jifeng Dai*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.03557) [**VisualBERT: A Simple and Performant Baseline for Vision and Language**](http://arxiv.org/abs/1908.03557),<br> by *Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh and Kai-Wei Chang*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2019-blue)](https://proceedings.neurips.cc/paper/2019/hash/c74d97b01eae257e44aa9d5bade97baf-Abstract.html) [**ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations
for Vision-and-Language Tasks**](https://proceedings.neurips.cc/paper/2019/hash/c74d97b01eae257e44aa9d5bade97baf-Abstract.html),<br> by *Jiasen Lu, Dhruv Batra, Devi Parikh and Stefan Lee*
<br><br>
- [![](https://img.shields.io/badge/ICCV-2019-blue)](https://doi.org/10.1109/ICCV.2019.00756) [**VideoBERT: A Joint Model for Video and Language Representation Learning**](https://doi.org/10.1109/ICCV.2019.00756),<br> by *Chen Sun, Austin Myers, Carl Vondrick, Kevin Murphy and Cordelia Schmid*
<br><br>
### LLM Reliability

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.09150) [**Prompting GPT-3 To Be Reliable**](https://doi.org/10.48550/arXiv.2210.09150),<br> by *Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan L. Boyd-Graber and Lijuan Wang*
<br><br>
### Dialogue System

- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.02851) [**DiSTRICT: Dialogue State Tracking with Retriever Driven In-Context
Tuning**](https://doi.org/10.48550/arXiv.2212.02851),<br> by *Praveen Venkateswaran, Evelyn Duesterwald and Vatche Isahagian*
<br><br>
- [![](https://img.shields.io/badge/COLING-2022-blue)](https://aclanthology.org/2022.coling-1.56) [**Does GPT-3 Generate Empathetic Dialogues? A Novel In-Context Example
Selection Method and Automatic Evaluation Metric for Empathetic Dialogue
Generation**](https://aclanthology.org/2022.coling-1.56),<br> by *Young-Jun Lee, Chae-Gyun Lim and Ho-Jin Choi*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21416) [**Fusing Task-Oriented and Open-Domain Dialogues in Conversational Agents**](https://ojs.aaai.org/index.php/AAAI/article/view/21416),<br> by *Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2206.11309) [**GODEL: Large-Scale Pre-Training for Goal-Directed Dialog**](https://doi.org/10.48550/arXiv.2206.11309),<br> by *Baolin Peng, Michel Galley, Pengcheng He, Chris Brockett, Lars Liden, Elnaz Nouri, Zhou Yu, Bill Dolan et al.*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09252) [**Mind the Knowledge Gap: A Survey of Knowledge-enhanced Dialogue
Systems**](https://doi.org/10.48550/arXiv.2212.09252),<br> by *Sagi Shaier, Lawrence Hunter and Katharina Kann*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.404) [**Dialogue State Tracking with a Language Model using Schema-Driven
Prompting**](https://doi.org/10.18653/v1/2021.emnlp-main.404),<br> by *Chia-Hsuan Lee, Hao Cheng and Mari Ostendorf*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2110.08118) [**Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**](https://arxiv.org/abs/2110.08118),<br> by *Andrea Madotto, Zhaojiang Lin, Genta Indra Winata and Pascale Fung*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.239) [**Action-Based Conversations Dataset: A Corpus for Building More In-Depth
Task-Oriented Dialogue Systems**](https://doi.org/10.18653/v1/2021.naacl-main.239),<br> by *Derek Chen, Howard Chen, Yi Yang, Alexander Lin and Zhou Yu*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.122) [**Fine-grained Post-training for Improving Retrieval-based Dialogue
Systems**](https://doi.org/10.18653/v1/2021.naacl-main.122),<br> by *Janghoon Han, Taesuk Hong, Byoungjae Kim, Youngjoong Ko and Jungyun Seo*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2105.04387) [**Recent Advances in Deep Learning Based Dialogue Systems: A Systematic
Survey**](https://arxiv.org/abs/2105.04387),<br> by *Jinjie Ni, Tom Young, Vlad Pandelea, Fuzhao Xue, Vinay Adiga and Erik Cambria*
<br><br>
- [![](https://img.shields.io/badge/WWW-2021-blue)](https://doi.org/10.1145/3442381.3449939) [**Slot Self-Attentive Dialogue State Tracking**](https://doi.org/10.1145/3442381.3449939),<br> by *Fanghua Ye, Jarana Manotumruksa, Qiang Zhang, Shenghui Li and Emine Yilmaz*
<br><br>
- [![](https://img.shields.io/badge/TACL-2021-blue)](https://doi.org/10.1162/tacl\_a\_00390) [**Pretraining the Noisy Channel Model for Task-Oriented Dialogue**](https://doi.org/10.1162/tacl\_a\_00390),<br> by *Qi Liu, Lei Yu, Laura Rimell and Phil Blunsom*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/17674) [**UBAR: Towards Fully End-to-End Task-Oriented Dialog System with
GPT-2**](https://ojs.aaai.org/index.php/AAAI/article/view/17674),<br> by *Yunyi Yang, Yunhao Li and Xiaojun Quan*
<br><br>
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.54) [**End-to-End Neural Pipeline for Goal-Oriented Dialogue Systems using
GPT-2**](https://doi.org/10.18653/v1/2020.acl-main.54),<br> by *DongHoon Ham, Jeong-Gwan Lee, Youngsoo Jang and Kee-Eung Kim*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2020-blue)](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html) [**A Simple Language Model for Task-Oriented Dialogue**](https://proceedings.neurips.cc/paper/2020/hash/e946209592563be0f01c844ab2170f0c-Abstract.html),<br> by *Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz and Richard Socher*
<br><br>
### Recommender System

- [![](https://img.shields.io/badge/TKDE-2022-blue)](https://doi.org/10.1109/TKDE.2020.3028705) [**A Survey on Knowledge Graph-Based Recommender Systems**](https://doi.org/10.1109/TKDE.2020.3028705),<br> by *Qingyu Guo, Fuzhen Zhuang, Chuan Qin, Hengshu Zhu, Xing Xie, Hui Xiong and Qing He*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2022-blue)](https://doi.org/10.1145/3477495.3531937) [**Are Graph Augmentations Necessary?: Simple Graph Contrastive Learning
for Recommendation**](https://doi.org/10.1145/3477495.3531937),<br> by *Junliang Yu, Hongzhi Yin, Xin Xia, Tong Chen, Lizhen Cui and Quoc Viet Hung Nguyen*
<br><br>
- [![](https://img.shields.io/badge/TOIS-2022-blue)](https://dl.acm.org/doi/abs/10.1145/3572835) [**Disentangled Representations Learning for Multi-Target Cross-Domain Recommendation**](https://dl.acm.org/doi/abs/10.1145/3572835),<br> by *Guo, Xiaobo, Li, Shaoshuai, Guo, Naicheng, Cao, Jiangxia, Liu, Xiaolei, Ma, Qiongxu, Gan, Runsheng and Zhao, Yunan*
<br><br>
- [![](https://img.shields.io/badge/SIGIR-2022-blue)](https://doi.org/10.1145/3477495.3531714) [**Rethinking Reinforcement Learning for Recommendation: A Prompt Perspective**](https://doi.org/10.1145/3477495.3531714),<br> by *Xin Xin, Tiago Pimentel, Alexandros Karatzoglou, Pengjie Ren, Konstantina Christakopoulou and Zhaochun Ren*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2101.09459) [**Advances and Challenges in Conversational Recommender Systems: A
Survey**](https://arxiv.org/abs/2101.09459),<br> by *Chongming Gao, Wenqiang Lei, Xiangnan He, Maarten de Rijke and Tat-Seng Chua*
<br><br>
- [![](https://img.shields.io/badge/MM-2021-blue)](https://doi.org/10.1145/3474085.3475709) [**Pre-training Graph Transformer with Multimodal Side Information for
Recommendation**](https://doi.org/10.1145/3474085.3475709),<br> by *Yong Liu, Susen Yang, Chenyi Lei, Guoxin Wang, Haihong Tang, Juyong Zhang, Aixin Sun and Chunyan Miao*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/5465) [**Towards Hands-Free Visual Dialog Interactive Recommendation**](https://ojs.aaai.org/index.php/AAAI/article/view/5465),<br> by *Tong Yu, Yilin Shen and Hongxia Jin*
<br><br>
### Event Extraction

- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.starsem-1.11) [**Word-Label Alignment for Event Detection: A New Perspective via
Optimal Transport**](https://doi.org/10.18653/v1/2022.starsem-1.11),<br> by *Amir Pouran Ben Veyseh and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.01593) [**CLIP-Event: Connecting Text and Images with Event Structures**](https://doi.org/10.1109/CVPR52688.2022.01593),<br> by *Manling Li, Ruochen Xu, Shuohang Wang, Luowei Zhou, Xudong Lin, Chenguang Zhu, Michael Zeng, Heng Ji et al.*
<br><br>
- [![](https://img.shields.io/badge/COLING-2022-blue)](https://aclanthology.org/2022.coling-1.200) [**Event Causality Identification via Derivative Prompt Joint Learning**](https://aclanthology.org/2022.coling-1.200),<br> by *Shirong Shen, Heng Zhou, Tongtong Wu and Guilin Qi*
<br><br>
- [![](https://img.shields.io/badge/ECML-2021-blue)](https://doi.org/10.1007/978-3-030-86523-8\_39) [**Augmenting Open-Domain Event Detection with Synthetic Data from GPT-2**](https://doi.org/10.1007/978-3-030-86523-8\_39),<br> by *Amir Pouran Ben Veyseh, Minh Van Nguyen, Bonan Min and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.691) [**SeqMix: Augmenting Active Sequence Labeling via Sequence Mixup**](https://doi.org/10.18653/v1/2020.emnlp-main.691),<br> by *Rongzhi Zhang, Yue Yu and Chao Zhang*
<br><br>
- [![](https://img.shields.io/badge/ACL-2019-blue)](https://doi.org/10.18653/v1/p19-1522) [**Exploring Pre-trained Language Models for Event Extraction and Generation**](https://doi.org/10.18653/v1/p19-1522),<br> by *Sen Yang, Dawei Feng, Linbo Qiao, Zhigang Kan and Dongsheng Li*
<br><br>
### Event Relation Extraction

- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://aclanthology.org/2022.emnlp-main.634) [**Learning Cross-Task Dependencies for Joint Extraction of Entities,
Events, Event Arguments, and Relations**](https://aclanthology.org/2022.emnlp-main.634),<br> by *Minh Van Nguyen, Bonan Min, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2022-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/21354) [**Selecting Optimal Context Sentences for Event-Event Relation Extraction**](https://ojs.aaai.org/index.php/AAAI/article/view/21354),<br> by *Hieu Man, Nghia Trung Ngo, Linh Ngo Van and Thien Huu Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP_Findings-2022-blue)](https://aclanthology.org/2022.findings-emnlp.407) [**Multilingual SubEvent Relation Extraction: A Novel Dataset and Structure
Induction Method**](https://aclanthology.org/2022.findings-emnlp.407),<br> by *Viet Dac Lai, Hieu Man, Linh Ngo Van, Franck Dernoncourt and Thien Nguyen*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2021-blue)](https://doi.org/10.18653/v1/2021.emnlp-main.107) [**Salience-Aware Event Chain Modeling for Narrative Understanding**](https://doi.org/10.18653/v1/2021.emnlp-main.107),<br> by *Xiyang Zhang, Muhao Chen and Jonathan May*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.51) [**Joint Constrained Learning for Event-Event Relation Extraction**](https://doi.org/10.18653/v1/2020.emnlp-main.51),<br> by *Haoyu Wang, Muhao Chen, Hongming Zhang and Dan Roth*
<br><br>
### Data Argumentation

- [![](https://img.shields.io/badge/EMNLP-2020-blue)](https://doi.org/10.18653/v1/2020.emnlp-main.691) [**SeqMix: Augmenting Active Sequence Labeling via Sequence Mixup**](https://doi.org/10.18653/v1/2020.emnlp-main.691),<br> by *Rongzhi Zhang, Yue Yu and Chao Zhang*
<br><br>
### Others

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.05578) [**Toward General Design Principles for Generative AI Applications**](https://doi.org/10.48550/arXiv.2301.05578),<br> by *Justin D. Weisz, Michael J. Muller, Jessica He and Stephanie Houde*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2212.12990) [**Unsupervised Representation Learning from Pre-trained Diffusion Probabilistic
Models**](https://doi.org/10.48550/arXiv.2212.12990),<br> by *Zijian Zhang, Zhou Zhao and Zhijie Lin*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6446) [**Parsing as Pretraining**](https://ojs.aaai.org/index.php/AAAI/article/view/6446),<br> by *David Vilares, Michalina Strzyz, Anders S\ogaard and Carlos G\'omez-Rodr\'\iguez*
<br><br>
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6757) [**Unsupervised Deep Learning via Affinity Diffusion**](https://ojs.aaai.org/index.php/AAAI/article/view/6757),<br> by *Jiabo Huang, Qi Dong, Shaogang Gong and Xiatian Zhu*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2009-blue)](https://doi.org/10.1109/CVPR.2009.5206594) [**Learning to detect unseen object classes by between-class attribute
transfer**](https://doi.org/10.1109/CVPR.2009.5206594),<br> by *Christoph H. Lampert, Hannes Nickisch and Stefan Harmeling*
<br><br>

## Related Works

### Git Repos

- [**Awesome-ChatGPT**](https://github.com/dalinvip/Awesome-ChatGPT),<br> ```ChatGPT资料汇总学习，持续更新......```

- [**Awesome ChatGPT Prompts**](https://github.com/f/awesome-chatgpt-prompts),<br> ```In this repository, you will find a variety of prompts that can be used with ChatGPT.```

- [**ChatRWKV**](https://github.com/BlinkDL/ChatRWKV),<br> ```ChatRWKV is like ChatGPT but powered by my RWKV (100% RNN) language model, which is the only RNN (as of now) that can match transformers in quality and scaling, while being faster and saves VRAM. Training sponsored by Stability EleutherAI.```

- [**ChatGPT-Hub**](https://github.com/chenweiphd/ChatGPT-Hub),<br> ```ChatGPT资源汇总```

- [**PaLM-rlhf-pytorch**](https://github.com/lucidrains/PaLM-rlhf-pytorch),<br> ```Implementation of RLHF (Reinforcement Learning with Human Feedback) on top of the PaLM architecture.```

- [**BAAI-WuDao/Data**](https://github.com/BAAI-WuDao/Data),<br> ```“悟道”项目构建了高质量的数据集，用于支撑大模型的训练和测评工作，本仓库提供所有开源数据集的链接。```

- [**Colossal-AI**](https://github.com/hpcaitech/ColossalAI),<br> ```Colossal-AI provides a collection of parallel components for you. We aim to support you to write your distributed deep learning models just like how you write your model on your laptop. We provide user-friendly tools to kickstart distributed training and inference in a few lines.```

### Articles

- [**Exploring Prompt Injection Attacks**](https://research.nccgroup.com/2022/12/05/exploring-prompt-injection-attacks/),<br>by Jose Selvi<br> ```Prompt Injection is a new vulnerability that is affecting some AI/ML models and, in particular, certain types of language models using prompt-based learning.```

- [**ChatGPT发展历程、原理、技术架构详解和产业未来**](https://zhuanlan.zhihu.com/p/590655677?utm_source=wechat_session&utm_medium=social&utm_oi=714896487502315520&s_r=0),<br>by 陈巍<br> ```本文将介绍ChatGPT的特点、功能、技术架构、局限、产业应用、投资机会和未来。作者本人曾担任华为系自然语言处理（ NLP ）企业的首席科学家。```

### Blogs

- [**How does GPT Obtain its Ability?**](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1),<br>by Yao Fu<br> ```Tracing emergent abilities of language models to their sources.```

- [**Open source solution replicates ChatGPT training process**](https://www.hpc-ai.tech/blog/colossal-ai-chatgpt),<br> ```Colossal-AI, as one of the hottest open-source solutions for large AI models, presents an open-source low-cost ChatGPT equivalent implementation process.```

### Demos

- [**CPM-Bee**](https://live.openbmb.org/models/bee),<br> ```CPM-Bee是一个开源的双语预训练语言模型，参数量为10B，拥有十余种原生能力和强大的通用语言能力，并支持结构化输入和输出。```

### Reports

- [**久谦：ChatGPT纪要分享**](https://github.com/KSESEU/LLMPapers/blob/main/res/%E4%B9%85%E8%B0%A6%EF%BC%9AChatGPT%E7%BA%AA%E8%A6%81%E5%88%86%E4%BA%AB.pdf),

- [**国泰君安ChatGPT研究框架**](https://github.com/KSESEU/LLMPapers/blob/main/res/%E5%9B%BD%E6%B3%B0%E5%90%9B%E5%AE%89ChatGPT%E7%A0%94%E7%A9%B6%E6%A1%86%E6%9E%B6.pdf),



## Related Works

### Git Repos

- [**Awesome-ChatGPT**](https://github.com/dalinvip/Awesome-ChatGPT),<br> ```ChatGPT资料汇总学习，持续更新......```

- [**Awesome ChatGPT Prompts**](https://github.com/f/awesome-chatgpt-prompts),<br> ```In this repository, you will find a variety of prompts that can be used with ChatGPT.```

- [**ChatRWKV**](https://github.com/BlinkDL/ChatRWKV),<br> ```ChatRWKV is like ChatGPT but powered by my RWKV (100% RNN) language model, which is the only RNN (as of now) that can match transformers in quality and scaling, while being faster and saves VRAM. Training sponsored by Stability EleutherAI.```

- [**ChatGPT-Hub**](https://github.com/chenweiphd/ChatGPT-Hub),<br> ```ChatGPT资源汇总```

- [**PaLM-rlhf-pytorch**](https://github.com/lucidrains/PaLM-rlhf-pytorch),<br> ```Implementation of RLHF (Reinforcement Learning with Human Feedback) on top of the PaLM architecture.```

- [**BAAI-WuDao/Data**](https://github.com/BAAI-WuDao/Data),<br> ```“悟道”项目构建了高质量的数据集，用于支撑大模型的训练和测评工作，本仓库提供所有开源数据集的链接。```

- [**Colossal-AI**](https://github.com/hpcaitech/ColossalAI),<br> ```Colossal-AI provides a collection of parallel components for you. We aim to support you to write your distributed deep learning models just like how you write your model on your laptop. We provide user-friendly tools to kickstart distributed training and inference in a few lines.```

### Articles

- [**Exploring Prompt Injection Attacks**](https://research.nccgroup.com/2022/12/05/exploring-prompt-injection-attacks/),<br>by Jose Selvi<br> ```Prompt Injection is a new vulnerability that is affecting some AI/ML models and, in particular, certain types of language models using prompt-based learning.```

- [**ChatGPT发展历程、原理、技术架构详解和产业未来**](https://zhuanlan.zhihu.com/p/590655677?utm_source=wechat_session&utm_medium=social&utm_oi=714896487502315520&s_r=0),<br>by 陈巍<br> ```本文将介绍ChatGPT的特点、功能、技术架构、局限、产业应用、投资机会和未来。作者本人曾担任华为系自然语言处理（ NLP ）企业的首席科学家。```

### Blogs

- [**How does GPT Obtain its Ability?**](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1),<br>by Yao Fu<br> ```Tracing emergent abilities of language models to their sources.```

- [**Open source solution replicates ChatGPT training process**](https://www.hpc-ai.tech/blog/colossal-ai-chatgpt),<br> ```Colossal-AI, as one of the hottest open-source solutions for large AI models, presents an open-source low-cost ChatGPT equivalent implementation process.```

### Demos

- [**CPM-Bee**](https://live.openbmb.org/models/bee),<br> ```CPM-Bee是一个开源的双语预训练语言模型，参数量为10B，拥有十余种原生能力和强大的通用语言能力，并支持结构化输入和输出。```

### Reports

- [**久谦：ChatGPT纪要分享**](https://github.com/KSESEU/LLMPapers/blob/main/res/%E4%B9%85%E8%B0%A6%EF%BC%9AChatGPT%E7%BA%AA%E8%A6%81%E5%88%86%E4%BA%AB.pdf),

- [**国泰君安ChatGPT研究框架**](https://github.com/KSESEU/LLMPapers/blob/main/res/%E5%9B%BD%E6%B3%B0%E5%90%9B%E5%AE%89ChatGPT%E7%A0%94%E7%A9%B6%E6%A1%86%E6%9E%B6.pdf),



## Researcher Recruitment 科研人员招聘
*Knowledge Science and Engineering Lab* is recruiting researchers! You are welcome to apply for the following positions:
- **Research Assistant**: Bachelor degree or above, proficient in Python/Java, familiar with machine learning espicially deep learning models.
- **Postdoctoral Fellow**: Doctoral research in Artificial Intelligence, published at least 3 high-quality papers. 
- **Lecturer, Associate Professor and Professor** 

If you are interested in our research and meet the above requirements, feel free to contact Prof. [Guilin Qi](https://cse.seu.edu.cn/2019/0103/c23024a257134/page.htm).

*知识科学与工程实验室*正在招聘科研人员！欢迎申请以下岗位：
- **科研助理**：本科学历以上，精通Python/Java，熟悉机器学习，特别是深度学习模型。
- **博士后**：博士研究人工智能相关方向，发表至少3篇高水平论文。
- **讲师、副教授、教授等教职** 

如果您对我们的研究工作感兴趣并满足以上要求，欢迎您与[漆桂林](https://cse.seu.edu.cn/2019/0103/c23024a257135/page.htm)教授联系。
