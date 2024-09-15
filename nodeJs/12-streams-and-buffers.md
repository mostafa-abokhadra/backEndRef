### streams
- it is a sequence of data that is being moved from one point to another over time

**Ex:**
- stream of data over the internet being moved from one computer to another
- a stream of data being tranferred from one file to another within the same computer

> [!NOTE]
> in node js the idea is to process streams of data in chunks as they arrive instead of waiting for the entire data to be available before processing
- e:g when you watch a youtube video you don't wait for the whole video to be downloaded to start watching it, the data arrives in chunks and you watch in chunks while the rest of the data arrives over time
- e:g when you are transferring file contents from file1 to file 2, you don't wait for the entire file1 content to be saved in temporary memmory before moving it to file 2 , the contents arrive in chunks and you transfer in chunks while the remaining contents arrive over time

in doing so we prevent unnescessary data downloads and memmory usage
