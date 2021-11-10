import * as handler from "../handler";

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
