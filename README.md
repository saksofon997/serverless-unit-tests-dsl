# Serverless Unit tests DSL Python + NodeJS

A DSL for specifying Unit tests for Lambda functions mostly resembling HTML. Tests can be generated locally or on CI/CD, which allows for a cleaner workspace and easier tests overview. Supports both Python and NodeJS Lambdas.

## DSL

Enter test fixtures, cases and expected results directly in text files with `sts` extension. For example:

```html
< function = hello
  < env = json
    {
      "HELLO": "Hello Serverless!"
    }
  >
  < case = helloCase1
    < input = json
      {
        "headers": {
          "headerName1": "Value1",
          "headerName2": "Value2"
        },
        "body": {
          "fieldName": "Value3"
        }
      }
    >
    < output = json
      {
        "statusCode": 200,
        "body": "{\\"message\\":\\"Hello Serverless!\\"}"
      }
    >
  >
  < case = helloCase2
    < input = json
      {
        "headers": {
          "badHeader": "Value1"
        }
      }
    >
    < output = json
      {
        "statusCode": 400,
        "body":"{\\"message\\":\\"Bad Request!\\"}"
      }
    >
  >
>
```

This will generate the following tests:

```javascript
describe("hello", () => {
  beforeAll(() => {
    process.env.HELLO = "Hello Serverless!";
  });

  test("helloCase1", async () => {
    const event = {
      headers: {
        headerName1: "Value1",
        headerName2: "Value2"
      },
      body: {
        fieldName: "Value3"
      }    
    };

    const result = await hello.handler(event);

    expect(result).toEqual({
      statusCode: 200,
      body: "{\"message\":\"Hello Serverless!\"}"    
    });
  });

  test("helloCase2", async () => {
    const event = {
      headers: {
        badHeader: "Value1"
      }    
    };

    const result = await hello.handler(event);

    expect(result).toEqual({
      statusCode: 400,
      body: "{\"message\":\"Bad Request!\"}"    
    });
  });
});
```

### Requirements

- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)
- [textX](https://github.com/textX/textX)

### Installation

Install the Node.js packages

```bash
$ npm install
```

For python, install the requirements in `requirements.txt`

```bash
$ pip install -r requirements.txt
```

Install textX

### Serverless Usage

To simulate API Gateway locally using [serverless-offline](https://github.com/dherault/serverless-offline)

```bash
$ serverless offline start
```

Deploy your project

```bash
$ serverless deploy
```

### Tests Usage

Generate tests using

```bash
$ textx generate serverless.sts --target Tests -o test
```

#### Running Tests

Run your tests using

```bash
$ npm test
```

For python, run tests using:

```bash
$ python -m pytest
```
