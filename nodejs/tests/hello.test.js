import * as hello from "../hello";

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
        badHeader: "Value1",
      },
    };

    const result = await hello.handler(event);

    expect(result).toEqual({
      statusCode: 400,
      body: '{"message":"Bad Request!"}',
    });
  });
});
