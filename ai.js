let currentModel = 'qwen'; // 默认模型

// 选择模型（修改为处理下拉框的change事件）
function selectModel(model) {
    currentModel = model;
}

// 初始化页面时设置默认模型
document.addEventListener('DOMContentLoaded', function () {
    var modelSelect = document.getElementById('model-select');
    modelSelect.value = 'qwen';
    currentModel = modelSelect.value;
});

// 发送消息到后端
function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const requestData = {
    message: userInput,
    model: currentModel
    };

    fetch('http://localhost:5000/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
    // 处理后端返回的回复
    const reply = data.reply;
    displayMessage('ai', reply);
    displayMessage('user', userInput);
    document.getElementById('user-input').value = '';
    })
    .catch(error => {
    console.error('Error:', error);
    });
}

// 显示消息
function displayMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add(`${sender}-message`);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 更新背景图片
function updateBackground(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function() {
    document.body.style.backgroundImage = `url(${reader.result})`;
    }
    reader.readAsDataURL(file);
}