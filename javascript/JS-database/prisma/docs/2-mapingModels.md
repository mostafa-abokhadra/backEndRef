### mapping models
- At this point, you have a Prisma schema but no database yet
- mapping models to database tables using `prisma migrate`
- run a migration to create your database table with prisma migrate
- ensure env var DATABASE_URL is set correctly first in your .env
```bash
npx prisma migrate dev --name init
```
this command witll create a new SQL migration file for this migration and  runs the SQL migration file against the database

> [!NOTE]
> generate is called under the hood by default, after running prisma migrate dev. If the prisma-client-js generator is defined in your schema, this will check if @prisma/client is installed and install it if it's missing.

### Install and generate Prisma Client
```bash
npm install @prisma/client
```