# my-toy-cli

A simple and functional CLI tool for basic tasks like greeting, fetching the current date, and time.

## Motivation

While using the aws cli tool , Just out of Curiosity ran the command "which aws" and subsequently "cat $(which aws)" the cli returned the following

``` python
#!/usr/bin/python3
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at

#     http://aws.amazon.com/apache2.0/

# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import sys
import os

if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'
import awscli.clidriver


def main():
    return awscli.clidriver.main()


if __name__ == '__main__':
    sys.exit(main())

```

This was a great surprise for me because "aws cli" was built using a highlevel language like python. If you go in depth , to the "which aws" 's corresponding python script, you could see that it is importing the "awscli" package. If you are still interested to know which framework awscli uses behind the scenes , it is the "argparse" package.


So, Cutting short, It shows that we could build a simple cli (a toy version) using python. After a bit of research a found another wrapper package (wrapper around argparse) named "click", which has much "good looking" APIs ( The "good look" may come at the expense of lesser fine-grained control..).

# toycli structure

The following is the sdk structure followed with in toycli:

    - toycli
        - datetime
            - complete
            - onlytime
            - onlydate
        - randomfacts
            - random
            - today
        - strutils
            - reverese
            - trim


    Note:
    
    - This is auto-generated using "print_command_tree" method availabe @ module/utils.py. 

# Installation

    1. clone the repo
    2. run "pip install --editable ."
    3. Ready to go , to verify type "toycli" and press enter.
        
        If installation is successful then you will get the following:

  
        ```
            Usage: toycli [OPTIONS] COMMAND [ARGS]...

            Welcome to toycli  !!

            provide keyname for the service that you are looking for

            example:

                toycli datetime

            Options:
            --help  Show this message and exit.

            Commands:
            datetime
            randomfacts
            strutils


## Citations/ Reference frameworks

 - Click (https://click.palletsprojects.com/en/8.1.x/ )
 - RandomFacts Public API (https://uselessfacts.jsph.pl/ )
 - Ofcourse ChatGPT and Perplexity.
        

