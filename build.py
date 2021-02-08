import yaml

from notion.client import NotionClient
from notion.block import *

from urllib.error import HTTPError

from .time_utils import *
from .schema import *

import warnings 
warnings.filterwarnings("ignore")

def logging_time(original_fn):

    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print(f"[{original_fn.__name__}] {end_time-start_time:.1f} sec")
        return result

    return wrapper_fn

# @logging_time
def login(cfg=None): # returns client
    '''
    cfg:
        configuration path or dictionary of config.
        uses default path './config.yml' if None given
    '''

    if isinstance(cfg, str):
        with open(cfg, 'r') as yml:
            config = yaml.load(yml)

    elif isinstance(cfg, dict):
        config = cfg

    elif cfg is None:
        with open('./config.yml', 'r') as yml:
            config = yaml.load(yml)

    else:
        print("Please give .yml path or dictionary")
        return 
        
    token_v2 = config['token_v2']
    client = NotionClient(token_v2=token_v2)
    root = client.get_block(config['url'], force_refresh=True)
    return root, client

# @logging_time
def make_page(root, title=None):
    '''
    root:
        notion.block.PageBlock
        main database notion page
    '''
    if title is None:
        title = 'Run '+today()

    return root.children.add_new(PageBlock, title=title)

# @logging_time
def make_db(page, client=None, **kwargs):
    '''
    page:
        root > page > DB
    '''

    # default values
    fold = None
    schema = get_schema()
    title = 'Untitled'
    view_type = 'table'
    for key, value in kwargs.items():

        if key == 'fold':
            assert(isinstance(value, int))
            fold = value
            title = f'Fold {value}'

        elif key == 'schema':
            if isinstance(value, str):
                schema = get_schema(value)

            elif isinstance(value, dict):
                schema = value

        elif key == 'title':
            assert(isinstance(value, str))
            title = value

        elif key == 'view_type':
            assert(isinstance(value, str))
            view_type = value

        else:
            pass

    db = page.children.add_new(CollectionViewBlock)
    if client is None:
        _, client = login()

    db.collection = client.get_collection(
        client.create_record('collection', parent=db, schema=schema)
    )
    db.title = title
    db.views.add_new(view_type=view_type)
    return db

# @logging_time
def write_db(db, data):

    try:
        row = db.collection.add_row()
        for prop, value in data.items():
            row.__setattr__(prop, value)
    
    except HTTPError as e:
        print(e)
        pass