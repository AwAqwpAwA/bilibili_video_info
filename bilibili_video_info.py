#哔哩哔哩视频信息
#感谢 https://github.com/SocialSisterYi/bilibili-API-collect 提供API文档!
#bilibili: https://space.bilibili.com/500328587
#github: https://github.com/AwAqwpAwA
#mail: cueavy@163.com/outlook.com
#哔哩哔哩干杯!

import requests , json , time

def T(Time):return time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(Time))#秒级时间戳转字符串

while 1:
    Get="?"
    av_or_bv=input("请输入AV号或BV号>>>")
    if len(av_or_bv) <= 2 :Get+=f"aid={av_or_bv}"#AV
    elif av_or_bv[:2] in ["BV","bv","Bv","bV"]:Get+=f"bvid=BV{av_or_bv[2:]}"#BV
    elif av_or_bv[:2] in ["AV","av","Av","aV"]:Get+=f"aid={av_or_bv[2:]}"#AV
    else:Get+=f"aid={av_or_bv}"#AV
    response=requests.get(f"https://api.bilibili.com/x/web-interface/view{Get}")#调用API
    List=json.loads(response.content)
    if List["code"] != 0:#没有成功加载
        print(List["code"],{-400:"请求错误",-403:"权限不足",-404:"无视频",62002:"稿件不可见",62004:"稿件审核中"}[List["code"]])
        continue
    d=List["data"]
    print(f"""{'==='*30}
标题:{d['title']}
aid: {d['aid']}
bvid: {d['bvid']}
类型: {['自制','搬运'][d['copyright']-1]}
稿件发布时间: {T(d['pubdate'])}
用户投稿时间: {T(d['ctime'])}
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