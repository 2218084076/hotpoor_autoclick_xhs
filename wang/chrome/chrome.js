// create node for user interface
 
var new_node = document.createElement('div');
new_node.innerHTML = `
<button id="A" onclick="clickA()">a</button>
`;
 
// inject new node
 
var target_node = document.querySelector('...');
target_node.parentNode.insertBefore(new_node, target_node);
 
// functions
 
function clickA() {
    alert('1');
}