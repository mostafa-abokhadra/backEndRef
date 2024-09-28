### setUp
```bash
npm install passport
npm install passport-local
```
Next, configure Passport. Open routes/auth.js and require() the newly installed packages at line 2, below require('express').
```js
const express = require('express');
const passport = require('passport');
const LocalStrategy = require('passport-local');
const crypto = require('crypto');
```