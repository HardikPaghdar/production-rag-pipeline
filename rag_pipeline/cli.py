import argparse,json
from .core import load,query
def main():
    p=argparse.ArgumentParser(description='Query a local text knowledge base')
    p.add_argument('path'); p.add_argument('question'); p.add_argument('--limit',type=int,default=5)
    a=p.parse_args(); print(json.dumps(query(a.path,a.question,a.limit),indent=2))
if __name__=='__main__': main()
