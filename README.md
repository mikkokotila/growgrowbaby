# growgrowbaby
AI driven sprout grow box

## What is required?

- Raspberry Pi 3 B+
- GrovePi+

### 1. Preparing for installing the Raspbian OS on your Raspberry Pi

**REQUIREMENTS**:

- USB drive or SD card (recommended at least 16Gb)
- Any regular computer
- An internet connection
- Roughly 15 minutes of time (depends on your internet speed)

If you already have a working Raspberry Pi or have NOOBS ready on an SD card, you can skip this section.

NOTE: It's highly recommended to use USB drive and not SD card. The SD card breaks easily and has other known issues. 

**STEPS**:

1) Download the Raspbian OS image [here](https://www.raspberrypi.org/downloads/raspbian/)
2) While waiting for the image to download, get Balena Etcher for a hassle-free image flashing [here](https://www.balena.io/etcher/)
3) Mount a USB drive with at least 16Gb on to your local machine
4) Follow the instructions in Balena Ethcher to flask your USB 
5) Unmount the USB from your local machine, and move onto the next step

### 2. Installing Raspbian OS on your Raspberry Pi

**REQUIREMENTS**:

- USB drive or SD card with Raspbian OS image flashed
- Raspberry Pi 3 B+
- Power sources for the Raspberry Pi
- Keyboard
- Mouse
- Screen

**STEPS**:

1) Stick the USB (or SD card) you have from the previous steps, into your Raspberry Pi
2) Power-on the Raspberry Pi (you nee
3) Follow the on-screen instructions to set your location, keyboard, and other settings
4) Make sure to connect to your local wireless network (we will need that in next steps)
5) Allow the automated update process to complete (might take a while)

### 3. Configuring your Raspberry Pi for remote access with SSH

We will now free ourselves from the need to have keyboard/mouse/screen attached to the Raspberry Pi, and instead connect to it from any other machine. 

NOTE: The machine you are using to remotely connect to your Raspberry Pi has to be in the same wireless network with your Raspberry Pi. 

**STEPS**:

1) Open `terminal` from the menu
2) Then run the following two commands:

```
sudo systemctl enable ssh
sudo systemctl start ssh
```

3) Next, we need to find out what is the IP address Raspberry Pi have taken in your wireless network:

```
ifconfig
```

...and find your IP address under the heading `wlan0`. It will be something like `192.168.1.12`.

4) Go to your local machine, open terminal and: 

```
ssh pi@192.168.1.12
```

...and follow the prompts on the screen. This should have you inside a terminal session giving you control over your Raspberry Pi. 

### 4. Setting up GrovePi+ on your Raspberry Pi

**REQUIREMENTS**:

- Raspberry Pi 3 B+ prepared as per the previous steps
- Power sources for the Raspberry Pi
- GrovePi+
- Internet connection
- Local machine (laptop or any other device with terminal)

**STEPS**:

1) Open `terminal` on your local machine and:

```
ssh pi@192.168.1.12
```

