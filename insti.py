institutions = ['ETH', 'EPFL', 'IBM','Stanford','MIT','Toronto','NVIDIA']

def get_institutions_complete_name():
    institutions = [
    'ETH Zurich',
    'EPFL',
    'IBM',
    'Stanford Univrsity',
    'MIT',
    'University of Toronto',
    'NVIDIA',
    'Google',
    'Berkeley',
    'Caltech',
    'Microsoft',
    'Carnegie Mellon',
    'University of Cambridge',
    'University of Oxford',
    'Princeton',
    'Georgia Tech',
    'University of Washington',
    'University of Texass at Austin',
    'Duke University',
    'Facebook',
    'Twitter',
    'Columbia University',
    'Harvard University',
    'Imperial College',
    'University of Michigan',
    'University of California, San Diego',
    'New York University',
    'Peking University',
    'Cornell University',
    'University of Minnesota',
    'University of Virginia',
    'Weizmann Institue of Science',
    'TUM',
    'Universita di Roma',
    'Universita di Pisa',
    'Politecnico di Milano',
    'Politecnico di Torino',
    'Universidad de Madrid',
    'Universidad de Barcelona',
    'Politecnica de Catalunya',
    'Universitat Politecnica de Valencia',
    'Universite de Paris',
    'Universite de Rennes',
    'Universite de Marseille',
    'University of Athens',
    'Apple',
    'Universitat Berlin',
    'University of Vienna',
    'University of Graz',
    'University of Konstanz',
    'TU Delft',
    'KTH Stockholm',
    'University od Singapore',
    'Nanyang Tech',
    'Nanyang Techn',
    'University of Hong Kong',
    'University of Montreal',
    'Hangzhou University',
    'Shenzhen University',
    'University of Adelaide',
    'University of Cardiff',
    'Northwestern Polytechnic University',
    'Tianjin University',
    'UCAS',
    'Keio University',
    'Nagoya University',
    'University of Tokyo',
    'University of Kyoto',
    'University of Sydney',
    'University of Melbourne',
    'Adobe',
    'Disney',
    'Technicolor',
    'Zhejiang University',
    'Northwestern Polytechnic University',
    'Xiamen University',
    'Tsinghua University',
    'University of Seul',
    'University of Delhi',
    'University of Seattle',
    'University of Massachusetts',
    'University of Osaka',
    'Nanjing University',
    'University of Shanghai',
    'Zhejiang University'
    ]
    return institutions

def get_institutions_list():
    institutions = [
    'ETH',
    'EPFL',
    'IBM',
    'Stanford',
    'MIT',
    'Toronto',
    'NVIDIA',
    'Google',
    'Berkeley',
    'Caltech',
    'Microsoft',
    'Carnegie',
    'DeepMind',
    'Cambridge',
    'Oxford',
    'Princeton',
    'Georgia',
    'Washington',
    'Austin',
    'Duke',
    'Facebook',
    'Twitter',
    'Columbia',
    'Harvard',
    'Imperial',
    'Michigan',
    'UCSD',
    'York',
    'Peking',
    'Beijing',
    'Cornell',
    'Minnesota',
    'Virginia',
    'Weizmann',
    'Munich',
    'Roma',
    'Pisa',
    'Milan',
    'Torino',
    'Madrid',
    'Barcelona',
    'Catalunya',
    'Valencia',
    'Paris',
    'Rennes',
    'Marseille',
    'Athens',
    'Apple',
    'Berlin',
    'Vienna',
    'Graz',
    'Konstanz',
    'Delft',
    'KTH',
    'Singapore',
    'Nanyang',
    'NTU',
    'Hong',
    'Montreal',
    'Hangzhou',
    'Shenzhen',
    'Adelaide',
    'Cardiff',
    'Northwestern',
    'Tianjin',
    'UCAS',
    'Keio',
    'Nagoya',
    'Tokyo',
    'Kyoto',
    'Sydney',
    'Melbourne',
    'Adobe',
    'Disney',
    'Technicolor',
    'Zhejiang',
    'NPU',
    'Xiamen',
    'Tsinghua',
    'Seul',
    'Delhi',
    'Seattle',
    'Massachusetts',
    'Osaka',
    'Nanjing',
    'Shanghai',
    'Zhejiang'
    ]
    return institutions





def get_institutions(tokens):

    institutions = get_institutions_list()
    nb_institutions = len(institutions)
    institutions_counter = [0] * nb_institutions
    try:
        index_abstract = tokens.index('Abstract')
    except ValueError:
        print('ValueError inside get_institutions')
        return institutions_counter
    first_words = tokens[:index_abstract]  
    previous_index = []
    for w in first_words:
        if w in institutions:
            index = institutions.index(w)
            if index not in previous_index:
                institutions_counter[index] += 1
                previous_index += [index]
    return institutions_counter