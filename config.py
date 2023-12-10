"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "KSESEU"  # github id
author1 = "Shenyu Zhang"  # used in introduction
author2 = "Runzhe Wang"
personal_link1 = r"https://github.com/ZSY-SZ"  # used in introduction
personal_link2 = r'https://github.com/sid0527'
repo_name = "LLMPapers"  # repository name
branch_name = "blob/main"  # branch name
your_research_topic = "llm_papers"  # used for dictionary name
your_research_topic_full_name = "LLMPapers"  # used for title
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV", "VLDB", 'OpenAI', 'ISoLA', 'ACL Findings',
                   'AutoML', 'EMNLP Findings', 'CIKM', 'SIGIR', 'ECIR', 'IA3', 'EDBT', 'Euro-Par', 'ICDCS', 'AIIoT',
                   'ICPADS', 'OSDI', 'ISSTA', 'openreview', 'FSE', 'ICSE', 'MSR', 'WASA', 'ICSME', 'ASE', 'ICER', 'ECML',
                   'CHI', 'EvoMUSART', 'KDD'],

    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."],
        ["FCST", "Journal of Frontiers of Computer Science & Technology"],
        ['JAIR', ' Journal of Artificial Intelligence Research'],
        ['JKSUCIS', ' Journal of King Saud University - Computer and Information Sciences'],
        ['T-PAMI', 'IEEE Transactions on Pattern Analysis and Machine Intelligence'],
        ['NeuroComputing', 'NeuroComputing'],
        ['FLPI', 'Federated Learning: Privacy and Incentive'],
        ['JIS', 'Journal of Information Science'],
        ['TNSE', 'Trans. Netw. Sci. Eng.', 'IEEE Transactions on Network Science and Engineering'],
        ['KIS', 'Knowl. Inf. Syst.', 'Knowledge and Information Systems'],
        ['TIST', 'Trans. Intell. Syst. Technol.'],
        ['JSTSP', 'J. Sel. Top. Signal Process.'],
        ['Applied Sciences', 'Applied Sciences'],
        ['TOIS', 'ACM Transactions on Information Systems'],
        ['JMLR', 'J. Mach. Learn. Res.'],
        ['IJRR', 'Int. J. Robotics Res.']],

    "Preprint": ["arXiv", "CoRR"],

    # 1: resource type
    "Contribution": ["Survey", "Important", "New Settings or Metrics", "New Application",
                     "Empirical Study", "Theory", "New Backbone Model", "New Method", "Thesis", "Library", "Workshop",
                     "Other Type"],
    # 2: Area
    "Area": ["CV", "NLP", "Multi-Modal", "Robotics"],

    # 3: Supervision
    "Supervision": ["Supervised Learning",
                    "Other Learning Paradigm"],

    # 4: Application
    "Application": ["Relation Extraction", "Event Extraction",
                    "Other Application", 'Dialogue State Tracking'],

    # 5: Approach
    "Approach": ["Rehearsal", "Meta-learning", "Other Approach"],

    # 6: Whether you need memory
    "Memory": ["w/ External Knowledge", "w/o External Knowledge"],

    # 7: Setting
    "Setting": ["Class Incremental", "N-way K-shot", "Other Setting"],

    # 8: Research Question
    "RQs": {"Catastrophic Forgetting", "Order Sensitivity", "Few-shot Adaptation", "Others RQs"},

    # 9: Backbone
    "Backbone": ["BERTs", "Transformers", "Adapter", "RNNs", "CNNs", "GNNs", "Attentions", "Capsule Net",
                 "Probabilistic Graphical Model", "VAEs", "Other Structure"],

    # 10: Dataset
    "Dataset": ["Fewrel", "SimpleQuestion", "Tacred",
                "FewEvent",
                "Other Dataset"
                ],

    # 11: Metrics
    "Metrics": ["Accuracy", "F1"],

    "Techniques": ['Evaluation',
                   'Survey',
                   'In-Context Learning', 'Instruction Tuning', 'RLHF',
                   'Pre-Training Techniques', 'Mixtures of Experts',
                   "Knowledge Enhanced", "Knowledge Distillation", 'Knowledge Generation', 'Knowledge Editing',
                   'Reasoning', 'Chain of Thought', 'Multi-Step Reasoning', 'Arithmetic Reasoning', 'Symbolic Reasoning','Chain of Verification','Knowledge Graph Embedding',
                   'Federated Learning', 'Distributed AI',
                   'Selective Annotation',
                   'Program&Code Generation', 'Code Representation', 'Code Fixing', 'Code Review', 'Program Generation',
                   'Software Engineering',
                   'AIGC', 'Controllable Text Generation',
                   "Continual Learning", 'Prompt Engineering', 'Natural Language Understanding',
                   'Multimodal', 'Multilingual',
                   'Reliability',
                   'Robustness',
                   'Dialogue System', 'Recommender System',
                   'Event Extraction', 'Event Relation Extraction',
                   'Data Argumentation', 'Data Annotation', 'Data Visualization',
                   'Information Extraction',
                   'Domain Adaptive',
                   'Question Answering',
                   'Application',
                   'Meta Learning',
                   'Generalizability',
                   'Language Model as Knowledge Base',
                   'Retrieval-Augmented Language Model',
                   'Quality',
                   'Interpretability/Explainability',
                   'Data Generation',
                   'Safety',
                   'Graph Learning',
                   'Knowledge Storage and Locating',
                   'Knowledge Fusion',
                   'Agent',
                   'LLM & GNN',
                   'Others']
}

sub_titles = {'Chain of Thought': 'Reasoning',
              'Multi-Step Reasoning': 'Reasoning',
              'Arithmetic Reasoning': 'Reasoning',
              'Symbolic Reasoning': 'Reasoning',
              'Chain of Verification': 'Reasoning',
              'Knowledge Graph Embedding':'Reasoning',
              'Controllable Text Generation': 'AIGC',
              'Code Representation': 'Program&Code Generation',
              'Code Fixing': 'Program&Code Generation',
              'Code Review': 'Program&Code Generation',
              'Program Generation': 'Program&Code Generation',
              'Mixtures of Experts': 'Pre-Training Techniques'}

plm_url = {
    'BERT': 'https://aclanthology.org/N19-1423/',
    'RoBERTa': 'https://arxiv.org/abs/1907.11692',
    'ELECTRA': 'https://openreview.net/forum?id=r1xMH1BtvB',
    'GPT-1': 'https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf',
    'GPT-2': 'https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf',
    'GPT-3': 'https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html',
    'DeBERTa': 'https://arxiv.org/abs/2006.03654',
    'GPT-Neo': 'https://huggingface.co/docs/transformers/model_doc/gpt_neo',
    'SBERT': 'https://aclanthology.org/D19-1410/',
    'GPT-J': 'https://huggingface.co/docs/transformers/model_doc/gptj',
    'Codex': 'https://arxiv.org/abs/2107.03374',
    'T5': 'http://jmlr.org/papers/v21/20-074.html',
    'OPT': 'https://arxiv.org/abs/2205.01068',
    'PaLM-E': 'https://arxiv.org/abs/2303.03378',
    'GPT-4': 'https://cdn.openai.com/papers/gpt-4.pdf',
    'ChatGPT': 'https://openai.com/blog/chatgpt',
    'InstructGPT': 'https://arxiv.org/abs/2203.02155z'
}
