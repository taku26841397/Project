from datetime import datetime

import requests
import json
import datetime
import time



for i in range(0,100):
    # We define a row that matches the schema we described earlier
    nowt=datetime.datetime.now()
    timestamp_ms=int(nowt.timestamp()*1000)
    #print(timestamp_ms)
    test="Test"+str(i)
    sample_data = {"timestamp":timestamp_ms,"value":test}
    post_uri = "https://honda.palantirfoundry.com/stream-proxy/api/streams/ri.foundry.main.dataset.e24f2163-e573-4e5c-a410-d7d9035b3a3a/views/ri.foundry-streaming.main.view.2047f250-c019-49bc-adbd-ba323b06d106/jsonRecords"

    # We use requests to create a post request with an array of streaming rows, in this case we have one row to push
    response = requests.post(
        post_uri,
        data=json.dumps([{"value": sample_data}]),
        headers={
            "Authorization": "Bearer " + FOUNDRY_TOKEN,
            "Content-Type": "application/json",
        }
    )
    print(i)
    print(response.status_code, response.reason, response.text)

    time.sleep(10)