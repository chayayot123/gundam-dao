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
        >>> sqllite3 sample.db < gundam_database.schema

        import the csv file
        >>> sqllite3 sample.db
        .mode csv
        .import data/gunpla_data.csv gunpla_info
        .import data/Media_data.csv medias

#### UML Class Diagram
[UML](../../wiki/uml-class-diagram)

#### Package Diagram
[Package Diagram](../../wiki/package-diagram)