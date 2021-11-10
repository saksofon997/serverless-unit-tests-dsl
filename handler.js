export const hello = async (event, context) => {
  if (event.headers.headerName1.includes("BadHeader")) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        message: `Bad Request!`,
      }),
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({
      message: `Go Serverless v2.0!`,
    }),
  };
};
