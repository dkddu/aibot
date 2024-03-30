from flask import Flask, request, jsonify
import qwen_api
import ernie_api
import xfyun_api
import moonshot_api
import tiangong_api
import zhipu_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有源访问/api开头的所有路由

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

@app.route('/api/chat', methods=['POST'])
def chat():
    # 获取前端发送的数据
    data = request.get_json()
    user_input = data['message']
    model = data['model']

    # 根据选择的模型生成回复
    if model == 'qwen':
        reply = generate_reply_qwen(user_input)
    elif model == 'ernie':
        reply = generate_reply_ernie(user_input)
    elif model =='xfyun':
        reply = generate_reply_xfyun(user_input)
    elif model =='moonshot':
        reply = generate_reply_moonshot(user_input)
    elif model =='tiangong':
        reply = generate_reply_tiangong(user_input)
    elif model =='zhipu':
        reply = generate_reply_zhipu(user_input)
    else:
        reply = "无效的模型选择"

    # 返回JSON格式的回复
    return jsonify({'reply': reply})

def generate_reply_qwen(user_input):
    # 调用通义千问 API 代码
    reply = qwen_api.generate_reply(user_input)
    return reply

def generate_reply_ernie(user_input):
    # 调用文心一言 API 代码
    reply = ernie_api.generate_reply(user_input)
    return reply

def generate_reply_xfyun(user_input):
    # 调用讯飞星火 API 代码
    reply = xfyun_api.generate_reply(user_input)
    return reply
def generate_reply_moonshot(user_input):
    # 调用月之暗面 API 代码
    reply = moonshot_api.generate_reply(user_input)
    return reply
def generate_reply_tiangong(user_input):
    # 调用天宫AI
    reply = tiangong_api.generate_reply(user_input)
    return reply
def generate_reply_zhipu(user_input):
    # 调用智谱清言
    reply = zhipu_api.generate_reply(user_input)
    return reply
if __name__ == '__main__':
    app.run()