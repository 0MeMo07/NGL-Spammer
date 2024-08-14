
# NGL-Spammer
This Python script is used to automatically send messages to [ngl.link](https://ngl.link) service. It sends a specified message to a given username a certain number of times.

## Requirements

- Python 3.x

## Installation

1. download this code:
   ```bash
   git clone https://github.com/0MeMo07/NGL-Spammer.git
2. Go to NGL-Spammer file:
    ```bash
     cd NGL-Spammer
3. Install the required libraries by running the following command:
    ```bash
    pip install -r requirements.txt
4. NGLSpamer.py Run:
     ```bash
     python NGLSpamer.py
## Usage

1. Enter your NGL username.
2. Enter the message you want to send.
3. Specify the number of messages to be sent.
4. Enter the delay between requests (in seconds). If you want the fastest possible requests, enter 0.
5. Choose whether to use a proxy (y/n).
   - If yes, ensure `proxies.txt` contains valid proxies.

The script will automatically start sending the specified message to the given username. Successful submissions will be marked with [+] while unsuccessful submissions will be marked with [-].

If there are 4 consecutive unsuccessful submissions, the script will change the device ID and user agent. If using proxies, it will also select a new proxy from `proxies.txt`.

## Error Handling

- If a bad proxy is encountered, the script will select a new proxy and retry.

## Screenshots
![image](https://github.com/0MeMo07/NGL-Spammer/assets/103096364/edba601d-7367-413c-94b5-44cb26b98759)

## Support me

<a href="https://www.buymeacoffee.com/SmakeMeMo" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee">
