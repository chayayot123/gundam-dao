## Gundam_model_data table

1. gunpla_id - Id number of the gunpla
2. gunpla_name - The specific name of gunpla in gunpla universe.
3. title - Name of the title in gundam universe.
4. rating_design - The user rating review of that gunpla.

## Gundam_Medias_data table
1. title_id -Title id of the gundam series
2. title - Name of the title in gundam universe.
3. media_type - Type of the media that have been show.
4. release_date - The year that release to show.
5. timeline - The timeline of the gundam universe.

#### Setup
        
        create database from command line

        >>> sqlite3 sample.db < gundam_database.schema

        import the csv file

        >>> sqlite3 sample.db

        sqlite3> .mode csv
        sqlite3> .import data/gunpla_data.csv gunpla_info
        sqlite3> .import data/Media_data.csv medias
        sqlite3> .quit


#### UML Class Diagram
[UML](https://github.com/chayayot123/gundam-dao/wiki/UML-diagram)

[Web API Service](../../wiki/Web-API-Service)
