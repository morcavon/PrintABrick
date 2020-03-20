# Updated 2020-03-20

The Third-Party API's have changed over time  and several code changes were needed to run this project successfully. As of now, it should work out of the box with the additional install notes and the original install notes below.

## Additional Install Notes

As far as i know, this project isn't compatible with PHP >= 7.3. 
The whole project with all models loaded is about 3 GB in size.

### Elastisearch
The easiest way to run Elastisearch is with the docker image. Download Version 5.5.0

`docker pull docker.elastic.co/elasticsearch/elasticsearch:5.5.0`

 and run it with
 
`docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.5.0`

I added a run script to the bin directory which executes this command.

### Composer
If you run PHP > 7.2.0, then you have to run composer with 
`composer install --ignore-platform-reqs`

### stl2pov
Simply download and extract the zip file and set the executable path to [absolute_path]/stltools-3.3/stl2pov.py either at the `composer install` stage or later in the parameters.yml. Python has to be installed.

### LDView
Make sure you use the osmesa version, which is the CLI version of the program.
You may need additional packages for ubuntu/debian:
[libgl2ps1](https://launchpad.net/ubuntu/bionic/amd64/libgl2ps1/1.3.9-4)
[libjpeg62-turbo](https://debian.pkgs.org/sid/debian-main-amd64/libjpeg62-turbo_1.5.2-2+b1_amd64.deb.html)


### NGinx
[config](https://symfony.com/doc/3.3/setup/web_server_configuration.html#nginx)

## Troubleshooting
If you got an error like

`no such index [index: app]`

The elastisearch index must be build:

`bin/console fos:elastica:populate`

`bin/console fos:elastica:populate --env=prod`

---

The import from rebrickable may complete with the message "Done with X errors.". This is normal. Most probably some parts/sets are faulty and haven't be imported.

---
From this point on, the original Readme text:

# PrintABrick
Web catalogue of LEGO® parts for 3D printing

A Symfony project 

## Install

### System requirements

* PHP needs to be a minimum version of PHP 7.0
* PHP Extensions
    * FTP 
    * SOAP 
    * GD
    * PDO 
    * Zip 
* *date.timezone* setting set in *php.ini*

You can check if your system meets requirements by running `$ bin/symfony_requirements`

For full requirements see Symfony 3.3 [docs](http://symfony.com/doc/3.3/reference/requirements.html).


#### Required 
* Elasticsearch >= 5

    Instructions for installing and deploying Elasticsearch may be found [here](https://www.elastic.co/downloads/elasticsearch). 
* POV-Ray [source](http://www.povray.org/).
* stl2pov [source](https://github.com/rsmith-nl/stltools/releases/tag/3.3).
* ADMesh 
* LDView OSMesa >= 4.2.1 [source](https://tcobbs.github.io/ldview/).

### Installing  
   
#### Back-end
1. Make sure your system meets the application requirements
2. Install dependencies via [Composer](https://getcomposer.org/), `$ composer install`

#### Front-end
1. Install dependencies via [npm](https://www.npmjs.com/), `$ npm install`
2. Install bower dependencies via [bower](https://bower.io), `$ bower install`
3. Compile assets by running [Gulp](http://gulpjs.com/), `$ gulp default [--env production]`

#### Initialization

##### Setup database 
1. Set application parameters in *app/config/parameters.yml*
2. Generate an empty database by running command (if it does not yet exist) `$ bin/console doctrine:database:create`   
3. Create database tables/schema by running command`$ bin/console doctrine:schema:create`
4. Load database fixtures `$ bin/console doctrine:fixtures:load`

##### Load data
You can load initial application data by running command `$ bin/console app:init`

This command consists of multiple subcommands that can be called separately:
1. Load LDraw models into database by running commad `$ bin/console app:load:ldraw [--ldraw=PATH] [--all] [--file=FILE] [--update] `
2. Load Rebrickable data into database by running command `$ bin/console app:load:rebrickable`  
3. Load relations between LDraw models and Rebrickable parts by running command `$ bin/console app:load:relations` 
4. Download images of models from rebrickable.com `$ bin/console app:load:images [--color=INT] [--rebrickable] [--missing]`
5. Populate Elastisearch index `$ bin/console fos:elastica:populate`

##### Adding part relation 
Relations between LDraw models and Rebrickable parts are matched automatically by identical (or similar) id/name when executing command `$ bin/console app:load:relation`. 

Unmatched relations can be specified by adding relation of IDs to `app/Resources/relations/part_model.yml` 

## Testing
The test database must be created before the first test runs. You can create new one by running:

1. Generate an empty database by running command (if it does not yet exist) `$ bin/console doctrine:database:create --env=test`   
2. Create database tables/schema by running command`$ bin/console doctrine:schema:create --env=test`


You can run complete system tests by `$ phpunit`. These should cover the main system functions and the functionality of calling the third-party programs that are required are needed to seamlessly retrieve the necessary application data.
