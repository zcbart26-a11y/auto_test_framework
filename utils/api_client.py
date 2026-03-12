# utils/api_client.py
import requests

class APIClient:
    """
    API 接口的底层封装类 (类似于 UI 自动化里的 BasePage)
    这里封装通用的请求头、域名，以及 GET/POST 方法。
    业务用例直接调用这个类，不需要自己去写 requests.get()
    """
    
    # 假设这是你们公司的测试域名
    BASE_URL = "http://api.test.metalv.net"
    
    def __init__(self, token=None):
        # 初始化一个带有持久会话的 session
        self.session = requests.Session()
        
        # 封装默认公共头部
        headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "AutoTest-Framework/1.0"
        }
        # 如果传了 token，就把鉴权也一并加上
        if token:
            headers["Authorization"] = f"Bearer {token}"
            
        self.session.headers.update(headers)
        
    def _send_request(self, method, endpoint, **kwargs):
        """
        内部的私有发送方法。
        endpoint: 接口的具体路径，比如 /api/login
        """
        # 自动把域名和路径拼起来
        url = f"{self.BASE_URL}{endpoint}"
        print(f"\n[APIClient] 正在发送 {method} 请求到: {url}")
        
        # 拦截发出的请求，如果需要记录日志，都在这里统一写！
        if "json" in kwargs:
            print(f"[APIClient] 请求参数: {kwargs['json']}")
        if "params" in kwargs:
            print(f"[APIClient] 请求参数: {kwargs['params']}")
            
        # 真正的发送请求动作
        response = self.session.request(method, url, **kwargs)
        
        print(f"[APIClient] 响应状态码: {response.status_code}")
        # 这里统一捕获解析 JSON 时可能出现的异常，防止代码直接炸掉
        try:
            return response.json()
        except Exception:
            return {"error": "返回的不是合法 JSON 格式", "text": response.text}

    # === 下面暴露出给外部用的便捷方法 ===
    
    def get(self, endpoint, params=None, **kwargs):
        return self._send_request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, json_data=None, **kwargs):
        return self._send_request("POST", endpoint, json=json_data, **kwargs)
