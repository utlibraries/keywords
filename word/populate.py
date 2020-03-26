from django.conf import settings


class Populator(object):

    @staticmethod
    def create_dict(form_data):
        new_dict = {'topic': form_data['topic'], 'concepts': []}
        for x in range(4):
            if form_data['concept{}'.format(x+1)]:
                new_dict['concepts'].append({'concept': form_data['concept{}'.format(x+1)], 'keyconcepts': []})
                for key, value in form_data.items():
                    if 'concept{}_keyword'.format(x+1) in key and value != '':
                        new_dict['concepts'][x]['keyconcepts'].append(value)
        new_dict['max_words'] = len(new_dict['concepts'])
        return new_dict

    @staticmethod
    def create_query(raw_query):
        query_string = ""
        for index, concept in enumerate(raw_query['concepts']):
            if index != 0:
                query_string += '+AND+'
            query_string += '('
            query_string += concept['concept']
            for c in concept['keyconcepts']:
                query_string += '+OR+' + c
            query_string += ')'
        search_link = {'catalog': settings.CATALOG_LINK + query_string + settings.CATALOG_SUFFIX,
                       'academic': settings.ACADEMIC_SEARCH_LINK + query_string,
                       'jstor': settings.JSTOR_LINK + query_string,
                       'query_string': query_string
                       }
        return search_link