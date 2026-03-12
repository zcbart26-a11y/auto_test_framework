# tests/api/test_legal_cases_api.py
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """
    我们将获取 Token 和初始化基础 Client 的动作结合。
    以后所有的 API 用例，直接拿这个 client 去 get/post
    """
    print("\n[Fixture] 初始化 API 客户端并执行登录...")
    # 第一步：用一个没有 Token 的 client 去登录
    login_client = APIClient() 
    login_res = login_client.post("/api/login", json_data={
        "username": "15511111111",
        "password": "aa123456"
    })
    
    token = login_res["data"]["token"]
    print(f"[Fixture] 拿到全局 Token: {token[:15]}...")
    
    # 第二步：创建一个带 Token 的真实业务 Client
    # 以后别的测试用例直接 yield 这个带了 token 满级装备的 Client！
    auth_client = APIClient(token=token)
    yield auth_client

# ==================================
# 下面是真正的业务测试用例
# ==================================

def test_legal_cases_search(api_client):
    """
    查询案件列表的接口测试。
    你看！没有任何长长的 URL 域名拼接，没有任何 Headers！极简！
    """
    print("\n--- 开始执行 test_legal_cases_search ---")
    
    # 业务参数
    params = {
        "in_sign": "LJ2641000047",
        "limit": 10,
        "page": 1,
        "show_type": 7
    }
    
    # 一句话发送请求！
    # (底层自动拼好 http.../api/legal-cases，自动加上 Token 和日志)
    res_data = api_client.get("/api/legal-cases", params=params)
    
    # 业务断言
    assert res_data["code"] == 10000
    
    cases_list = res_data["data"]["data"]
    assert len(cases_list) > 0, "期望查询结果有数据，但列表为空"
    
    first_case_in_sign = cases_list[0]["in_sign"]
    print(f"提取到的第一个案子的 in_sign: {first_case_in_sign}")
    assert first_case_in_sign == "LJ2641000047"
    
    print("✅ 用例层极简代码测试完成！")
