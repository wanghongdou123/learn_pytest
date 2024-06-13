import yaml
import os.path
import pytest

# 获取项目路径
def get_obj_path():
    # print(os.path.dirname(__file__))
    return os.path.dirname(__file__).split('common')[0]

#
# def write_yaml(key):
#     with open(os.getcwd()+"/extract.yaml", mode='a+', encoding='utf-8') as f:
#         value = yaml.dump(key,stream=f, allow_unicode=True)
#         return value
#
#
# def read_yaml(key):
#     with open(os.getcwd()+"/extract.yaml",mode='r',encoding='utf-8') as f:
#         value = yaml.load(stream=f,Loader=yaml.FullLoader)
#         return value[key]
#
#
# def clear_yaml(yamlpath):
#     with open(get_obj_path()+yamlpath,mode='w',encoding='utf-8') as f:
#         f.truncate()


def read_yaml_testcase(yamlpath):
    with open(get_obj_path()+yamlpath,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        print(value)
        return value



if __name__ == '__main__':
    # print(get_obj_path())
    # print(os.getcwd())
    print(read_yaml_testcase('testcase/my_manage/testapi.yml'))