# Keywords App
A learning tool that teaches students how to make complex searches. It is built by UT Austin and made extensible to be used by other institutions.

## To use:
Clone the repository and run the following command in your terminal inside the project:

`docker-compose up`

You should see the following in your terminal:

```buildoutcfg
Starting keywords_web_1 ... done
Attaching to keywords_web_1
web_1  | Watching for file changes with StatReloader
web_1  | Performing system checks...
web_1  | 
web_1  | System check identified no issues (0 silenced).
web_1  | March 25, 2020 - 22:04:43
web_1  | Django version 3.0.4, using settings 'keywords.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

In a browser, go to http://localhost:8000/keywords and you have the app!


## Customizations
#### Catalog links
The search query currently automatically builds search links to the following:
* UT Austin's Catalog
* EBSCO (requires login)
* JSTOR

To add/remove, you will need to make changes to the following files:

* `keywords/keywords/settings.py`
    
Global variables set here correlate to the base search link. Add your institution catalog link and
additional search links here. 

<br>

* `keywords/word/populate.py`  

This file creates the query strings and links passed to the search template (search.html).
For example `'catalog': settings.CATALOG_LINK + query_string + settings.CATALOG_SUFFIX`

<br>

* `keywords/word/templates/word/search.html` 

Links are created based on the query results.

An example `<a class="search-link" href="{{ search.catalog }}" target="_blank">Search Everything</a>`
    
<br>

* `keywords/word/templates/word/email.html`

These are the links provided in the email. An example: `<a href="{{ params.query.catalog }}">Search everything for books, articles and more.</a>`

<br>


#### Email
If you would like to use the email functionality, which would send the results to the user, then update 
the sender's email found in `keywords/word/views.py` in the search function.


```buildoutcfg
params['sender'] = 'INSTITUTION_EMAIL' # TODO: edit with your institution's email
```

## Dependencies
[Docker](https://www.docker.com/products/docker-desktop)

[Docker Compose](https://docs.docker.com/compose/install/)

[SMTP Server](https://docs.djangoproject.com/en/3.0/topics/email/)
If you want to utilize the email functionality, you will need to set up a SMTP server.


## Release History

* 1.0.0
    * Start of project
    * Dockerized
    * Generic styling