# Pillow 
## Sur une Raspberry Pi 2 
```bash
sudo apt-get install -y zlib1g-dev libjpeg-dev libtiff-dev libfreetype6-dev
sudo apt-get install -y libopenjp2-7-dev
```

```bash
sudo apt-get update
```

Install Pillow using a precompiled binary wheel. 
Avoids the need for compiling from source.

```bash
pip install --only-binary :all: pillow
```

