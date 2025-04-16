from glob import glob
from argparse import ArgumentParser
from pprint import pprint
import json


class KiviExtraction:
    
    def __init__(self):
        self.saved_books = []
        self.get_books_from_json()
 
    def get_authors(self,name):
        if name != 'all':
            for each in self.saved_books:
                if each['author'] == name:
                    return each

    def get_titles(self,specific=None):
        return_list = []
        if specific != None:
            for books in specific['books']:
                    for context in books['context']:
                        if context['title'] not in return_list:
                            return_list.append( context )
            return return_list
        else:
            for books in self.saved_books['books']:
                for context in books['context']:
                    if context['title'] not in return_list:
                        return_list.append(context['title'] )
            return return_list

    def get_context_by_title(self,title):
        return_list = []
        for books in self.saved_books['books']:
            for context in books['context']:
                if context['title'] == title:
                    return_list.append(context)
        return return_list

    def get_books(self,title):
        return_list = []
        for books in self.saved_books['books']:
            if books['booktitle'] == title:
                return_list.append(books)
        return return_list

    def get_authors_books(self):
        pass

    def get_books_from_json(self):
        for file_path in (glob('kivisrc/*.json')):    
            with open(file_path,"r+",encoding="utf-8") as file:
                self.saved_books.append( json.load(file) )


parser = ArgumentParser(description="tamilkavipy",epilog="~~~~~")

parser.add_argument("-a",'--authors',dest="authors",type=str,help="---")
parser.add_argument("-t",'--title',dest="title",type=str,help="---")


args = parser.parse_args()
liberary = KiviExtraction()

global_store = []

if args.authors:
    global_store = liberary.get_authors(args.authors)

if args.title:
    global_store = liberary.get_titles(global_store)
    


pprint(global_store)