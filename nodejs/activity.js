const p = require("phin");

export async function handler(event) {
  const res = await p({
    url: process.env.API_URL,
    parse: "json",
  });

  return { statusCode: res.statusCode };
}
