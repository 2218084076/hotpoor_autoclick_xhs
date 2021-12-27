// alert("");
  // 评论区博主名字


function doit(){
	setTimeout(function(){
		a = document.getElementsByClassName('daren-card')
		for(var i=0;i<list_now.length;i++){
			console.log(a[i].getAttribute('data-item-uid'));
		}
	},5000)
}
doit()


//a=[];console.log(users.length)
//for (i = 0; i<users.length; i++) {
////   console.log(users[i].getAttribute('data-item-uid'));
//a.push(users[i].getAttribute('data-item-uid'))
//}
//console.log(JSON.stringify(a))
