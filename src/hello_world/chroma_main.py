import chromadb

headers= {"host": "chroma.cn-shanghai.alb.aliyuncsalb.com" }
# client = chromadb.HttpClient(host='alb-k3be64v8cuzhlhksl0.cn-shanghai.alb.aliyuncsslb.com', port=80,
#                              # ssl=False)
# client = chromadb.HttpClient(host='47.117.189.172', port=80)
client = chromadb.HttpClient(host='47.117.35.119', port=80)
# client = chromadb.HttpClient(host='chroma-service', port=8000)
# client = chromadb.HttpClient(host='192.168.195.197', port=8000) # service
# client = chromadb.HttpClient(host='172.16.1.201', port=8000) # VIP

try:
    # 尝试创建一个集合, 这一步可验证连接后能否正常执行操作
    collection = client.create_collection(
        name="test_collection",
        metadata={"hnsw:space": "cosine"}
    )
    print("成功连接到Chroma DB, 并且能够创建集合。")
except Exception as e:
    print(f"连接或操作失败, 错误信息: {e}")

# 添加这行代码用于查看所有的collection
collections = client.list_collections()
print("当前所有的collection:", collections)
