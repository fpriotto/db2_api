# db2_api

This project aims to connect to Db2 on cloud and use ibm_db API to issue SQL statements to specific and different tables in a database to answer common questions that could be found in a Data Engineer routine, such as "Which Schools have Average Student Attendance lower than 70%?" or "List 5 schools with lowest safety score". As a Data Engineer, one must know how to:

- Access databases using python;
- Write code using APIs;
- Work with real world Datasets; and
- Issue SQL statements using python libraries.

This project shows these concepts applied to a real world scenario, and was developed according to and following recommendations of IBM Data Engineer course (available at https://www.coursera.org/professional-certificates/ibm-data-engineer).

## Usage

In order to reproduce results obtained, it is necessary to execute the setup script in a Linux environment:

```bash
bash setup.sh
```

Once requirements are installed, run the script as below:

```bash
bash run.sh
```

This will install requirements listed in requirements.txt file, activate the virtual environment and run the python script responsible for connecting to Db2 and issue SQL commands. Note that in order for the db2-api.py file to work, valid credentials must be entered in respective fields below "confident info" comment such as host name, user id, password, etc.

The data used to practice the concepts mentioned above can be found at:

- [Chicago Crime Data](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01);
- [Chicago Public Schools](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01); and
- [Socioeconomic Indicators in Chicago](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01).
