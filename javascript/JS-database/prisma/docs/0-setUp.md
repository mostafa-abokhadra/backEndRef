### prisma
- is a next-generation Node.js and TypeScript ORM 
- It covers data **modeling**, **migrations** and **querying** a database.

1. **initialize typescript project**
```bash
npm init -y
npm install typescript ts-node @types/node --save-dev
```
2. **initialize typescript**
```bash
npx tsc --init
```
3. **install prisma**
```bash
npm install prisma --save-dev
```
4. **set up Prisma ORM with the init command of the Prisma CLI**
```bash
npx prisma init --datasource-provider sqlite
```
This creates a new prisma directory with a schema.prisma file and configures SQLite as your database. You're now ready to model your data and create your database with some tables.