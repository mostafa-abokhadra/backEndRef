### send queris to your database
```ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  await prisma.user.create({
    data: {
      name: 'Alice',
      email: 'alice@prisma.io',
      posts: {
        create: { title: 'Hello World' },
      },
      profile: {
        create: { bio: 'I like turtles' },
      },
    },
  })
// findMany() returns all records as an array of objects
  const allUsers = await prisma.user.findMany({
    include: {
      posts: true,
      profile: true,
    },
  })
  console.dir(allUsers, { depth: null })
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
- Import the PrismaClient constructor from the @prisma/client node module
- Instantiate PrismaClient
- Define an async function named main to send queries to the database
- Call the main function
- Close the database connections when the script terminates

> [!NOTE]
> By default, Prisma Client only returns scalar fields in the result objects of a query. That's why, even though you also created a new Post record for the new User record, the console only printed an object with three scalar fields: id, email and name.

> In order to also retrieve the Post records that belong to a User, you used in the above example the include option via the posts relation field

### run code
```bash
npx ts-node script.ts
```

### udpates
```ts
async function main() {
  const post = await prisma.post.update({
    where: { id: 1 },
    data: { published: true },
  })
  console.log(post)
}
```
### prisma studio
```bash
npx prisma studio
```