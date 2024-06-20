# Metamask-Selenium-Auto-Import-Mnemonic
`chrome.py` and `edge.py` are main script. You can choose either script to run if you have installed both browser.

`MetaMask_Chrome.crx` and `MetaMask_Edge.crx` are Metamask extension download from Chrome Web Store and Edge Web Store, modified one line code. [Why modify?](https://github.com/LavaMoat/LavaMoat/pull/360#issuecomment-1547271080)

You can download the Metamask extension using [CRX Extractor](https://chrome.google.com/webstore/detail/crx-extractordownloader/ajkhmmldknmfjnmeedkbkkojgobmljda) and modify the extension by yourself if you don't trust this crx file.

`chromedriver.exe` and `msedgedriver.exe` are browser driver.

I use `Edge 126.0.2592.61` and `Chrome 126.0.6478.115`.

If you use different version of Edge or Chrome, download the following driver version by yourself and replace `msedgedriver.exe` or `chromedriver.exe` with it.

[Download chromedriver (version <= 115)](https://chromedriver.chromium.org/downloads) | [Download chromedriver (version >= 116)](https://googlechromelabs.github.io/chrome-for-testing/#stable) | [Download msedgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

# Video Demo
[![video](https://img.youtube.com/vi/BEqc2wEX3iY/maxresdefault.jpg)](https://www.youtube.com/watch?v=BEqc2wEX3iY)

# FAQ
Why does it says `selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div[2]/div/div/section/div[1]/div/button/span"}`?

Probably because you did not use the extension(chromedriver.exe and msedgedriver.exe) provided in the repository. If you prefer use your own version, make sure you modified one line code to solve the [LavaMoat problem](https://github.com/LavaMoat/LavaMoat/pull/360#issuecomment-1547271080).