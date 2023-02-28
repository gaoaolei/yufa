q = [{
                "id": 70749,
                "qk_id": 4777,
                "parent_id": 0,
                "sub_id": [],
                "name": "商户可在哪里查看到平台通知",
                "answer": [
                    236549,
                    236543
                ],
                "analysis": "首页工作台及企业中心中均可查看到平台相关通知",
                "selects": [
                    236543,
                    236545,
                    236547,
                    236549
                ],
                "tags": [],
                "type": "multiple",
                "media_type": 1,
                "media": [],
                "score": 0,
                "wrong_count": 675,
                "done_count": 2354,
                "creator": "awangjingwen_v",
                "updator": "awangjingwen_v",
                "delete_flag": 1,
                "created_at": "2022-11-24T06:35:27.000Z",
                "updated_at": "2022-11-30T11:36:28.000Z",
                "option": [
                    {
                        "id": 236543,
                        "name": "首页工作台",
                        "sort": 0
                    },
                    {
                        "id": 236545,
                        "name": "司机管理",
                        "sort": 1
                    },
                    {
                        "id": 236547,
                        "name": "司机数据",
                        "sort": 2
                    },
                    {
                        "id": 236549,
                        "name": "企业中心",
                        "sort": 3
                    }
                ],
                "right_answer": [
                    236543,
                    236549
                ],
                "ok": "true"
            },
            {
                "id": 70751,
                "qk_id": 4777,
                "parent_id": 0,
                "sub_id": [],
                "name": "可以代他人申请权限吗？",
                "answer": [
                    236551
                ],
                "analysis": "代他人申请权限并不违反权限最小化原则",
                "selects": [
                    236551,
                    236553
                ],
                "tags": [],
                "type": "single",
                "media_type": 1,
                "media": [],
                "score": 0,
                "wrong_count": 890,
                "done_count": 2237,
                "creator": "awangjingwen_v",
                "updator": "awangjingwen_v",
                "delete_flag": 1,
                "created_at": "2022-11-24T06:35:27.000Z",
                "updated_at": "2022-11-30T11:36:27.000Z",
                "option": [
                    {
                        "id": 236551,
                        "name": "可以",
                        "sort": 0
                    },
                    {
                        "id": 236553,
                        "name": "不可以",
                        "sort": 1
                    }
                ],
                "right_answer": [
                    236551
                ],
                "ok": "true"
            }]

for i in q:
    print(i['name'])
    for j in i['option']:
        if j['id'] in i['right_answer']:
            print(j['name'])