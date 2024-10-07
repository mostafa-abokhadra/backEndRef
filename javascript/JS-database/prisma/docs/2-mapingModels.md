### mapping models
- At this point, you have a Prisma schema but no database yet
- mapping models to database tables using `prisma migrate`
- run a migration to create your database table with prisma migrate
- ensure env var DATABASE_URL is set correctly first in your .env
```bash
npx prisma migrate dev --name init
```