# LLM Papers & Related Works
This repository is maintained by [Shenyu Zhang](https://github.com/ZSY-SZ) & [Runzhe Wang](https://github.com/sid0527). The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

This page categorizes the literature by the **Last Post**.

## Papers

### Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time\README.md#hyperlink)
- [![](https://img.shields.io/badge/2023-4-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time\README.md#2023)
- [![](https://img.shields.io/badge/2022-17-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time\README.md#2022)
- [![](https://img.shields.io/badge/2020-1-blue)](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time\README.md#2020)
### Hyperlinks 
- [[Overview]](https://github.com/KSESEU/LLMPapers/blob/main/README.md) -- [Homepage](https://github.com/KSESEU/LLMPapers/blob/main/README.md)
-  -- [Summary](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/./)
-  -- [Application](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/application)
-  -- [Approach](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/approach)
-  -- [Author](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/author)
-  -- [Backbone Model](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/backbone_model)
-  -- [Contribution](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/contribution)
-  -- [Dataset](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/dataset)
-  -- [Metrics](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/metrics)
-  -- [Research Questions](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/research_question)
-  -- [Setting](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/setting)
-  -- [ Learning Paradigm](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/supervision)
-  -- [Published Time](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/time)
-  -- [Published Venue](https://github.com/KSESEU/LLMPapers/blob/main/taxonomy/venue)

### 2023

- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.04023) [**A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning,
Hallucination, and Interactivity**](https://doi.org/10.48550/arXiv.2302.04023) , <br> by *Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu and Pascale Fung*
<br>```本文提出了一个使用公开数据集定量评估交互式LLM（如ChatGPT）的框架。我们使用涵盖8个不同的常见NLP应用任务的21个数据集对ChatGPT进行了广泛的技术评估。我们基于这些数据集和一个新设计的多模态数据集评估了ChatGPT的多任务、多语言和多模态方面。我们发现ChatGPT在大多数任务上优于zero-shot学习的LLM，甚至在某些任务上优于微调的模型。我们发现它更擅长于理解非拉丁字母语言而不是生成它们。它能够通过中间代码生成步骤从文本提示生成多模态内容。此外，我们发现ChatGPT在逻辑推理、非文本推理和常识推理这10个不同的推理类别中，平均准确率为64.33%，因此它是一个不可靠的推理器。例如，它比归纳推理更擅长演绎推理。ChatGPT像其他LLM一样遭受幻觉问题，并且由于它不能访问外部知识库，它从其参数记忆中产生更多的外部幻觉。最后，ChatGPT的交互特性使人能够与底层的LLM协作，以改进其性能，例如，以多回合“即时工程”的方式，8%的ROUGE-1用于摘要，2%的ChrF++用于机器翻译。```<br><br>
- [![](https://img.shields.io/badge/EACL-2023-blue)](https://doi.org/10.48550/arXiv.2301.12810) [**Crawling the Internal Knowledge-Base of Language Models**](https://doi.org/10.48550/arXiv.2301.12810) , <br> by *Roi Cohen, Mor Geva, Jonathan Berant and Amir Globerson*
<br>```本文提出一种从语言模型中提取结构化知识图谱的方法；使用专门设计的提示来控制提取过程中的精度和召回率；在GPT-3上进行了评估，显示了高精确度的结果。 TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2301.00303) [**Rethinking with Retrieval: Faithful Large Language Model Inference**](https://doi.org/10.48550/arXiv.2301.00303) , <br> by *Hangfeng He, Hongming Zhang and Dan Roth*
<br>```本文通过用GPT-3在三个复杂的推理任务：常识推理，时间推理和表格推理上进行大量实验来评估RR的有效性。结果表明，RR可以产生更忠实的解释，并提高LLM的性能。TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2023-blue)](https://doi.org/10.48550/arXiv.2302.00923) [**Multimodal Chain-of-Thought Reasoning in Language Models**](https://doi.org/10.48550/arXiv.2302.00923) , <br> by *Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis and Alex Smola*
<br><br>
### 2022

- [![](https://img.shields.io/badge/ACL-2022-blue)](https://doi.org/10.18653/v1/2022.acl-long.53) [**Meta-learning via Language Model In-context Tuning**](https://doi.org/10.18653/v1/2022.acl-long.53) , <br> by *Yanda Chen, Ruiqi Zhong, Sheng Zha, George Karypis and He He*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.12810) [**Code4Struct: Code Generation for Few-Shot Structured Prediction from
Natural Language**](https://doi.org/10.48550/arXiv.2210.12810) , <br> by *Xingyao Wang, Sha Li and Heng Ji*
<br><br>
- [![](https://img.shields.io/badge/CVPR-2022-blue)](https://doi.org/10.1109/CVPR52688.2022.00024) [**Learning to Prompt for Continual Learning**](https://doi.org/10.1109/CVPR52688.2022.00024) , <br> by *Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer G. Dy and Tomas Pfister*
<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://doi.org/10.48550/arXiv.2203.08568) [**In-Context Learning for Few-Shot Dialogue State Tracking**](https://doi.org/10.48550/arXiv.2203.08568) , <br> by *Yushi Hu, Chia-Hsuan Lee, Tianbao Xie, Tao Yu, Noah A. Smith and Mari Ostendorf*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://doi.org/10.48550/arXiv.2205.12673) [**Improving Zero and Few-shot Generalization in Dialogue through Instruction
Tuning**](https://doi.org/10.48550/arXiv.2205.12673) , <br> by *Prakhar Gupta, Cathy Jiao, Yi-Ting Yeh, Shikib Mehri, Maxine Esk\'enazi and Jeffrey P. Bigham*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/EMNLP-2022-blue)](https://arxiv.org/abs/2202.12837) [**Rethinking the Role of Demonstrations: What Makes In-Context Learning
Work?**](https://arxiv.org/abs/2202.12837) , <br> by *Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi and Luke Zettlemoyer*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2210.07128) [**Language Models of Code are Few-Shot Commonsense Learners**](https://doi.org/10.48550/arXiv.2210.07128) , <br> by *Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang and Graham Neubig*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.167) [**Do Prompt-Based Models Really Understand the Meaning of Their Prompts?**](https://doi.org/10.18653/v1/2022.naacl-main.167) , <br> by *Albert Webson and Ellie Pavlick*
<br><br>
- [![](https://img.shields.io/badge/NAACL-2022-blue)](https://doi.org/10.18653/v1/2022.naacl-main.201) [**MetaICL: Learning to Learn In Context**](https://doi.org/10.18653/v1/2022.naacl-main.201) , <br> by *Sewon Min, Mike Lewis, Luke Zettlemoyer and Hannaneh Hajishirzi*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2209.12356) [**News Summarization and Evaluation in the Era of GPT-3**](https://doi.org/10.48550/arXiv.2209.12356) , <br> by *Tanya Goyal, Junyi Jessy Li and Greg Durrett*
<br><br>
- [![](https://img.shields.io/badge/NeurIPS-2022-blue)](https://doi.org/10.48550/arXiv.2210.09338) [**Deep Bidirectional Language-Knowledge Graph Pretraining**](https://doi.org/10.48550/arXiv.2210.09338) , <br> by *Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang and Jure Leskovec*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2209.01975) [**Selective Annotation Makes Language Models Better Few-Shot Learners**](https://doi.org/10.48550/arXiv.2209.01975) , <br> by *Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf, Luke Zettlemoyer, Noah A. Smith and Tao Yu*
<br><br>
- [![](https://img.shields.io/badge/VLDB-2022-blue)](https://www.vldb.org/pvldb/vol15/p1466-li.pdf) [**Selective Data Acquisition in the Wild for Model Charging**](https://www.vldb.org/pvldb/vol15/p1466-li.pdf) , <br> by *Chengliang Chai, Jiabin Liu, Nan Tang, Guoliang Li and Yuyu Luo*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2212.09420) [**When Neural Model Meets NL2Code: A Survey**](https://doi.org/10.48550/arXiv.2212.09420) , <br> by *Daoguang Zan, Bei Chen, Fengji Zhang, Dianjie Lu, Bingchao Wu, Bei Guan, Yongji Wang and Jian-Guang Lou*
<br><br>
- [![](https://img.shields.io/badge/TKDE-2022-blue)](https://doi.org/10.48550/arXiv.2212.13428) [**A Survey on Knowledge-Enhanced Pre-trained Language Models**](https://doi.org/10.48550/arXiv.2212.13428) , <br> by *Chaoqi Zhen, Yanlei Shang, Xiangyu Liu, Yifei Li, Yong Chen and Dell Zhang*
<br>```TODO: Update URL when formally published```<br><br>
- [![](https://img.shields.io/badge/FCST-2022-blue)](https://doi.org/10.3778/j.issn.1673-9418.2108105) [**Review of Knowledge-Enhanced Pre-trained Language Models**](https://doi.org/10.3778/j.issn.1673-9418.2108105) , <br> by *Yi, HAN, Linbo, QIAO, Dongsheng, LI and Xiangke, LIAO*
<br><br>
- [![](https://img.shields.io/badge/CoRR-2022-blue)](https://doi.org/10.48550/arXiv.2211.09110) [**Holistic Evaluation of Language Models**](https://doi.org/10.48550/arXiv.2211.09110) , <br> by *Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang Yuan, Bobby Yan, Ce Zhang, Christian Cosgrove, Christopher D. Manning, Christopher R\'e, Diana Acosta-Navas, Drew A. Hudson, Eric Zelikman, Esin Durmus, Faisal Ladhak, Frieda Rong, Hongyu Ren, Huaxiu Yao, Jue Wang, Keshav Santhanam, Laurel J. Orr, Lucia Zheng, Mert Y\"uksekg\"on\"ul, Mirac Suzgun, Nathan Kim, Neel Guha, Niladri S. Chatterji, Omar Khattab, Peter Henderson, Qian Huang, Ryan Chi, Sang Michael Xie, Shibani Santurkar, Surya Ganguli, Tatsunori Hashimoto, Thomas Icard, Tianyi Zhang, Vishrav Chaudhary, William Wang, Xuechen Li, Yifan Mai, Yuhui Zhang and Yuta Koreeda*
<br><br>
### 2020

- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/6446) [**Parsing as Pretraining**](https://ojs.aaai.org/index.php/AAAI/article/view/6446) , <br> by *David Vilares, Michalina Strzyz, Anders S\ogaard and Carlos G\'omez-Rodr\'\iguez*
<br><br>