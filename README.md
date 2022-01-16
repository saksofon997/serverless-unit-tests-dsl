# Serverless Unit tests DSL Python + NodeJS

A DSL for specifying Unit tests for Lambda functions directly in serverless.yml. Tests can be generated locally or on CI/CD, which allows for a cleaner workspace and easier tests overview. Supports both Python and NodeJS Lambdas.

## DSL

Enter test fixtures, cases and expected results directly in serverless yml. Example:

```bash
custom:
  tests:
    hello:
      - env:
          - HELLO: "Hello Serverless!"
      - cases:
          - case:
              event:
                - headerName1: "Value1"
                - headerName2: "Value2"
                - body:
                    - fieldName: "Value3"
              result: '{"statusCode":200,"body":"{\"message\":\"Hello Serverless!\"}"}'
          - case:
              event:
                - BadHeader: "Value1"
              result: '{"statusCode":400,"body":"{\"message\":\"Bad Request!\"}"}'
```

This will generate the following tests:

```javascript
describe("hello", () => {
  beforeAll(() => {
    process.env.HELLO = "Hello Serverless!";
  });

  test("case", async () => {
    const event = {
      headers: {
        headerName1: "Value1",
        headerName2: "Value2",
      },
      body: {
        fieldName: "Value3",
      },
    };

    const result = await hello.handler(event);

    expect(result).toEqual({
      statusCode: 200,
      body: '{"message":"Hello Serverless!"}',
    });
  });

  test("case", async () => {
    const event = {
      headers: {
        BadHeader: "Value1",
      },
    };

    const result = await hello.handler(event);

    expect(result).toEqual({
      statusCode: 400,
      body: '{"message":"Bad Request!"}',
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

Install textX

### Usage

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
$ textx generate serverless.yml
```

#### Running Tests

Run your tests using

```bash
$ npm test
```

We use Jest to run our tests. You can read more about setting up your tests [here](https://facebook.github.io/jest/docs/en/getting-started.html#content).
