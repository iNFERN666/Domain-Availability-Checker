# Domain Checker

This Python script checks the availability of a list of domain names using the WHOIS protocol. The list of domain names to check should be provided in a file named `list.txt`, with one domain per line.

## Installation

To use this script, you will need to have Python 3.x installed on your computer. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

You will also need to install the `whois` package, which can be installed using pip:


## Usage

1. Clone this repository to your local machine using Git:

       git clone https://github.com/<username>/domain-checker.git
  
2. Navigate to the directory where the script is located:

        cd domain-checker
  
3. Add the list of domain names you want to check to a file named `list.txt`, with one domain per line.
4. Run the script using Python:

The script will read the list of domain names from `list.txt`, check the availability of each domain, and print a message for each domain indicating whether it is available for purchase or not.

Note that WHOIS data may not always be accurate or up-to-date, and the availability of a domain may depend on various factors such as the domain registrar, the domain's history, and the specific TLD (top-level domain). Therefore, it's always a good idea to verify the availability of a domain using multiple sources before making any purchase decisions.
