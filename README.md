# ML-for-CSRF-detection
This web application makes use of machine learning for detecting if a website is vulnerable to any possible CSRF attacks and if so, it alerts the user. It uses the RandomForest Classifier to predict possible CSRF attacks from the data generated by the below processes.

It crawls the target website at a specified depth and stores all the HTML forms found in a database for further processing to find out the tokens which aren't strong enough and the forms which are not protected.

It also detects any possible replay attack scenarios and hence checks if a token has been issued more than one time. It calculates the levenshtein distance between all the tokens to see if they are similar and are also compared with a database containing many hash patterns.

100 simultaneous requests are made to a single webpage to see if same tokens are generated for the requests.

We also perform testing which is aimed at providing an active testing of the CSRF protection mechanism. It includes checking if the protection exists for mobile browsers too by submitting requests with a self-generated token and testing if the token is being checked to a certain length.

Various statistical tests like monobit frequency test, block frequency test. runs test, spectral test, etc., are performed.

# Usage
Run manage.py in the root directory and you will be able to see the possible subcommands that you can perform.

Start with the command "python manage.py runserver" you will be able to see the localhost address on which the server is hosted. Go to that link and make a user account.

Sign in to the admin account (whose password you can change later, for now username and password are both admin) and activate the user account which you just signed up with.

Once your user account is activated you can login into the account and input the link and the depth at which you want to test the website for.
