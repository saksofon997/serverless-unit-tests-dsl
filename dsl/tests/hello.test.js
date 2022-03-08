// Autogenerated Lambda test
// Template: JS

import * as hello from "../hello";

describe("hello", () => {
  beforeAll(() => {
      process.env.HELLO = "Hello Serverless!";
  });

  test("helloCase1", async () => {
    const event = {
      "headerName1": "Value1",       "headerName2": "Value2",       "body": {
            "fieldName": "Value3"
      }    };
    const result = await hello.handler(event);

    expect(result).toEqual({
      "statusCode": 200,       "body": "{\"message\":\"Hello Serverless!\"}"    });
  });
  test("helloCase2", async () => {
    const event = {
      "badHeader": "Value1"    };
    const result = await hello.handler(event);

    expect(result).toEqual({
      "statusCode": 400,       "body": "{\"message\":\"Bad Request!\"}"    });
  });
});