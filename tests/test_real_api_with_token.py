import pytest
import requests

def test_get_legal_cases(login_token):
    # 使用 login_token 作为依赖注入的参数
    assert login_token != "", "Token 是空的"
    
    # 获取案件的查询接口地址
    url = "http://api.test.metalv.net/api/legal-cases?in_sign=LJ2641000047&limit=10&page=1&show_type=7" 
    
    # 这里的 headers 实际上后续会被封装到底层的 Request 工具类里
    # 现在的用例中只需要专注请求地址和断言逻辑
    headers = {
        "Authorization": f"Bearer {login_token}"  # 修正：使用传入的 login_token
    }
    
    response = requests.get(url, headers=headers)
    res_data = response.json()
    
    print(f"\n接口请求状态码: {response.status_code}")
    print(f"接口部分返回结果: {str(res_data)[:200]}...")  # 打印前 200 个字符防刷屏
    
    # ---------------------------
    # 根据你的需求，进行 3 重断言
    # ---------------------------
    
    # 1. 查询成功（假设成功的 code 是 10000，和登录一样）
    assert res_data["code"] == 10000, f"期望查询成功，实际 code 为 {res_data.get('code')}"
    
    # 2. 查询结果有数据：判断 data 里面的 data 数组长度大于 0
    # 通常分页接口的数据结构是 {"data": {"data": [...]}} 或 {"data": [...]}，保险起见我们通过 len() 判断
    cases_list = res_data["data"]["data"]
    assert len(cases_list) > 0, "期望查询结果有数据，但列表为空"
    
    # 3. 指定数据的 value 断言
    # data.data[0].in_sign的value=LJ2641000047
    first_case_in_sign = cases_list[0]["in_sign"]
    print(f"提取到的第一个案子的 in_sign: {first_case_in_sign}")
    assert first_case_in_sign == "LJ2641000047", f"期望 in_sign 是 LJ2641000047，实际是 {first_case_in_sign}"
    
    print("✅ 该案件查询测试多重断言全部通过！")
