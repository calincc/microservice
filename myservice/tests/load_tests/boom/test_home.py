from boom.boom import load, print_stats, print_server_info, print_json

result = load(
    url='http://127.0.0.1:5000/',
    requests=50,
    concurrency=None,
    duration=5,
    method='GET',
    data=None,
    ct='text/plain',
    auth=None,
    headers=None,
    pre_hook=None,
    post_hook=None,
    quiet=True
)

print_server_info(url='http://127.0.0.1:5000/hello', method='GET', headers=None)
print("===============================================================================================================")
print_stats(result)
print("===============================================================================================================")
print_json(result)
