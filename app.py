

<!DOCTYPE html>
<html>
<head>
    <title>Real-time Drawing</title>
    <style>
        #canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="canvas" width="500" height="500"></canvas>
    <button id="clearButton">Clear</button>
    <input type="color" id="colorPicker">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.3.2/socket.io.min.js"></script>
    <script>
        // 连接到后端的WebSocket服务器
        const socket = io.connect('https://aimetaverseserver2.azurewebsites.net/');//http://127.0.0.1:5000/  //https://aimetaverseserver2.azurewebsites.net/

        // 获取画布元素和2D上下文
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        // 定义绘制标志变量
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;
        let currentColor = '#000000';

        // 监听鼠标按下事件
        canvas.addEventListener('mousedown', startDrawing);

        // 监听鼠标移动事件
        canvas.addEventListener('mousemove', draw);

        // 监听鼠标松开和离开画布事件
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mouseout', stopDrawing);

        // 监听清空按钮点击事件
        const clearButton = document.getElementById('clearButton');
        clearButton.addEventListener('click', clearCanvas);

        // 监听颜色选择器变化事件
        const colorPicker = document.getElementById('colorPicker');
        colorPicker.addEventListener('change', updateColor);

        // 开始绘制
        function startDrawing(event) {
            isDrawing = true;
            [lastX, lastY] = [event.offsetX, event.offsetY];

            // 发送起始坐标和颜色到后端
            socket.emit('draw', { type: 'start', x: lastX, y: lastY, color: currentColor });
        }

        // 停止绘制
        function stopDrawing() {
            isDrawing = false;

            // 发送停止信号到后端
            socket.emit('draw', { type: 'stop' });
        }

        // 绘制事件处理
        function draw(event) {
            if (!isDrawing) return;
            updateColor() ;
            const x = event.offsetX;
            const y = event.offsetY;

            // 发送坐标和颜色到后端
            socket.emit('draw', { type: 'draw', x: x, y: y, color: currentColor });

            // 绘制到本地画布
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(x, y);
            ctx.strokeStyle = currentColor;
            ctx.stroke();

            [lastX, lastY] = [x, y];
        }

        // 清空画布
        function clearCanvas() {
            // 清空本地画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 发送清空信号到后端
            socket.emit('draw', { type: 'clear' });
        }

        // 更新当前画笔颜色
        function updateColor() {
            currentColor = colorPicker.value;
            console.log(currentColor);
        }

        // 接收从后端发送过来的坐标并绘制到本地画布
        socket.on('draw', function(data) {
            if (data.type === 'start') {
                [lastX, lastY] = [data.x, data.y];
                currentColor = data.color;
            } else if (data.type === 'draw') {
                const x = data.x;
                const y = data.y;
                const color = data.color;

                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(x, y);
                ctx.strokeStyle = color;
                ctx.stroke();

                [lastX, lastY] = [x, y];
            } else if (data.type === 'stop') {
                isDrawing = false;
            } else if (data.type === 'clear') {
                // 清空本地画布
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
        });
    </script>
</body>
</html>
