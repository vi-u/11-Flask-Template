# Flask-Template
>>>>    Simple Flask Template

Basic understanding of Flask Templates will help to implement ypur Python code in web.


To run it, 

first, in a terminal clone the repository and "cd" to directory "11-Flask-Template"

    $ git clone https://github.com/vi-u/11-Flask-Template.git
    $ cd 11-Flask-Template
    
    
second, in a terminal run command that starts a web server in your browser

    $ python template.py


third, in your browser open this page:

    localhost:5000/blogs/5

*****
The exact working of a web template system is as follows:

    Extracts required data from DB or Form
    Combine the Data into the HTML file(using the template language) with the template engine
    Template Processor then processes it and outputs the resulting template file

*****
The structure of current application is as follows 
* application file "template.py" is in root directory
* all related html files in directory called "templates"
* all additional files with pictures, css ets are in "static" directory

![image](https://user-images.githubusercontent.com/118408434/202371181-f99cf6c8-2395-4a7d-aa9a-244a460cf6c4.png)



