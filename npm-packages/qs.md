## qs 转对象

```js
const Qs = require('qs');

let url = 'method=query_sql_dataset_data&projectId=85&appToken=7d22e38e-5717-11e7-907b-a6006ad3dba0';

Qs.parse(url);

console.log(Qs.parse(url));
```
