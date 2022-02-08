# document.getElementsByClassName("product-select-color")[0].getElementsByTagName("span").length
<div>
    <textarea id="xialiwei_20220120_json_check_content"></textarea>
    <button id="xialiwei_20220120_json_check_btn">check</button>
</div>
<script type="text/coffeescript">
check_content_need_create = (base_json,key,value,chat_id)->
    $.ajax
        url:"/api/page/add"
        type:"POST"
        dataType:"json"
        data:
            title:"追踪【#{value}】"
            desc:"追踪【#{value}】描述 品牌"
        success:(data)->
            console.log data
            console.log "已创建了品牌专区"
            if data.info == "ok"
                page_entity_id = data.block_id
                $.ajax
                    url:"/api/page/add_comment"
                    type:"POST"
                    dataType:"json"
                    data:
                        block_id:page_entity_id
                        dom_content: uuid2(6,null)
                    success:(data)->
                        console.log data
                        if data.info == "ok"
                            comment_entity_id = data.comment_entity
                            send_json =
                                "#{key}":value
                                "page_entity_id":page_entity_id
                                "chat_id":comment_entity_id
                            $(".comments_area[data-block=#{chat_id}]>div>textarea.comment_content").val JSON.stringify(send_json)
                            $(".comments_area[data-block=#{chat_id}]>div>button.comment_submit").click()
                            check_content_in_chat base_json,"product-code-value",base_json["product-code-value"],page_entity_id,comment_entity_id,null
                    error:(data)->
                        console.log data
        error:(data)->
            console.log data

check_content_need_add = (base_json,key,value,page_id,chat_id)->
    $.ajax
        url:"/api/page/comment/submit"
        data:
            block_id: BLOCK_ID
            chat_id: chat_id
            content: JSON.stringify(base_json)
            uuid: uuid2(6,null)
        dataType: 'json'
        type: 'POST'
        success:(data)->
            console.log JSON.stringify(data)
            if data.info == "ok"
                console.log data
        error:(data)->
            console.log data

check_content_need_create_and_add = (base_json,key,value,page_id,chat_id)->
    $.ajax
        url:"/api/page/add_comment"
        type:"POST"
        dataType:"json"
        data:
            block_id:page_id
            dom_content: uuid2(6,null)
        success:(data)->
            console.log data
            if data.info == "ok"
                comment_entity_id = data.comment_entity
                base_json["history_json_entity_id"]=comment_entity_id
                check_content_need_add base_json,key,value,page_id,chat_id
                check_content_need_add base_json,key,value,page_id,comment_entity_id

check_content_in_chat = (base_json,key,value,page_id,chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log data
            if data.info == "ok"
                for comment in data.comments
                    comment_json = null
                    try
                        comment_json = JSON.parse(comment[4])
                    catch e
                        continue
                    if comment_json[key] == value
                        console.log comment_json
                        console.log "action",comment_json
                        history_json_entity_id = comment_json["history_json_entity_id"]
                        check_content_need_add base_json,key,value,page_id,history_json_entity_id
                        return
                last_comment_id = data.last_comment_id
                if last_comment_id == null
                    check_content_need_create_and_add base_json,key,value,page_id,chat_id
                    return
                else
                    check_content_in_chat base_json,key,value,page_id,chat_id,last_comment_id
            else
                check_content_need_create_and_add base_json,key,value,page_id,chat_id
        error:(data)->
            console.log data

check_content_in_action = (base_json,key,value,chat_id,comment_id=null)->
    $.ajax
        url:"/api/page/comment/load"
        type:"GET"
        dataType:"json"
        data:
            chat_id:chat_id
            comment_id:comment_id
        success:(data)->
            console.log data
            if data.info == "ok"
                for comment in data.comments
                    comment_json = null
                    try
                        comment_json = JSON.parse(comment[4])
                    catch e
                        continue
                    if comment_json[key] == value
                        console.log comment_json
                        console.log "action",comment_json
                        check_content_in_chat base_json,"product-code-value",base_json["product-code-value"],comment_json["page_entity_id"],comment_json["chat_id"],null
                        return
                last_comment_id = data.last_comment_id
                if last_comment_id == null
                    console.log "need create",value
                    check_content_need_create base_json,key,value,chat_id
                    return
                else
                    check_content_in_action base_json,key,value,chat_id,last_comment_id
            else
                console.log "need create",value
                check_content_need_create base_json,key,value,chat_id
                return
        error:(data)=>
            console.log data
$("body").on "click","#xialiwei_20220120_json_check_btn",(e)->
    check_content = $("#xialiwei_20220120_json_check_content").val()
    check_content_json = null
    try
        check_content_json = JSON.parse(check_content)
    catch e
        alert "content is not json"
        return
    detail_box_title = check_content_json["detail-box-title"]
    check_content_in_action check_content_json,"detail-box-title",detail_box_title,"8125d3358cc143d09d274d67e906b0fa",null
</script>
<script src="/static/js/coffeescript.js"></script>
