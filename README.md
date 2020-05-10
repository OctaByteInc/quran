# Quran API [![Build Status](https://travis-ci.org/octabytes/quran.svg?branch=master)](https://travis-ci.org/octabytes/quran)
---

## Audio
There are two kind of **Audios** one is *Arabic* and second is *Translation*.
Here are some endpoints you can use to get **Audios**

- ### Find Audio by id [Try it Now]()  

    Provide a single **Audio** based on the `id`

    [https://quran-api.octabyte.io/v1/audio/audio-id-123]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Audio} = require("quran-client");

    const res = await Audio.byId('audio-id');
    ```

- ### Find Audio by Ayah id [Try it Now]()  

    Multiple **Audios** will return in this case, These **Audio** can be *Arabic* and *Translation*.
    
    [https://quran-api.octabyte.io/v1/audio/ayah/ayah-id-123]()

    You can also `limit` the number of results.

    [https://quran-api.octabyte.io/v1/audio/ayah/ayah-id-123?limit=10]()

    `Cursor` can used for fetching next results.  
    Fetching the next 10 results. 

    [https://quran-api.octabyte.io/v1/audio/ayah/ayah-id-123?cursor=CURSOR_STRING_FROM_PREVIOUS_RESULTS]()

    You can also `limit` the `cursor` if you want. For example fetch the next 5 resutls.

    [https://quran-api.octabyte.io/v1/audio/ayah/ayah-id-123?limit=5&cursor=CURSOR_STRING_FROM_PREVIOUS_RESULTS]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Audio} = require("quran-client");

    const res = await Audio.byAyahId('ayah-id', null, 10);

    // Fetch next results using cursor

    const nextResults = await Audio.byAyahId('ayah-id', res.cursor)

    // Limit the cursor for next results

    const nextResults = await Audio.byAyahId('ayah-id', res.cursor, 5)
    ```

- ### Find Audio by Edition id [Try it Now]()  

    Multiple **Audios** will return in this case, These **Audio** can be *Arabic* and *Translation*.
    
    [https://quran-api.octabyte.io/v1/audio/edition/edition-id]()

    You can also `limit` the number of results.

    [https://quran-api.octabyte.io/v1/audio/edition/edition-id?limit=10]()

    `Cursor` can used for fetching next results.  
    Fetching the next 10 results. 

    [https://quran-api.octabyte.io/v1/audio/edition/edition-id?cursor=CURSOR_STRING_FROM_PREVIOUS_RESULTS]()

    You can also `limit` the `cursor` if you want. For example fetch the next 5 resutls.

    [https://quran-api.octabyte.io/v1/audio/edition/edition-id?limit=5&cursor=CURSOR_STRING_FROM_PREVIOUS_RESULTS]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Audio} = require("quran-client");

    const res = await Audio.byEditionId('edition-id', null, 10);

    // Fetch next results using cursor

    const nextResults = await Audio.byEditionId('edition-id', res.cursor)

    // Limit the cursor for next results

    const nextResults = await Audio.byEditionId('edition-id', res.cursor, 5)
    ```

- ### Find Only Arabic Audio [Try it Now]()  

    Provide a single **Audio** based on the `edition-id` and `ayah-id`

    [https://quran-api.octabyte.io/v1/audio/audio/arabic?ayah_id=ayah-id&edition_id=edition-id]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Audio} = require("quran-client");

    const res = await Audio.arabicAudio('ayah-id', 'edition-id');
    ```

- ### Find Only Translation Audio [Try it Now]()  

    Provide a single **Audio** based on the `edition-id` and `ayah-id`

    [https://quran-api.octabyte.io/v1/audio/audio/translation?ayah_id=ayah-id&edition_id=edition-id]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Audio} = require("quran-client");

    const res = await Audio.translationAudio('ayah-id', 'edition-id');
    ```

## Edition
There are many **edition** you can use to fetch different data according to these **editions**
If you does not specifiy and **edition** then by default edition `edition-en` will be applied. 

- ### Get All Editions [Try it Now]()

    Gel all available editions. 

    [https://quran-api.octabyte.io/v1/edition/all]()

    You can also apply `limit` and `cursor` like **Aduio**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.getAll();
    ```

- ### Find Edition by id [Try it Now]()

    [https://quran-api.octabyte.io/v1/edition/edition-id]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.byId('edition-id');
    ```

- ### Find Edition by Language [Try it Now]()

    Get edition by specific *language*. 

    [https://quran-api.octabyte.io/v1/edition/language/en]()

    You can also apply `limit` and `cursor`.

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.byLanguage('en');
    ```

- ### Find Edition by Name [Try it Now]()

    Get edition by specific *name*. 

    [https://quran-api.octabyte.io/v1/edition/name/NAME]()

    You can also apply `limit` and `cursor`.

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.byName('name');
    ```

- ### Find Edition by Translator [Try it Now]()

    Get edition by specific *Translator*. 

    [https://quran-api.octabyte.io/v1/edition/translator/NAME]()

    You can also apply `limit` and `cursor`.

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.byTranslatior('name');
    ```

- ### Find Edition by Type [Try it Now]()

    There are two kind of the **types** one is *Arabic* second is *Translation*

    [https://quran-api.octabyte.io/v1/edition/type/TYPE]()

    You can also apply `limit` and `cursor`.

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Edition} = require("quran-client");

    const res = await Edition.byType('type');
    ```