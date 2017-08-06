# # -*- coding: utf-8 -*-
# import glob
# import json
# import sys
# import urllib2
#
# from poster.encode import multipart_encode, MultipartParam
# from poster.streaminghttp import register_openers
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# # 服务器地址
# _server_path = "http://www.eccpos.com"
#
# # 磁盘图片路径
# _file_path = "E:\\imgupload\\error\\"
#
# # 用于记录异常路径
# _img_record = ""
#
#
# def upload_img(img_path):
#     try:
#         print "正在上传" + img_path
#         # 在 urllib2 上注册 http 流处理句柄
#         register_openers()
#
#         url = _server_path + "/DocCenterService/upload"
#
#         # 开始对文件 "***.jpg" 的 multiart/form-data 编码
#         # "image1" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置
#
#         # headers 包含必须的 Content-Type 和 Content-Length
#         # datagen 是一个生成器对象，返回编码过后的参数
#         filename = img_path.split('\\')[-1]
#         barcode = filename.split('_')[0]
#         file_dr = img_path.split('.')[-1]
#         # 此处目的是为了处理文件名称长度过长，上传至文档中心时，字段超长报错的问题
#         files = MultipartParam('file', filename=barcode + '.' + file_dr, fileobj=open(img_path, "rb"))
#         datagen, headers = multipart_encode(
#             {"file": files, "uid": "superadmin", "folder_id": "5557555", "type": "image",
#              "default_place": "weibo"})
#
#         # 创建请求对象
#         request = urllib2.Request(url, datagen, headers)
#
#         # 实际执行请求并取得返回
#         rtn_str = urllib2.urlopen(request).read()
#         print rtn_str
#         dict_obj = json.loads(rtn_str)
#         photo_id = dict_obj['photo_id']
#
#         # 图片上传后的的url
#         rtn_img_path = _server_path + "/DocCenterService/image?photo_id=" + str(photo_id)
#         print img_path + " 已经上传完成！url为" + rtn_img_path
#
#         # 记录上传后的url 以barcode,img_url为标识
#         record_upload_log("upload.csv", barcode + ',' + rtn_img_path)
#         # 记录已经上传的图片文件路径
#         record_upload_log("has_upload.log", img_path)
#         # 记录已经上传的文件sql
#         img_par = "'" + rtn_img_path + "'"
#         barcode_par = "'" + barcode + "'"
#         update_sql = "UPDATE PUB_GOODSINFO SET IMG_PATH= " + img_par + " WHERE BARCODE= " + barcode_par + " AND IMG_PATH <> '' AND IMG_PATH IS NOT NULL;"
#         record_upload_log("PUB_GOODSINFO.sql", update_sql)
#
#         update_mall_sql = "UPDATE PUB_MALLGOODSINFO SET IMG_PATH= " + img_par + " WHERE BARCODE= " + barcode_par + " AND IMG_PATH <> '' AND IMG_PATH IS NOT NULL;"
#         record_upload_log("PUB_MALLGOODSINFO.sql", update_mall_sql)
#
#         print img_path + " 记录日志完成"
#
#     except Exception as e:
#         print e
#         # 异常文件可记可不计 断点上传不根据此记录实现
#         record_upload_log("error.log", img_path)
#
#
# # 记录上传文件记录
# def record_upload_log(file_path, content):
#     with open(file_path, "a+", 2) as file_obj:
#         content = unicode(content)
#         file_obj.write(content)
#         file_obj.write('\n')
#
#
# # 从Log文件读每个图片在磁盘上的路径 返回barcode
# def read_img_file_path_dict(file_path):
#     img_path_dict = {}
#     with open(file_path, "a+", 2) as file_obj:
#         for line in file_obj:
#             filename = line.split('\\')[-1]
#             barcode = filename.split('_')[0]
#             img_path_dict[barcode] = line
#     return img_path_dict
#
#
# # 取图片文件完整路径
# def get_img_path():
#     all_img_path_set = set()
#
#     path = _file_path + "\\*".decode('utf-8')
#     for filename in glob.glob(path):
#         # all_img_path_set.add(filename.encode('utf-8').decode('cp936'))
#         all_img_path_set.add(filename)
#     return all_img_path_set
#
#
# # 断点上传实现 返回
# def go():
#     try:
#         # 已经上传的数据
#         has_upload_dict = read_img_file_path_dict('has_upload.log')
#
#         # 全部数据
#         all_img_path_set = get_img_path()
#
#         has_upload_num = len(has_upload_dict)
#         print_str = "已经上传图片" + str(has_upload_num) + "张"
#         print print_str
#
#         all_img_num = len(all_img_path_set)
#         print_str = "全部图片" + str(all_img_num) + "张"
#         print print_str
#
#         sy_img_num = all_img_num - has_upload_num
#         print_str = "剩余上传图片" + str(sy_img_num) + "张"
#         print print_str
#
#         for img_path in list(all_img_path_set):
#             global _img_record
#             _img_record = img_path
#             filename = img_path.split('\\')[-1]
#             barcode = filename.split('_')[0]
#             if has_upload_dict.get(barcode) is None:
#                 upload_img(img_path)
#                 sy_img_num -= 1
#                 print "剩余图片" + str(sy_img_num) + "张"
#
#     except Exception, e:
#         print e
#         record_upload_log("error.log", _img_record)
#
#
# if __name__ == '__main__':
#     go()
#     #print get_img_path()
