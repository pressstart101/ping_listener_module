arr = [];
window.setInterval(function(){
    
    $.get('/api/ping.json', (data) => {



        if(data){
            let len = data.length;
            let txt = "";
            let cur_val = ""
            

            if(len > 0){
                for(let i=0;i<len;i++){
                    if(data[i].time && data[i].source_ip){
                        txt = "<tr><td>"+data[i].time+"</td><td>"+data[i].source_ip+"</td></tr>";
                        cur_val = {"time":data[i].time, "ip":data[i].source_ip}
                        
                    }
                }
                if(txt != ""){
                    arr.push(cur_val)
                    let latest = arr.slice(Math.max(arr.length - 5, 0));

                    //   }
                    txt = ""
                    for(let i=0;i<latest.length;i++){
                        txt += `<tr><td>${latest[i].time}</td><td>${latest[i].ip}</td></tr>`
                    }
                    $("#table_body").html(txt);
                    
                    
                }
            }
            let latest = arr.slice(Math.max(arr.length - 5, 0))
            
        }


    });
}, 1000);