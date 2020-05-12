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

## Ayah
Get **ayah** of Quran. All **ayah** endpoints contains additional `parts` system which hold more
information about this **ayah**. For example you can get **ayah** with it's `Trnasltion`, `Image` and
`Surah` etc.  

Possible `parts` are `Translation`, `Surah`, `Edition`, `Arabic_Audio`, `Translation_Audio` and `Image`

Each **Ayah Parts** also contain the `edition-id` if you don't specify any by default edition `en` apply.

- ### Find Ayah by id [Try it Now]()

    without parts 

    [https://quran-api.octabyte.io/v1/ayah/AYAH-ID]()

    with parts 
    
    [https://quran-api.octabyte.io/v1/ayah/AYAH-ID?parts.list=Translation,Image,Edition]()

    with parts and Edition
    
    [https://quran-api.octabyte.io/v1/ayah/AYAH-ID?parts.list=Translation,Image,Edition&parts.edition_id=EDITION-ID]()


    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    // Without parts
    const res = await Ayah.byId('AYAH-ID');
    console.log(res.ayahResponse)

    // With parts
    const res = await Ayah.byId('AYAH-ID', ['Translation', 'Image', 'Edition']);
    console.log(res.ayahResponse.ayah)
    console.log(res.ayahResponse.translation)

    // With parts and edition
    const res = await Ayah.byId('AYAH-ID', ['Translation', 'Image', 'Edition'], 'EDITION-ID');
    ```

- ### Find Ayah by surah id [Try it Now]()

    without parts 

    [https://quran-api.octabyte.io/v1/ayah/surah/SURAH-ID]()

    with parts 
    
    [https://quran-api.octabyte.io/v1/ayah/surah/SURAH-ID?parts.list=Translation,Image,Edition]()

    with limit, cursor and parts
    [https://quran-api.octabyte.io/v1/ayah/surah/SURAH-ID?limit=5&cursor=CURSOR&parts.list=Translation,Image,Edition]()


    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    // Without parts
    const res = await Ayah.bySurahId('SURAH-ID');

    // With parts
    const res = await Ayah.bySurahId('SURAH-ID', null, nul, ['Translation', 'Image', 'Edition']);

    // With limit, cursor and parts
    const res = await Ayah.bySurahId('SURAH-ID', CURSOR, LIMIT, ['Translation', 'Image', 'Edition']);
    ```

- ### Find Ayah by number [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/number/AYAH-NUMBER]()

    **Parts endpoint also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byNumber('AYAH-NUMBER');
    ```

- ### Find Ayah by number in surah [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/number_in_surah/NUMBER]()

    **Parts endpoint also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byNumberInSurah('NUMBER');
    ```

- ### Find Ayah by Juz [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/juz/NUMBER]()

    **Parts endpoint and limit, cursor also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byJuz('NUMBER');
    ```

- ### Find Ayah by Manzil [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/manzil/NUMBER]()

    **Parts endpoint and limit, cursor also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byManzil('NUMBER');
    ```

- ### Find Ayah by Ruku [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/ruku/NUMBER]()

    **Parts endpoint and limit, cursor also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byRuku('NUMBER');
    ```

- ### Find Ayah by Hizb Quarter [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/hizb_quarter/NUMBER]()

    **Parts endpoint and limit, cursor also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.byHizbQuarter('NUMBER');
    ```

- ### Find Ayah by Sajda [Try it Now]()

    [https://quran-api.octabyte.io/v1/ayah/sajda/TRUE-OR-FALSE]()

    **Parts endpoint and limit, cursor also apply like others**

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Ayah} = require("quran-client");

    const res = await Ayah.bySajda(TRUE-OR-FALSE);
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

## Image
Get image of the **ayah**

- ### Find image by Ayah Id [Try it Now]()

    [https://quran-api.octabyte.io/v1/image/ayah/AYAH-ID]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Image} = require("quran-client");

    const res = await Image.byAyahId('AYAH-ID');
    ```

## Surah

- ### Get All Surahs [Try it Now]()

    Gel all available surahs. 

    [https://quran-api.octabyte.io/v1/surah/all]()

    You can also apply `limit` and `cursor`

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.getAll();
    ```

- ### Find surah by id [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/SURAH-ID]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byId('SURAH-ID');
    ```

- ### Find surah by number [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/number/SURAH-NUMBER]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byNumber('SURAH-NUMBER');
    ```

- ### Find surah by name [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/name/SURAH-NAME]()


    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byName('SURAH-NAME');
    ```

- ### Find Surah by English Name [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/english_name/SURAH-ENGLISH-NAME]()


    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byEnglishName('SURAH-ENGLISH-NAME');
    ```

- ### Find Surah by English Name Translation [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/english_name_translation/ENGLISH-NAME-TRANSLATION]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byEnglishNameTranslation('ENGLISH-NAME-TRANSLATION');
    ```

- ### Find surah by Revelation Type [Try it Now]()

    [https://quran-api.octabyte.io/v1/surah/revelation_type/TYPE]()

    You can also apply `limit` and `cursor`

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Surah} = require("quran-client");

    const res = await Surah.byRevelationType();
    ```

## Translation

- ### Find Translation by id [Try it Now]()

    [https://quran-api.octabyte.io/v1/translation/ID]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Translation} = require("quran-client");

    const res = await Translation.byId();
    ```

- ### Find Translation by Ayah id [Try it Now]()

    [https://quran-api.octabyte.io/v1/translation/ayah/AYAH-ID]()

    You can also apply `limit` and `cursor`

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Translation} = require("quran-client");

    const res = await Translation.byAyahId('AYAH-ID');
    ```

- ### Find Translation by Edition id [Try it Now]()

    [https://quran-api.octabyte.io/v1/translation/edition/EDITION-ID]()

    You can also apply `limit` and `cursor`

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Translation} = require("quran-client");

    const res = await Translation.byEditionId('EDITION-ID');
    ```

- ### Filter translation [Try it Now]()

    Filter translation by `ayah-id` and `edition-id`

    [https://quran-api.octabyte.io/v1/translation/filter?ayah_id=AYAH-ID&edition_id=EDITION-ID]()

    **Using clinet library in NodeJs** [Quran Client NodeJs](https://www.npmjs.com/package/quran-client)
    ```nodejs
    const {Translation} = require("quran-client");

    const res = await Translation.filter('AYAH-ID', 'EDITION-ID');
    ```