// Autogenerated Serverless test
// Template: JS

import * as hello from "../hello";

describe("hello", () => {
  beforeAll(() => {
    process.env.HELLO = "Hello Serverless!";
  });

  test("case", async () => {
    const result = await hello.handler();

    expect(result).toMatchObject({ statusCode: 200 });
  });
  test("case", async () => {
    const result = await hello.handler();

    expect(result).toMatchObject({ statusCode: 200 });
  });
});