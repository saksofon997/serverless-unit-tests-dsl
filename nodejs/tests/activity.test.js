import * as activity from "../activity";

describe("activity", () => {
  beforeAll(() => {
    process.env.API_URL = "https://www.boredapi.com/api/activity";
  });

  test("case", async () => {
    const result = await activity.handler();

    expect(result).toMatchObject({ statusCode: 200 });
  });
});
