# s3tagger

[![asciicast](https://asciinema.org/a/338802.svg)](https://asciinema.org/a/338802)

# Installation
Pre-requisites:
* Have Python 3.8, preferably running in a virtualenv.
* Have admin-ish AWS permissions to the S3 bucket you're modifying.

```sh
pip install -U -i https://pypiserver.aapdev.com/simple/ s3tagger 
```

# Usage

## tldr

```
s3tagger populate -b aaptiv-ivan-test -m .png -m .txt
s3tagger process -b aaptiv-ivan-test -t test:mytag
s3tagger clean -b aaptiv-ivan-test
```

## Commands

```
Usage: s3tagger [OPTIONS] COMMAND [ARGS]...

  A CLI to tag lots and lots of files in a bucket.

Options:
  -v, --verbose  Enables verbose mode.
  --help         Show this message and exit.

Commands:
  clean     Cleans up on-disk queue.
  populate  Loads S3 files into disck-backed queue.
  process   Tags files in queue.
  status    Prints information about s3tagger configuration.
```

```
Usage: s3tagger populate [OPTIONS]

  Loads S3 files into disck-backed queue.

Options:
  -m, --match TEXT   Keys must include one of these match strings to be
                     processed.

  -b, --bucket TEXT  S3 bucket.
  --help             Show this message and exit.
```


```
Usage: s3tagger process [OPTIONS]

  Tags files in queue.

Options:
  -w, --workers INTEGER  Number of threads to run in parallel.
  -t, --tags TEXT        Tags to put on objects.  Should be in the `KEY:VALUE'
                         format e.g. '-m autodelete:true'

  -b, --bucket TEXT      S3 bucket.
  --help                 Show this message and exit.
```

```
Usage: s3tagger clean [OPTIONS]

  Cleans up on-disk queue.

Options:
  -b, --bucket TEXT  S3 bucket.
  --help             Show this message and exit.
```
