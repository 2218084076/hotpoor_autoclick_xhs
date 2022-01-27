
marker = new AMap.Marker({
			icon: icon,
			position: [lng,lat],
			offset: new AMap.Pixel(-16,-45),
			title: data[i].number,
			map: map
		});
  				
  	   //内容
	   marker.content =  '<div class="info-title">'+data[i].name+" "+data[i].number+" "+'</div><div class="info-content">'+
             			   '可借:'+data[i].rentcount+'<br/>'+
             			   '可还:'+(data[i].restorecount-data[i].rentcount)+'<br/>'+
             			   '</div>'
         marker.on('click', markerClick);