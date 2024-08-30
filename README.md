# IoT Config and Test Project

## 1. Configuring the Modem:

### **1. Device Info**

Raspberry Pi 4 Model B
HAT: Sixfab 3G/4G & LTE Base HAT
Modem: Quectel Wireless Solutions Co., Ltd. BG96 CAT-M1/NB-IoT modem


- The connection to the device is done via SSH, using the terminal.
- SSH is done using an SSH key, which is a more secure way to connect to a device than using a password.

**NOTE 1:** The modem is connected to the Raspberry Pi via USB.
**NOTE 2:** to connect to the Raspberry Pi via SSH, you need to know the IP address of the device. This can be found in the router settings or by using the command:

```shell
your-user@your_pc:~ $ ping raspberr
```

You need the location of the key file to connect to the Raspberry Pi. This is usually in the .ssh folder in your home directory.

```shell
your-user@your_pc:~ $ ssh -i ~/.ssh/your_key_file your_user@your_ip
```

And then, create the environment variables for the connection, by creating an env.py file with the following content:

```python
import os

os.environ['HOST'] = 'RASPBERRY_IP'
os.environ['USERNAME'] = 'YOUR_USER_IN_RASPBERRY'
os.environ['SSH_KEY_PATH'] = 'SHH_KEY_PATH_IN_YOUR_COMPUTER'
```





### 2. Check that the hardware is correctly installed

**NOTE:** the modems are listed as USB devices, therefore, it is needed to list the USB port connections… the same ls (list command, but with USB ;-) )

```bash
your-user@your_pi:~ $lsusb
```

```
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

Bus 001 Device 003: ID 2c7c:0125 Quectel Wireless Solutions Co., Ltd. EC25 LTE modem

Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub

Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

In my case:

```
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

Bus 001 Device 020: ID 2c7c:0296 Quectel Wireless Solutions Co., Ltd. BG96 CAT-M1/NB-IoT modem

Bus 001 Device 003: ID 046d:c52b Logitech, Inc. Unifying Receiver

Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub

Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

And if we check the tree (list tree… ls -t), then we can see the device and port:

Here it can be seen that the modem is recognized by Linux (Device 003).

```shell
your-user@your_pi:~ $ lsusb -t

...

/: Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M

  |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M

    |__ Port 2: Dev 3, If 4, Class=Vendor Specific Class, Driver=qmi_wwan, 480M
```

In my case:

```
/: Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M

/: Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/1p, 480M

  |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M

    |__ Port 3: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 12M

    |__ Port 3: Dev 3, If 1, Class=Human Interface Device, Driver=usbhid, 12M

    |__ Port 3: Dev 3, If 2, Class=Human Interface Device, Driver=usbhid, 12M

    |__ Port 4: Dev 5, If 4, Class=Vendor Specific Class, Driver=qmi_wwan, 480M

    |__ Port 4: Dev 5, If 2, Class=Vendor Specific Class, Driver=option, 480M

    |__ Port 4: Dev 5, If 0, Class=Vendor Specific Class, Driver=option, 480M

    |__ Port 4: Dev 5, If 3, Class=Vendor Specific Class, Driver=option, 480M

    |__ Port 4: Dev 5, If 1, Class=Vendor Specific Class, Driver=option, 480M
```



**NOTE:** QMI stands for Qualcomm MSM Interface.

If you want to check the kernel logs, to see the modem messages:

```shell
your-user@your_pi:~ $ dmesg | grep qmi

[  5.701450] qmi_wwan 1-1.2:1.4: cdc-wdm0: USB WDM device

[  5.703022] qmi_wwan 1-1.2:1.4 wwan0: register 'qmi_wwan' at usb-0000:01:00.0-1.2, WWAN/QMI device, 02:5c:84:4e:14:51

[  5.703245] usbcore: registered new interface driver qmi_wwanIoT Project to configure and test devices
```



### 3. AT Commands

First, let's make some terminology clear:

**IMEI:** The International Mobile Equipment Identity is a numeric identifier, usually unique, for 3GPP and iDEN mobile phones, as well as some satellite phones.

**IMSI:** The international mobile subscriber identity is a number that uniquely identifies every user of a cellular network. It is stored as a 64-bit field and is sent by the mobile device to the network.

**ICCID:** The Integrated Circuit Card Identification number is an 18-22-digit number typically printed on the back of a SIM card. No two SIM cards have the same ICCID number.

Now, even though the AT commands are dictated by the 3gpp TS 27.005 and 27.007, vendors create their own to enhance the capabilities of the device and its functionalities. To get all possible commands from a modem, use the AT+CLAC command.

In our case:

```
Enter the AT command: AT+CLAC

&C
&D
&F
&W
&V
E
Q
V
X
Z
&S
I
L
M
A
D
H
O
S0
S2
S3
S4
S5
S6
S7
S8
S10
+ICF
+IFC
+IPR
+GMI
+GMM
+GMR
+GSN
+GCAP
+CMEE
+WS46
+CLCC
+CEREG
+CEMODE
+CSCS
+CRC
+CGDCONT
+CGDSCONT
+CGEREP
+CGCONTRDP
+CGPADDR
+CGSMS
+CSMS
+CMGF
+CSAS
+CRES
+CSCA
+CSMP
+CREG
+CGREG
+CGSCONTRDP
+CGPIAF
+CSDH
+CSQ
+CPIN
+CMER
+CPMS
+CNMI
+CMGL
+CMGR
+CMGS
+CMSS
+CMGW
+CMGD
+CMGC
+CNMA
+CMMS
+COPS
+CIMI
+CGMI
+CGMM
+CGMR
+CGSN
+CLAC
+CVMOD
+CGATT
+CGACT
+CPAS
+CGCMOD
+CLCK
+CPWD
+CNUM
+CSIM
+CRSM
+CCLK
+COPN
+CPOL
+CPLS
+CTZR
+CTZU
+CUAD
+CMUX
+CSDF
+CSTF
+CUSD
+ICCID
+CIND
+CPSMS
+CEDRXS
+CEDRXRDP
+CFUN
$QCPWRDN
+QPOWD
+QSCLK
+QFOTADL
+QLWM2M
+QIIC
+QDAI
+QRESET
+QGPSCFG
+QFWD
+QADC
+CBC
+QTEMP
+QVBATT
+QCFGEXT
+QPRTPARA
+QNANDTEST
+QCTEMP
+QDIAGPORT
+QTEST
+QFTEST
$QCRMCALL
$QCPDPP
$QCDGEN
$QCPDPIMSCFGE
$QCPDPCFGE
$QCSIMSTAT
$QCRSRP
$QCRSRQ
$QCRATSTATE
$QCEXTCLTSTATE
```

* All those starting with $Q are vendor-specific.
* The syntax for all of them can vary from vendor to vendor.

**NOTE:** in case you are using "***minicom***" to communicate with the modem and send AT commands, the baud rate for the BG96 (our modem) is 96000, not 115200

The definition of each command can be found in the 3gpp documentation.

### 4. Handling errors

AT command responses should be OK or ERROR, plus the output or error cause.

AT+CMEE=1 or AT+CMEE=2 gives a more detailed error reason.

The handling of errors is performed automatically by the APP during initialization of the connection with the modem.



### 5. Modem and SIM Info

The app displays the following information at launch:

- Modem Brand
- Modem Model
- IMSI
- IMEI
- ICCID

In the code, the function handling such a task is:

comms.get_modem_info( )



## 2. GUI

The GUI has been created with Tkinter, which is a package included in Python.

To test that Tkinter is working properly and check the installed version, you can run:

```shell
python -m tkinter
```



This will open a window like this:

![Screenshot 2024-07-28 at 12.05.10](/Users/pauloarbelaez/Documents/GitHub/iot_config_and_test/docs_images/readme/Screenshot 2024-07-28 at 12.05.10.png)

**NOTE:** To be able to work with Tkinter in your Raspberry Pi via SSH, it is necessary to run the connection through the X11 Protocol, which lets your device create a graphical user interface based on what is sent by the PI. As this project was created on Mac, we used XQuartz to handle this task.

Tkinter works with widgets. All graphical elements should be first created and then displayed. And, there are two display formats: pack and grid.

Pack, are stacked components, one on top of the other, while the grid is exactly that, a grid: the programmer gets to choose the column and row in which the widget will be placed.

It is worth noticing that Tkinter relies on Tcl/Tk. Tcl is language by itself that is commonly embedded inte C applications as a scripting engine or an interface to the Tk toolkit. While, Tk is a Tcl package implemented in C that adds custom commands to create and manipulate GUI widgets. So, when running Tkinter, you have C underlying your python code.

Tsk are more modern widgets for a much better appearance, but both: Tk and Tty, use the facilities of the OS where they run, replicating the look and feel of it.

More info on how to work with Tkinter on: https://docs.python.org/3/library/tkinter.html#


