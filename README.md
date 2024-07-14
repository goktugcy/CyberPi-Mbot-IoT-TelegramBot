# IoT and Telegram Integration Project

## Overview

This project contains two main components:
1. A webhook server using the Hono framework in TypeScript.
2. An IoT script for the mBot robot to detect sound and motion, and send notifications via a webhook.

## Features

### Webhook Server (TypeScript)
- A server built using the Hono framework.
- Receives POST requests on `/webhook` and sends messages to a specified Telegram chat.
- Provides a simple GET endpoint on `/` that returns a greeting message.

### IoT Script for mBot (Python)
- Connects to a specified Wi-Fi network.
- Uses the mBot's sensors to detect sound and motion.
- Sends a notification to a specified webhook URL when sound or motion is detected.

## Installation

### Prerequisites
- Node.js and npm installed for the webhook server.
- Cloudflare account and Wrangler CLI installed for deployment.
- Python and necessary libraries installed for the mBot script.
- mBot robot with the necessary sensors.
- Telegram bot token and chat ID for sending messages.
- Wi-Fi network credentials.

### Webhook Server

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject/server
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Develop locally using Wrangler:
    ```sh
    wrangler dev
    ```

4. Deploy the server using Wrangler:
    ```sh
    wrangler deploy
    ```

### IoT Script for mBot

1. Navigate to the bot directory and set up your environment:
    ```sh
    cd ../bot
    ```

2. Ensure the mBot library and other dependencies are installed on your mBot device.

3. Replace the Wi-Fi credentials and webhook URL in `mbot.py` with your actual details.

4. Use mBlock to load the `mbot.py` script onto your mBot.

## Usage

### Webhook Server

After deploying the server, it will be accessible at the URL provided by Cloudflare. The server listens for POST requests on `/webhook` to forward messages to a Telegram chat. The root endpoint can be accessed to see a greeting message.

### IoT Script for mBot

The mBot script will automatically connect to the specified Wi-Fi network on startup. It continuously monitors sound and motion using its sensors. When sound or motion is detected, it sends a notification to the specified webhook URL.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-foo`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some foo'`).
5. Push to the branch (`git push origin feature-foo`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
