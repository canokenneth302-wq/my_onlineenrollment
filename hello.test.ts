import { expect, test } from "bun:test";

test("script.js logs 'Hello world' to the console", async () => {
  const proc = Bun.spawn(["bun", "script.js"], { stdout: "pipe" });
  const output = await new Response(proc.stdout).text();

  expect(await proc.exited).toBe(0);
  expect(output.trim()).toBe("Hello world");
});

test("index.html shows a Hello world heading and loads script.js", async () => {
  const html = await Bun.file("index.html").text();

  expect(html).toContain("<h1>Hello world</h1>");
  expect(html).toContain('<script src="script.js" defer></script>');
});
