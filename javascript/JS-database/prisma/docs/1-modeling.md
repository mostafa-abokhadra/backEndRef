### model your data in prisma schema
- in your `shema.prisma` file
```ts
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}
```
```ts
model Post {
  id        Int     @id @default(autoincrement())
  title     String
  content   String?
  published Boolean @default(false)
  author    User    @relation(fields: [authorId], references: [id])
  authorId  Int
}
```

### connect to your database URL
- in your prisma.schema file
```ts
datasourece db {
  provider = "mysql" | "postgresql"
  url      = env("DATABASE_URL")
}
```
> [!NOTE]
> - databse url format for sql and MariaDB is `"mysql://USER:PASSWORD@HOST:PORT/DATABASE"`
> - for postgres `"postgresql://admin:secret@localhost:5432/mydb?schema=public"`
> - for sqlite `"file:./path-to-your-database.db"
> - for sqlserver (microsoft) `"sqlserver://USER:PASSWORD@HOST:PORT;database=DATABASE;schema=SCHEMA_NAME"`