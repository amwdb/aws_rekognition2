import base64
import boto3
from cgi import parse_multipart, parse_header
from io import BytesIO

def lambda_handler(event, context):
    print(f"{event=}")
    print(f"{context=}")

    clt = boto3.client("rekognition")

    # body部分にエンコードされた送信データが含まれている
    body = event["body"]
    #print(f"{body=}")
    decoded = base64.b64decode(body)
    #print(f"{decoded=}")
    #改行b"\r\n"バイト型の改行
    #elems = decoded.split(b"\r\n")
    #for elem in elems:
    #    print(elem)
    
    c_type, c_data = parse_header(event['headers']['content-type'])
    assert c_type == 'multipart/form-data'
    decoded_string = base64.b64decode(event['body'])
    #For Python 3: these two lines of bugfixing are mandatory
    #see also: https://stackoverflow.com/questions/31486618/cgi-parse-multipart-function-throws-typeerror-in-python-3
    c_data['boundary'] = bytes(c_data['boundary'], "utf-8")
    c_data['CONTENT-LENGTH'] = event['headers']['content-length']
    form_data = parse_multipart(BytesIO(decoded_string), c_data)
    #print(form_data.keys())
    for image_str in form_data['image']:
        print(image_str)
    
    
    #boto3のclient作成、rekognitionとリージョンを指定
    client = boto3.client('rekognition','ap-northeast-1')
    # rekognitionのdetect_labelsにバイト列を渡してラベル検出実行
    response = client.detect_labels(
        Image={
            'Bytes': image_str
        }
    )
    # 返ってきたresponseからラベル名(Name)と確度(Confidence)を整形して出力
    #for label in response['Labels']:
        #print("{Name:30},{Confidence:.2f}%".format(**label))
    results = []
    for label in response["Labels"]:
        s = "{Name:30},{Confidence:.2f}%".format(**label)
        print(s)
        results.append(s)
    result = "\r\n".join(results)
    return result
