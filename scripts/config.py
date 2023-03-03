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
                   'CHI', 'EvoMUSART'],

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
        ['TOIS', 'ACM Transactions on Information Systems']],

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
                   "Knowledge Enhanced", "Knowledge Distillation", 'Knowledge Graph Generation',
                   'Reasoning', 'Chain of Thought', 'Multi-Step Reasoning', 'Arithmetic Reasoning', 'Symbolic Reasoning',
                   'Federated Learning', 'Distributed AI',
                   'Selective Annotation',
                   'Code Generation', 'Code Representation', 'Code Fixing', 'Code Review',
                   'Software Engineering',
                   'Text Generation', 'Controllable Text Generation',
                   "Continual Learning", 'Prompt Learning', 'Natural Language Understanding',
                   'Multimodal',
                   'Reliability',
                   'Dialogue System', 'Recommender System',
                   'Event Extraction', 'Event Relation Extraction',
                   'Data Argumentation', 'Data Annotation', 'Data Visualization',
                   'Information Extraction',
                   'Domain Adaptive',
                   'Question Answering',
                   'Application',
                   'Meta-Learning',
                   'Others']
}

sub_titles = {'Chain of Thought': 'Reasoning',
              'Multi-Step Reasoning': 'Reasoning',
              'Arithmetic Reasoning': 'Reasoning',
              'Symbolic Reasoning': 'Reasoning',
              'Controllable Text Generation': 'Text Generation',
              'Code Representation': 'Code Generation',
              'Code Fixing': 'Code Generation',
              'Code Review': 'Code Generation',
              'Mixtures of Experts': 'Pre-Training Techniques'}