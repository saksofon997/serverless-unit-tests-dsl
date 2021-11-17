# Serverless Unit tests DSL Python + NodeJS

A DSL for specifying Unit tests for Lambda functions directly in serverless.yml. Tests can be generated locally or on CI/CD, which allows for a cleaner workspace and easier tests overview. Supports both Python and NodeJS Lambdas.

## DSL

Enter test fixtures, cases and expected results directly in serverless yml. Example:

``` bash
custom:
  tests:
    hello:
      - case1:
          event:
            - headerName1: "Value1"
            - headerName2: "Value2"
            - body:
                - fieldName: "Value3"
          result: "{\n    statusCode: 200,\n    body: {\n      message: `Go Serverless v2.0!`,\n    },\n}"

      - case2:
          event:
            - headerName1: "BadHeader"
          result: "{\n    statusCode: 400,\n    body: {\n      message: `Bad Request!`,\n    },\n}"
```

This will generate the following tests:

``` javascript
test("case1", async () => {
  const event = {
    headers: {
      headerName1: "Value1",
      headerName2: "Value2",
    },
    body: {
      fieldName: "Value3",
    },
  };

  const result = await handler.hello(event, context);

  expect(result).toEqual(
    "{\n    statusCode: 200,\n    body: {\n      message: `Go Serverless v2.0!`,\n    },\n}"
  );
});

test("case2", async () => {
  const event = {
    headers: {
      headerName1: "BadHeader",
    },
  };

  const result = await handler.hello(event, context);

  expect(result).toEqual(
    "{\n    statusCode: 400,\n    body: {\n      message: `Bad Request!`,\n    },\n}"
  );
});
```

### Requirements

- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)
- [textX](https://github.com/textX/textX)

### Installation

Install the Node.js packages

``` bash
$ npm install
```

Install textX

### Usage

To simulate API Gateway locally using [serverless-offline](https://github.com/dherault/serverless-offline)

``` bash
$ serverless offline start
```

Deploy your project

``` bash
$ serverless deploy
```

### Tests Usage

Generate tests using

``` bash
$ textx generate serverless.yml
```

#### Running Tests

Run your tests using

``` bash
$ npm test
```

We use Jest to run our tests. You can read more about setting up your tests [here](https://facebook.github.io/jest/docs/en/getting-started.html#content).
