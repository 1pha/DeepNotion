# DeepNotion

`Kor`   
딥러닝 프로젝트 규모가 커지기 시작하면 변수나 손실함수, 성능 등의 기록이 남기고 보관하는 것이 문제가 됩니다. 집에서 혼자 뚱땅뚱땅 거리면 상관 없지만 이게 연구라면 더더욱... 그렇다고 새롭게 DB를 배우고 싶진 않고 내가 그나마 잘 쓰는 건 노션 뿐인데라는 생각에서 시작된 Deep Learning 기록을 Notion DB에 넘기기 프로젝트를 하게 되었습니다. 프로젝트라니까 거창한데 그냥 결과물 노션에 보내는 겁니다. 생각 보다 간단하네요.

`Eng`   
As your deep learning project gets larger, it's hard to keep track of all the parameters, hyperparameters, loss e.t.c. If project is on your own, it's fine but when it comes to bigger project... Since I didn't want to learn another database languages and only thing I can use is Notion, I came up with the idea of sending those data to the notion database! More simple than you think. Give it a try!

## Usage
0. **Install `notion`**
   ```bash
   pip install notion
   ```
1. **Make Configuration File (config.yml)**
   + yaml file that contains `token_v2`
   + This token can be found with Chrome - F12 - Applications - token_v2 - Copy!
     + Don't show your token to anyone...!
2. **Prepare Data and Schema**
    + They should be `dict` type
    + _Schema_ columns of Database
       ```python
       schema = {
           'PROPERTY': {'name': 'PROPERTY', 'type': 'text'}
           ...
           # e.g.
           'title': {'name': 'Epoch', 'type': 'text'}
           'loss' : {'name': 'Loss (MAE)', 'type': 'number'}
       }
       ```
       * Note that value of the `'name'` will show up on your notion page, not `'PROPERTY'`
       * Figuring out the difference between those... To change the database, you need to call them with their `'name'`. (Thought it was alias but some types doesn't change the value)
       * Look [here](./schema.py) to see sample schemas.
       * I'll update list of `'type'`s... I asked the original 

    + _Data_ Data you want to wrtie on the db
      ```python
      data = {
          'NAME': 'VALUE',
          ...
          # e.g.
          'Epoch': '1',
          'Loss (MAE)': 3.4,
      }
      ```
      * Name of the keys should match the `'name'` from your schema!
3. **Run below**
    ```python
    root, client = login(cfg) # LOGIN. dictionary of config or path of your .yml
    page = make_page(root, title=title) # PAGE OF COLLECTED DBs. title is optional
    db = make_db(page, schema=schema) # DB, schema is optional!
    write_row(db, data) # WRITE ROWS ON THE DB
    ```
This will give   
```bash
root # (url in the config)
└- page # (made with make_page)
    └- db # (made with make_db)
        data
```
