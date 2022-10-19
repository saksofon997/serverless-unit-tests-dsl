export async function handler(event) {
  switch (process.env.OPERATION) {
    case "add":
      return parseInt(event.a) + parseInt(event.b);
    case "multiply":
      return parseInt(event.a) * parseInt(event.b);
  }
}
