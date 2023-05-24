# Webscraping by Building Request

This is a simple code to show how to simulate the same request that was made when you access the page, but using Python.

When it cames to webscraping we have a lot of approaches. This simple repository aims to simple simulate a POST request in order to avoid
the hard work by mapping every component on the website.

You will need an application to test APIs. I personaly like to use POSTMAN.

1 - You need to open your tool of development in your brow and then perform the action that is happening. To see the information you need to go to the networking session.

2 - Analyse the header field and the payload. The payload is the data the will be mandatory to receve the data back to the server.

3 - You can click with right click button and ask to show the sorce code, in order to see a json object.

4 - Go to POSTMAN and put the link that you saw on the request header.

5 - In the body section you will choose RAW and the type is JSON

6 - Make the requsition and see what the server returns

After that you can use the method request.json() to create a dataframe or analyse what kind of data you will need.

I will let a code as an exemple on the main.py.

