// var socket  = io.connect('http://192.168.0.100:8000');
var socket  = io.connect('192.168.0.103:8000');
var c       = document.getElementById("myCanvas2");
var ctx     = c.getContext("2d");
var cur_XY  = document.getElementById("cur_XY");
var des_XY  = document.getElementById("des_XY");
var js_data;

socket.on('connect', function() {
    console.log("Connected to server")
});

socket.on('coords', data => {
    js_data = JSON.parse(data);
    console.log(`[RECV.]X : ${js_data.x}, Y: ${js_data.y}`)
    cur_XY.innerHTML = `${js_data.x},${js_data.y}`
    ctx.beginPath();
    ctx.arc(js_data.x,js_data.y,10,0,2*Math.PI);
    ctx.strokeStyle = '#fc0303';
    ctx.fillStyle = 'orange';
    ctx.fill();
    ctx.stroke();
});

function ttpX(num) {
    num_new = ((num - 0)/300)*500 + 150;
    return num_new;
}
function ttpY(num) {
    num_new = ((num - 0)/300)*500 + 50;
    return num_new;
}

function canvas_clear() {
    ctx.clearRect(0, 0, 300, 300);
}