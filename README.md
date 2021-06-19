# websocket-api-test-framework

This is basic test framework which aims at testing websocket apis.  

### File Contents  
1. tests folder  
   contains the tests for different components of application  
   a. test_instrumentData  
      includes tests for instrument data(basic tests)  
   b. test_instrumentTicker
      includes tests for instrument ticker(basic tests)  
2. config file  
   contains the configuration and data required for running the tests  
3. requirements.txt
   install the libraries mentioned in this file using `pip`.      
### Execution
To run the test scripts with help of command line(Linux machine):  
`pytest`  

Note: PyCharm was used to write this test-scripts. Just setup a pytest run configuration to run the scripts in PyCharm.

### Tech Stack 
> *python 3.8*  
  *test framework - pytest*  
  *libraries - websocket, pytz, json*  
>
The sole purpose of selecting python is the availability of various libraries to perform different kinds of tests on different components.
As seen from above websocket-client library is used to establish connection with the server and send subscription requests.  
pytz library is an excellent library which helps specify the time zone and evaluate time in that specific timezone.  
json library is the library that is utilised to parse the received data and verify different attributes present in response.    


### Shortcoming  
The script currently doesn't address the following points -   
1. parameterized data for tests 
2. exception/error handling
3. parallel execution

The above listed points can be explored more when more tests are added and the test suite inflates.  

### Implementing indirect requirements
1. Reporting(with html-reports) and Notification(e-mail) on failure can be added.
2. Performance testing can be targeted with help of other python libraries present.  