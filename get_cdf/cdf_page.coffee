add_page = (name)->
    do ->
        $.aiax
            url:"/api/page/add"

            data:
                box-title = "cdf海南免税店_#{name}"
            dataType:"json"
            type: 'POST'
            success:(data) ->
                console.log data
                if data.info == "ok"
                    page_entity_id = data.block_id

                    $.ajax
                        url:""
                        type:"POST"
                        dataType:"json"
                        data:
                            block_id:page_entity_id

                        success:(data) ->
                            console.log data
                            if data.info == "ok"
                                comment_entity_id = data.comment_entity

                                send_json =
                                    "#{key}":value
                                    "page_entity_id":page_entity_id
                                    "chat_id":comment_entity_id
                                $(.comments_area[data-block=#{chat_id}]>div>textarea.comment_content)

check_content = (aim_str,find_now=false,comment_id=null)->
    do ()->
        $.ajax
            url:"/api/page/comment/load"
            data:
                chat_id: chat_id
                comment_id: comment_id
                time_now: (new Date()).getTime()
            dataType: 'json'
            type: 'GET'

            success:(data)->
                console.log data
                if data.info !="ok"
                    console.log "data_info_ok"
                    console.log data
                    
                for i in data.comments
                    console.log aim_str,JSON.parse(i[4])["box-title"],JSON.parse(i[4])["box-title"] == aim_str
                    if JSON.parse(i[4])["box-title"] == aim_str
                        result = [true,JSON.parse(i[4])]
                        console.log "https://www.qianshanghua.com/home/page/#{JSON.parse(i[4])["page_entity"]}"
                        find_now = true
                        break
                if find_now == true
                    return result_next_action(result)
                if data.last_comment_id == null
                    return result_next_action(result)
                check_str aim_str,false,data.last_comment_id
            error:(data)->
                console.log "false"
                console.log data

$("body").on "click","#wlb_2022_01_19_check_value_check",(evt)->
    dom = $("#wlb_2022_01_19_check_value")
    dom_json = JSON.parse dom.val()
    console.log dom_json["detail-box-title"]
    check_content dom_json["detail-box-title"],false,null
