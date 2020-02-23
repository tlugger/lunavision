LunaVision
==========
An OpenCV powered Raspberry Pi for spying on my dog

Inspiration
-----------
Nearly all of the credit for this project goes to Adrian Rosebrock of [pyimagesearch](https://www.pyimagesearch.com/).

The source code from this project specifically is entirely based on his project: _[Building a Raspberry Pi security camera with OpenCV](https://www.pyimagesearch.com/2019/03/25/building-a-raspberry-pi-security-camera-with-opencv/)_.

Install
-------
- Install OpenCV libraries
  - `sudo install_scripts/install_opencv.sh`
- Install Python 3 pip package manager (includes virtualenv)
  - `sudo install_scripts/install_pip.sh`

- Make a new virtualenv and install pip dependencies
  - `virtualenv venv`
  - `pip install -r requirements.txt`

Run
---
- Create your config/config.json file:
```
{
	// two constants, first threshold for detecting if the
	// refrigerator is open, and a second threshold for the number of
	// seconds the refrigerator is open
	"thresh": 50,
	"open_threshold_seconds": 60,

	// variables to store your aws account credentials
	"aws_access_key_id": "YOUR_AWS_ACCESS_KEY_ID",
	"aws_secret_access_key": "YOUR_AWS_SECRET_ACCESS_KEY",
	"s3_bucket": "YOUR_AWS_S3_BUCKET",

	// variables to store your twilio account credentials
	"twilio_sid": "YOUR_TWILIO_SID",
	"twilio_auth": "YOUR_TWILIO_AUTH_ID",
	"twilio_to": "YOUR_PHONE_NUMBER",
	"twilio_from": "YOUR_TWILIO_PHONE_NUMBER"
}
```
- Run detect script
  - `python detect.py --conf=config/config.json`

TODO
----
- [x] Readme
- [x] Install scripts
- [x] Add copied security camera code
- [ ] Adjust to detect/record Luna