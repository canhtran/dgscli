# dgscli
A command line tool created by Calvin and mostly use in his videos.

## Installation

```
pip install -U git+https://github.com/canhtran/dgscli
```

## Generation
Generate the dummy car selling company data. Rules of thumbs:
- Number of inventory = Number of product
- Number of User = Number of User Details
- Number of Order = Number of Order Details.

```
Usage: dgscli generate [OPTIONS]

Options:
  --data TEXT             Choose the dummy data: order, product, user
  --num INTEGER           Number of records
  --no_userid INTEGER     Number of user_id for orders
  --no_productid INTEGER  Number of product_id for orders
  --help                  Show this message and exit.
```

Example commands
```
# Generate 100 products
$ dgscli generate --data product --num 10

# Generate 10 customers
$ dgscli generate --data users --num 10

# Generate 10 orders of 5 customers and 7 products
$ dgscli generate --data order --num 10 --no_userid 5 --no_productid 7
```