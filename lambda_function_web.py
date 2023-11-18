#html表示用
def lambda_handler(event, context):

    with open("index.html", 'r') as source_file: #画像含むバイナリの時はrb,テキストファイル場合はrのみ
        source_code = source_file.read()

    # TODO implement
    return {
        'statusCode': 200,
        'body': source_code,
        "headers": {
            'Content-Type': 'text/html'
        }
    }
    
