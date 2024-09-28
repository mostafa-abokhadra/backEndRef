### installing packages
- once you install your first package, a node_modules folder will be created and the package installed will be inside it.
- also package.json file will be updated, dependencies field will be added with the package installed e:g
- dependencies field used to track the packages that are required for our code
- don't forget to gitignore node_modules directory
```json
{
    "dependencies": {
        "packageName": "^packageVersion"
    }
}
```
- also package-lock.json file will be created once you installed your first package, then the same file will be updated for subsequent packages, this file simpley keeps track of the packages and version you install using npm in the project and ensuring there is no inconsistincies when some one else install the same packages

### uninstall
```bash
npm uninstall pacakgeName
```

### using packages
- any package you install is basically a module in js
- a package is called a third-party module, it's not a built-in module or local moudle
```js
const upperCase = require("upper-case").upperCase; 
```

> [!NOTE]
> our project in github doesn't have node_modules directory, so when someone clone our repo how does the project work? well here comes package.json into play, when user runs the command `npm install` it will install all the dependecies needed for the project to work from the depenedenceis field in package.json