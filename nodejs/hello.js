export async function handler(event) {
  console.log(event);
  if ("badHeader" in event.headers) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        message: "Bad Request!",
      }),
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({
      message: process.env.HELLO,
    }),
  };
}
