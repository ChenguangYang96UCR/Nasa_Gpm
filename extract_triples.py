import json
import os
import utils

def Extract_triples_from_json(file_path):
    logger =  utils.get_logger()
    if not os.path.isfile(file_path):
        logger.info(file_path + ' does not exist!')
        exit()
    with open(file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        triples = []
        for triple in json_data:
            subject = ''
            relation = ''
            object = ''
            for element in triple:
                # * labels have three type 'Dataset' 'Keyword' 'Platform' 'Publication'
                if element == 'n':
                    if triple[element]['labels'][0] == 'Dataset':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Keyword':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Platform':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Publication':
                        print(triple[element]['labels'][0])
                if element == 'r':
                    print(triple[element][0]['type'])
                if element == 'm':
                    if triple[element]['labels'][0] == 'Dataset':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Keyword':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Platform':
                        print(triple[element]['labels'][0])
                    if triple[element]['labels'][0] == 'Publication':
                        print(triple[element]['labels'][0])
            triples.append([subject, relation, object])
            
            exit()

Extract_triples_from_json('./data/data.json')

# TODO change format of json, string may include some special char(tab) or change line