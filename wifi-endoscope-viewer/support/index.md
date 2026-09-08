---
title: Support for WiFi Endoscope Camera Viewer
permalink: /wifi-endoscope-viewer/support/
lang: en
---

# Support

WiFi Endoscope Camera Viewer is shown as **ScopeLens** inside the app.

## Before connecting

1. Turn on the inspection camera.
2. Open iPhone Settings and join the Wi-Fi network created by the camera.
3. Return to the app and allow Local Network access.
4. Use automatic detection first. If it does not connect, open manual setup and enter the camera's host, port, stream path and transport from its instructions.

Many compatible raw MJPEG cameras use `192.168.10.123` on port `7060`. HTTP MJPEG cameras require the correct local address and stream path.

## If no video appears

- Confirm the iPhone is still joined to the camera's Wi-Fi network.
- Temporarily disable VPN, Private Relay or another network filter if it blocks private local addresses.
- Check that the address is private IPv4, localhost or a `.local` host.
- Try the camera manufacturer's documented port and MJPEG path.
- Power-cycle the camera and reconnect.
- If the device provides only RTSP or a proprietary encrypted, authenticated or cloud stream, it is not supported.

## Purchases and restore

The free compatibility preview is remembered after a valid feed is detected. If the camera Wi-Fi has no internet, switch briefly to cellular data or internet Wi-Fi to buy or restore Lifetime Unlock, then reconnect to the saved camera endpoint.

See [Purchases and Refunds](/wifi-endoscope-viewer/purchases/) for details.

## Captures

Photos and recordings are stored locally in the app. Open Captures to preview, share or delete them. Deleting the app removes its local app data, subject to iOS backup and restoration behavior.

## Contact

Email **info@worksbienstudios.com** and include:

- your iPhone model and iOS version;
- the camera brand/model, if known;
- the local host, port, path and transport used; and
- what appeared after you tapped Connect.

Do not send sensitive inspection images unless they are necessary for support and you are authorized to share them.
