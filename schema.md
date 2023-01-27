# `/api/series/<slug>`


Returns everything you need for a particular series.


Pages are at `/media/manga/<slug>/chapters/<folder>/<group_id>/<filename>`


```
{
    "slug" : series_slug,
    "title" : series_title
    "chapters" : {
        "1" : {
            "volume" : chapter_volume,
            "title" : chapter_title,
            "folder" : chapter_folder,
            "groups" : {
                "1" : [
                    "01.png",
                    "02.png",
                    ...
                ],
                "2" : [
                    "01.png",
                    "02.png",
                    ...
                ],
                ...
            }
        },
        "2" : {
            ...
        },
        ...
    }
}
```

# `/api/get_all_series/`


Returns metadata on all the series currently available.


```
{
    series_title : {
        "author" : author_name,
        "artist" : artist_name,
        "description" : series_description,
        "slug" : series_slug,
        "cover" : cover_url_slug,
        "groups" : {
            "1" : group_name,
            "2" : group_name,
            ...
        }
    }
}
```

# `/api/get_groups/<slug>`


Returns the scanlator groups available for a particular series. 


```
{
    "groups" : {
        "1" : group_name,
        "2" : group_name,
        ...
    }
}
```

# `/api/get_all_groups/`


Returns all the scanlator groups available site-wide. 

```
{
    "1" : group_name,
    "2" : group_name,
    ...
}
```