import os
from os.path import exists

if __name__ == '__main__':

	run_all = False

	if not exists('jsonnn'):
		os.mkdir('jsonnn')

	json_files = [f'{i}.json' for i in range(1, 395)]
	file_exist = [file in os.listdir('./jsonnn/') for file in json_files]

	if not all(file_exist):
		from jsonconverter import jsonconverter
		print('Running jsonconverter.py')
		jsonconverter()
		run_all = True

	if not exists('savers'):
		os.mkdir('savers')

	json_files = ['authors_list.json', 'category.json', 'document_tokens_list.json', 'vocabulary.json', \
					'primeDictionary.json', 'normaliseddenom.json', 'score.json']

	file_exist = {file: file in os.listdir('./savers/') for file in json_files}

	if run_all or not file_exist['category.json'] or not file_exist['authors_list.json']:
		from store_categories_authors import create_author_category
		print('Running store_categories_authors.py')
		create_author_category()
		run_all = True

	if run_all or not file_exist['document_tokens_list.json']:
		from store_document_tokens_list import create_document_tokens_list
		print('Running store_document_tokens_list.py')
		create_document_tokens_list()
		run_all = True

	if run_all or not file_exist['vocabulary.json']:
		from store_vocabulary import compute_vocabulary
		print('Running store_vocabulary.py')
		compute_vocabulary()
		run_all = True

	if run_all or not file_exist['primeDictionary.json']:
		from store_megadict import create_megadict
		print('Running store_megadict.py')
		create_megadict()
		run_all = True

	if run_all or not file_exist['normaliseddenom.json'] or not file_exist['score.json']:
		from document_normalized_denominator import compute_denominator
		print('Running document_normalized_denominator.py')
		compute_denominator()
		run_all = True

	print('Running final_gui.py')
	from final_gui import run_gui
	run_gui()