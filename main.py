import time
import random

# 需要修改的地方: 请输入您的讯飞星火认知大模型 API 密钥
API_KEY = "3608320494e50122b5b6631839e23914"

def generate_joke():
    # 调用讯飞星火认知大模型 API 来生成笑话
    url = f"ws(s)://spark-api.xf-yun.com/v3.1/chat?text=笑话&apiKey=3608320494e50122b5b6631839e23914"
    response = requests.get(url)
    joke = response.json()["result"]
    return joke

def write_to_file(joke):
    # 获取当前日期
    date_str = time.strftime("%Y%m%d%H%M%S")
    
    # 写入笑话到以当前日期命名的文档中
    with open(f"{date_str}.txt", "w") as f:
        f.write(joke)

def delete_old_file(days_ago):
    # 获取指定天数前的日期
    old_date_str = (datetime.now() - timedelta(days=days_ago)).strftime("%Y%m%d%H%M%S")

    # 删除指定日期的文档
    os.remove(old_date_str + ".txt")

if __name__ == "__main__":
    while True:
        # 生成一个15-30的随机数，表示等待的时间（单位：分钟）
        wait_time = random.randint(15, 30)
        
        # 生成一个笑话
        joke = generate_joke()
        
        # 写入笑话到文件
        write_to_file(joke)
        
        # 等待指定的时间
        time.sleep(wait_time * 60)
        
        # 如果今天是第31天，则删除第1天生成的文档
        if datetime.now().day % 31 == 0:
            delete_old_file(30)
