# db2_api

This project aims to connect to Db2 on cloud and use ibm_db API to issue SQL statements to specific tables in the database. As a Data Engineer, one must know how to:

- Access databases using python;
- Write code using APIs;
- Work with real world Datasets; and
- Issue SQL statements using python libraries.

This project shows these concepts applied to a real world scenario.

## Usage

In order to reproduce results obtained by the .py script, it is necessary to execute the following line in a Linux environment:

```bash
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
```

This will install requirements listed in requirements.txt file and activate the virtual environment. Once this is done, it is possible to execute the .py script given that the credentials to access Db2 on cloud are valid.

The data used to practice the concepts mentioned above can be found in https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t/data