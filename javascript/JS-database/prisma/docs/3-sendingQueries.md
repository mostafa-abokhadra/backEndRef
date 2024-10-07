### send queris to your database
```ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
    const user = await prisma.user.create({
        data: {
        name: 'Alice',
        email: 'alice@prisma.io',
        },
  })
  console.log(user)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
```
This code contains a main function that's invoked at the end of the script. It also instantiates PrismaClient which represents the query interface to your database.

### run code
```bash
npx ts-node script.ts
```

### reading from database
#### findMany()
- returns all records
- it returns an array of objects
```ts
async function main() {
  const users = await prisma.user.findMany()
  console.log(users)
}
```

### create a User and a Post record in a nested write query
```ts
async function main() {
  const user = await prisma.user.create({
    data: {
      name: 'Bob',
      email: 'bob@prisma.io',
      posts: {
        create: [
          {
            title: 'Hello World',
            published: true
          },
          {
            title: 'My second post',
            content: 'This is still a draft'
          }
        ],
      },
    },
  })
  console.log(user)
}
```

> [!NOTE]
> By default, Prisma Client only returns scalar fields in the result objects of a query. That's why, even though you also created a new Post record for the new User record, the console only printed an object with three scalar fields: id, email and name.

> In order to also retrieve the Post records that belong to a User, you can use the include option via the posts relation field:

```ts
async function main() {
  const usersWithPosts = await prisma.user.findMany({
    include: {
      posts: true,
    },
  })
  console.dir(usersWithPosts, { depth: null })
}
```

### prisma studio