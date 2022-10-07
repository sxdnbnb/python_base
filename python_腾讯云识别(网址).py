# _*_coding : utf-8 _*_
# @Time : 2022/8/5 16:39
# @Author : SunShine
# @File : python_腾讯云识别
# @Project : python基础_爬虫

import os

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

secretId='AKIDYv1qOhjUzC9pELCNL2UfYAVQ8alhLjqg'
secretKey='bvykFUSAdsrZ0A3f05uSjkUx94j8KK5a'
try:
    cred = credential.Credential(secretId, secretKey)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

    req = models.GeneralFastOCRRequest()
    req.ImageUrl = "https://so.gushiwen.cn/RandCode.ashx"
    resp = client.GeneralFastOCR(req)
    content=resp.to_json_string()

    import json
    content_dict = json.loads(content)
    content_final=content_dict.get('TextDetections')[0].get('DetectedText')
    print(content_final)
    # print(type(content_dict.get('TextDetections')[0])) #字典
    # print(type(content_dict.get('TextDetections')))   #列表
    # print(type(content_dict))                         #字典


except TencentCloudSDKException as err:
    print(err)
