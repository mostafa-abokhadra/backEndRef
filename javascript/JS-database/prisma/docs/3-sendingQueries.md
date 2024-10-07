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
```ts
async function main() {
  const users = await prisma.user.findMany()
  console.log(users)
}
```