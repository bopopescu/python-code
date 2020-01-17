#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-23 15:51
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py.py
import requests

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.text)
    print('-------- HTTP response * end -------\n\n')

imgdata={

    'images': [('123.png', open('123.png', 'rb'), 'image/png')]



}
headers={

'Authorization':'8apKVotLM9oPH17',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
data2={
# 'page':0
# 'id':83,
#     'cate_id':6
#     'page':1,
# 'cate_id':6,
# 'search_name':'香烟礼盒'
# 'cart_num':22
'goods_id':143,


'goods_attr':'1:1',

'goods_attr_val':'红色+休闲',


'cart_num':1,

'goods_sku_id':12


}
data1={
# 'id':13,
# 'order_status':1
# 'ate_id':18
# 'id':145
'goods_id':144,
# 'attr_val':'1:1'
# 'goods_num':123456,
#
# 'attr_val':'1:1',
#
# 'sku':50,
#
# 'is_kill':0,
#
# 'kill_sku':1

}
data={

'goods_number':100123,
'goods_name':"6G手机",
'goods_images':'http://api.ing.com',
'goods_size_price':360,
'goods_price':400,
'goods_stock':20,
'goods_cate_id':3,
'goods_content':"手机中的战斗机",
'is_sale':'yes',
'is_kill':1,
'start_time':'2019.12.25 10:28',
'end_time':'2019.12.30 10:28',
'kill_price':300


}
data3={

'goods_id':144,

'goods_name':"粉玫瑰小花束",

'goods_thumb':'https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/nfpmz01580v7a61l9u2orik3esb2x9j5.jpeg',

'goods_attr':'1:1',

'goods_attr_val':'1:1',

'goods_num':'1',

'memo':'测试数据',

'sku_id':'12',

'oods_price':'38.00'


}
#添加分类
url="http://tuangou.woooge.cn/admin/Cate/add"
# 获取分类列表
url1="http://tuangou.woooge.cn/admin/Cate/cate_list"
# 属性列表
url2="http://tuangou.woooge.cn/admin/Attribute/attribute_list"
# 添加编辑商品属性
url3="http://tuangou.woooge.cn/admin/Attribute/add"
#商品属性---添加/编辑商品属性值
url4="http://tuangou.woooge.cn/admin/Attribute/add_attr_val"
# 商品属性---根据属性得到属性值
url5="http://tuangou.woooge.cn/admin/Attribute/get_attr_val"
# 商品属性---删除商品属性值
url6="http://tuangou.woooge.cn/admin/Attribute/del_attr_val"
# 商品分类----给分类添加/编辑属性
url7="http://tuangou.woooge.cn/admin/Cate/add_cate_attr"
# 商品--添加/编辑
url8="http://tuangou.woooge.cn/admin/Goods/add"
# 商品-----商品列表
url9="http://tuangou.woooge.cn/admin/Goods/index"

# 商品----商品详情
url10="http://tuangou.woooge.cn/admin/Goods/detail"
# 商品-----添加商品库存
url11="http://tuangou.woooge.cn/admin/Goods/addGoodSku"
# 商品----删除商品库存
url12="http://tuangou.woooge.cn/admin/Goods/deleteGoodsSku"
# 商品---删除商品
url13="http://tuangou.woooge.cn/admin/Goods/delete_goods"

# 订单列表
url14="http://tuangou.woooge.cn/admin/Order/orderList"
# 修改订单状态
url15="http://tuangou.woooge.cn/admin/Order/change_order_status"
# 用户列表 User/user_order
url16="http://tuangou.woooge.cn/admin/User/user_order"
# 图片上传
url17="http://tuangou.woooge.cn/admin/Goods/upload_images"
# 分类商品
url18="http://tuangou.woooge.cn/Api/Goods/get_cate_goods"
# 商品详情

url19='http://tuangou.woooge.cn/Api/Goods/get_goods_content'
# 根据规格获取库存
url20='http://tuangou.woooge.cn/Api/Goods/getsku'
# 加入购物车
url21='http://tuangou.woooge.cn/Api/Goods/addcart'
# 登录
url22='http://tuangou.woooge.cn/Api/Login/login'
# 购物车详情
url23='http://tuangou.woooge.cn/Api/Goods/cart_list'
# 修改购物车数量
url24='http://tuangou.woooge.cn/Api/Goods/cart_num'
# 删除购物车
url25='http://tuangou.woooge.cn/Api/Goods/cart_delete'
# 直接购买
url26='http://tuangou.woooge.cn/Api/Order/create_order'
# 购物车下单购买
url27='http://tuangou.woooge.cn/Api/Order/add_order_cart'
# 选中购物车商品
url28='http://tuangou.woooge.cn/Api/Goods/cart_check'
# 取消订单
url29='http://tuangou.woooge.cn/Api/Order/cancel_order'
# 订单详情
url30='http://tuangou.woooge.cn/Api/Order/order_detail'
# 个人中心 /Api/User/profile
url31='http://tuangou.woooge.cn/Api/User/profile'
# 积分明细列表
url32='http://tuangou.woooge.cn/Api/User/integralList'
# 我的订单
url33='http://tuangou.woooge.cn/Api/Order/get_order_list'
# 意见反馈
url34='http://tuangou.woooge.cn/Api/User/addfeedback'
data5={

'id':83,
"is_check":1
# 'is_check':0
# "order_id":"27"
# 'page':0,
# 'order_status':0
#     'content':"6666666"
# 'page':1
}
response = requests.post(url26,data=data3,headers=headers)


printResponse(response)
# {"code":1,"msg":"success","time":1577243298,"data":[{"id":145,"goods_number":"0001","goods_name":"粉百合","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20191105\/6b51eht72437nkdp4s3m80u86lx9yavr.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20191105\/6b51eht72437nkdp4s3m80u86lx9yavr.jpeg","goods_size_price":null,"goods_price":"50.00","goods_stock":0,"goods_cate_id":0,"goods_cate_child":0,"goods_content":"<p>双头粉百合10枝<\/p>","is_sale":1,"sale_time":1572925939,"create_time":1572925939,"update_time":1572925939,"listorder":1,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20191105\/6b51eht72437nkdp4s3m80u86lx9yavr.jpeg"]},{"id":99,"goods_number":"0002","goods_name":"米奇之爱","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/l3bf4oaxz02i52up49w73867n8chyq1t.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/l3bf4oaxz02i52up49w73867n8chyq1t.jpeg","goods_size_price":null,"goods_price":"258.00","goods_stock":0,"goods_cate_id":7,"goods_cate_child":0,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578061185097.jpg\" title=\"1564578061185097.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578050245600.jpg\" title=\"1564578050245600.jpg\" alt=\"0002米奇之爱.jpg\"\/><\/p>","is_sale":1,"sale_time":1568452167,"create_time":1564578071,"update_time":1568452167,"listorder":2,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":2,"attr_val":"蓝色"},{"id":5,"attr_val":"紫色"}]},{"attr_val":[{"id":3,"attr_val":"休闲款"},{"id":4,"attr_val":"运动款"}]}],"goods_attr_sku":[{"id":5,"goods_id":99,"goods_num":null,"attr_val":"1:1","sku":"30.00","freeze_sku":null,"status":1}],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/l3bf4oaxz02i52up49w73867n8chyq1t.jpeg"]},{"id":102,"goods_number":"0005","goods_name":"女王","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7c85iqamz21359l319y8g6te4kfbo0r0.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7c85iqamz21359l319y8g6te4kfbo0r0.jpeg","goods_size_price":null,"goods_price":"358.00","goods_stock":0,"goods_cate_id":7,"goods_cate_child":0,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578292181305.png\" title=\"1564578292181305.png\" alt=\"0005女王2.png\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578283821985.png\" title=\"1564578283821985.png\" alt=\"0005女王.png\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578304813197.jpg\" title=\"1564578304813197.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p>","is_sale":1,"sale_time":1568453662,"create_time":1564578317,"update_time":1568453662,"listorder":5,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":2,"attr_val":"蓝色"},{"id":5,"attr_val":"紫色"}]},{"attr_val":[{"id":3,"attr_val":"休闲款"},{"id":4,"attr_val":"运动款"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7c85iqamz21359l319y8g6te4kfbo0r0.jpeg"]},{"id":103,"goods_number":"0006","goods_name":"公主","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/y3m9k6z6tw240h2ax9pv1885ircu1d75.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/y3m9k6z6tw240h2ax9pv1885ircu1d75.jpeg","goods_size_price":null,"goods_price":"288.00","goods_stock":0,"goods_cate_id":7,"goods_cate_child":0,"goods_content":"<p><strong><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578393962777.jpg\" title=\"1564578393962777.jpg\" alt=\"0006公主.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578402373405.jpg\" title=\"1564578402373405.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/strong><br\/><\/p>","is_sale":1,"sale_time":1568454112,"create_time":1564578408,"update_time":1568454112,"listorder":6,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":2,"attr_val":"蓝色"},{"id":5,"attr_val":"紫色"}]},{"attr_val":[{"id":3,"attr_val":"休闲款"},{"id":4,"attr_val":"运动款"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/y3m9k6z6tw240h2ax9pv1885ircu1d75.jpeg"]},{"id":105,"goods_number":"0008","goods_name":"甜美可人","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190809\/nes286c1042q9z9jmv4lx05fp6dait57.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190809\/nes286c1042q9z9jmv4lx05fp6dait57.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190809\/9r8siv9mt28yajwp56udb4chfgqxe71o.jpeg","goods_size_price":null,"goods_price":"188.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":0,"goods_content":"<p><br\/><\/p><p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190809\/1565358181644759.jpg\" title=\"1565358181644759.jpg\" alt=\"绣球花束粉.jpg\"\/><\/p><p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190809\/1565358195319920.jpg\" title=\"1565358195319920.jpg\" alt=\"绣球花束粉2.jpg\"\/><\/p><p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578624382923.jpg\" title=\"1564578624382923.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p>","is_sale":1,"sale_time":1568463542,"create_time":1564578637,"update_time":1568463542,"listorder":8,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190809\/nes286c1042q9z9jmv4lx05fp6dait57.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190809\/9r8siv9mt28yajwp56udb4chfgqxe71o.jpeg"]},{"id":106,"goods_number":"0009","goods_name":"素颜","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7w09ycrbh6vje57m36s34kt0p825qfd8.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7w09ycrbh6vje57m36s34kt0p825qfd8.jpeg","goods_size_price":null,"goods_price":"168.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":0,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578703842862.jpg\" title=\"1564578703842862.jpg\" alt=\"009素颜.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190731\/1564578715365048.jpg\" title=\"1564578715365048.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p>","is_sale":1,"sale_time":1568463494,"create_time":1564578722,"update_time":1568463494,"listorder":9,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190731\/7w09ycrbh6vje57m36s34kt0p825qfd8.jpeg"]},{"id":20,"goods_number":"EGDR01","goods_name":"厄瓜多尔七彩玫瑰","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190629\/08nza3l9f4rp1e7sjm69g5whu1824o6i.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190629\/08nza3l9f4rp1e7sjm69g5whu1824o6i.jpeg","goods_size_price":null,"goods_price":"1088.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":12,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190629\/1561773297171771.jpg\" title=\"1561773297171771.jpg\" alt=\"厄瓜多尔玫瑰_副本.jpg\" width=\"417\" height=\"409\" style=\"width: 417px; height: 409px;\"\/><\/p><p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190726\/1564129815576897.jpg\" title=\"1564129815576897.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p><p><br\/><\/p>","is_sale":1,"sale_time":1564130075,"create_time":1561773314,"update_time":1564130075,"listorder":101,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190629\/08nza3l9f4rp1e7sjm69g5whu1824o6i.jpeg"]},{"id":22,"goods_number":"103","goods_name":"你若安好","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190914\/u1a09ti5dfwzlhk2yx8o43vj0728gcp3.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190914\/u1a09ti5dfwzlhk2yx8o43vj0728gcp3.jpeg","goods_size_price":null,"goods_price":"268.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":12,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190914\/1568463173345713.jpg\" title=\"1568463173345713.jpg\" alt=\"103.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190727\/1564203736786769.jpg\" title=\"1564203736786769.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p>","is_sale":1,"sale_time":1568463223,"create_time":1561774996,"update_time":1568463223,"listorder":103,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190914\/u1a09ti5dfwzlhk2yx8o43vj0728gcp3.jpeg"]},{"id":96,"goods_number":"104","goods_name":"爱心藤编花束","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/p3ym190oh80u9xzc6l1dki5fqg4s7r4t.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/p3ym190oh80u9xzc6l1dki5fqg4s7r4t.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/68zgsyrw10hbd74ac3nul8t21pm460e9.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/glsj83bdyv98x5c463ani421p0fkqt1m.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/b9fk62pl2og7wiyrs7481e5q3th395xv.jpeg","goods_size_price":null,"goods_price":"208.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":12,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190728\/1564317999786188.jpg\" title=\"1564317999786188.jpg\" alt=\"104_副本.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190728\/1564317992870811.jpg\" title=\"1564317992870811.jpg\" alt=\"104_副本 (3).jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190728\/1564317984679710.jpg\" title=\"1564317984679710.jpg\" alt=\"104_副本 (2).jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190728\/1564318022731248.jpg\" title=\"1564318022731248.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><\/p>","is_sale":1,"sale_time":1568463385,"create_time":1564318036,"update_time":1568463385,"listorder":104,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/p3ym190oh80u9xzc6l1dki5fqg4s7r4t.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/68zgsyrw10hbd74ac3nul8t21pm460e9.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/glsj83bdyv98x5c463ani421p0fkqt1m.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190728\/b9fk62pl2og7wiyrs7481e5q3th395xv.jpeg"]},{"id":131,"goods_number":"105","goods_name":"粉玫瑰满天星圆形花束","goods_thumb":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/hua71efm075g2156ti3jl4869c42zkxy.jpeg","goods_images":"https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/hua71efm075g2156ti3jl4869c42zkxy.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/z6tug3hv59690dsk7ci818lbm2pj27wy.jpeg","goods_size_price":null,"goods_price":"288.00","goods_stock":0,"goods_cate_id":6,"goods_cate_child":12,"goods_content":"<p><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190917\/1568714709293005.jpg\" title=\"1568714709293005.jpg\" alt=\"微信图片_20190726155437_副本2.jpg\"\/><img src=\"https:\/\/tuangou.woooge.cn\/ueditor\/php\/upload\/image\/20190917\/1568714666161188.jpg\" title=\"1568714666161188.jpg\" alt=\"105_副本.jpg\"\/><\/p>","is_sale":1,"sale_time":1568714713,"create_time":1568714713,"update_time":1568714713,"listorder":105,"status":1,"is_kill":1,"start_time":null,"end_time":null,"kill_price":null,"goods_attr":[{"attr_val":[{"id":6,"attr_val":"20"},{"id":8,"attr_val":"60"}]}],"goods_attr_sku":[],"images":["https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/hua71efm075g2156ti3jl4869c42zkxy.jpeg@wiyoo@https:\/\/kala.wugee.xyz\/uploads\/Goods\/20190917\/z6tug3hv59690dsk7ci818lbm2pj27wy.jpeg"]}]}
