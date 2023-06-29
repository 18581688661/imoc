import json

import pytest
from common.login import login
from common.tools import sep, getprojectpath
from common.mysql_operate import Mysql_operate
import os


@pytest.fixture(scope="function")
def gettoken():
    def _gettoken(user):
        # 判断存放token的目录是否存在，不存在就创建
        token_json_dir = sep([getprojectpath(), "token_dir"])
        if not os.path.exists(token_json_dir):
            print("目录不存在，创建中...")
            os.mkdir(token_json_dir)

        token_json_path = sep([token_json_dir, user + "_token.json"])
        if not os.path.exists(token_json_path):
            res = login(user)
            token = res.json()["data"]["token"]
            print("json文件不存在，创建中")
            with open(token_json_path, "w+") as write_token:
                write_token.write(json.dumps({"token": token}))
            return token
        else:
            # 文件存在则取出token的值
            with open(token_json_path, "r") as token_info:
                print("json文件存在，读取中")
                token = json.loads(token_info.read())
                return token["token"]

    return _gettoken


@pytest.fixture(scope="function")
def get_balance_from_db():
    sql = "select balance from wallet where user_id=3"
    db_balance = Mysql_operate().query(sql)[0][0]
    print(db_balance)
