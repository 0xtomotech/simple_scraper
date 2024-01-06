# Simple Scraper

This is a simple web scraper that retrieves news articles from the Hacker News website and sorts them based on the number of votes.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/simple-scraper.git`
2. Install the required dependencies: `pip install requests beautifulsoup4`

## Usage

1. Open the `scraper.py` file.
2. Run the script: `python scraper.py`
3. The script will fetch the news articles from the Hacker News website and display the top articles based on the number of votes.

## Example Output
[{'link': 'https://www.robinsloan.com/notes/home-cooked-app/',
  'title': 'An app can be a home-cooked meal (2020) (robinsloan.com)',
  'votes': 928},
 {'link': 'https://www.clicks.tech/',
  'title': 'Clicks – Physical keyboard for iPhone (clicks.tech)',
  'votes': 918},
 {'link': 'https://matduggan.com/fixing-macs-door-to-door/',
  'title': 'Fixing Macs door to door (matduggan.com)',
  'votes': 723},
 {'link': 'https://papereditor.app/dev',
  'title': '9 years of Apple text editor solo dev (papereditor.app)',
  'votes': 700},
 {'link': 'https://time.fyi/timezones',
  'title': 'Show HN: I made a tool to compare time zones (time.fyi)',
  'votes': 555},
 {'link': 'https://www.digitalcameraworld.com/news/this-holographic-camera-turns-any-window-into-an-invisible-camera',
  'title': 'Zeiss\'s "Holocam" turns glass windows into cameras '
           '(digitalcameraworld.com)',
  'votes': 516},
 {'link': 'https://andykong.org/blog/icloudconfusion',
  'title': 'Cleaning up my 200GB iCloud with some JavaScript (andykong.org)',
  'votes': 312},
 {'link': 'https://www.theguardian.com/us-news/2024/jan/06/alaska-airlines-grounds-boeing-737-max-9-planes-after-mid-air-window-blowout',
  'title': 'Alaska Airlines grounds Boeing 737 Max 9 planes after mid-air '
           'window blowout (theguardian.com)',
  'votes': 295},
 {'link': 'https://www.reddit.com/r/aviation/comments/18znz5p/as_1282_kpdx_to_kont_diverted_for_rapid/',
  'title': 'Alaska Airlines 737 Max makes emergency landing due to '
           'depressurization (reddit.com)',
  'votes': 228},
 {'link': 'https://lyra.horse/misc/chromium_vrp_tree.html',
  'title': 'Chromium bug bounty money tree browser (lyra.horse)',
  'votes': 185},
 {'link': 'https://blogsystem5.substack.com/p/hard-disk-leds-and-noisy-machines',
  'title': 'Hard disk LEDs and noisy machines (blogsystem5.substack.com)',
  'votes': 185},
 {'link': 'https://tidyfirst.substack.com/p/niklaus-wirth-1934-2024',
  'title': 'Niklaus Wirth, 1934-2024: Geek For Life (tidyfirst.substack.com)',
  'votes': 171},
 {'link': 'https://blog.regehr.org/archives/1393',
  'title': 'Teaching C (2016) (regehr.org)',
  'votes': 170},
 {'link': 'https://yosefk.com/blog/why-bad-scientific-code-beats-code-following-best-practices.html',
  'title': 'Bad scientific code beats code following "best practices" (2014) '
           '(yosefk.com)',
  'votes': 165},
 {'link': 'https://looo.lol/',
  'title': 'Looo.lol – a binary math site (looo.lol)',
  'votes': 157},
 {'link': 'https://huggingface.co/microsoft/phi-2/commit/7e10f3ea09c0ebd373aebc73bc6e6ca58204628d',
  'title': 'Microsoft Phi-2 model changes licence to MIT (huggingface.co)',
  'votes': 155},
 {'link': 'https://nautil.us/what-you-dont-know-about-sperm-482001/',
  'title': 'Human sperm cooperate on the competitive pathway to fertilization: '
           'study (nautil.us)',
  'votes': 155},
 {'link': 'https://github.com/YS-L/csvlens',
  'title': 'Csvlens: Command line CSV file viewer. Like less but made for CSV '
           '(github.com/ys-l)',
  'votes': 152},
 {'link': 'https://www.lysator.liu.se/c/dmr-on-or.html',
  'title': 'Dennis Ritchie on the priorities of && || vs. == etc. (1982) '
           '(liu.se)',
  'votes': 149},
 {'link': 'https://jvns.ca/blog/2024/01/05/do-we-think-of-git-commits-as-diffs--snapshots--or-histories/',
  'title': 'Do we think of Git commits as diffs, snapshots, and/or histories? '
           '(jvns.ca)',
  'votes': 149},
 {'link': 'https://austinvernon.site/blog/navyshipbuilding.html',
  'title': 'Revitalizing US Navy Shipbuilding (austinvernon.site)',
  'votes': 135},
 {'link': 'https://github.com/MegaManSec/SSH-Snake',
  'title': 'SSH-Snake: Automated SSH-Based Network Traversal '
           '(github.com/megamansec)',
  'votes': 130},
 {'link': 'item?id=38878354',
  'title': 'Ask HN: What to do with text from old, unarchived, online forums?',
  'votes': 116},
 {'link': 'https://tratt.net/laurie/blog/2024/choosing_what_to_read.html',
  'title': 'Choosing what to read (tratt.net)',
  'votes': 115},
 {'link': 'https://medium.com/bull-market/sweaty-january-and-how-gyms-make-money-7d682ff5eeaf',
  'title': 'How Gyms Make Money (2015) (medium.com/bull-market)',
  'votes': 114}]