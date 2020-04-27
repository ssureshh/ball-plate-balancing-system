// var socket  = io.connect('http://192.168.0.100:8000');
var socket  = io.connect('192.168.0.103:8000');
var c       = document.getElementById("myCanvas3");
var ctx     = c.getContext("2d");
var cur_XY  = document.getElementById("cur_XY");
var des_XY  = document.getElementById("des_XY");
var js_data;

socket.on('connect', function() {
    console.log("Connected to server")
});

socket.on('coords', data => {
    js_data = JSON.parse(data);

    new_x = pttX(js_data.x);
    new_y = pttY(js_data.y);
    new_x = Math.round(new_x);
    new_y = Math.round(new_y); 

    // console.log(`[RECV.- PLATE ]X : ${new_x}, Y: ${new_y}`)
    //console.log(`[RECV.]X : ${js_data.x}, Y: ${js_data.y}`)

    cur_XY.innerHTML = `${js_data.x},${js_data.y}`
    ctx.beginPath();
    ctx.arc(new_x,new_y,10,0,2*Math.PI);
    ctx.stroke();
});


function getMousePosition(canvas, event) { 
    let rect = canvas.getBoundingClientRect(); 
    let x = event.clientX - rect.left;
    let y = event.clientY - rect.top; 
    x = Math.round(x);
    y = Math.round(y); 

    console.log("Coordinate x: " + x,  
                "Coordinate y: " + y); 

    new_x = ttpX(x);
    new_y = ttpY(y);
    new_x = Math.round(new_x);
    new_y = Math.round(new_y); 
    
    console.log("Coordinate x: " + new_x, "Coordinate y: " + new_y); 
    des_XY.innerHTML = `${new_x},${new_y}`

    socket.emit('des_event', {"x":new_x, "y":new_y});
    ctx.clearRect(0, 0, 300, 300);
    ctx.beginPath();
    ctx.arc(x,y,20,0,2*Math.PI);
    ctx.fillStyle = 'orange';
    ctx.fill();
    ctx.stroke();
} 
let canvasElem = document.querySelector("canvas"); 
canvasElem.addEventListener("mousedown", function(e) 
{ 
    getMousePosition(canvasElem, e); 
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
function pttX(num) {
    num_new = ((num - 20)/730)*300;
    return num_new;
}
function pttY(num) {
    num_new = ((num - 10)/590)*300;
    return num_new;
}