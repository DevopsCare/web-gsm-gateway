# web-gsm-gateway
Initiate calls on your behalf from web. Used for GSM activated gates and barriers

### Usage
Update `template.yaml` with your data. Provision template with [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html#serverless-getting-started-hello-world-deploy)

```shell
sam deploy --guided
```

### DynamoDB records format

```json
{
  "id": {
    "S": "1_elm_plumber"
  },
  "owner": {
    "S": "Fred C"
  },
  "caller_id": {
    "S": "+555222333444"
  },
  "chat_id": {
    "N": "-12345678"
  }
}
```

 * `id` - is part of url. You will give your guests url like `https://my.example.com/open/1_elm_plumber`
 * `owner` - your name, free form, for reference only
 * `caller_id` - your number, registered in gate/barrier whitelist that will be used as call originator
 * `chat_id` - (optional) telegram chat to get notified when plumber opened the gate/barrier
