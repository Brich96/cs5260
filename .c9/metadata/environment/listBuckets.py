{"filter":false,"title":"listBuckets.py","tooltip":"/listBuckets.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["l"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["i"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["s"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["t"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["B"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["u"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["c"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["k"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["e"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["s"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["."]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["p"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":14},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":14},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":3},{"start":{"row":0,"column":14},"end":{"row":9,"column":12},"action":"insert","lines":["import boto3","","def listClient():","    session = boto3.Session()","    s3_client = session.client('s3')","    b = s3_client.list_buckets()","    for item in b['Buckets']:","        print(item['Name'])","","listClient()"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["listBuckets.pyimport boto3",""],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":5},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":6},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["b"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["o"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"],"id":7},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["3"]}],[{"start":{"row":0,"column":12},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":8}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":12},"end":{"row":9,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1665431956472,"hash":"5fd839676f0ba857b34d817d647b40bed1d2a825"}