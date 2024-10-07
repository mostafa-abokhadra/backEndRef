### mapping models
- mapping models to database tables using prisma migrate
- run a migration to create your database table with prisma migrate
- At this point, you have a Prisma schema but no database yet
- ensure env var DATABASE_URL is set correctly first
```bash
npx prisma migrate dev --name init
```