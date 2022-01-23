# Serverless Plugin Tests

Test your application by running `serverless test`, or test automatically before deployment.

Tests are described with a DSL for easy and no-code writing, and so they can be transpiled to Python or JS code.


## Install
Using npm:
```
npm install serverless-plugin-tests --save-dev
```

Add the plugin to your `serverless.yml` file:
```yaml
plugins:
  - serverless-plugin-tests
```

## Configuration

```yaml
custom:
  tests:
    test_file: relative location of the file containing test descriptions
    auto: set to `true` to run tests automatically on deploy

```
