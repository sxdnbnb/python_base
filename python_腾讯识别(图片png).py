# _*_coding : utf-8 _*_
# @Time : 2022/8/8 16:40
# @Author : SunShine
# @File : python_腾讯识别图片
# @Project : python基础_爬虫
import base64
import os
import sys

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from tencentcloud.ocr.v20181119 import ocr_client
from tencentcloud.ocr.v20181119 import models

secretId='AKIDYv1qOhjUzC9pELCNL2UfYAVQ8alhLjqg'
secretKey='bvykFUSAdsrZ0A3f05uSjkUx94j8KK5a'

cred = credential.Credential(secretId, secretKey)
client = ocr_client.OcrClient(cred, "ap-guangzhou")
req = models.GeneralAccurateOCRRequest()
dirname = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(dirname, "kunling.png"), "rb") as f:
    if sys.version_info[0] == 2:
        # py2 base64 returns str
        content = base64.b64encode(f.read())
    else:
        # py3 base64 returns byte but sdk requires string, so decode it
        content = base64.b64encode(f.read()).decode('utf-8')
req.ImageBase64 = content
try:
    resp = client.GeneralAccurateOCR(req)
    content = resp.to_json_string()
    import json

    content_dict = json.loads(content)
    content_final = content_dict.get('TextDetections')[0].get('DetectedText')
    print(content_final)
except TencentCloudSDKException as e:
    # expected behavior because ocr requires high solution pictures
    assert e.code == 'FailedOperation.UnOpenError'



