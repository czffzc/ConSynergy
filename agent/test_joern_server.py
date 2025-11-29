from cpgqls_client import CPGQLSClient, import_code_query, workspace_query

server_endpoint = "localhost:8080"
basic_auth_credentials = ("username", "password")
client = CPGQLSClient(server_endpoint, auth_credentials=basic_auth_credentials)

# execute a simple CPGQuery
query = "val a = 1"
result = client.execute(query)
print(result)

# execute a `workspace` CPGQuery
query = workspace_query()
result = client.execute(query)
print(result['stdout'])

# execute an `importCode` CPGQuery
query = import_code_query("/Users/feng/Documents/workspace/joern-mcp-server", "my-c-project")
result = client.execute(query)
print(result['stdout'])

# 查询所有调用点
query = "cpg.call.l"
result = client.execute(query)
print(result['stdout'])  # 打印所有调用点

# 查询所有字面量
query = "cpg.literal.l"
result = client.execute(query)
print(result['stdout'])  # 打印所有字面量