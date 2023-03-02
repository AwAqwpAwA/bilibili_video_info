#哔哩哔哩视频信息
#感谢 https://github.com/SocialSisterYi/bilibili-API-collect 提供API文档!
#bilibili: https://space.bilibili.com/500328587
#github: https://github.com/AwAqwpAwA
#mail: cueavy@163.com/outlook.com
#哔哩哔哩干杯!

import Core

while 1:
    List=Core.Video_info(input("请输入AV/BV号>>>"))
    if List['code'] != 0 :
        print(f"{List['code']} {Core.error_code[List['code']]}")
        continue
    d=List['data']
    print(f"""{'==='*30}
标题:{d['title']}
aid: {d['aid']}
bvid: {d['bvid']}
类型: {['自制','搬运'][d['copyright']-1]}
稿件发布时间: {Core.T(d['pubdate'])}
用户投稿时间: {Core.T(d['ctime'])}
播放数: {d['stat']['view']}
弹幕数: {d['stat']['danmaku']}
评论数: {d['stat']['reply']}
收藏数: {d['stat']['favorite']}
投币数: {d['stat']['coin']}
分享数: {d['stat']['share']}
获赞数: {d['stat']['like']}
点踩数: {d['stat']['dislike']}
当前排名: {d['stat']['now_rank']}
历史最高排行: {d['stat']['his_rank']}
封面: {d['pic']}
简介: 
{'---'*30}
{d['desc']}
{'---'*30}
作者: {d['owner']['name']}
作者UID: {d['owner']['mid']}
作者头像: {d['owner']['face']}
{'==='*30}""")