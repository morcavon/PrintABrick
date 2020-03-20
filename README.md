# Changes

src/LoaderBundle/Service/ModelLoader.php
Added an iteration counter for parent models and abort model if it has too many parents.

src/LoaderBundle/Service/RebrickableLoader.php
Added a fourth column "material_id" which is new in the csv file. You have to add this field in the database manually! (material_id, varchar 128, null)

## Install Notes
The easiest way to run Elastisearch is with the docker image. Download Version 5.5.0

`docker pull docker.elastic.co/elasticsearch/elasticsearch:5.5.0`

 and run it with
 
`docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.5.0`

If you run PHP > 7.2, then you have to run composer with 
`composer install --ignore-platform-reqs`


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
