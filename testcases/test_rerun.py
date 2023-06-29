# import random
#
#
# class TestMy:
#     def testmy(self):
#         num=random.randint(1,3)
#         print("num:",num)
#         if num!= 1:
#             print("失败")
#             raise Exception("出错了")
#         else:
#             print("成功")


import pytest


@pytest.fixture()
def setup_database():
    print("Setting up database...")
    yield
    print("Tearing down database...")


# @pytest.mark.usefixtures("setup_database")
# def test_query_data():
#     print("Querying data from database...")


@pytest.mark.usefixtures("setup_database")
class TestDatabase:
    @pytest.mark.run(order=2)
    def test_insert_data(self):
        print("Inserting data into database...")

    @pytest.mark.run(order=3)
    def test_update_data(self):
        print("Updating data in database...")
