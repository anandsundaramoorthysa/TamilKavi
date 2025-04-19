from glob import glob
from argparse import ArgumentParser
from pprint import pprint
import json
import sys


class KiviExtraction:
    
    def __init__(self):
        self.saved_books = []
        self.get_books_from_json()
 
    def get_authors(self,name):
        if name != 'all':
            for each in self.saved_books:
                if each['author'] == name:
                    return each

    def get_titles(self,title,specific=None):
        return_list = []
        if title != None:
            if specific != []:
                for books in specific['books']:
                    for context in books['context']:
                        if context['title'] == title:
                            return_list.append(context)
                return return_list
            else:    
                for each_author in self.saved_books:
                    for books in each_author['books']:
                        for context in books['context']:
                            if context['title'] == title:
                                return_list.append(context)
                return return_list
        
    def get_book(self,book,specific=None):
        return_list = []
        match = False
        if book != None:
            if specific != []:
                for books in specific['books']:
                    if books['booktitle'] == book:
                        specific['books'] = [books]
                        match = True
            else:    
                for each_author in self.saved_books:
                    for books in each_author['books']:
                        if books['booktitle'] == book:
                            return_list.append( books['booktitle'] )
                            match = True
        if not match:
            specific['books'] = []
            return specific
        else:
            return specific
         
    def get_books_from_json(self):
        for file_path in (glob('kivisrc/*.json')):    
            with open(file_path,"r+",encoding="utf-8") as file:
                self.saved_books.append( json.load(file) )


parser = ArgumentParser(description="tamilkavipy",epilog="~~~~~")

parser.add_argument("-a",'--authors',dest="authors",default=None,type=str,help="---")
parser.add_argument("-t",'--title',dest="title", default=None,type=str,help="---")
parser.add_argument("-b",'--book',dest="book", default=None,type=str,help="---")
parser.add_argument("-s",'--show',dest="show", default=None,type=str,help="---")

args = parser.parse_args()
liberary = KiviExtraction()

sys_len = int(len(sys.argv)) - 1
global_store = []

if args.authors != None:
    global_store = liberary.get_authors(args.authors)
    sys_len = sys_len - 2
    if sys_len == 0:
        for key,value in global_store.items():
            if not isinstance(value,list):
                print(key," : ",value)
            else:
                all_books_1 = [ v["booktitle"] for v in value]
                print("books : ")
                for index, each_book in enumerate(all_books_1):
                    print("\t",index," : ",each_book)

if args.book != None:
    global_store = liberary.get_book(args.book, global_store)
    sys_len = sys_len - 2
    if sys_len == 0:
        for key,value in global_store.items():
            if not isinstance(value,list):
                print(key," : ",value)
            else:
                all_books_1 = [ v["booktitle"] for v in value]
                print("books : ")
                for index, each_book in enumerate(all_books_1):
                    print("\t",index," : ",each_book)

if args.title != None:
    global_store = liberary.get_titles(args.title, global_store)
    sys_len = sys_len - 2
    if sys_len == 0:
        for each in global_store:
            pprint(each)
   
