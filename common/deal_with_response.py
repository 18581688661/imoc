import allure

def del_with_response(data, res):
    request_url = str(res.request.url)
    allure.attach(request_url, "请求URL")

    request_method = str(res.request.method)
    allure.attach(request_method, "请求方法")

    request_headers = str(res.request.headers)
    allure.attach(request_headers, "请求头")

    request_data = str(data)
    allure.attach(request_data, "入参")

    response_time = str(res.elapsed.total_seconds() * 1000)
    allure.attach(response_time, "响应时间")

    response_code = str(res.status_code)
    allure.attach(response_code, "状态码")

    response_text = str(res.text)
    allure.attach(response_text, "响应内容")
