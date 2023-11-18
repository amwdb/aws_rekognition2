#rekognition解析用
import boto3

def lambda_handler(event, context):
    print(event)
    # -*- coding: utf-8 -*-
    #boto3のclient作成、rekognitionとリージョンを指定
    client = boto3.client('rekognition','ap-northeast-1')
    picture_sample ='dog01.jpg'
    # 画像ファイルを読み込んでバイト列を取得
    with open(picture_sample, 'rb') as source_image:
        source_bytes = source_image.read()

    # rekognitionのdetect_labelsにバイト列を渡してラベル検出実行
    response = client.detect_labels(
       Image={
           'Bytes': source_bytes
       }
    )

    # 返ってきたresponseからラベル名(Name)と確度(Confidence)を整形して出力
    for label in response['Labels']:
        print("{Name:30},{Confidence:.2f}%".format(**label))
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
