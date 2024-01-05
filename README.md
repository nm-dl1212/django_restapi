# 概要
djangoのRESTAPIを作成する

# 参考
https://zenn.dev/whitecat_22/articles/f826daf43155cd

https://cloudsmith.co.jp/blog/backend/2023/08/2462017.html

# 使用方法
1. devcontainerで開く
　
2. `.env.org`をコピーして`.env`に書き換える

3. マイグレーションファイルを生成
    ``` bash
    $ python manage.py makemigrations products
    ```

4. マイグレーションを実行し，テーブルを作成する
    ``` bash
    $ python manage.py migrate
    ```

5. 管理ユーザーを作成する。

    (ユーザー名，メールアドレス，パスワードを設定。)
    ``` bash
    $ python manage.py createsuperuser
    ```
    
6. 開発サーバーを起動
    ``` bash
    $ python manage.py runserver
    ```

7. 以下のurlにアクセス。

    `http://localhost:8000/admin/`

    Product>追加と進み，テーブルに適当な要素を追加してみる。
    たとえば，`Name: あんぱん, Price:120, Description": "あんこたっぷり", "review": "Good"`など。

8. APIでデータベースにアクセスしてみる。
    * GET
        ``` bash 
        curl -X GET http://localhost:8000/products/products/

        # 以下のようにレスポンスが返る。"priceWithTax"が計算され，テーブルに追記されているのがポイント。
        # [{"name":"あんぱん","price":120,"description":"あんこたっぷり","review":"Good","priceWithTax":132}]
        ```

    * POST
        ``` bash 
        curl -X POST -H "Content-Type: application/json" -d '{"name": "しょくぱん", "price": 150, "description": "もちもち", "review": "Soso"}' http://localhost:8000/products/products/
        ```

    * DELETE
        ``` bash
        curl -X DELETE http://localhost:8000/products/products/1/
        ```