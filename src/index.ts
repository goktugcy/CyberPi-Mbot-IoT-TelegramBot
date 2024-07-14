import { Hono } from "hono";

const app = new Hono();

app.post("/webhook", async (c) => {
  try {
    const data = await c.req.json();

    // Telegram bot and chat details
    const telegramBotToken = "7xxxxxxxx:AAHK5c7CDnxxxxxxxxxxxxxxxxxxx";
    const chatId = "8112xxxxxx";

    const message = data.message || "No message provided";
    const telegramUrl = `https://api.telegram.org/bot${telegramBotToken}/sendMessage`;

    const response = await fetch(telegramUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        chat_id: chatId,
        text: message,
      }),
    });

    if (response.ok) {
      return c.json({
        success: true,
        message: "Message sent to Telegram successfully!",
      });
    } else {
      const error = await response.json();
      return c.json({ success: false, error }, 500);
    }
  } catch (error) {
    return c.json({ success: false, error: error }, 500);
  }
});

app.get("/", async (c) => {
  return c.json({ message: "Hello, World!" });
});

export default app;
