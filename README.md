<!-- ABOUT THE PROJECT -->

## About The Project

I made this project because I wanted to generate an Ethereum address starting with seven zeroes, that is, 0x0000000....

There wasn't a specific reason for this, it just sounded fun!

  

### Built With

  

*  [Python](https://www.python.org/)

*  [Web3-Py](https://web3py.readthedocs.io/en/stable/)

  

<!-- GETTING STARTED -->

## Getting Started

With this script you can generate an Ethereum address that start with a sequence of zeroes (in my case, 7). It has two

paramters: the desired number of zeroes and a minimum number of zeroes to store the address. Second parameter is needed

because the time to generate an address with more leading zeroes increases exponentially, so it's a good idea to store

also private keys for addresses with less zeroes the what we desire.

  

### Prerequisites and Installation

In order to setup the project you have to create a virtual environment (optional)

```sh

virtualenv env

```

The you activate the environment

```sh

source env/bin/activate

```

  

The you have to install the required python dependencies


```sh

pip3 install -r requirements.txt

```

  

<!-- USAGE EXAMPLES -->

## Usage

In order to start the script you have specify the number of leading zero you want and the minimum number of zeroes you want in order to store the private key. 
```sh

pip3 generator.py <optimal> <minimum>

```
For example, I wanted to generate an address with 7 leading zeroes but I decided to store the private keys of any address with 4 leading zeroes. To do so I execute this command:
```sh

pip3 generator.py 7 4

```
  

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.