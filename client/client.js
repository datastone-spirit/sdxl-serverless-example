// write script to request which equal to run following cur command:
//curl -X POST https://api-serverless.datastone.cn/v1/{serverlessID}/sync \
//        -H "Content-Type: application/json" \
//        -H "Authorization: Bearer {apiSecret}" \
//        -d '{"input": { "prompt": "a cute puppy"}}'
// value of serverlessID and apiSecret  read from input button

queuePrompt = async () => {
    console.log("sending request")
    const serverlessID = document.getElementById('serverlessID').value;
    const apiSecret = document.getElementById('apiSecret').value;
    const prompt = document.getElementById('prompt').value;
    if (serverlessID == "" || apiSecret == "" || prompt == "") {
        document.getElementById('message').innerText = "请填写所有字段"
        return
    }

    document.getElementById('message').innerText = "计算中....."
    statusElem = document.getElementById('status')
    statusElem.style.display = "inline-block"
    const response = await fetch(`https://api-serverless.datastone.cn/v1/${serverlessID}/sync`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiSecret}`
        },
        body: JSON.stringify({
            input: { prompt }
        })
    });
    // display the inferencing message in the label
    const data = await response.json();
    statusElem.style.display = "none"
    image = JSON.parse(data);
    document.getElementById('status').setAttribute("style", "display: none;")
    document.getElementById('message').innerText = "结果："
    document.getElementById('result').src = "data:image/png;base64, " + image.image;
}