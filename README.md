# PyMap
A python medium for nmap scans

## Installation
You have to install [Nmap](https://nmap.org/download.html) and python-nmap in order for this to work.

```
pip install python-nmap
```

Then, simply clone the repository and navigate to the PyMap folder:

```
git clone https://github.com/yourusername/pymap.git
cd pymap
```

## Usage

```
python pymap.py -t ip --scan-type type
```

Replace "ip" with the IP address you want to scan; and replace "type" with the scan type.

### Scan Types

    Fast: Scans a predefined set of common ports.
    Medium: Scans a wider range of common ports.
    Top: Scans an extensive list of ports, suitable for a thorough examination.
    Normal: Scans the first 1000 ports.
    Full: Scans all 65535 ports (time-consuming).

## Example Input/Output:

```
python pymap.py -t 127.0.0.1 --scan-type fast
```

```
Port 20 is open. / Service: ftp-data
Port 21 is open. / Service: ftp
...
```
