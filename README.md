# Brute Force

## Overview
* A brute-force application to get credentials of user and password in a website.

### Run locally
Install dependencies, virtual environment is recommended.

#### Virtual environment in linux

```python 
python3 -m venv env
source ./env/bin/activate
deactivate
```

#### Virtual environment in windows

```python 
python3 -m venv env
.\env\Scripts\activate
deactivate
```

#### Install the libraries
```python
pip install -r requirements.txt
```


### How to run:
* `Git clone https://github.com/Alanghj/Brute-Force-app.git`. 
* You will see the analysis in: `python3 run.py`.
* Do no forget to Install the `requirements.txt`.


## License

* See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).


## :mortar_board: Author

```shell
Fast web spider written in Go - v1.1.5 by @thebl4ckturtle & @j3ssiejjj

Usage:
  gospider [flags]

Flags:
  -s, --site string               Site to crawl
  -S, --sites string              Site list to crawl
  -p, --proxy string              Proxy (Ex: http://127.0.0.1:8080)
  -o, --output string             Output folder
  -u, --user-agent string         User Agent to use
                                  	web: random web user-agent
                                  	mobi: random mobile user-agent
                                  	or you can set your special user-agent (default "web")
      --cookie string             Cookie to use (testA=a; testB=b)
  -H, --header stringArray        Header to use (Use multiple flag to set multiple header)
      --burp string               Load headers and cookie from burp raw http request
      --blacklist string          Blacklist URL Regex
      --whitelist string          Whitelist URL Regex
      --whitelist-domain string   Whitelist Domain
  -t, --threads int               Number of threads (Run sites in parallel) (default 1)
  -c, --concurrent int            The number of the maximum allowed concurrent requests of the matching domains (default 5)
  -d, --depth int                 MaxDepth limits the recursion depth of visited URLs. (Set it to 0 for infinite recursion) (default 1)
  -k, --delay int                 Delay is the duration to wait before creating a new request to the matching domains (second)
  -K, --random-delay int          RandomDelay is the extra randomized duration to wait added to Delay before creating a new request (second)
  -m, --timeout int               Request timeout (second) (default 10)
  -B, --base                      Disable all and only use HTML content
      --js                        Enable linkfinder in javascript file (default true)
      --subs                      Include subdomains
      --sitemap                   Try to crawl sitemap.xml
      --robots                    Try to crawl robots.txt (default true)
  -a, --other-source              Find URLs from 3rd party (Archive.org, CommonCrawl.org, VirusTotal.com, AlienVault.com)
  -w, --include-subs              Include subdomains crawled from 3rd party. Default is main domain
  -r, --include-other-source      Also include other-source's urls (still crawl and request)
      --debug                     Turn on debug mode
      --json                      Enable JSON output
  -v, --verbose                   Turn on verbose
  -l, --length                    Turn on length
  -L, --filter-length             Turn on length filter
  -R, --raw                       Turn on raw
  -q, --quiet                     Suppress all the output and only show URL
      --no-redirect               Disable redirect
      --version                   Check version
  -h, --help                      help for gospider

```


<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/Alanghj">
                <img src="https://user-images.githubusercontent.com/81534309/151803029-df474faf-bb04-4c5b-8b0d-072d7b4b40b1.png" width="150px;" alt="Image Alanghj" />
                <br />
                <sub><b>Alanghj</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   Made by <a href="/" target="#"> Alanghj</a>
</h4>
