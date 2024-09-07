### npm
> [!NOTE]
> Yarn and pnpm are alternatives to npm cli. You can check them out as well.

### installing dependencies
- if the project has **package.json** file by running
```bash
npm install
```
- it will install everything the project needs in the node_modules folder

### install specific package
```bash
npm install package_name
```
Often you'll see more flags added to this command:

```bash
--save-dev installs and adds the entry to the package.json file devDependencies
--no-save installs but does not add the entry to the package.json file dependencies
--save-optional installs and adds the entry to the package.json file optionalDependencies
--no-optional will prevent optional dependencies from being installed
```

The difference between <mark>devDependencies</mark> and <mark>dependencies</mark> is that the former contains development tools, like a testing library, while the latter is bundled with the app in production.

As for the optionalDependencies the difference is that build failure of the dependency will not cause installation to fail. But it is your program's responsibility to handle the lack of the dependency.

### update packages
```bash
node update
node update package_name
```

### to install specific version
```bash
npm install package_name@version
```

### running tasks
- package.json support a format for specifying command line tasks that can be run using
```bash
npm run task_name
```

##### example
```json
{
  "scripts": {
    "start-dev": "node lib/server-development",
    "start": "node lib/server-production"
  }
}

{
  "scripts": {
    "watch": "webpack --watch --progress --colors --config webpack.conf.js",
    "dev": "webpack --progress --colors --config webpack.conf.js",
    "prod": "NODE_ENV=production webpack -p --config webpack.conf.js"
    }
  }
```
So instead of typing those long commands, which are easy to forget or mistype, you can run
```bash
npm run prod
npm run watch
npm run dev
```
